from utils import SettingLoader as sl
from splitter import ExcelSplitter as es

if __name__ == '__main__':
    settings = sl.SettingLoader()
    split = es.ExcelSplitter(settings)

    split.splitExcelFile()