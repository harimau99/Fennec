import os
import sys
import logging

class Settings:
    """
    Settings manager for fennec.
    """

    settings = { }
    dflt_settings = { }

    def __init__(self, root_path):
        """
        Initialize default settings
        """
        self.logger = logging.getLogger('fennec')
        # Set default settings
        try:
            execfile(os.path.join(root_path, "settings/config/default.py"), self.dflt_settings)
        except IOError:
            self.logger.error("The default settings file is missing !\n")
            exit()
        # Add base path to settings
        self.dflt_settings['BR_ROOT_PATH'] = root_path
        # Copy default settings to normal settings
        self.settings = self.dflt_settings.copy()

    def set(self, option_name, value):
        """
        Setter for specified option, you can add your custom options too !
        """
        if ('BR_' + option_name.upper()) in self.settings:
            self.settings['BR_' + option_name.upper()] = value;
        else:
            self.settings['BR_CUSTOM_' + option_name.upper()] = value;

    def get(self, option_name, default = None):
        """
        Getter for specified option and the possibility to return the default
        if none specified
        """
        try:
            result = self.settings['BR_' + option_name.upper()]
            return (result)
        except KeyError:
            pass
        try:
            result = self.settings['BR_CUSTOM_' + option_name.upper()]
            return (result)
        except KeyError:
            pass
        if default == None:
            try:
                result = self.dflt_settings['BR_' + option_name.upper()]
                return (result)
            except KeyError:
                raise
        else:
            return default

    def read_file(self, settings_file_path):
        """
        Read and set what is in the given settings file path. It will override
        all set settings and the custom ones. Should be used with caution !
        """
        execfile(settings_file_path, self.settings)

    def show_settings(self):
        print "===== Settings ====="
        for conf, value in self.settings.iteritems():
            if (conf.startswith('BR_')):
                print "Settings[{0}] = {1}".format(conf, value)
        print "===== Default ====="
        for conf, value in self.dflt_settings.iteritems():
            if (conf.startswith('BR_')):
                print "Settings.Default[{0}] = {1}".format(conf, value)
        print "===== End Settings ====="
