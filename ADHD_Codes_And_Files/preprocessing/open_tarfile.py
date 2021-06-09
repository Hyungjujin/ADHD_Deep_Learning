import os
import tarfile
import shutil

downloaded_path='/hdd_ext/hdd_adhd/adhd_eeg_data2/'
flist_path='/home/jykang/data_adhd/classify_by_diagnosis/'
flist=os.listdir(flist_path)

for directory in flist:
	'make directorys by diagnosis'
	diagnosis_dir_name='/hdd_ext/hdd_adhd/unzipped/'+directory.rstrip('_clean.txt')
	if not os.path.exists(diagnosis_dir_name):
		os.makedirs(os.path.join(diagnosis_dir_name))	
	'read list of ID in directory'
	print('now saving '+directory.rstrip('_clean.txt'))
	IDfile=open(flist_path+'/'+directory)
	filename_list=IDfile.readlines()
	IDfile.close()
	
	i=1
	for filename in filename_list:
		filename=filename.rstrip('\n')
		if filename+'.tar.gz' in os.listdir(downloaded_path):
			outdir=diagnosis_dir_name
			print('now processing '+filename)
			if os.path.isfile(outdir+'/'+filename+'_rawRestingstate.mat'):
				print('already extracted')
				i+=1
				continue
			else:
				try:
					tmp=tarfile.open(downloaded_path+'/'+filename+'.tar.gz')
					tmp.extractall(outdir)
					tmp.close()
					try:
						os.rename(outdir+'/'+filename+'/EEG/raw/mat_format/RestingState.mat',outdir+'/'+filename+'_rawRestingstate.mat')
						print('saved')
						shutil.rmtree(outdir+'/'+filename)
					except Exception as e:
						print(filename+' has no EEG')
						print(e)
						no_eeg.append(filename)
				
					print(str(i)+' item done')
				except Exception as e:
					print('error opening file '+filename)
					print(e)
				i+=1
				

