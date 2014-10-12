#!/usr/bin/env python3
"""KnightOS SDK

Usage:
  knightos init <name> [<root>]
  knightos package
  knightos install [--site-only] <package>
  knightos uninstall <package>
  knightos -h | --help
  knightos --version

Options:
  init          Initializes a new KnightOS project here
  package       Bundles this project into a package
  install       Installs the specified dependency
  uninstall     Removes the specified dependency
  --site-only   Installs the package but does not add it to your dependencies
  -h --help     Show this screen.
  --version     Show version.
  

"""
from docopt import docopt
from init import execute as cmd_init
from install import execute as cmd_install

args = docopt(__doc__, version="0.0.1")

if args["init"]: cmd_init(args["<name>"], root=args["<root>"])
if args["install"]: cmd_install(args["<package>"], site_only=args["--site-only"])