import pandas as pd
import os
import tarfile
import shutil

'----------preperation----------'

downloaded_path='/home/jykang/data_adhd/dat1/EEG/'
flist_path='/home/jykang/data_adhd/classify_by_diagnosis/'
flist=os.listdir(flist_path)
f=open('/home/jykang/data_adhd/dat1/unzipped/no_video.txt','r')
no_video=f.readlines()
f.close()
csv=pd.read_csv('/home/jykang/data_adhd/data_set_result.csv')
csv['EEGFiles']=0

'----------start process---------'

for directory in flist:
	'make directorys by diagnosis'
	diagnosis_dir_name='/home/jykang/data_adhd/dat1/movie_unzipped'+'/'+directory.rstrip('_clean.txt')
	if not os.path.exists(diagnosis_dir_name):
		os.makedirs(os.path.join(diagnosis_dir_name))	
	'read list of ID in directory'
	print('now saving '+directory.rstrip('_clean.txt'))
	IDfile=open(flist_path+'/'+directory)
	filename_list=IDfile.readlines()
	IDfile.close()
	
	'process data in directory name'
	
	i=1
	for filename in filename_list:
		filename=filename.rstrip('\n')
		if filename+'.tar.gz' in os.listdir(downloaded_path):
			outdir=diagnosis_dir_name
			print('now processing '+filename)
			'if already extracted, skip'
			if os.path.isfile(outdir+'/'+filename+'_rawRestingstate.mat') or (filename in no_video):
				print('already extracted')
				i+=1
				continue
			else:
				try:
					'unzip'
					tmp=tarfile.open(downloaded_path+'/'+filename+'.tar.gz')
					tmp.extractall(outdir)
					tmp.close()
					'make list of existing EEG_file_list if it exists'
					unzipped_dir=outdir+'/'+filename+'/EEG/raw/mat_format'
					if os.path.isdir(unzipped_dir):
						EEG_file_list=os.listdir(unzipped_dir)
						'save file in csv'
						csv.loc[csv.data_name==filename,('EEGFiles')]=str(EEG_file_list)
						csv.to_csv('/home/jykang/data_adhd/data_set_dataFilesAdded.csv')
						
						'save indiv. data to NDAR*_video folder'
						data_path=outdir+'/'+filename+'_video'
						os.makedirs(os.path.join(data_path))
						
						for item in EEG_file_list:
							if 'Video' in item:
								os.rename(unzipped_dir+'/'+item, data_path+'/'+filename+'_'+item)
								print('saved')
						shutil.rmtree(outdir+'/'+filename)
						print(str(i)+' item done')
				except Exception as e:
					print('error opening file '+filename)
					print(e)
				i+=1
				
f= open('/home/jykang/data_adhd/dat1/unzipped/no_video.txt','w')
for item in no_video:
	f.write(item+'\n')
f.close()

