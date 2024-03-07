import pandas as pd
import requests
from env_params import *
import pymssql
from api_table_pairs import *
from utils import new_dict, list_replace
from datetime import datetime
import numpy as np
#from utils import 


START_DATE = datetime.now()


conn = pymssql.connect(server=server_ip_address, user=username, password=password, database=database)
cursor = conn.cursor()


cursor = conn.cursor(as_dict=True)

query = "SELECT DISTINCT id, activity_id FROM input_catapult_periods WHERE created_at >GETDATE()-" + str(days_to_load) + ";"
print(query)
cursor.execute(query)
dict_of_already_loaded_periods = cursor.fetchall()
list_of_to_load_periods = []
hibak = []


cursor = conn.cursor()

query = "SELECT DISTINCT id FROM input_catapult_periods;"
print(query)
cursor.execute(query)
list_of_already_loaded_periods = set([ r[0] for r in cursor.fetchall() ])
#list_of_already_loaded_periods = set([ r[0] for r in results ])
list_of_to_load_periods = []
hibak = []


query = 'SELECT DISTINCT id FROM input_catapult_athletes;'
cursor.execute(query)
results = cursor.fetchall()
list_of_already_loaded_athletes = set([ r[0] for r in results ])
list_of_to_load_athletes = []


query = 'SELECT DISTINCT id FROM input_catapult_activities;'
cursor.execute(query)
results = cursor.fetchall()
list_of_already_loaded_activities = set([ r[0] for r in results ])
list_of_to_load_activities = []



if first_load:
    for api, values in api_dict.items():
        print(api)
        url = feedurl + api
        response = requests.get(url, headers = headers)
        data_json = response.json()
        dataframes = {}
        print('MEGJÖTT A LEKÉRDEZÉS')
        #print(values)
        if 'extra' in values.keys():
            for subpart in values['extra']:
                dataframes[values['table_name'] + '_' + subpart] = pd.DataFrame()

                for row in data_json:
                    if len(row[subpart]) == 0:
                        continue
                    temp_df = pd.DataFrame(row[subpart])
                    if subpart == 'tags':
                        
                        temp_df['tag_id'] = temp_df['id']
                        temp_df['id'] = row['id']
                        temp_df = temp_df[['id','tag_id']]
                    dataframes[values['table_name'] + '_' + subpart] = pd.concat([dataframes[values['table_name'] + '_' + subpart],temp_df])


                data_json = [ {key: value for key, value in dict.items() if key != subpart} for dict in data_json ]

        dataframes[values['table_name']] = pd.json_normalize(data_json, sep = '_')
        #print('EZ AZ API: ' + api)

        for key, df in dataframes.items():
            for column in df.columns:
                df[column] = df[column].astype(str)


        
        for table_name, table in dataframes.items():
            print('TÖLT IDE: ' + table_name)
            cursor.execute('TRUNCATE TABLE ' + table_name)
            query = '%s,'*len(table.columns)
            query = 'INSERT INTO ' + table_name + '(' + ','.join(list_replace(table.columns,'default','[default]')) + ') VALUES ('  + query[0:-1] + ')'
            #cursor.execute('BEGIN TRANSACITON')
            #table = table.to_numpy()
            #table = tuple(map(tuple))
            for i in tuple(map(tuple,table.to_numpy())):
                #cursor.execute(query,i)
                #try:
                cursor.execute(query,i)
                #except:
                #    print('ITT VAN GOND')
                #    print(i)
            conn.commit()


