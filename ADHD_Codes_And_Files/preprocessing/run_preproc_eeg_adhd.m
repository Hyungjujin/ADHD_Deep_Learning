%rawdata: '/home/jykang/data_adhd/dat1/unzipped/';
addpath('/home/jykang/matlabtool/eeglab2021.0/plugins/Fieldtrip-lite20210411/')
addpath('/home/jykang/matlabtool/eeglab2021.0/plugins/fitTwoDipoles0.01')

dataPath = '/home/jykang/data_adhd/dat1/unzipped/';
resultPath = '/home/jykang/data_adhd/dat1/preproced/';

groupName   = {'ADHD_Combined_Type','ADHD_Inattentive_Type','No_Diagnosis_Given','ADHD_Hyperactive_Impulsive_Type'};
for num_group = 3 %:length(groupName)
    clearvars nowList
    group_dataPath = fullfile(dataPath, groupName{num_group});
    group_resultPath = fullfile(resultPath, groupName{num_group});

    %cd(group_path);
    tmp = dir([group_dataPath '/NDAR*raw*.mat']);
    for nS = 1:length(tmp)
        nowList{nS} = tmp(nS).name(1:12); %NDARxx
        preproc_eeg_adhd(group_dataPath, nowList{nS}, group_resultPath, nowList{nS}) 
    end
end