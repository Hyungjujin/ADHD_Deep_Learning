
%addpath(genpath('~/matlabtool/eeglab2021.0/'))
function preproc_eeg_adhd(fin_path, fin_name, fout_path, fout_name) 

file_input = fullfile(fin_path, [fin_name '_rawRestingstate']);
file_sft = '/home/jykang/calc_hjjin/HBN-ADHD_3g_3s_2/GSN_HydroCel_129.sfp';

out_dir = fullfile(fout_path, fout_name); % '/home/jykang/data_adhd/dat1/preproced/YYY'
%EEG = pop_loadset('filename','XXX_rawRestingState','filepath','/projects1/pi/jsur/HBN-ADHD/rawdata/YYY/');
EEG = pop_loadset(file_input);

EEG = pop_resample( EEG, 250);

EEG = pop_eegfiltnew(EEG,'locutoff',1,'hicutoff',0,'filtorder',1650,'revfilt',0,'usefft',[],'plotfreqz',0);
%EEG = pop_eegfiltnew(EEG, 'locutoff',1,'revfilt',1,'plotfreqz',1);

%EEG=pop_chanedit(EEG, 'load','C:\EEG\HBN-ADHD_3g_3s\\GSN_HydroCel_129.sfp','filetype','sfp');
EEG = pop_chanedit(EEG, 'load',{ file_sft 'filetype' 'autodetect'});
originalEEG = EEG;

%EEG = pop_cleanline(EEG, 'bandwidth',2,'chanlist',[1:129] ,'computepower',1,'linefreqs',60,'newversion',0,'normSpectrum',0,'p',0.01,'pad',2,'plotfigures',0,'scanforlines',0,'sigtype','Channels','taperbandwidth',2,'tau',100,'verb',1,'winsize',4,'winstep',1);
%EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion',5,'ChannelCriterion',0.8,'LineNoiseCriterion',4,'Highpass','off','BurstCriterion',20,'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian','WindowCriterionTolerances',[-Inf 7] );

EEG = pop_cleanline(EEG,'bandwidth',2,'chanlist',[1:EEG.nbchan],...
    'computepower',0,'linefreqs',[50 100 150 200 250]        ,...
    'normSpectrum',0,'p',0.01,'pad',2,'plotfigures',0        ,...
    'scanforlines',1,'sigtype','Channels','tau',100,'verb',1 ,...
    'winsize',4,'winstep',4);

EEG = clean_rawdata(EEG,5,-1,0.85,4,20,0.25);

EEG = pop_interp(EEG, originalEEG.chanlocs, 'spherical');

EEG.nbchan = EEG.nbchan+1;
EEG.data(end+1,:) = zeros(1, EEG.pnts);
EEG.chanlocs(1,EEG.nbchan).labels = 'initialReference';
EEG = pop_reref(EEG, []);
EEG = pop_select( EEG,'nochannel',{'initialReference'});

if  isfield(EEG.etc,'clean_channel_mask')
    dataRank = min([rank(double(EEG.data')) sum(EEG.etc.clean_channel_mask)]);
else
    dataRank = rank(double(EEG.data'));
end

%[EEG.icawieghts,EEG.icasphere,
runamica15(EEG.data,'num_chans',EEG.nbchan, ...
    'outdir', out_dir, ...
    'pcakeep',dataRank,'num_models',1,'do_reject',1,...
    'numrej',15,'rejsig',3,'rejint',1, 'max_threads', 32);
EEG.etc.amica = loadmodout15(out_dir);
EEG.etc.amica.S = EEG.etc.amica.S(1:EEG.etc.amica.num_pcs,:);
EEG.icaweights = EEG.etc.amica.W;
EEG.icasphere = EEG.etc.amica.S;
EEG = eeg_checkset(EEG,'ica');

for i = 1:length(EEG.chaninfo.nodatchans)
    if strfind(EEG.chaninfo.nodatchans(i).labels,'Fid')==1
        EEG.chaninfo.nodatchans(i).labels(1:3) = [];
    end
end


[~,coordinateTransformParameters] = coregister(EEG.chaninfo.nodatchans, ...
    fullfile(fileparts(which('eeglab')),'plugins','dipfit','standard_BEM'     , ...
    'elec','standard_1005.elc'),'warp','auto','manual','off');

templateChannelFilePath = fullfile(fileparts(which('eeglab')),...
    'plugins','dipfit','standard_BEM',...
    'elec','standard_1005.elc');
hdmFilePath = fullfile(fileparts(which('eeglab')),'plugins',...
    'dipfit','standard_BEM','standard_vol.mat');
mriFile = fullfile(fileparts(which('eeglab')),'plugins',...
    'dipfit','standard_BEM','standard_mri.mat');

EEG = pop_dipfit_settings(EEG,'hdmfile',hdmFilePath,'coordformat','MNI',...
    'mrifile',mriFile,'chanfile',templateChannelFilePath, ...
    'coord_transform',coordinateTransformParameters,'chansel',1:EEG.nbchan);
EEG = pop_multifit(EEG,1:EEG.nbchan,'threshold',100,'dipplot','off',...
    'plotopt',{'normlen','on'});

EEG = fitTwoDipoles(EEG,'LRR',35);


%EEG = pop_runica(EEG, 'icatype', 'runica', 'extended',1,'interrupt','on');

EEG = pop_saveset( EEG, 'filename',[fout_name '_amica_result.set'],'filepath',fout_path);
end
