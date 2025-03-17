import os, sys, time

from xbot2_cli import utils

class Context:
    
    SRV_TIMEOUT_SEC = 1
    
    def __init__(self):
        user = os.getlogin()
        self.cache_file = f'/tmp/xbot2_cli_cache_{user}.yaml'
        self.node = None
        
        if os.path.exists(self.cache_file):
            cache_age = time.time() - os.path.getmtime(self.cache_file)
        else:
            cache_age = 1000
                
        if cache_age < 60:
            import yaml
            cache_dict = yaml.safe_load(open(self.cache_file, 'r'))
            self.plugin_list = cache_dict['plugin_list']
            self.param_list = cache_dict['param_list']
        else:
            self.init_ros()
            try:
                self.plugin_list = self.list_plugins(None, verbose=False)
                self.param_list = self.list_params(None, verbose=False)
                import yaml
                cache_dict = {'plugin_list': self.plugin_list, 'param_list': self.param_list}
                yaml.dump(cache_dict, open(self.cache_file, 'w'))
            except TimeoutError:
                self.plugin_list = []
                self.param_list = []
            
            
    def init_ros(self):
        if self.node is not None:
            return
        import rclpy
        rclpy.init()
        self.node = rclpy.create_node('xbot2_cli')
        
    def call_service(self, client, request):
        import rclpy
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self.node, future, timeout_sec=self.SRV_TIMEOUT_SEC)
        if not future.done():
            raise TimeoutError("Service call timed out")
        return future.result()
            
    def clear_cache(self, args):
        os.remove(self.cache_file)
        print("Cache cleared.")
    
    def tune_param(self, args):
        from xbot2_cli import tuning
        tuning.tuning_tui(self, args)

    def get_param(self, args, verbose=True):
        from xbot_msgs.srv import GetParameterInfo
        import yaml
        cli = self.node.create_client(GetParameterInfo, 'xbotcore/get_parameter_info')
        req = GetParameterInfo.Request()
        req.name = [args.name]
        res: GetParameterInfo.Response = self.call_service(cli, req)
        verbose and print(res.value[0])
        return yaml.safe_load(res.value[0])

    def set_param(self, args, verbose=True):
        from xbot_msgs.srv import SetString
        cli = self.node.create_client(SetString, 'xbotcore/set_parameters')
        req = SetString.Request()
        req.request = f'{args.name}: "{args.value}"'
        res: SetString.Response = self.call_service(cli, req)
        if not res.success:
            raise RuntimeError(res.message)
        verbose and print(f"Successfully set parameter: {args.name} to {args.value}")
        
    def list_params(self, args, verbose=True):
        from xbot_msgs.srv import GetParameterInfo
        cli = self.node.create_client(GetParameterInfo, 'xbotcore/get_parameter_info')
        req = GetParameterInfo.Request()
        req.tunable_only = False if not args else args.tunable_only 
        res: GetParameterInfo.Response = self.call_service(cli, req)
        type = [utils.pretty_cpp_types(t) for t in res.type]
        verbose and utils.print_table(zip(res.name, type))
        return res.name

    def switch_plugin(self, args, verbose=True):
        from std_srvs.srv import SetBool
        cli = self.node.create_client(SetBool, f'xbotcore/{args.name}/switch')
        req = SetBool.Request()
        req.data = self._str_to_bool(args.value)
        res: SetBool.Response = self.call_service(cli, req)
        if not res.success:
            raise RuntimeError(res.message)
        verbose and print(f"Successfully switched plugin: {args.name} to {args.value}")

    def list_plugins(self, args, verbose=True):
        from xbot_msgs.srv import GetPluginList
        cli = self.node.create_client(GetPluginList, 'xbotcore/get_plugin_list')
        req = GetPluginList.Request()
        res: GetPluginList.Response = self.call_service(cli, req)
        if verbose and args.status:
            status = [self.status_plugin(p, verbose=False) for p in res.plugins]
            utils.print_table(zip(res.plugins, status))
        elif verbose:
            print('\n'.join(res.plugins))
        return res.plugins

    def status_plugin(self, args, verbose=True):
        from xbot_msgs.srv import PluginStatus
        name = args if isinstance(args, str) else args.name
        cli = self.node.create_client(PluginStatus, f'xbotcore/{name}/state')
        req = PluginStatus.Request()
        res: PluginStatus.Response = self.call_service(cli, req)
        verbose and print(res.status)
        return res.status
    
    def watch_stats(self, args):
        import rclpy
        from xbot_msgs.msg import Statistics2, ThreadStatistics, TaskStatistics
        prev_time = time.time()
        f = utils.format_float
        def stats_callback(msg: Statistics2):
            nonlocal prev_time
            now = time.time()
            dt = now - prev_time
            if dt < args.num_secs:
                return
            prev_time = now
            # clear console
            print("\033[H\033[J")
            rows = []
            for th in msg.thread_stats:
                th: ThreadStatistics
                row = [th.name, f(th.total_time), f(th.period), f(th.expected_period)]
                rows.append(row)
                for task in msg.task_stats:
                    task: TaskStatistics
                    if task.thread != th.name:
                        continue
                    perc = int(100 * task.run_time / th.expected_period)
                    row = [f'  {task.name}', f(task.run_time) + f' ({perc} %)', task.state, '']
                    rows.append(row)
            utils.print_table(rows)
        
        sub = self.node.create_subscription(Statistics2, 'xbotcore/statistics', stats_callback, 1)
        try:
            rclpy.spin(self.node)
        except KeyboardInterrupt:
            pass
                
                

    def set_filter(self, args, verbose=True):
        from xbot_msgs.srv import SetFilterProperties
        cli = self.node.create_client(SetFilterProperties, 'xbotcore/set_filter_properties')
        req = SetFilterProperties.Request()
        req.cutoff_hz = float(args.value)
        req.enabled = True
        res: SetFilterProperties.Response = self.call_service(cli, req)
        if not res.success:
            raise RuntimeError(res.message)
        verbose and print(f"Setting filter: to {args.value} Hz")

    def get_filter(self, args):
        print(f"Getting filter: {args.value}")

    def enable_filter(self, args, verbose=True):
        from xbot_msgs.srv import SetFilterProperties
        cli = self.node.create_client(SetFilterProperties, 'xbotcore/set_filter_properties')
        req = SetFilterProperties.Request()
        req.cutoff_hz = -1.0
        req.enabled = self._str_to_bool(args.value)
        res: SetFilterProperties.Response = self.call_service(cli, req)
        if not res.success:
            raise RuntimeError(res.message)
        verbose and print(f"Enabling filter: {self._str_to_bool(args.value)}")
        
    def _str_to_bool(self, s):
        if s.lower() in ['true', '1']:
            return True
        elif s.lower() in ['false', '0']:
            return False
        else:
            raise ValueError("Invalid boolean value")