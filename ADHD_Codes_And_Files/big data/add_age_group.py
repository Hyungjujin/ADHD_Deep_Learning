import pandas as pd
import numpy as np

data=pd.read_csv('C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\data_set_dataFilesAdded.csv')
"data2=pd.read_csv('C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\data_set_dataFilesToAdd2.csv')"

age_group=[]
for age in data['age']:
    if age>=15:
        age_group.append('15~')
    elif age>=10:
        age_group.append('10~14')
    else:
        age_group.append('5~9')

data['age_group']=age_group
                      
data.to_csv('C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\data_set_dataFilesAdded.csv')
