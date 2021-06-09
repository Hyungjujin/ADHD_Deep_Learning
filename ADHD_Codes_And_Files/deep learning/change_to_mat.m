
%addpath(genpath('~/matlabtool/eeglab2021.0/'))
function change_to_mat(fin_path, fin_name, fout_path, fout_name) 

file_input = fullfile(fin_path, [fin_name '_ICLabel_result.set']);
filename=strcat(fin_name, '_ICLabel_result.set')
file_sft = '/home/jykang/calc_hjjin/HBN-ADHD_3g_3s_2/GSN_HydroCel_129.sfp';

out_dir = fullfile(fout_path, fout_name);
%EEG = pop_loadset(file_input)

EEG = pop_loadset(filename, fin_path);
fname=strcat(fout_path,'/', fout_name, '.mat');
data=EEG.data;
data=reshape(data,1,129,[]);

save(fname,'data');

end
