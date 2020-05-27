## 원내처방 + 원외처방 + 처방메모
import glob; import csv; import time; import os; import numpy;
import pandas as pd

start = time.time() #시작 시간 저장

file_list=[]

input_folder_directory = "D:/TEST/챠트프로2"
output_folder_directory = "D:/PythonFile/"
os.makedirs(output_folder_directory, exist_ok=True) #폴더생성

patient = []
prescription = []
prescription_slip = []
prescription_memo = []
receiption = []
payment = []
foundation = []

# 마이그레이션할 컬럼
patient_column = ["챠트번호","수진자명","주민등록","전화번호","우편번호","주소1","주소2","성별","나이","최종내원일","보험구분"]
prescript_column = ["챠트번호","진료일자","순번","처방코드","처방명칭","용량","일투","처방의번호"]
prescript_slip_column = ["챠트번호","발행일자","순번","처방코드","처방명칭","용량","일투","연번호"]
prescript_memo_column = ["챠트번호","진료일자","순번","내역코드","메모1","메모2","메모3","메모4","메모5"]
receiption_column = ["진료일자","챠트번호","접수구분","접수시간","나이","개월수","진료의사","진료시간"]
payment_column = ["진료일자","챠트번호","보험총진료비","보험본인부담금","보험청구액","비급여","수납액"]
foundation_column = ["처방코드","한글명칭","영문명칭","설정용량","설정일수","청구코드","항","목"]

# 마이그레이션할 파일
#file_list.replace("/","\")
patient_list = glob.glob(os.path.join(input_folder_directory,'환자정보.MDB_환자정*')) #환자정보
reception_list = glob.glob(os.path.join(input_folder_directory,'진료색인*_진료색인.csv')) #접수정보
medicalcare_list1 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방.csv')) #원내처방정보
#medicalcare_list2 = glob.glob(os.path.join(input_folder_directory,'처방전19*_처방.csv')) #원외처방정보
medicalcare_list3 = glob.glob(os.path.join(input_folder_directory,'챠트19*_처방메모.csv')) #처방메모정보
foundation_list = glob.glob(os.path.join(input_folder_directory,'처방자료.MDB_처방자료.csv')) #등록처방정보
foundation_list2 = glob.glob(os.path.join(input_folder_directory,'처방자료.MDB_처방경고.csv')) #등록처방메모정보
foundation_list3 = glob.glob(os.path.join(input_folder_directory,'참고자료.MDB_처방.csv')) #등록처방정보

def get_list(database, dirlist):
    for path_list in dirlist:
        file_list = pd.read_csv(path_list, sep="|", dtype='unicode')
        database.append(file_list)
    database_data = pd.concat(database, axis = 0, ignore_index = True)
    return database_data

######################환자 정보#################################
df00 = pd.DataFrame(get_list(patient, patient_list), columns=patient_column)
df00.to_csv('{}patient.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig') # csv 생성
######################접수 정보#################################
df01 = pd.DataFrame(get_list(receiption, reception_list), columns=receiption_column)
df01.to_csv('{}receipt.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig') # csv 생성
######################수납 정보#################################
df02 = pd.DataFrame(get_list(payment, reception_list), columns=payment_column)
df02.to_csv('{}payment.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig') # csv 생성
######################진료 정보#################################
df03 = pd.DataFrame(get_list(prescription, medicalcare_list1), columns=prescript_column) #원내 처방
df04 = pd.DataFrame(get_list(prescription_memo, medicalcare_list3), columns=prescript_memo_column)  #처방 메모
merged_medicalcare = pd.merge(df03,df04, left_on=["챠트번호","진료일자","순번"], right_on=["챠트번호","진료일자","순번"], how= 'left')
merged_medicalcare.to_csv('{}jinryo.csv' .format(output_folder_directory), index=False, encoding='utf-8-sig')

######################기초 자료#################################
#df05 = pd.DataFrame(get_list(foundation, foundation_list), columns = foundation_column )
#df06 = pd.DataFrame(get_list(fo))


print("총 소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

##############################################################################




