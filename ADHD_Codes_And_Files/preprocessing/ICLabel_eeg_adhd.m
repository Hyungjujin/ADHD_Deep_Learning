
%addpath(genpath('~/matlabtool/eeglab2021.0/'))
function ICLabel_eeg_adhd(fin_path, fin_name, fout_path, fout_name) 

file_input = fullfile(fin_path, [fin_name '_amica_result.set']);
filename=strcat(fin_name, '_amica_result.set');
file_sft = '/home/jykang/calc_hjjin/HBN-ADHD_3g_3s_2/GSN_HydroCel_129.sfp';

out_dir = fullfile(fout_path, fout_name);
%EEG = pop_loadset(file_input)

EEG = pop_loadset(filename, fin_path);

EEG = iclabel(EEG, 'default');
brainIdx = find(EEG.etc.ic_classification.ICLabel.classifications(:,1) >= 0.7);
rvList= [EEG.dipfit.model.rv];
goodRvIdx= find(rvList < 0.15); 
goodIcIdx= intersect(brainIdx, goodRvIdx);
EEG = pop_subcomp(EEG, goodIcIdx, 0, 1);
%EEG.etc.ic_classification.ICLabel.classifications = EEG.etc.ic_classification.ICLabel.classifications(goodIcIdx,:);


EEG = pop_saveset( EEG, 'filename',[fout_name '_ICLabel_result.set'],'filepath',fout_path);

end
