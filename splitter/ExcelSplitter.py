import pandas as pd
import numpy as np

class ExcelSplitter:
    def __init__(self, settingLoader):
        self.settings = settingLoader.loadSettings()
        pass
    def splitExcelFile(self):
        try:
            #settings = self.settingLoader.loadSettings()
            data_frame = pd.read_excel(self.settings['data_file'], sheet_name=0)
            column = self.getColumnName(data_frame)
            ls = self.getColumnValues(data_frame, columnName=column)
            self.createExcel(data_frame, ls, column)

        except IOError as io:
            print(io.__doc__)

    def createExcel(self, data_frame, listOfnames, columnName):
        outputType = self.settings['output_type']
        outputFolder = self.settings['output_folder']

        for item in listOfnames:
            df = data_frame.loc[data_frame[columnName] == item]
            print(columnName + ': ' + item + '.'+outputType+' being created')
            if outputType == 'xlsx':
                df.to_excel(outputFolder+item+'.'+outputType)
            else:
                df.to_csv(outputFolder+item+'.'+outputType)

    def getColumnName(self, data_frame):

        return data_frame.columns.values[self.settings['column']]

    def getColumnValues(self, data_frame, columnName):
        listOfColumnValues = data_frame[columnName].values
        cleanedList = [x for x in listOfColumnValues if str(x) != 'nan']
        uniqueList = list(set(cleanedList))
        #uniqueList.remove('nan')
        return uniqueList