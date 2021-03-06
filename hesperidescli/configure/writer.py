import sys

from hesperidescli.configure.configfile import ConfigFile


class ConfigFileWriter(ConfigFile):
    def update_config(self, section, values, extra_config_flag):
        self._write(self._CONFIG_FILE_PATH, section, values, extra_config_flag)

    def update_credentials(self, section, values, extra_config_flag):
        self._write(self._CREDENTIALS_FILE_PATH, section, values, extra_config_flag)

    def remove_config_section(self, section):
        self._remove_section(self._CONFIG_FILE_PATH, section)

    def remove_profile(self):
        self.config.remove_option('config', 'profile')
        with open(self._CONFIG_FILE_PATH, 'w') as configfile:
            self.config.write(configfile)

    def remove_credentials_section(self, section):
        self._remove_section(self._CREDENTIALS_FILE_PATH, section)

    def _remove_section(self, file_path, section):
        self.config.read(file_path)
        if section in self.config.sections():
            self.config.remove_section(section)
        with open(file_path, 'w') as configfile:
            self.config.write(configfile)

    def _write(self, file_path, section, values, extra_config_flag):
        self.config.read(file_path)
        if extra_config_flag:
            # set current profile
            if 'profile' in values:
                if values['profile'] not in self.config.sections():
                    print('Could not add profile. Profile conf does not exist')
                    sys.exit(1)
        else:
            if section not in self.config.sections():
                self.config.add_section(section)
        for key in values.keys():
            self.config.set(section, key, values[key])
        with open(file_path, 'w') as configfile:
            self.config.write(configfile)
