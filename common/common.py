import os
import readConfig as readConfig
from xlrd import open_workbook
proDir = readConfig.proDir
def get_xls(xls_name,sheet_name):
    """
    get interface data from xls file
    :param xls_name:
    :param sheet_name:
    :return:
    """
    cls=[]
    xlsPath=os.path.join(proDir,"testFile",'case',xls_name)
    file=open_workbook(xlsPath)
    #get sheet by name
    sheet=file.sheet_by_name(sheet_name)
    nrows=sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0]!=u'case_name':
            cls.append(sheet.row_values(i))
    return cls
if __name__=="__main__":
    result=get_xls("tokenCase.xlsx","gettoken")
    print(isinstance(result[0][0],str))