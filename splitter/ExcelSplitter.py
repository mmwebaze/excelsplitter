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
            #rows, columns = data_frame.shape
            #print(data_frame[0])
            #df = data_frame.loc[data_frame['CountryName'] == 'Ghana']
            #print(df.head(100))
        except IOError as io:
            print(io.__doc__)

    def createExcel(self, data_frame, listOfnames, columnName):
        #df = data_frame.loc[data_frame['CountryName'] == 'Ghana']
        for item in listOfnames:
            print(columnName + ':' + item+'.xlsx being created')
            df = data_frame.loc[data_frame[columnName] == item]
            df.to_excel(self.settings['output_folder']+item+'.xlsx');



    def getColumnName(self, data_frame):

        return data_frame.columns.values[self.settings['column']]

    def getColumnValues(self, data_frame, columnName):
        listOfColumnValues = data_frame[columnName].values
        cleanedList = [x for x in listOfColumnValues if str(x) != 'nan']
        uniqueList = list(set(cleanedList))
        #uniqueList.remove('nan')
        return uniqueList