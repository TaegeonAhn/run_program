import glob
import csv
import time
import os
import pandas as pd
import numpy

start = time.time() #시작 시간 저장

file_list=[]
all_patient = []
input_folder_directory = "D:/챠트프로/ExportFiles"
output_folder_directory = "D:/PythonFile/"
os.makedirs(output_folder_directory, exist_ok=True) #폴더생성
#file_list.replace("/","\")
patient_list = glob.glob(os.path.join(input_folder_directory,'환자정보.MDB_환자정*')) #환자정보
print(patient_list)

for patient_path in patient_list:
    patient_data = pd.read_csv(patient_path,sep="|", dtype='unicode')
    all_patient.append(patient_data)

dataCombine = pd.concat(all_patient, axis = 0, ignore_index= True )
dataCombine.to_csv('{}patient.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')



print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

