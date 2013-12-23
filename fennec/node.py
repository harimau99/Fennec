
import os
import logging

class Node(object):
    """
    A Node is a file of directory. It contains data associated to a file
    and other useful file manipulation information used with fennec.
    """
    def __init__(self, node_path):
        self.logger = logging.getLogger('fennec')
        # check if exists
        try:
            with open(node_path, 'r'):
                # exists, create object
                if (os.path.isfile(node_path)):
                    self.is_file = True
                elif (os.path.isdir(node_path)):
                    self.is_dir = True
                self.path = os.path.abspath(node_path)
                self.logger.info("The \"{0}\" path exists".format(node_path))
        except IOError:
           self.logger.error("The \"{0}\" path doesn't exist !".format(node_path))
           raise
