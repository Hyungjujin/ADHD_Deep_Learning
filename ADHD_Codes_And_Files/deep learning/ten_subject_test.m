
dataPath = '/home/jykang/data_adhd/Deeplearning/target/MAT';
groupName   = {'ADHD_Combined_Type','No_Diagnosis_Given'};
ACT={'NDARAC462DZH.mat', 'NDARAD224CRB.mat', 'NDARBP398JHL.mat', 'NDARHF568GL5.mat', 'NDARDN924BV2.mat', 'NDAREY741MG9.mat', 'NDARFW038ZNE.mat', 'NDARHG594GKH.mat','NDARKW521EMY.mat', 'NDARKW565ZT9.mat'};
NDJ={'NDARBK082PDD.mat', 'NDAREK549XUQ.mat', 'NDARGX443CEU.mat', 'NDARJJ356DAL.mat', 'NDARMF508PA2.mat', 'NDARVV473XTY.mat', 'NDARVV926KLM.mat', 'NDARXC418YG7.mat', 'NDARMW178UDD.mat', 'NDARTC527WPZ.mat'}
for num_group =1 :length(groupName)
    clearvars nowList
    group_dataPath = fullfile(dataPath, groupName{num_group});
    tmp = dir([group_dataPath '/NDAR*.mat']);
    for nS = 1:10%length(tmp)
        nowList{nS} = tmp(nS).name; 
        load(nowList{nS}, 'data');
        data_all(id_subject,:,:)=data(1,:,1:15000);
        label(id_subject)=num_group-1;
        id_subject=id_subject+1;
    end
end 
save('total_data.mat', 'data_all')
label=reshape(label,20,[]);
save('total_label.mat', 'label')
