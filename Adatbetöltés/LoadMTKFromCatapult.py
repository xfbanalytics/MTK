import pandas as pd
import requests
from env_params import *
import pymssql
from api_table_pairs import *
from utils import new_dict
#from utils import 


conn = pymssql.connect(server=server_ip_address, user=username, password=password, database=database)
cursor = conn.cursor()


for api, values in api_dict.items():
    url = feedurl + api
    response = requests.get(url, headers = headers)
    data_json = response.json()
    dataframes = {}
    #print(values)
    if 'extra' in values.keys():
        for subpart in values['extra']:
            dataframes[values['table_name'] + '_' + subpart] = pd.json_normalize(data_json, subpart, sep = '_')
            #print(subpart)
            data_json = map(lambda x: new_dict(old_dict=x,key_to_pop=subpart),data_json)
    dataframes[values['table_name']] = pd.json_normalize(data_json)
    #print('EZ AZ API: ' + api)

    for key, df in dataframes.items():
        for column in df.columns:
            df[column] = df[column].astype(str)


    print(dataframes.keys())
    for table_name, table in dataframes.items():
        query = '%s,'*len(table.columns)
        query = 'INSERT INTO ' + table_name + '(' + ','.join(table.columns) + ') VALUES ('  + query[0:-1] + ')'
        print(query)
        #cursor.execute('BEGIN TRANSACITON')
        #table = table.to_numpy()
        #table = tuple(map(tuple))
        for i in tuple(map(tuple,table.to_numpy())):
            cursor.execute(query,i)
            try:
                cursor.execute(query,i)
            except:
                print('ITT VAN GOND')
                print(i)
        conn.commit()
        #with pymssql.connect(server=server_ip_address, user=username, password=password, database=database) as conn:
        #    with conn.cursor() as cursor:

    ############EZZEL LEHET MEGCSINÁLNI A CREATE_TABLE DOLGOKAT
    #for table_ane, table in dataframes.items():
    #    string = 'CREATE TABLE ' + table_ane + '(load_timestamp DATETIME DEFAULT GETDATE(),'
    #    for column in table.columns:
    #        string = string +'\n' + column + ' NVARCHAR(MAX),'
    #    string = string[0:-1] + ')'
    #    print(string)

'''

#Creating connection with Database
with pymssql.connect(server=server_ip_address, user=username, password=password, database=database) as conn:
    with conn.cursor() as cursor:
        #load_manager_dict = prepare_load_manager_dict(cursor)'''