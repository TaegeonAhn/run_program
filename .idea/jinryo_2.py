## 원내처방 + 원외처방 합치기
import glob; import csv; import time; import os;
import pandas as pd; import numpy;

start = time.time() #시작 시간 저장

file_list=[]

input_folder_directory = "D:/TEST/챠트프로2"
output_folder_directory = "D:/PythonFile/"
os.makedirs(output_folder_directory, exist_ok=True) #폴더생성

prescription = []
prescription_slip = []

prescript_column = ["챠트번호","진료일자","순번","처방코드","처방명칭","용량","일투","처방의번호"]
prescript_slip_column = ["챠트번호","발행일자","순번","처방코드","처방명칭","용량","일투","연번호"]

#file_list.replace("/","\")
#patient_list = glob.glob(os.path.join(input_folder_directory,'환자정보.MDB_환자정*')) #환자정보
#reception_list = glob.glob(os.path.join(input_folder_directory,'진료색인*')) #접수정보
workspace_list1 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방.csv')) #원내처방정보
workspace_list2 = glob.glob(os.path.join(input_folder_directory,'처방전19*_처방.csv')) #원외처방정보
#workspace_list3 = glob.glob(os.path.join(input_folder_directory,'처방전19*_원내주사.csv')) #원내주사정보
#workspace_list4 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방메모.csv')) #처방메모정보

print(workspace_list1)
print("끗")
print(workspace_list2)
print("끗")
#print(workspace_list3)
#print("끗")
#print(workspace_list4)
#print("끗")

for work_path1 in workspace_list1:
    pre1 = pd.read_csv(work_path1,sep="|", dtype='unicode')
    prescription.append(pre1)

prescription_data = pd.concat(prescription, axis = 0, ignore_index= True)
#prescription_data.columns =  [prescript_column]

print(prescription_data.columns)

for work_path2 in workspace_list2:
    pre2 = pd.read_csv(work_path2,sep="|", dtype='unicode')
    prescription_slip.append(pre2)


prescription_slip_data = pd.concat(prescription_slip, axis = 0, ignore_index= True)
#prescription_slip_data.columns = prescript_slip_column

merged_prescript = pd.concat([prescription_data, prescription_slip_data], axis = 0, join = 'outer')

#= pd.merge (prescription_data, prescription_slip_data, how = 'outer')

merged_prescript.to_csv('{}mm19.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')

print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

##############################################################################


#dataCombine = pd.concat(all_workspace, axis = 0, ignore_index= True )
#dataCombine.to_csv('{}workspace.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')


