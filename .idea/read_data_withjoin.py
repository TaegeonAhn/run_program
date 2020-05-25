import glob
import csv
import time
import os
import pandas as pd
import numpy

start = time.time() #시작 시간 저장

file_list=[]
all_workspace = []
input_folder_directory = "D:/챠트프로/ExportFiles"
output_folder_directory = "D:/PythonFile/"
os.makedirs(output_folder_directory, exist_ok=True) #폴더생성
#file_list.replace("/","\")
#patient_list = glob.glob(os.path.join(input_folder_directory,'환자정보.MDB_환자정*')) #환자정보
#reception_list = glob.glob(os.path.join(input_folder_directory,'진료색인*')) #접수정보
workspace_list = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방.csv')) #처방정보

print(workspace_list)

for workspace_path in workspace_list:
    workspace_data = pd.read_csv(workspace_path,sep="|", dtype='unicode')
    all_workspace.append(workspace_data)

dataCombine = pd.concat(all_workspace, axis = 0, ignore_index= True )
dataCombine.to_csv('{}workspace.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')

print(dataCombine.head)

print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

