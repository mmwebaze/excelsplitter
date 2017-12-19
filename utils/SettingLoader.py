import json

class SettingLoader:
    configFile = '/Users/mwebazem/development/python/ExcelSplitter/config.json'

    def __init__(self):
        #self.configFile = configFile;
        pass

    def loadSettings(self):
        return json.load(open(self.configFile, 'r'))
    def updateSettings(self):
        '''updates saved config file'''
        pass

    def checkConfig(self, configFile):
        '''check config file before saving it'''
        pass