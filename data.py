# comapany wants call on  numbers whom they can call


import pandas as pd
import numpy as np
df=pd.read_excel("Customer Call List (1).xlsx")

#dropping duplicates
df=df.drop_duplicates()
#droping unsuefull coulmn 
df=df.drop(columns="Not_Useful_Column")
#stiping the extra characters from last_name column 
df["Last_Name"]=df['Last_Name'].str.strip("_./")
#phone number cleaning we will make them to certain order format and wholly numeric 
df['Phone_Number'] = df['Phone_Number'].replace(r'[\/\-|]', '', regex=True)
df["Phone_Number"]=df['Phone_Number'].apply(lambda x:str(x))
df["Phone_Number"]=df['Phone_Number'].apply(lambda x:x[0:3] + "-" + x[3:6] + "-" +x[6:10])
df['Phone_Number'] = df['Phone_Number'].replace('Na--', '')
df['Phone_Number'] = df['Phone_Number'].replace('nan--', '')

#Cleaning the address column by spiliting ito colums 
df[['Street_Address', 'State']] = df['Address'].apply(lambda x: pd.Series(x.split(',', 1)))


#making paying cutomers columns yes,No to y or n
df['Paying Customer']=df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer']=df['Paying Customer'].str.replace('No','N')

#making Do not contact  columns yes,No to y or n
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')

# eliminating the N/a from all dataset 
df=df.replace("N/a","")

df=df.fillna('')


#removing all those whom we have not to call 
for i in df.index:
   if  df.loc[i,"Do_Not_Contact"]=='Y':
    df.drop(i,inplace=True)
for i in df.index:
   if  df.loc[i,"Phone_Number"]=='':
    df.drop(i,inplace=True)
#assigning all N whom we can call
df['Do_Not_Contact']=df['Do_Not_Contact']='N'
#filling empty data of state with unkowmn

df['State'] = df['State'].apply(lambda x: 'unknown' if  x == '' else x)
df.reset_index(drop=True, inplace=True)
print(df)
#importing matplotlib
import matplotlib.pyplot as pyplot

fn=df['First_Name'] + df['Last_Name']
pyplot.plot(df['Paying Customer'],fn ,marker='o',color='green',lw='7')
pyplot.xlabel('Paying or Not')
pyplot.ylabel('Customers Names')
pyplot.title('Paying and Non Paying Customers ')
pyplot.savefig('pnpvisual.png',facecolor="yellow",edgecolor='black')
pyplot.show()

