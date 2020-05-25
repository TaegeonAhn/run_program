import pyodbc
import csv
import time
import os
import pandas as pd

import numpy

start = time.time() #시작 시간 저장

file_list=[]
all_data = []

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.csv':
                    #print(full_filename)
                    #full_filename = full_filename.replace("/", "\\")
                    file_list.append(full_filename)
                    #print(full_filename)
    except PermissionError:
        pass
search('D:/TEST/챠트프로2/')

folder_directory = "D:/PythonFile/"
os.makedirs(folder_directory, exist_ok=True)
#file_list.replace("/","\")
print(file_list)
#data = pandas.DataFrame([])
    #read_csv (file_path,sep=",",dtype ='unicode')

for file_path in file_list:
    #print(file_path)
    data = pd.read_csv(file_path,sep="|", dtype='unicode')
    all_data.append(data)
dataCombine = pd.concat(all_data, axis = 0, ignore_index= True )
dataCombine.to_csv('{}result_line.csv' .format(folder_directory), index=False, encoding='utf-8-sig')

#result_line = pd.read_csv()
#df1 = data[["검사일자","챠트번호","검사코드","검사명칭","검사결과"] ]


#    data.(pandas.DataFrame(read_csv (file_path)))

 #   print(conn_str)
  #  file_path_tokens = file_path.split("\\")
   # file_name = file_path_tokens[-1]
    #print(file_path_tokens)
    #print(file_name)
    #conn_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별9.mdb;')
    #UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;axScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DefaultDir=C:\;
    #conn = pyodbc.connect(conn_str)

    #cursor = conn.cursor()

print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

