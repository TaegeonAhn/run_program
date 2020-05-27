## 원내처방 + 원외처방 + 처방메모
import glob; import csv; import time; import os;
import pandas as pd
import numpy

start = time.time() #시작 시간 저장

file_list=[]

input_folder_directory = "D:/TEST/챠트프로2"
output_folder_directory = "D:/PythonFile/"
os.makedirs(output_folder_directory, exist_ok=True) #폴더생성

def get_list(database, dirlist):
    for path_list in dirlist:
        file_list = pd.read_csv(path_list, sep="|", dtype='unicode')
        return database.append(file_list)


patient = []
prescription = []
prescription_slip = []
prescription_memo = []
receiption = []
payment = []

patient_column = ["챠트번호","수진자명","주민등록","전화번호","우편번호","주소1","주소2","성별","나이","최종내원일","보험구분"]
prescript_column = ["챠트번호","진료일자","순번","처방코드","처방명칭","용량","일투","처방의번호"]
prescript_slip_column = ["챠트번호","발행일자","순번","처방코드","처방명칭","용량","일투","연번호"]
prescript_memo_column = ["챠트번호","진료일자","순번","내역코드","메모1","메모2","메모3","메모4","메모5"]
receiption_column = ["진료일자","챠트번호","접수구분","접수시간","나이","개월수","진료의사","진료시간"]
payment_column = ["진료일자","챠트번호","보험총진료비","보험본인부담금","보험청구액","비급여","수납액"]

#file_list.replace("/","\")
patient_list = glob.glob(os.path.join(input_folder_directory,'환자정보.MDB_환자정*')) #환자정보
reception_list = glob.glob(os.path.join(input_folder_directory,'진료색인*_진료색인.csv')) #접수정보
workspace_list1 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방.csv')) #원내처방정보
workspace_list2 = glob.glob(os.path.join(input_folder_directory,'처방전19*_처방.csv')) #원외처방정보
workspace_list4 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방메모.csv')) #처방메모정보

######################환자 정보#################################
for patient_path in patient_list:
    p_list = pd.read_csv(patient_path, sep="|", dtype='unicode')
    patient. append(p_list)

patient_data = pd.concat(patient, axis = 0, ignore_index= True)
df = pd.DataFrame (patient_data, columns= patient_column)

######################접수 정보#################################
for receipt_path in reception_list:
    r_list = pd.read_csv(receipt_path, sep="|", dtype='unicode')
    receiption. append(r_list)

receiption_data = pd.concat(receiption, axis = 0, ignore_index= True)
df0 = pd.DataFrame (receiption_data, columns= receiption_column)

######################수납 정보#################################
for payment_path in payment_list:
    pay_list = pd.read_csv(payment_path, sep="|", dtype='unicode')
    payment. append(r_list)

payment_data = pd.concat(payment, axis = 0, ignore_index= True)
df5 = pd.DataFrame (payment_data, columns= payment_column)

######################원내 처방#################################
for jinryo_path1 in workspace_list1:
    pre1 = pd.read_csv(jinryo_path1,sep="|", dtype='unicode')
    prescription.append(pre1)

prescription_data = pd.concat(prescription, axis = 0, ignore_index= True)
df1 = pd.DataFrame (prescription_data, columns= prescript_column)

######################원외 처방#################################
#for work_path2 in workspace_list2:
#    pre2 = pd.read_csv(work_path2,sep="|", dtype='unicode')
#    prescription_slip.append(pre2)

#prescription_slip_data = pd.concat(prescription_slip, axis = 0, ignore_index= True)
#df2 = pd.DataFrame (prescription_slip_data, columns = prescript_slip_column)

######################처방 메모#################################
for jinryo_path4 in workspace_list4:
    pre4 = pd.read_csv(jinryo_path4,sep="|", dtype='unicode')
    prescription_memo.append(pre4)

prescription_memo_data = pd.concat(prescription_memo, axis = 0, ignore_index= True)
df4 = pd.DataFrame (prescription_memo_data, columns = prescript_memo_column)

merged_prescript = pd.merge(df1,df4,left_on=['챠트번호','진료일자','순번'], right_on=['챠트번호','진료일자','순번'], how = 'left')

df0.to_csv('{}receipt.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig') # csv 생성
df.to_csv('{}patient.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig') # csv 생성
merged_prescript.to_csv('{}jinryo.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')


print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

##############################################################################




