import logging
import os
import datetime
import string
import random

class Logger():
	"""
	Creates a beautifully crafted logger object to use with fennec.
	"""

	def __init__(self, root_path):
		self.logger = logging.getLogger('fennec')
		self.logger.setLevel(logging.DEBUG)
		trace_id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(12))
		# Log file that logs everything
		filename = datetime.datetime.now().strftime('log_%Y_%m_%d_%H_%M_%S_' + trace_id + '.log')
		log_file = os.path.join(root_path, 'log', filename)
		self.log_handler = logging.FileHandler(log_file, mode='w')
		self.log_handler.setLevel(logging.DEBUG)
		# Trace file that logs depending on what is asked - Warning by default
		filename = datetime.datetime.now().strftime('trace_%Y_%m_%d_%H_%M_%S_' + trace_id + '.log')
		trace_file = os.path.join(root_path, 'trace', filename)
		self.trace_handler = logging.FileHandler(trace_file, mode='w')
		self.trace_handler.setLevel(logging.WARNING)
		# Console logger - Prints warnings and above
		self.console_handler = logging.StreamHandler()
		self.console_handler.setLevel(logging.WARNING)
		# Formatter of messages
		formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)-8s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		self.log_handler.setFormatter(formatter)
		self.trace_handler.setFormatter(formatter)
		self.console_handler.setFormatter(formatter)
		# Add the handlers to the logging
		self.logger.addHandler(self.log_handler);
		self.logger.addHandler(self.trace_handler);
		self.logger.addHandler(self.console_handler);
		# Start logs by entering message
		self.logger.debug("Starting logger...Done")

	def get_logger(self):
		return self.logger
