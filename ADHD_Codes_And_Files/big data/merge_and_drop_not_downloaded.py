import pandas as pd
import numpy as np

filename='/projects4/CMIdata2021/data_set_isFiles.csv'
csv1=pd.read_csv(filename, low_memory=False)


filename2='/projects4/CMIdata2021/data_set_withvideoloc.csv'
csv2=pd.read_csv(filename2)
csv2=csv2.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'isRestingstate', 'isVideo', 'EEGFiles'], axis=1)

csv2.rename(columns={"data_name": "filename"}, inplace=True)

result_csv=pd.merge(csv1, csv2, on='filename', how='right')
result_csv=result_csv.dropna(subset=['isResting'])

result_csv=result_csv[['filename','sex','age','age_group','diagnosis','EEG_file_list','isResting','isVideo1','isVideo2','isVideo3','isVideo4','isVideoDM','isVideoFF','isVideoTP','isVideoWK','fourvid','isEyeRestingtxt', 'isEyeVideo1txt', 'isEyeVideo2txt', 'isEyeVideo3txt', 'isEyeVideo4txt', 'isEyeVideoDMtxt', 'isEyeVideoFFtxt', 'isEyeVideoTPtxt', 'isEyeVideoWKtxt', 'eyefourvidtxt', 'isEyeRestingidf', 'isEyeVideo1idf', 'isEyeVideo2idf', 'isEyeVideo3idf', 'isEyeVideo4idf', 'isEyeVideoDMidf', 'isEyeVideoFFidf', 'isEyeVideoTPidf', 'isEyeVideoWKidf', 'eyefourvididf', 'isRestingPreproc','VideoOrder']]

print(result_csv)

result_csv.to_csv('data_set_isFiles_result.csv', index=False)
