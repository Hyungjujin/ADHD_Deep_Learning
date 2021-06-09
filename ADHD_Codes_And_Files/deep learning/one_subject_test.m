load('NDARKA958FAH.mat','data');
for i= 0: 9
   total_data(i+1,:,:)= data(1,:,i*7500+1:(i+1)*7500);
   label(i+1)=0;
end
clearvars('data')
load('NDARRZ653HKY.mat','data');
i=0;
for i=0 : 9
    total_data(i+11,:,:)=data(1,:,i*7500+1:(i+1)*7500);
    label(i+11)=1;
end
save('test2_data.mat', 'total_data');
label=reshape(label,20,[]);
save('test2_label.mat', 'label');
