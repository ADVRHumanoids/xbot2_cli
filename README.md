
# xbot2_cli

xbot2_cli is a command-line interface (CLI) application designed to provide an easy way to interact with the XBot framework. 

## Setup

### Prerequisites
```bash
# install system dependencies
sudo apt update
sudo apt install python3-pip python3-venv

# create a virtualenv for this package (mandatory on Python >= 3.12)
cd xbot2_cli
python3 -m venv venv/xbot2_cli
source venv/xbot2_cli/bin/activate
```

### Installing the package
To install xbot2_cli, you can use pip. Make sure you have sourced your virtualenv, then run:

```bash
pip install -e .
```

This will install the package along with its dependencies.

Tab completion is supported via running the following line in your shell.

```bash
echo eval \"\$(register-python-argcomplete xbot2)\" >> ~/.bashrc
```

## Usage

Make sure you sourced the virtualenv; you can run the CLI by executing the following command in your terminal:

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

# watch execution statustics (refreshed every half second)
xbot2 watch stats -n 0.5

# clear the internal cache (this is used to avoid querying xbot2 for params and plugins on each TAB press)
xbot2 clear
```
