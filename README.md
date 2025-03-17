# xbot2_cli/xbot2_cli/README.md

# xbot2_cli

xbot2_cli is a command-line interface (CLI) application designed to provide an easy way to interact with the XBot framework. 

## Installation

To install xbot2_cli, you can use pip. Make sure you have Python 3.6 or higher installed, then run:

```bash
pip install .
```

This will install the package along with its dependencies.

Tab completion is supported via running the following line in your shell (it can be added to bashrc)

```bash
eval "$(register-python-argcomplete xbot2)"  # note the ""!
```

## Usage

After installation, you can run the CLI by executing the following command in your terminal:

```bash
xbot2
```

You can view the available commands and options by using the `--help` flag:

```bash
xbot2 --help
```

### Examples

```bash
# list available plugins, optionally with their current status
xbot2 plugin list 
xbot2 plugin list --status

# start a plugin
xbot2 plugin switch homing start

# set filters cutoff freq
xbot2 filter set 10.0

# disable filter
xbot2 filter enable false

# clear the internal cache (this is used to avoid querying xbot2 for params and plugins on each TAB press)
xbot2 clear
```