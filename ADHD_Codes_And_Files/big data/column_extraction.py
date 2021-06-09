import pandas as pd
filename='C:\\Users\\jinhj\\OneDrive\\바탕 화면\\연대의대\\예2\\초연멘\\11주차\\9994_ConsensusDx_20210504.csv'
csv1=pd.read_csv(filename, low_memory=False)
csv_row=csv1.iloc[:,[4,13]]
csv_row.to_csv(filename+'_clean.csv', index=False, header=False)
