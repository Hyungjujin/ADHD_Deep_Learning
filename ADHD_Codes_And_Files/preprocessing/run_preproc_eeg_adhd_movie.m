%rawdata: '/home/jykang/data_adhd/dat1/unzipped/';
addpath('/home/jykang/calc_hjjin/matlabtool/eeglab2021.0/plugins/Fieldtrip-lite20210411/')
addpath('/home/jykang/calc_hjjin/matlabtool/eeglab2021.0/plugins/fitTwoDipoles0.01')

dataPath = '/home/jykang/data_adhd/dat1/movie_unzipped/';
resultPath = '/home/jykang/data_adhd/dat1/movie_preproced/';

groupName   = {'ADHD_Combined_Type','ADHD_Inattentive_Type','No_Diagnosis_Given','ADHD_Hyperactive_Impulsive_Type'};
for num_group = 3 %:length(groupName)  
    group_dataPath = fullfile(dataPath, groupName{num_group});
    group_resultPath = fullfile(resultPath, groupName{num_group});
    tmp = dir([group_dataPath '/NDAR*video']);
    for nS = 32 :length(tmp)
        nowList{nS} = tmp(nS).name; %NDARxx_video
        video_datapath=fullfile(group_dataPath, nowList{nS});
        video_resultpath=fullfile(group_resultPath, nowList{nS});
        mkdir(video_resultpath)
        tmp2= dir([video_datapath '/NDAR*Video*.mat']);
        for n=1:length(tmp2)
            nowList2{n}=tmp2(n).name;
            try
                preproc_eeg_adhd_movie(video_datapath, nowList2{n}, video_resultpath, nowList2{n}) 
            catch
                disp('error')
            end    
        end
    end
end 