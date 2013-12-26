"""
Default configuration for Fennec
"""

BR_DEBUG = False;

BR_PARSERS = {
	# The order defines the priority of the parsers
    'fennec.parsers.parser_text',
    'fennec.parsers.parser_author',
    'fennec.parsers.parser_makefile',
    # 'parsers.parser_c',
}

BR_READ_ENV = True # If set to False, the info will be inferred from the files
