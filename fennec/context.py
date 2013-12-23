import os
import logging
from . import node

class Context(object):
    """
    Context is the brain of fennec: it manages the global varibles,
    the file paths and the parser to apply to each file and in what order.
    """

    files = [ ]

    def __init__(self, settings):
        self.logger = logging.getLogger('fennec')
        self.settings = settings
        if (self.settings.get('read_env')):
            self.read_env()

    def read_env(self):
        if (os.environ.get('USER') != None):
            self.settings.set('user_name', os.environ.get('USER'))
        else:
            self.logger.error("There is no USER environment variable ! You should check your shell !")
        if (os.environ.get('GROUP') != None):
            self.settings.set('user_group', os.environ.get('GROUP'))
        else:
            self.logger.error("There is no GROUP environment variable ! You should check your shell !")
        if (os.environ.get('MAIL') != None):
            self.settings.set('user_mail', os.environ.get('MAIL'))
        else:
            self.logger.error("There is no MAIL environment variable ! You should check your shell !")

    def load_path(self, file_path):
        try:
            with open(file_path):
                self.files.append(node.Node(file_path))
                self.logger.info("The \"{0}\" path was added".format(file_path))
        except IOError:
            self.logger.error("The \"{0}\" path doesn't exist".format(file_path))
            return

