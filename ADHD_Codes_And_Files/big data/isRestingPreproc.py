import pandas as pd
import numpy as np
import os
'cd /projects4/CMIdata2021/preproced/rawRestingState/by_diagnosis/'
csv_path='/projects4/CMIdata2021/preproced/data_set.csv'
data=pd.read_csv(csv_path)

group_list=['ADHD_Combined_Type','ADHD_Inattentive_Type','No_Diagnosis_Given','ADHD_Hyperactive_Impulsive_Type']
result=[]
data['isRestingPreproc']=0
for i in range (0,len(group_list)):
	path_dir='/projects4/CMIdata2021/preproced/rawRestingState/by_diagnosis/'+group_list[i]
	file_list = os.listdir(path_dir)
	
	for item in file_list:
		if 'set' in item:
			item=item.rstrip('_amica_result.set')
			result.append(item)
isRestingPreproc=[]
for data_name in data['data_name']:
  	if data_name not in result:
  		isRestingPreproc.append(0)
  	else:
  		isRestingPreproc.append(1)
data['isRestingPreproc']=isRestingPreproc

data.to_csv(csv_path)
