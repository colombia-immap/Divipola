# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:48:30 2022

@author: Lisa
"""


import os
import pandas as pd



# Select the directory
os.chdir("C:/Users/Lisa/Documents/Bases de Python/Bases Actualizables")

#read my database 
df_5w  = pd.read_excel("C:/Users/Lisa/Documents/Bases de Python/Bases Actualizables/5W_Colombia_-_RMRP_2022_Consolidado dos_25042022.xlsx")

#create a new column name: Full Name, it is generated through the concatenation of the department and municipality names 
df_5w["Full Name"] = df_5w["Admin Departamento"] + df_5w["Admin Municipio"]

#See the names for the months and select the one to filter 
df_5w['Mes de atención'].unique()

#See the names for the sectors and select the one to filter
df_5w['_ Sector'].unique()

#Filter by the month and the sector 
df_5w_sector_mes = df_5w[(df_5w['_ Sector']=='Salud')&(df_5w['Mes de atención'] == '03_Marzo')]

#read another database 
df_api_ind_mpio  = pd.read_excel("C:/Users/Lisa/Documents/Bases de Python/Bases Actualizables/API_Consolidado GENERAL_ciclo dos_26042022.xlsx", sheet_name= "Indicador y Municipio")

#create a new column name: Full Name, it is generated through the concatenation of the department and municipality names 
df_api_ind_mpio["Full Name"] = df_api_ind_mpio["Departamento"] + df_api_ind_mpio["Municipio"]

#Filter by the month and the sector 
df_api_sector_mes = df_api_ind_mpio[(df_api_ind_mpio['Sector']=='Salud')&(df_api_ind_mpio['Mesdeatención'] == '03_Marzo')]

#read my database of divipola: there are the right names and codes we want to add 

divipola = pd.read_excel("C:/Users/Lisa/Documents/Bases de Python/Bases Actualizables/divipolita.xlsx")

#Same proces:create a new column name: Full Name, it is generated through the concatenation of the department and municipality names 
divipola["Full Name"] = divipola["Departamento"] + divipola["Municipio"]
divipola["Full Name"] = divipola["Full Name"].drop_duplicates()

#Clean the text, delete numbers, delete acents, lowercase, replace names.. 
def standardize_territories(column):
    column = column.str.replace("_"," ", regex=True)
    column = column.map(lambda x: x.lower())
    column = column.map(lambda x: x.strip())
    column = column.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    column = column.str.replace(r'[^\w\s]+', '', regex=True)
    column = column.str.replace("narinotumaco","narinosan andres de tumaco", regex=True)
    return column


# Apply the funtion made before 
df_5w_sector_mes['Full Name'] = standardize_territories(df_5w_sector_mes['Full Name'])
df_api_sector_mes['Full Name'] = standardize_territories(df_api_sector_mes['Full Name'])
divipola['Full Name'] = standardize_territories(divipola['Full Name'])


#Aditioning the Divipola Code

df_5w_sector_mes = pd.merge(df_5w_sector_mes, divipola, how= 'left', left_on = 'Full Name',
                 right_on = 'Full Name')

#See if there is any error 
if df_5w_sector_mes['Full Name'].isna().sum() > 1:
    print('Ajustar full name')
    
if df_5w_sector_mes['dpto'].isna().sum() > 1:
    print('Ajustar Divipola dpto')
    
if df_5w_sector_mes['mpio'].isna().sum() > 1:
    print('Ajustar Divipola mpio')

# Generate a dataframe with the values sorted to see the error more easily if needed

#prueba = df_5w_sector_mes['Full Name'].sort_values()

#prueba1 = divipola['Full Name'].sort_values()


#Aditioning the Divipola Code# Adicionar el divipola más adecuado
df_api_sector_mes = pd.merge(df_api_sector_mes, divipola, how= 'left', left_on = 'Full Name',
                 right_on = 'Full Name')

#See if there is any error 
if df_api_sector_mes['Full Name'].isna().sum() > 1:
    print('Ajustar full name')
    
if df_api_sector_mes['dpto'].isna().sum() > 1:
    print('Ajustar Divipola dpto')
    
if df_api_sector_mes['mpio'].isna().sum() > 1:
    print('Ajustar Divipola mpio')
    
# Generate a dataframe with the values sorted to see the error more easily if needed

#prueba = df_api_sector_mes['Full Name'].sort_values()

#prueba1 = divipola['Full Name'].sort_values()    


# see the columns and select the ones needed
df_api_sector_mes.columns 
df_api_sector_mes = df_api_sector_mes[['Mesdeatención', 'Sector','dpto','Departamento_x','mpio', 'Municipio_x','bene_mensuales']]

#see the columns and select the ones needed
df_5w_sector_mes.columns 
df_5w_sector_mes = df_5w_sector_mes[['Socio Principal Nombre','dpto','Admin Departamento', 'mpio', 'Admin Municipio']]

#Save the new datasets and imported to the folder
Writer= pd.ExcelWriter("C:/Users/Lisa/Documents/Bases de Python/Bases Actualizables/final.xlsx")

df_api_sector_mes.to_excel(Writer, sheet_name='Api_sector_mes.xlsx')
df_5w_sector_mes.to_excel(Writer, sheet_name='5w_sector_mes.xlsx')



Writer.save()
