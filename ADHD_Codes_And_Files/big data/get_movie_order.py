import pandas as pd
import os
import tarfile
import shutil
import numpy as np

downloaded_path='/projects4/CMIdata2021/rawdata/'
data=pd.read_csv('/projects4/CMIdata2021/data_set.csv')
data['VideoOrder']=0
'isVideo=col 10, fname=col 2'
"]"
for i in range(0,len(data['data_name'])):
	tmplist=data.loc[i].tolist()
	filename=tmplist[2]
	if tmplist[10]==1:
		f=tarfile.open(downloaded_path+filename+'.tar.gz')
		flist=f.getnames()
		target_csv_name=filename+'/Behavioral/csv_format/'+filename+'_Video_1.csv'
		if target_csv_name in flist:
			print('now processing '+filename)
			try:
				f.extractall('/projects4/CMIdata2021/')
				tmpdata=pd.read_csv('/projects4/CMIdata2021/'+target_csv_name)
				tmpdata=tmpdata.dropna(subset=['block_perm'])
				name_list=np.array(tmpdata['block_perm'].tolist())
				tmplist[12]=str(name_list)
				data.loc[i]=tmplist
				shutil.rmtree('/projects4/CMIdata2021/'+filename)
			except Exception as e:
				print('error processing file '+filename)
				print(e)			
		f.close()
data.to_csv('/projects4/CMIdata2021/data_set_withvideoloc.csv')
