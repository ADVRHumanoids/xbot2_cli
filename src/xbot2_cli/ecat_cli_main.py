import argparse
import argcomplete
from xbot2_cli.ecat_context import Context

def main():

    context = Context()

    parser = argparse.ArgumentParser(description="ECAT CLI")
    parser.add_argument('--uri', type=str, required=False, help='URI of the ECAT master')
    parser.add_argument('--update-cache', action='store_true', help='Update autocompletion cache')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # config command
    config_parser = subparsers.add_parser('config', help='Configuration operations')
    # config_subparsers = config_parser.add_subparsers(dest='subcommand', help='Configuration subcommands')

    # config uri
    config_parser.add_argument('name', type=str, choices=['uri',], help='Option name')
    config_parser.add_argument('value', type=str, nargs='?', help='Option value (leave empty to print)')
    config_parser.set_defaults(func=context.set_config_or_print)

    # sdo command
    sdo_parser = subparsers.add_parser('sdo', help='SDO operations')
    sdo_subparsers = sdo_parser.add_subparsers(dest='subcommand', help='SDO subcommands')

    # sdo list
    sdo_list_parser = sdo_subparsers.add_parser('list', help='List SDOs')
    sdo_list_parser.add_argument('--id', type=int, required=True, help='ID of the ECAT slave')
    sdo_list_parser.set_defaults(func=context.list_sdo)

    # sdo read
    sdo_read_parser = sdo_subparsers.add_parser('read', help='Read SDO')
    sdo_read_parser.add_argument('name', nargs='+', choices=context.sdo_list, help='Name of the SDO to read')
    sdo_read_parser.add_argument('--id', nargs='+', type=int, help='ID of the ECAT slave')
    sdo_read_parser.set_defaults(func=context.read_sdo)

    # sdo write
    sdo_write_parser = sdo_subparsers.add_parser('write', help='Write SDO')
    sdo_write_parser.add_argument('name', type=str, choices=context.sdo_list, help='name of the SDO to write')
    sdo_write_parser.add_argument('value', type=str, help='Value to write to the SDO')
    sdo_write_parser.add_argument('--id', nargs='+', type=int, help='ID of the ECAT slave')
    sdo_write_parser.set_defaults(func=context.write_sdo)

    # sdo cmd
    cmd_parser = subparsers.add_parser('cmd', help='Send cmd via SDO')
    cmd_parser.add_argument('cmd', type=str, choices=context.cmd_dict.keys(), help='Command name')
    cmd_parser.add_argument('--id', type=int, required=True, help='ID of the ECAT slave')
    cmd_parser.set_defaults(func=context.exec_cmd)

    # list command
    list_parser = subparsers.add_parser('list', help='List available items')
    list_parser.set_defaults(func=context.list_id)

    argcomplete.autocomplete(parser)

    args = parser.parse_args()

    if args.uri:
        context.set_uri(args)
        return

    if args.update_cache:
        context.update_cache()
        return

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()