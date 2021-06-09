import pandas as pd

filename='C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\9994_ConsensusDx_20210504_col_clean.csv'
csv1=pd.read_csv(filename, low_memory=False)


filename2='C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\9994_Basic_Demos_20210504_col_clean.csv'
csv2=pd.read_csv(filename2)

diagnosis=['ADHD-Combined Type','ADHD-Hyperactive/Impulsive Type', 'ADHD-Inattentive Type', 'No Diagnosis Given']
is_ADHD= ((csv1['ConsensusDx_010']==diagnosis[0]) | (csv1['ConsensusDx_010']==diagnosis[1]) | (csv1['ConsensusDx_010']==diagnosis[2]) | (csv1['ConsensusDx_010']==diagnosis[3]))
ADHD=csv1[is_ADHD]

ADHD=ADHD.drop_duplicates(['ConsensusDx_001'])
csv2=csv2.drop_duplicates(['BASIC1_001'])


csv2.rename(columns={"BASIC1_001": "ConsensusDx_001", "BASIC1_004" : "Sex", "BASIC1_005" : "Age"}, inplace=True)
result_csv=pd.merge(csv2, ADHD, on='ConsensusDx_001', how='right')

result_csv=result_csv.astype({'Sex':int, 'Age':int})


result_csv.to_csv('data_set_result.csv', index=False, header=False)
csv1.to_csv(filename+'_clean.csv', index=False, header=False)
csv2.to_csv(filename2+'_clean.csv', index=False, header=False)


