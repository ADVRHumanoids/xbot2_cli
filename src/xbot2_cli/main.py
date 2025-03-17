import argparse
import argcomplete
import logging

from xbot2_cli.context import Context



def main():
    
    ctx = Context()

    parser = argparse.ArgumentParser(description="xbot2 CLI")
    subparsers = parser.add_subparsers(title="verbs", dest="verb")

    # Param subcommands
    param_parser = subparsers.add_parser('param', help='Manage parameters')
    param_subparsers = param_parser.add_subparsers(title="subcommands", dest="subcommand")

    param_get_parser = param_subparsers.add_parser('get', help='Get a parameter')
    param_get_parser.add_argument('name', type=str, choices=ctx.param_list, help='Name of the parameter')
    param_get_parser.set_defaults(func=ctx.get_param)

    param_set_parser = param_subparsers.add_parser('set', help='Set a parameter')
    param_set_parser.add_argument('name', type=str, choices=ctx.param_list, help='Name of the parameter')
    param_set_parser.add_argument('value', type=str, help='Value of the parameter')
    param_set_parser.set_defaults(func=ctx.set_param)

    param_list_parser = param_subparsers.add_parser('list', help='List all parameters')
    param_list_parser.add_argument('--tunable-only', '-t', action='store_true', help='Show only tunable parameters')
    param_list_parser.set_defaults(func=ctx.list_params)

    param_tune_parser = param_subparsers.add_parser('tune', help='Tune a parameter')
    param_tune_parser.add_argument('name', type=str, choices=ctx.param_list, help='Name of the parameter')
    param_tune_parser.set_defaults(func=ctx.tune_param)

    # Plugin subcommands
    plugin_parser = subparsers.add_parser('plugin', help='Manage plugins')
    plugin_subparsers = plugin_parser.add_subparsers(title="subcommands", dest="subcommand")

    plugin_switch_parser = plugin_subparsers.add_parser('switch', help='Start or stop or abort a plugin')
    plugin_switch_parser.add_argument('name', type=str, choices=ctx.plugin_list, help='Name of the plugin')
    plugin_switch_parser.add_argument('value', type=str, choices=('start', 'stop', 'abort', '1', '0'), help='Flag to start or stop or abort the plugin')
    plugin_switch_parser.set_defaults(func=ctx.switch_plugin)

    plugin_list_parser = plugin_subparsers.add_parser('list', help='List all plugins')
    plugin_list_parser.add_argument('--status', action='store_true', help='Show status of the plugins')
    plugin_list_parser.set_defaults(func=ctx.list_plugins)

    plugin_status_parser = plugin_subparsers.add_parser('status', help='Get status of a plugin')
    plugin_status_parser.add_argument('name', type=str, choices=ctx.plugin_list, help='Name of the plugin')
    plugin_status_parser.set_defaults(func=ctx.status_plugin)

    # Filter subcommands
    filter_parser = subparsers.add_parser('filter', help='Manage filters')
    filter_subparsers = filter_parser.add_subparsers(title="subcommands", dest="subcommand")

    filter_set_parser = filter_subparsers.add_parser('set', help='Set a filter')
    filter_set_parser.add_argument('value', type=str, help='Value of the filter cutoff frequency [Hz]')
    filter_set_parser.set_defaults(func=ctx.set_filter)

    filter_get_parser = filter_subparsers.add_parser('get', help='Get the filter cutoff frequency')
    filter_get_parser.set_defaults(func=ctx.get_filter)

    filter_enable_parser = filter_subparsers.add_parser('enable', help='Enable a filter')
    filter_enable_parser.add_argument('value', type=str, help='Flag to enable or disable the filter')
    filter_enable_parser.set_defaults(func=ctx.enable_filter)

    # Clear cache command
    clear_parser = subparsers.add_parser('clear', help='Clear the cache')
    clear_parser.set_defaults(func=ctx.clear_cache)
    
    # Watch command
    watch_parser = subparsers.add_parser('watch', help='Watch the robot state')
    
    watch_stats = watch_parser.add_subparsers(title="subcommands", dest="subcommand")
    watch_stats_parser = watch_stats.add_parser('stats', help='Watch the robot stats')
    watch_stats_parser.add_argument('--num-secs', '-n', type=float, default=1, help='Number of seconds between each update')
    watch_stats_parser.set_defaults(func=ctx.watch_stats)
    
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    
    ctx.init_ros()

    try:    
        args.func(args)
    except TimeoutError:
        print("timeout error: check that xbot2 is running")

if __name__ == "__main__":
    main()