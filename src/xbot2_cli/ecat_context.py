#todo(@alaurenzi) generate python code from proto if needed

from xbot2_cli.ecat.api import read_sdo, write_sdo, set_uri, reply_cmd, set_timeout
from xbot2_cli.ecat.base_io import master_cmd_get_slave_descr, flash_cmd_save_flash
from xbot2_cli.ecat.base_cmd import SdoInfo
from xbot2_cli.utils import print_table, as_list, fetch_from_cache, write_to_cache

from dataclasses import dataclass, field
import os
import yaml
from typing import List, Dict

@dataclass
class Arguments:
    uri: str = ''
    id: int = -1
    name: List[str] = field(default_factory=list)
    value: str = ''
    cmd: str = ''

class Context:

    def __init__(self, cli=True, uri=None):

        # cmds
        self.cmd_dict = {
            'CIRCULO_SAVE_PARAMS': ('Save_Params', 1702257011), 
            'ADVRF_POWER_MOTORS_ON': ('ctrl_status_cmd', 72), 
            'ADVRF_POWER_MOTORS_OFF': ('ctrl_status_cmd', 132),
        }

        # set uri from persistent config
        if uri is None:
            uri = self.get_config('uri', 'localhost:5555')
            self.set_uri(Arguments(uri=uri))
        else:
            self.set_uri(Arguments(uri=uri))

        # fetch sdo list from cache
        self.cache_file = os.path.expanduser('~/.config/xbot2_cli/cache_ecat.yaml')
        cache_dict = fetch_from_cache(self.cache_file, ['sdo_list', 'sdo_dict'])
        if cache_dict is not None:
            self.sdo_list = cache_dict['sdo_list']
            self.sdo_dict = cache_dict['sdo_dict']
        else:
            self.sdo_list = None 
            self.sdo_dict = None


    def update_cache(self):
        self.sdo_list = set()
        self.sdo_dict = dict()
        for id in self.list_id(Arguments(), verbose=False):
            if id < 0:
                continue
            print(id)
            sdo = self.list_sdo(Arguments(id=id), verbose=False)
            self.sdo_dict[id] = sdo
            self.sdo_list.update(sdo)
        write_to_cache(self.cache_file, {'sdo_list': list(self.sdo_list), 'sdo_dict': self.sdo_dict})

    def set_config_or_print(self, args: Arguments, verbose=True):
        if args.value is None:
            config = self.get_config(args.name)
            if verbose:
                print(config)
            return config
        self.set_config({args.name: args.value})

    def set_config(self, config_dict):
        config_dir = os.path.expanduser('~/.config/xbot2_cli')
        config_file = os.path.join(config_dir, 'config.yaml')
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                existing_config = yaml.safe_load(file)
                existing_config.update(config_dict)
                config_dict = existing_config
        os.makedirs(config_dir, exist_ok=True)
        
        with open(config_file, 'w') as file:
            yaml.dump(config_dict, file)
    
    def get_config(self, key, default=None):
        config_dir = os.path.expanduser('~/.config/xbot2_cli')
        config_file = os.path.join(config_dir, 'config.yaml')
        if not os.path.exists(config_file):
            return default
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            return config.get(key, default)

    def set_uri(self, args: Arguments, verbose=True):
        set_uri(args.uri)

    def list_id(self, args: Arguments, verbose=True):
        try:
            res = reply_cmd(master_cmd_get_slave_descr)
        except KeyError:
            verbose and print('Failed to list IDs')
            return []
        ids = [int(v['robot_id']) for v in res.values()]
        verbose and print(ids)
        return ids
    
    def list_sdo(self, args: Arguments, verbose=True):
        res = reply_cmd(SdoInfo(u'SDO_NAME').set_bid(args.id))
        if not isinstance(res, list):
            raise RuntimeError('Failed to list SDOs')
        if verbose:
            print('\n'.join(res))
        return res

    def read_sdo(self, args: Arguments, verbose=True):
        # check args.id is a list of integers
        id = as_list(args.id, check_none=False)
        if len(id) == 0:
            id = self.list_id(args, verbose=False)
        name = as_list(args.name)
        res = read_sdo(name, id)
        rows = [['ID'] + name]
        if verbose:
            for id, sdos in res.items():
                if not isinstance(sdos, dict):
                    continue
                row = [id]
                for n in name:
                    row.append(sdos[n])
                rows.append(row)
            print_table(rows)
        return res
    
    def write_sdo(self, args: Arguments, verbose=True):
        id = as_list(args.id, check_none=False)
        if len(id) == 0:
            id = self.list_id(args, verbose=False)
        name = as_list(args.name)
        value = as_list(args.value)
        res = write_sdo(dict(zip(name, value)), id)
        self.read_sdo(args, verbose=verbose)
    
    def exec_cmd(self, args: Arguments, verbose=True):
        sdo_name, sdo_value = self.cmd_dict[args.cmd]
        self.write_sdo(args=Arguments(id=args.id, value=sdo_value, name=sdo_name), verbose=True)
    

# set_uri('kyon-mio-5375:5555')

# res = reply_cmd(master_cmd_get_slave_descr)
# print(res)

# ids = [v['robot_id'] for v in res.values()]
# print(ids)


# res = read_sdo(['Assigned_name'], ids[1:])
# print(res)

# res = reply_cmd(SdoInfo(u'SDO_NAME').set_bid(61))
# print(res)

# res = reply_cmd(SdoInfo(u'SDO_OBJD').set_bid(61))
# print(res)
