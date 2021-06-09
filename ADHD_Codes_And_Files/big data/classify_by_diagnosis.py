import pandas as pd

'extract only ID and diagnosis'
csv=pd.read_csv('9994_ConsensusDx_20210504.csv',usecols=['EID','DX_01'])

'make dictionary&classify'
dic={}

i=1
while i<len(csv):
    diagnosis=str(csv.loc[i,'DX_01'])
    EID=str(csv.loc[i,'EID'])
    'print(diagnosis)'
    if diagnosis not in dic.keys():
        dic[diagnosis]=[EID]
    else:
        dic[diagnosis].append(EID)
    i+=1

'name correction- some contain /'
tmp=[]
mod_tmp=[]
for diagnosis in dic.keys():
    if "/" in diagnosis:
        mod_diagnosis=diagnosis.replace("/","_")
        tmp.append(diagnosis)
        mod_tmp.append(mod_diagnosis)
    else:
        continue

for i in range(len(tmp)):
    dic[mod_tmp[i]]=dic[tmp[i]]
    del dic[tmp[i]]


"""   
'save by diagnosis'
path='C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\10주차 과제\\classify_by_diagnosis'
for diagnosis in dic.keys():
    fname=path+'\\'+diagnosis+'_subjects.txt'
    file=open(fname ,'w')
    for subject in dic[diagnosis]:
            file.write(subject+'\n')
    file.close
    
"""
