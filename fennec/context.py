"""
Context processor

This is the main brain of Fennec.

TODO:
  - LOAD files and sort them: author > Makefiles > Headers > C source
"""

import os
import copy
import logging
import importlib
from collections import defaultdict
from . import node

class Context(object):
    """
    Context is the brain of fennec: it manages the global variables,
    the file paths and the parser to apply to each file and in what order.
    """

    files = [ ]

    parsers = [ ]

    tests = defaultdict(list)

    flags = {
        'has_DS_Store': False,
        'has_hidden_files': False
    }

    def __init__(self, settings):
        self.logger = logging.getLogger('fennec')
        self.settings = settings
        if (self.settings.get('read_env')):
            self.read_env()
        self.load_parsers()
        self.create_container()

    def read_env(self):
        if (os.environ.get('USER') != None):
            self.user_name = os.environ.get('USER')
        else:
            self.logger.warning("There is no USER environment variable !"
                                " You should check your shell !")
        if (os.environ.get('GROUP') != None):
            self.user_group = os.environ.get('GROUP')
        else:
            self.logger.warning("There is no GROUP environment variable !"
                                " You should check your shell !")
        if (os.environ.get('MAIL') != None):
            self.user_mail = os.environ.get('MAIL')
        else:
            self.logger.warning("There is no MAIL environment variable !"
                                " You should check your shell !")

    def load_parsers(self):
        for parser in self.settings.get('parsers'):
            self.load_parser(parser)

    def load_parser(self, name):
        try:
            module = importlib.import_module(name)
        except ImportError:
            self.logger.error("The {0} parser could not be imported !!".
                            format(name))
            raise
        self.parsers.append(module.parser)

    def load_path(self, path):
        if (os.path.isdir(path)):
            for dirpath, dnames, fnames in os.walk(path):
                dnames[:] = [d for d in dnames if not d == '.git']
                for f in fnames:
                    if f == '.DS_Store':
                        self.flags['has_DS_Store'] = True
                    elif f.startswith('.'):
                        self.flags['has_hidden_files'] = True
                    elif f.endswith('.o'):
                        continue
                    elif f.endswith('.a'):
                        continue
                    else:
                        self.load_file(os.path.join(dirpath, f))
        else:
            self.load_file(path)

    def load_file(self, file_path):
        try:
            with open(file_path):
                n = node.Node(file_path, self.settings)
                self.files.append(n)
                self.logger.debug("The \"{0}\" path was added".
                                    format(file_path))
        except IOError:
            self.logger.error("The \"{0}\" path doesn't exist".
                                    format(file_path))
            return
        for parser in self.parsers:
            if (parser.accepted(n)):
                self.tests[n].append(parser)

    def create_container(self):
        self.container = {
            'env_user_name': self.user_name,
            'env_user_group': self.user_group,
            'env_user_email': self.user_mail,
            'author': None,
            'makefile': list(),
            'header': None,
            'source': None
        }

    def check_container_consistency(self):
        # TODO: Must check if author (or authors) are consistent accross files
        # (author +++, Makefile and header ++, source files +)
        pass

    def check_context_flags(self):
        if self.flags['has_DS_Store'] == True:
            self.logger.info("Your path(s) contains .DS_Store file(s).")
        if self.flags['has_hidden_files'] == True:
            self.logger.warning("Your path(s) contains one or more "
                                "hidden files. Be careful.")

    def order_by_priority(self):
        # Order nodes by priority: Author files first, then Makefiles,
        # then headers and then C files
        # -- TODO --
        pass

    def audit(self):
        self.order_by_priority()
        for node, parsers in self.tests.iteritems():
            for parser in parsers:
                pars = parser(self.container, self.settings, node)
                pars.audit()
        self.check_container_consistency()
        self.check_context_flags()



