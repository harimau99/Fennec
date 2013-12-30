VERSION = "0.0.3"

__author__ = "Klemen Sever <ksever@student.42.fr>"
__copyright__ = "Copyright 2013, Klemen Sever"
__credits__ = []
__license__ = "GPL"
__version__ = VERSION
__status__ = "Prototype"

import os
import os.path as path
import glob
import inspect
from settings.settings import Settings
from logger import Logger
from context import Context

class Fennec(object):

    def __init__(self, files_list, root_path = None):
        if (root_path == None):
            root_path = path.abspath(path.join(
                        path.abspath(path.dirname(
                        path.abspath(inspect.getfile(
                            inspect.currentframe())))), ".."))
        self.logger = Logger(root_path)
        self.settings = Settings(root_path)
        self.context = Context(self.settings)
        for filepath in files_list:
            self.context.load_path(filepath)

    def set_settings(self, name, value):
        self.settings.set(name, value)

    def set_configfile(self, path_config):
        # try importing from given path
        try:
            self.settings.read_file(path_config)
            return
        except IOError:
            pass
        # try importing in default config dir
        root_path = self.settings.get('root_path')
        try:
            self.settings.read_file(path.join(
                        root_path, "settings", "config", path_config + '.py'))
            return
        except IOError:
            pass
        # try importing from current working directory in config dir
        curr_dir = path.abspath(os.getcwd())
        try:
            self.settings.read_file(path.join(
                        curr_dir, "config", path_config + '.py'))
            return
        except:
            self.logger.get_logger().error("Could not impot configuration file")
            raise

    def add_paths(self, paths):
        for path in paths:
            self.context.load_path(path)

    def audit(self):
        """
        Launch code audit process
        """
        self.context.audit()

    def clean(self):
        """
        Cleans the logs, traces and temporary files (if there are some)
        """
        log_path = os.path.join(self.settings.get('root_path'), "log", "*")
        traces_path = os.path.join(self.settings.get('root_path'), "trace", "*")
        to_remove = glob.glob(log_path)
        for node in to_remove:
           os.remove(node)
        to_remove = glob.glob(traces_path)
        for node in to_remove:
           os.remove(node)
        self.logger.get_logger().info("Finished cleaning.")
