import os
import logging
import importlib
from . import node

class Context(object):
    """
    Context is the brain of fennec: it manages the global variables,
    the file paths and the parser to apply to each file and in what order.
    """

    files = [ ]

    parsers = { }

    def __init__(self, settings):
        self.logger = logging.getLogger('fennec')
        self.settings = settings
        if (self.settings.get('read_env')):
            self.read_env()
        self.load_parsers()

    def read_env(self):
        if (os.environ.get('USER') != None):
            self.user_name = os.environ.get('USER')
        else:
            self.logger.error("There is no USER environment variable ! You should check your shell !")
        if (os.environ.get('GROUP') != None):
            self.user_group = os.environ.get('GROUP')
        else:
            self.logger.error("There is no GROUP environment variable ! You should check your shell !")
        if (os.environ.get('MAIL') != None):
            self.user_mail = os.environ.get('MAIL')
        else:
            self.logger.error("There is no MAIL environment variable ! You should check your shell !")

    def load_parsers(self):
        for parser in self.settings.get('parsers'):
            self.load_parser(parser)

    def load_parser(self, name):
        try:
            module = importlib.import_module(name)
        except ImportError:
            self.logger.error("The {0} parser could not be imported !!".format(parser))
            raise
        self.parsers[module.name] = module.Parser

    def load_path(self, file_path):
        try:
            with open(file_path):
                self.files.append(node.Node(file_path))
                self.logger.debug("The \"{0}\" path was added".format(file_path))
        except IOError:
            self.logger.error("The \"{0}\" path doesn't exist".format(file_path))
            return

