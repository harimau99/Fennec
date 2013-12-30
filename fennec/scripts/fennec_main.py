"""
Fennec
======

Fennec main
"""

import sys
import argparse

from .. import __version__
from .. import Fennec

def fennec_main(root_path):
    # Parsing the command line for options and names
    cli_args = argparse.ArgumentParser(
        #usage = '',
        description = 'A 42 School source code format checker. Maybe more.'
        )
    cli_args.add_argument('--version', '-v', action='version',
                        version="fennec " + __version__)
    cli_args.add_argument('--config', '-c', help='configuration file to use.',
                        metavar='<config/file>')
    cli_args.add_argument('--clean', help='clean logs and traces of code audit.',
                        action='store_true', default=False)
    cli_args.add_argument('paths', help='path(s) of files or directories to audit.',
                        nargs='*')

    cli_param = cli_args.parse_args()

    if len(sys.argv) == 1:
        cli_args.print_help()
        exit()

    # Initialize Fennec and load file paths
    fennec = Fennec(cli_param.paths, root_path)

    if cli_param.clean == True:
        fennec.clean()
        print "Done cleaning of log/* and trace/*."
        exit()

    # Set complementary flags
    if cli_param.config != None:
        fennec.set_configfile(cli_param.config)

    if cli_param.clean == True:
        fennec.clean()

    # Audit the code !
    fennec.logger.get_logger().info("Starting code audit...")
    fennec.audit()
    fennec.logger.get_logger().info("Done code audit.")
    print "Done."
