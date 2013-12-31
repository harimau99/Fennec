"""
Default configuration for Fennec
"""

BR_DEBUG = False;

BR_PARSERS = [
	# The order defines the priority of the parsers
    'fennec.parsers.parser_text',
    'fennec.parsers.parser_author',
    'fennec.parsers.parser_makefile',
    'fennec.parsers.parser_c_lang',
    'fennec.parsers.parser_c_headers',
    'fennec.parsers.parser_c_source',
]

BR_READ_ENV = True # If set to False, the info will be inferred from the files