for api, values in always_load_dict.items():
    print(api)
    url = feedurl + api
    response = requests.get(url, headers=headers)
    data_json = response.json()
    dataframes = {}
    final_data_json = []
    if 'extra' in values.keys():
        for subpart in values['extra']:
            if subpart == 'tag_list':
                table_name_subpart = 'tags'
            else:
                table_name_subpart = subpart
            dataframes[values['table_name'] + '_' + table_name_subpart] = pd.DataFrame()
            #dataframes[values['table_name'] + '_' + subpart] = pd.json_normalize(data_json, subpart,'id', sep = '_')
            for row in data_json:

                if api == 'activities':
                    to_check_list = list_of_already_loaded_activities
                if api == 'periods':
                    to_check_list = list_of_already_loaded_periods
                if api == 'athletes':
                    to_check_list = list_of_already_loaded_athletes
                    print(row['id'])
                    print(len(to_check_list))
                if row['id'] in to_check_list:
                    #data_json = [data for data in data_json if data != row]
                    continue
                final_data_json.append(row)
                final_data_json = [ {key: value for key, value in dict.items() if key != subpart} for dict in final_data_json ]

                if len(row[subpart]) == 0:
                    continue
                temp_df = pd.DataFrame(row[subpart])


                if table_name_subpart == 'tags':
                    
                    temp_df['tag_id'] = temp_df['id']
                    temp_df['id'] = row['id']
                    temp_df = temp_df[['id','tag_id']]
                if table_name_subpart == 'periods':
                    temp_df['period_id'] = temp_df['id']
                    temp_df['id'] = row['id']
                    temp_df = temp_df[['id','period_id']]
                    
                dataframes[values['table_name'] + '_' + table_name_subpart] = pd.concat([dataframes[values['table_name'] + '_' + table_name_subpart],temp_df])



        dataframes[values['table_name']] = pd.json_normalize(final_data_json, sep = '_')
        #print('EZ AZ API: ' + api)

        for key, df in dataframes.items():
            for column in df.columns:
                df[column] = df[column].astype(str)


        
        for table_name, table in dataframes.items():
            query = '%s,'*len(table.columns)
            query = 'INSERT INTO ' + table_name + '(' + ','.join(list_replace(table.columns,'default','[default]')) + ') VALUES ('  + query[0:-1] + ')'

            for i in tuple(map(tuple,table.to_numpy())):
                #cursor.execute(query,i)
                #try:
                cursor.execute(query,i)
                #except:
                #    print('ITT VAN GOND')
                #    print(i)
            conn.commit()





    ###########EZZEL LEHET MEGCSINÁLNI A CREATE_TABLE DOLGOKAT
        #for table_ane, table in dataframes.items():
        #    string = 'CREATE TABLE ' + table_ane + '(load_timestamp DATETIME DEFAULT GETDATE(),'
        #    for column in table.columns:
        #        string = string +'\n' + str(column) + ' NVARCHAR(MAX),'
        #    string = string[0:-1] + ')'
        #    print(string)








