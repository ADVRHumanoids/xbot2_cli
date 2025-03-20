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

class Context:

    def __init__(self):
        # set uri from persistent config
        uri = self.get_config('uri', 'localhost:5555')
        self.set_uri(Arguments(uri=uri))
        set_timeout(200)

        # fetch sdo list from cache
        cache_file = '/tmp/xbot2_cli_cache_ecat.yaml'
        self.sdo_list = fetch_from_cache(cache_file, ['sdo_list'])
        if self.sdo_list is None:
            self.sdo_list = set()
            for id in self.list_id(Arguments(), verbose=False):
                if id < 0:
                    continue
                sdo = self.list_sdo(Arguments(id=id), verbose=False)
                self.sdo_list.update(sdo)
            write_to_cache(cache_file, {'sdo_list': list(self.sdo_list)})
        else:
            self.sdo_list = self.sdo_list['sdo_list']

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
    
    def save_to_flash(self, args: Arguments, verbose=True):
        res = reply_cmd(flash_cmd_save_flash.set_bid(args.id))
        verbose and print(res)
    

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
