import pyodbc
import csv
import time
import os
import pandas
import numpy

start = time.time() #시작 시간 저장

file_list=[]
k = []
data_run = subprocess.run()
("D:\챠트프로\test.exe")

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.mdb':
                    print(full_filename)
                    full_filename = full_filename.replace("/", "\\")
                    file_list.append(full_filename)
                    #print(full_filename)
    except PermissionError:
        pass
search('D:/TEST/')
#search('D:/타사B migration test/챠트자료')

folder_directory = "D:/PythonFile/"
os.makedirs(folder_directory, exist_ok=True)
#file_list.replace("/","\")
#print(file_list)
for file_path in file_list:
    conn_str = (r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                r"DBQ="+file_path+";"r"Uid=admin;")
    #r"Uid=admin;""UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;axScanRows=8;MaxBufferSize=2048;")
    print(conn_str)
    file_path_tokens = file_path.split("\\")
    file_name = file_path_tokens[-1]
    #print(file_path_tokens)
    #print(file_name)
    #conn_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별9.mdb;')
    #UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;axScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DefaultDir=C:\;
    conn = pyodbc.connect(conn_str)

    cursor = conn.cursor()
    table_name_list = [] # table_name reset
    for table_info in cursor.tables(tableType ='TABLE'): #mdb 파일 내 테이블명 획득
        table_name_list.append(table_info.table_name)

    print(table_name_list)

    for table_name in table_name_list:
        print(table_name)

        with open('{}{}.{}.csv'.format(folder_directory,file_name, table_name), 'w', newline='') as f:
            writer=csv.writer(f)
            cursor.execute ('SELECT * FROM {}'.format(table_name))
            columns = [column[0] for column in cursor.description] # 컬럼명 출력
            writer.writerow(columns)
            for row in cursor.fetchall():
                writer.writerow(row)

    print("소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

    cursor.close()
    conn.close()

print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간
k=input("press close to exit")
