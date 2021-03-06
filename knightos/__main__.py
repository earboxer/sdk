#!/usr/bin/env python3
import sys
import os
import pkg_resources  # part of setuptools

version = pkg_resources.require("knightos")[0].version

default_emulator="z80e-sdl"
default_debugger="z80e-sdl --debug"

if os.name == 'nt': # Windows
    default_emulator="wabbitemu"
    default_debugger="wabbitemu"

doc = """KnightOS SDK

Usage:
  knightos init [<name>]
        [--emulator=<emulator>]
        [--assembler=<assembler>]
        [--compiler=<compiler>]
        [--template=<template>]
        [--debugger=<debugger>]
        [--platform=<platform>]
        [--vcs=<vcs>]
        [--kernel-source=<path>]
        [--force]
        [--reinit-missing]
  knightos install [--site-only] [--local-path=<path>] <packages>...
  knightos install-base
  knightos query <key>
  knightos -h | --help
  knightos --version

Options:
  init                      Initializes a new KnightOS project here or sets up an existing one
                            [name] is required when creating new projects.
  install                   Installs the specified packages
  install-base              Installs packages required to run a complete version of KnightOS
  query                     Queries the project's package.config for <key>. Useful for automation.
  --site-only               Installs the package but does not add it to package.config
  --local-path=<path>       Installs the package using a local copy of the source code.
  --assembler=<assembler>   Specifies an alternate assembler. [default: sass]
  --compiler=<compiler>     Specifies an alternate C compiler. [default: kcc]
  --template=<template>     Specifies a template. [default: assembly]
  --emulator=<emulator>     Specifies an alternate emulator. [default: {0}]
  --debugger=<debugger>     Specifies an alternate debugger. [default: {1}]
  --platform=<platform>     Specifies the calculator model to target. [default: TI84pSE]
                            Supported platforms are: TI73, TI83p, TI83pSE, TI84p, TI84pSE, TI84pCSE
  --vcs=<vcs>               Specifies an alternate version control system. [default: git]
                            Supported systems are: git, hg
  --kernel-source=<path>    Instead of downloading a kernel, compile one from <path>. Useful for testing kernels.
  --reinit-missing          Regenerate missing files from the template
  --force                   Installs the SDK in this directory even if not empty
  -h --help                 Show this screen.
  --version                 Show version.


""".format(default_emulator, default_debugger)

from docopt import docopt
from knightos.commands.init import execute as cmd_init
from knightos.commands.install import execute as cmd_install
from knightos.commands.installbase import execute as cmd_installbase
from knightos.commands.query import execute as cmd_query

if __name__ == "__main__":
    args = docopt(doc, version=version)

    if args["--platform"]:
        if not args["--platform"] in [ "TI73", "TI83p", "TI83pSE", "TI84p", "TI84pSE", "TI84pCSE" ]:
            sys.stderr.write("'{0}' is not a supported platform.\n".format(args["--platform"]))
            sys.exit(1)
        if args["--emulator"] == 'z80e-sdl':
            args["--emulator"] += " -d " + args["--platform"]
            args["--debugger"] += " -d " + args["--platform"]

    if args["init"]:
        cmd_init(project_name = args["<name>"],
            assembler = args["--assembler"],
            emulator = args["--emulator"],
            debugger = args["--debugger"],
            platform = args["--platform"],
            vcs = args["--vcs"],
            kernel_source = args["--kernel-source"],
            compiler = args["--compiler"],
            template = args["--template"],
            force = args["--force"],
            reinit_missing = args["--reinit-missing"])
    if args["install"]:
        cmd_install(args["<packages>"],
                site_only=args["--site-only"],
                local_path=args["--local-path"])
    if args["install-base"]:
        cmd_installbase()
    if args["query"]:
        cmd_query(args["<key>"])