count = 0
print('ENNYI PERIOD: ' + str(len(dict_of_already_loaded_periods)))
for period_id_dict in dict_of_already_loaded_periods:
    count = count + 1
    print('Ennyinél tartunk: ' + str(count))
    url = feedurl + 'periods/' + period_id_dict['id'] + '/athletes'
    available_players = requests.get(url,headers=headers)
    if available_players.status_code != 200:
        continue
    available_players = available_players.json()

    for athlete in available_players:
        athlete_id = athlete['id']
        #load Get Events Data for Athlete in Activity
        table_name = 'input_catapult_events'
        url = feedurl + 'periods/' + period_id_dict['id'] + '/athletes/' + athlete_id + '/events?event_types=ima_acceleration,ima_jump,ima_impact,goalkeeping_v1,goalkeeping_v2,running_symmetry,free_running,football_movement_analysis'
        response = requests.get(url, headers = headers)
        if response.status_code != 200:
            continue
        list_of_dataframes = {}
        data_json = response.json()
        if 'status' in data_json:
            if data_json['status'] == 'error':
                continue
        for data in data_json:
            try:
                list_of_data = list(data['data'].keys())
            except:
                hibak.append(data)
                continue
            for datatype in list_of_data:
                if 'input_catapult_events_' + datatype not in list_of_dataframes.keys():
                    list_of_dataframes['input_catapult_events_' + datatype] = pd.DataFrame()
                temp_df = pd.DataFrame(data['data'][datatype])
                temp_df['activity_id'] = period_id_dict['activity_id']
                temp_df['period_id'] = period_id_dict['id']
                temp_df['athlete_id'] = athlete_id
                list_of_dataframes['input_catapult_events_' + datatype] = pd.concat([list_of_dataframes['input_catapult_events_' + datatype],temp_df])
                #list_of_dataframes['input_catapult_events_' + datatype].append(data['data'][datatype])
            data['data'] = str(list_of_data)
            list_of_dataframes['input_catapult_events'] = pd.DataFrame(data_json)
            list_of_dataframes['input_catapult_events']['activity_id'] = period_id_dict['activity_id']
            list_of_dataframes['input_catapult_events']['period_id'] = period_id_dict['id']
            list_of_dataframes['input_catapult_events']['athlete_id'] = athlete_id
        #for key, value in list_of_dataframes.items():
        #    list_of_dataframes[key] = pd.DataFrame(value)


        #for table_name, table in list_of_dataframes.items():
        #    string = 'CREATE TABLE ' + table_name + '(load_timestamp DATETIME DEFAULT GETDATE(),'
        #    for column in table.columns:
        #        string = string +'\n' + column + ' NVARCHAR(MAX),'
        #    string = string[0:-1] + ')'
        #    print(string)
        for table_name, table in list_of_dataframes.items():
            #try:
            #    cursor.execute('TRUNCATE TABLE ' + table_name)
            #except:
            #    print(table_name)
            query = '%s,'*len(table.columns)
            query = 'INSERT INTO ' + table_name + '(' + ','.join(list_replace(table.columns,'default','[default]')) + ') VALUES ('  + query[0:-1] + ')'
            #cursor.execute('BEGIN TRANSACITON')
            #table = table.to_numpy()
            #table = tuple(map(tuple))
            for i in tuple(map(tuple,table.to_numpy())):
                try:
                    cursor.execute(query,i)
                except:
                    print('ITT VAN GOND')

            try:
                conn.commit()
            except:
                print('')


        #for period_id_dict in dict_of_already_loaded_periods:
    url = feedurl + 'periods/' + period_id_dict['id'] + '/athletes'
    available_players = requests.get(url,headers=headers).json()
    for athlete in available_players:
        print('EFFORTS')

        athlete_id = athlete['id']
        #load Get Events Data for Athlete in Activity
        table_name = 'input_catapult_efforts'
        url = feedurl + 'periods/' + period_id_dict['id'] + '/athletes/' + athlete_id + '/efforts?effort_types=acceleration,velocity'
        response = requests.get(url, headers = headers)
        if response.status_code != 200:
            continue
        list_of_dataframes = {}
        data_json = response.json()
        if 'status' in data_json:
            if data_json['status'] == 'error':
                #print('ILYEN NINCS ')
                continue
        for data in data_json:
            list_of_data = list(data['data'].keys())
            for datatype in list_of_data:
                if 'input_catapult_efforts_' + datatype not in list_of_dataframes.keys():
                    list_of_dataframes['input_catapult_efforts_' + datatype] = pd.DataFrame()

                temp_df = pd.DataFrame(data['data'][datatype])
                temp_df['activity_id'] = period_id_dict['activity_id']
                temp_df['period_id'] = period_id_dict['id']
                temp_df['athlete_id'] = athlete_id
                list_of_dataframes['input_catapult_efforts_' + datatype] = pd.concat([list_of_dataframes['input_catapult_efforts_' + datatype],temp_df])
                #list_of_dataframes['input_catapult_events_' + datatype].append(data['data'][datatype])
            data['data'] = str(list_of_data)
        list_of_dataframes['input_catapult_efforts'] = pd.DataFrame(data_json)


        for table_name, table in list_of_dataframes.items():
            #try:
            #    cursor.execute('TRUNCATE TABLE ' + table_name)
            #except:
            #    print(table_name)
            query = '%s,'*len(table.columns)
            query = 'INSERT INTO ' + table_name + '(' + ','.join(list_replace(table.columns,'default','[default]')) + ') VALUES ('  + query[0:-1] + ')'
            #cursor.execute('BEGIN TRANSACITON')
            #table = table.to_numpy()
            #table = tuple(map(tuple))
            for i in tuple(map(tuple,table.to_numpy())):
                    cursor.execute(query,i)
            try:
                conn.commit()
            except:
                print('')

    for athlete in available_players:
        payload = {
                "filters": [
                    {
                        "values": [period_id_dict['activity_id']], #MTKIIE1201P
                        "name": "activity_id",
                        "comparison": "="
                    },
                    {
                        "values": [athlete['id']], #244 Molnár
                        
                        "name": "athlete_id",
                        "comparison": "="
                    }
                ],
            #    "group_by": ["activity"],
                "group_by": ["activity", "period"],
                "source": "cached_stats",
                "requested_only": True
            }
        
        feedurl = "https://connect-eu.catapultsports.com/api/v6"
        url = f'{feedurl}/stats'
        response = requests.post(url, json=payload, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            continue
        data = response.json()
        for row in data:
            row.pop('errors',None)

        data = pd.DataFrame(data)

        table1_df = data.iloc[:,:998]
        replace_dict = {'á':'a','é':'e','í':'i','ö':'o','ő':'o','ó':'o','ü':'u','ú':'u','ű':'u','/':'_per_',"'":''}
        table1_df['athlete_id'] = athlete['id']
        for column in table1_df.columns:
            col = column
            for word, to_replace in replace_dict.items():
                col = col.lower().replace(word.lower(),to_replace)
            table1_df = table1_df.rename(columns={column : col})
            #print(data.columns[0])

        table1_df['date_id'] = pd.to_datetime(table1_df['date_id'])
        table1_df['date_name'] = pd.to_datetime(table1_df['date_name'])
        table1_df['date'] = pd.to_datetime(table1_df['date'])



        query = '%s,'*len(table1_df.columns)
        query = 'INSERT INTO ' + 'input_catapult_stats_1' + '([' + '],['.join(table1_df.columns) + ']) VALUES ('  + query[0:-1] + ')'
        table1_df = table1_df.replace(np.nan, None)
        for i in tuple(map(tuple,table1_df.to_numpy())):
            cursor.execute(query,i)
            
        conn.commit()


        table2_df = data.iloc[:,998:]
        replace_dict = {'á':'a','é':'e','í':'i','ö':'o','ő':'o','ó':'o','ü':'u','ú':'u','ű':'u','/':'_per_',"'":''}
        table2_df['athlete_id'] = athlete['id']

        for column in table2_df.columns:
            col = column
            for word, to_replace in replace_dict.items():
                col = col.lower().replace(word.lower(),to_replace)
            table2_df = table2_df.rename(columns={column : col})
            #print(data.columns[0])



        query = '%s,'*len(table2_df.columns)
        query = 'INSERT INTO ' + 'input_catapult_stats_2' + '([' + '],['.join(table2_df.columns) + ']) VALUES ('  + query[0:-1] + ')'
        table2_df = table2_df.replace(np.nan, None)
        for i in tuple(map(tuple,table2_df.to_numpy())):
            cursor.execute(query,i)
            
        conn.commit()





#for key, value in list_of_dataframes.items():
#    list_of_dataframes[key] = pd.DataFrame(value)


#for table_name, table in list_of_dataframes.items():
#    string = 'CREATE TABLE ' + table_name + '(load_timestamp DATETIME DEFAULT GETDATE(),'
#    for column in table.columns:
#        string = string +'\n' + column + ' NVARCHAR(MAX),'
#    string = string[0:-1] + ')'
#    print(string)





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


END_DATE = datetime.now()
print(START_DATE)
print(END_DATE)
duration = END_DATE-START_DATE
print(duration.total_seconds())