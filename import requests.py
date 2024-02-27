import requests
import json


headers = {
    "accept": "application/json",
    "content-type": "application/json",
#eredeti
 #   "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0NjFiMTExMS02ZjdhLTRkYmItOWQyOS0yMzAzOWZlMjI4OGUiLCJqdGkiOiI2Zjc4ZDk1MjRlNDE5NjUyMTc1Yzg5ZDYwMWU1NmFmNDE1NmZhYzE2Y2VjMjI4YWFiMTNlZTRhYTM5MjIyZmU0YzBhNzIzYzBjYTJlNTIxMCIsImlhdCI6MTY5MTA3OTAzOC4wMTc1MjMsIm5iZiI6MTY5MTA3OTAzOC4wMTc1MjYsImV4cCI6NDg0NDY3OTAzOC4wMDY4Miwic3ViIjoiMzZhYjVkMGItNjM4ZC00ZDZlLWIwMmUtY2Q1MzMyNzE0NTE0Iiwic2NvcGVzIjpbImNvbm5lY3QiXX0.YfVF_Fn7OJUkA6w6kieBzSlbgI_3qgdy-hoTkCU2zbc7UT9SjTDLKpBj12mL3cPnbGGH3mARU0SiFZzw4-lG_5eTS-tBFwN7SFlELfWbe3yDC1ZFKTyVMv2XcS9imeTiL_QkU6CO7s46P136PWrSbeeE8ARO1xYeR8gyrHNKlp-vSkeJA2MIrNdlJutvITbTRVM8yNTuHUUP9niAtTNkqAsivb_AUHmATtZxmGzjKVLsDPk_MhjVjniq-04X4wBhPE5qi7B0Y4r6gAmakAteIinbAE3wjyXErEwQTDeycRW4hsd_kaubt9Fp9OSf-YrWJzbXGNiCIdrhtkejJG75sMdqdbLCh786giLwnvr9gWsNHSAxqx9ihApi__16tpQp_GekphZnZEMi3Jw3kjPiyUVdR7n8OdqCMhk87_u9VJw_I6R9qNITCdq-AwqLOthjfk8DljA8_JYiA_kbfsa-kSxK1XN5m4AeCacKDECzIDQlWOR0K3MwR4aLDaGeuf4elKL3zbHJaWVPw6udknb0BSnYaEU9_zPJPuscOnt3WwfJCeV5ssW-ypIWZjDmEAousSpujuUX63OTTIkti2MLKgZzwNYbtkqTd--fZqvQ7C2JxJyoxBNsXXI-FIMCltHZ359bw_05mFqeRqJonAeBQz5SyrO5cCtfFvJFJg_r8h8"

#ideiglenes
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0NjFiMTExMS02ZjdhLTRkYmItOWQyOS0yMzAzOWZlMjI4OGUiLCJqdGkiOiJmODQ2MWIwZGZkMjU2NjExNGExMmU0ZDJmYjk0YzJhYjViNDlmM2MwZGM3YTg3NWU3YjEzMzllMjE3MjhhNzJhMDBhMzUwNzM5OTgzNmM4MCIsImlhdCI6MTY5OTM1ODY2Mi40NDI1NjksIm5iZiI6MTY5OTM1ODY2Mi40NDI1NzMsImV4cCI6NDg1Mjk1ODY2Mi40MzEzMTMsInN1YiI6IjM2YWI1ZDBiLTYzOGQtNGQ2ZS1iMDJlLWNkNTMzMjcxNDUxNCIsInNjb3BlcyI6WyJjb25uZWN0Il19.Fqa6D1DIYg5YJo9kCCzxEO51hxisBqokysGmt7WEhg1_RDo2LazYV1IZ9qUDtNNxjByWgfpa6uH9FUnwRS4yhxG2qIWN0wZBBx8HC-viSSs79bJMtlBiUQqxc8sPYgT-KkYNEfy5fh8XZZLunfVkRooULbKWMcgka-0WdDKI4EmrXihMk0ieEeFO9YsK9J9JdcAGOFB6ibhA11EFiO7gWsYFJL7OtxtXp9M_s8Xhqqo-5jTEtPKX_nNZRG0ZT_nu4Lm5jXX8SShuLDd8O_I-4HRwi5UQp8hSzT005MRoWzy6M-yj09ZlqWt9M0GkSf6Tmx4bovBU1h_QFVkynI-zuxEWl9-VWuRCnA5bzSMa9CGq7yIB70AWkr-rvCmjP3b2fdmSjoyJgwZTVeP0uQHvXoo3DCxgVhqPhsxUslR9KKtc7pd0Fc0O9upzWFQisxxHRWyyNGYNpyiyiFdAlIgOb_CGlra-ZAQooatMQf7bdsAUz_V0LTQxwpFFeGtbz1jz_rT-ppw1SLYjJbWAf2G-lV7_qHYxcemyCSSjcxMAdWz3R74j9xrfKCohSQQ60PJmLOHxp3hnvrjtekIwUG7GvGZtcB3Cd90IrK-SspybzbWHKi6qMo-cmi0bgZGuOiPALsyV-S1zAkolArrGzxxqgP3WKZf0PtuFitmdljsYbOw"
}

outputRoot = "c:/Users/Gábor/Downloads/"

feedurl = "https://connect-eu.catapultsports.com/api/v6"


### ------------------- SPEC --------------------- ###

# OAS in JSON format -----------------------------
#url = f'{feedurl}/docs/spec'
#fileName = outputRoot + "catapult_specification.json"


### ------------------- TEAMS -------------------- ### BEGIN
# Teams: Lists teams to which athletes are assigned in your OpenField account

# Get list of Teams ------------------------------
#url = f'{feedurl}/teams'
#fileName = outputRoot + "catapult_SKLA_teams.json"

# Get Team Details -------------------------------
#url = f'{feedurl}/teams/4f8e73ea-117d-47c9-8208-7d4e2cb67a18'
#fileName = outputRoot + "catapult_SKLA_ARCH_team_details.json"
#url = f'{feedurl}/teams/7d1f48de-a213-4d03-b37a-6c87c08f3168'
#fileName = outputRoot + "catapult_SKLA_U15_team_details.json"
#url = f'{feedurl}/teams/ac34ebb5-08d3-4d51-a1da-a018d07b8252'
#fileName = outputRoot + "catapult_SKLA_U16_team_details.json"
#url = f'{feedurl}/teams/a86c8db4-dd9c-465a-a1b0-ba1a166ee737'
#fileName = outputRoot + "catapult_SKLA_U17_team_details.json"
#url = f'{feedurl}/teams/75054b55-9900-11e3-b9b6-22000af8166b'
#fileName = outputRoot + "catapult_SKLA_U19_team_details.json"

# Get all Athletes For a Team --------------------
#url = f'{feedurl}/teams/4f8e73ea-117d-47c9-8208-7d4e2cb67a18/athletes'
#fileName = outputRoot + "catapult_SKLA_ARCH_team_athletes.json"
#url = f'{feedurl}/teams/7d1f48de-a213-4d03-b37a-6c87c08f3168/athletes'
#fileName = outputRoot + "catapult_SKLA_U15_team_athletes.json"
#url = f'{feedurl}/teams/ac34ebb5-08d3-4d51-a1da-a018d07b8252/athletes'
#fileName = outputRoot + "catapult_SKLA_U16_team_athletes.json"
#url = f'{feedurl}/teams/a86c8db4-dd9c-465a-a1b0-ba1a166ee737/athletes'
#fileName = outputRoot + "catapult_SKLA_U17_team_athletes.json"
#url = f'{feedurl}/teams/75054b55-9900-11e3-b9b6-22000af8166b/athletes'
#fileName = outputRoot + "catapult_SKLA_U19_team_athletes.json"

### ------------------- TEAMS -------------------- ### END


### ------------------ ATHLETES ------------------ ### BEGIN
# Athletes: Lists athletes and associated information recorded in your OpenField account

# Get List of Athletes ---------------------------
#url = f'{feedurl}/athletes'
#fileName = outputRoot + "catapult_SKLA_athletes.json"

# Get Athlete Details ----------------------------
#url = f'{feedurl}/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2'
#fileName = outputRoot + "catapult_SKLA_athletes_#264_Kenesei.json"

### ------------------ ATHLETES ------------------ ### END


### ----------------- ACTIVITIES ----------------- ### BEGIN
# Activities: Lists activities and associated information

# Get List of Activities -------------------------
#url = f'{feedurl}/activities'
#fileName = outputRoot + "catapult_SKLA_activities.json"

# Get Activity Details ---------------------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e'
#fileName = outputRoot + "catapult_SKLA_activities_MTKIIE1012CS.json"

#url = f'{feedurl}/activities/dfca5239-27d2-4f10-a269-2b01e808bacc'
#fileName = outputRoot + "catapult_SKLA_activities_15E1011SZE_EXT.json"

#url = f'{feedurl}/activities/730ac34b-324e-4bd8-86d1-e5ee5d34b5da'
#fileName = outputRoot + "catapult_SKLA_activities_MTKIIE1130CS.json"

#url = f'{feedurl}/activities/71ea2c0e-c71c-4259-9558-83fde24fad07'
#fileName = outputRoot + "catapult_SKLA_activities_MTKIIE1201P.json"


# Get all Athletes for an Activity ---------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/athletes'
#fileName = outputRoot + "catapult_SKLA_activities_athletes_MTKIIE1012CS.json"

#url = f'{feedurl}/activities/dfca5239-27d2-4f10-a269-2b01e808bacc/athletes'
#fileName = outputRoot + "catapult_SKLA_activities_athletes_15E1011SZE_EXT.json"

#url = f'{feedurl}/activities/730ac34b-324e-4bd8-86d1-e5ee5d34b5da/athletes'
#fileName = outputRoot + "catapult_SKLA_activities_athletes_MTKIIE1130CS.json"

#url = f'{feedurl}/activities/71ea2c0e-c71c-4259-9558-83fde24fad07/athletes'
#fileName = outputRoot + "catapult_SKLA_activities_athletes_MTKIIE1201P.json"


# Get all Periods for an Activity ----------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/periods'
#fileName = outputRoot + "catapult_SKLA_activities_periods_MTKIIE1012CS.json"

# Get all Tags for an Activity -------------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/tags'
#fileName = outputRoot + "catapult_SKLA_activities_tags_MTKIIE1012CS.json"

# Get Deep Activity Details ----------------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e?include=all'
#fileName = outputRoot + "catapult_SKLA_activities_detailed_MTKIIE1012CS.json"

### ----------------- ACTIVITIES ----------------- ### END


### ----------------- ANNOTATIONS ---------------- ### BEGIN
# Annotations provide an additional way to bring context to performance data associated with an Activity
# in OpenField, and are often used to represent data from external systems such as play data, ball-possession etc.

# Get all Annotations For an Activity ------------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/annotations'
#fileName = outputRoot + "catapult_SKLA_activities_annotations_MTKIIE1012CS.json"

# Get all Annotations For a Period ---------------
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582/annotations'
#fileName = outputRoot + "catapult_SKLA_periods_annotations_$1$.json"

# Get all Athlete Annotations For an Athlete -----
#url = f'{feedurl}/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/annotations'
#fileName = outputRoot + "catapult_SKLA_athletes_annotations_#264_Kenesei.json"

# Get an Annotation ------------------------------
#https://connect-au.catapultsports.com/api/v6/annotations/{id}

# Get all Annotation Categories ------------------
#url = f'{feedurl}/annotation_categories'
#fileName = outputRoot + "catapult_SKLA_annotation_categories.json"

# Get an Annotation Category by Id or name -------
#https://connect-au.catapultsports.com/api/v6/annotation_categories/{idOrName}

# Get an Athlete Annotation ----------------------
#https://connect-au.catapultsports.com/api/v6/athletes/{athlete_id}/annotations/{annotation_athlete_id}

### ----------------- ANNOTATIONS ---------------- ### END


### ------------------ PERIODS ------------------- ### BEGIN
# Periods: Lists periods and associated information, either all or captured for a specific activity

# Get all Periods --------------------------------
#url = f'{feedurl}/periods'
#fileName = outputRoot + "catapult_SKLA_periods.json"

# Get Period Details -----------------------------
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582'
#fileName = outputRoot + "catapult_SKLA_periods_MTKIIE1012CS_$1$.json"

# Get all Athletes in a Period -------------------
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582/athletes'
#fileName = outputRoot + "catapult_SKLA_periods_athletes_MTKIIE1012CS_$1$.json"

### ------------------ PERIODS ------------------- ### END


### ----------------- PARAMETERS ----------------- ### BEGIN
# Parameters: List the parameters for which measures are captured within OpenField, including Player Load, heart rate, banded velocity and acceleration metrics, amongst many others

# Get all Parameters -----------------------------
#url = f'{feedurl}/parameters'
#fileName = outputRoot + "catapult_SKLA_parameters.json"

# Get Parameter Details --------------------------
#url = f'{feedurl}/parameters/6dd4c229-22d8-40d4-8bde-5620aebea2b0'
#fileName = outputRoot + "catapult_SKLA_parameters_total_ima_events_high_(total)_new_(db).json"

# Get All Parameter Types ------------------------
#url = f'{feedurl}/parameter_types'
#fileName = outputRoot + "catapult_SKLA_parameter_types.json"

### ----------------- PARAMETERS ----------------- ### END


### ----------------- POSITIONS ------------------ ### BEGIN
# Positions represent the role Athletes play in their sport.

# Get All Positions ------------------------------
#url = f'{feedurl}/positions'
#fileName = outputRoot + "catapult_SKLA_positions.json"

### ----------------- POSITIONS ------------------ ### END


### ------------------ SETTINGS ------------------ ### BEGIN
# Various User Settings for the authenticated user can be retrieved from the Get User Settings endpoint, including velocity and distance units.

# Get User Settings ------------------------------
#url = f'{feedurl}/settings'
#fileName = outputRoot + "catapult_SKLA_settings.json"

### ------------------ SETTINGS ------------------ ### END


### --------------- TAGS, TAG TYPES--------------- ### BEGIN
# Tags can be used to label Activities, Periods, Athletes and other entities in OpenField to associate additional metadata and make it possible to filter and group collected data.
# Tag Types are categories of Tags that can be applied to entities within OpenField.

# Get all Tag Types ------------------------------
#url = f'{feedurl}/tagtype'
#fileName = outputRoot + "catapult_SKLA_tagtype.json"

# Get TagType Details ----------------------------
#url = f'{feedurl}/tagtype/0c368f8a-e8d5-41cb-a304-9f821c585cc4'
#fileName = outputRoot + "catapult_SKLA_tagtype_Edzes.json"

# Get all Tags -----------------------------------
#url = f'{feedurl}/tags'
#fileName = outputRoot + "catapult_SKLA_tags.json"

# Get All Tags Of TagType ------------------------
#url = f'{feedurl}/tags/0c368f8a-e8d5-41cb-a304-9f821c585cc4'
#fileName = outputRoot + "catapult_SKLA_tags_Edzes.json"

### --------------- TAGS, TAG TYPES--------------- ### END


### ------------------- VENUES ------------------- ### BEGIN
# Venue refers to the location that an Activity took place, and is required to be correctly mapped in OpenField to enable the correct calculation of x,y position relative to the field of play.

# List venues ------------------------------------
#url = f'{feedurl}/venues'
#fileName = outputRoot + "catapult_SKLA_venues.json"

# Get one venue ----------------------------------
#url = f'{feedurl}/venues/689e447d-f24e-44e6-97c2-5af428a19cc5'
#fileName = outputRoot + "catapult_SKLA_venues_Center.json"

### ------------------- VENUES ------------------- ### END


### ----------------- THRESHOLDS ----------------- ### BEGIN
# Athlete thresholds

# List threshold sets ----------------------------
#url = f'{feedurl}/threshold_sets'
#fileName = outputRoot + "catapult_SKLA_threshold_sets.json"

# Show a threshold set ---------------------------
#url = f'{feedurl}/threshold_sets/b872f642-c140-4587-bd33-b24fad57babc'
#fileName = outputRoot + "catapult_SKLA_threshold_sets_Match.json"

# Get threshold alert settings -------------------
#url = f'{feedurl}/threshold_alerts'
#fileName = outputRoot + "catapult_SKLA_threshold_alerts.json"

### ----------------- THRESHOLDS ----------------- ### END


### ---------------- EFFORTS DATA ---------------- ### BEGIN
# Efforts refers to Acceleration and Velocity Efforts recorded by an Athlete.
# https://docs.connect.catapultsports.com/reference/efforts-data

# Get Efforts Data For Athlete in Period ---------
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/efforts?effort_types=acceleration, velocity'
#fileName = outputRoot + "catapult_SKLA_efforts_MTKIIE1012CS_$1$_#264_Kenesei.json"

# Get Efforts Data for Athlete in Activity -------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/efforts?effort_types=acceleration, velocity'
#fileName = outputRoot + "catapult_SKLA_efforts_MTKIIE1012CS_#264_Kenesei.json"

### ---------------- EFFORTS DATA ---------------- ### END


### ----------------- EVENTS DATA ---------------- ### BEGIN
# Events refers to sports-specific IMA metrics recorded by an Athlete.
# The list of available Events in a given OpenField account are configured by Catapult staff and based on your sport.
# https://docs.connect.catapultsports.com/reference/events-data

# Get Events Data For Athlete in Period ----------
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/events?event_types=ima_acceleration,ima_jump,ima_impact,goalkeeping_v1,goalkeeping_v2,running_symmetry,free_running,football_movement_analysis'
#fileName = outputRoot + "catapult_SKLA_events_MTKIIE1012CS_$1$_#264_Kenesei.json"

# Get Events Data for Athlete in Activity --------
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/events?event_types=ima_acceleration,ima_jump,ima_impact,goalkeeping_v1,goalkeeping_v2,running_symmetry,free_running,football_movement_analysis'
#fileName = outputRoot + "catapult_SKLA_events_MTKIIE1012CS_#264_Kenesei.json"

### ----------------- EVENTS DATA ---------------- ### END


### ----------------- SENSOR DATA ---------------- ### BEGIN
# Sensor data endpoints return a number of parameters in a time series for activities that have been 'full-synced' with OpenField Cloud.
# 10Hz Sensor Data: Return high-frequency positional and inertial data for an athlete and period of time
# https://docs.connect.catapultsports.com/reference/sensor-data-10hz

# Get Dual Stream 10hz Sensor Data for Athlete in Period
#url = f'{feedurl}/periods/c6e05cb4-12b4-42af-a7a3-d29385d48582/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/sensor'
#fileName = outputRoot + "catapult_SKLA_sensor_MTKIIE1012CS_$1$_#264_Kenesei.json"
# 401 Client Error: Unauthorized for url

# Get Dual Stream 10Hz Sensor Data for Athlete in Activity
#url = f'{feedurl}/activities/063bb3d7-30a4-4702-a064-0e9ca93be91e/athletes/43ae7760-ea60-4de4-a042-527c62e4dff2/sensor'
#fileName = outputRoot + "catapult_SKLA_sensor_MTKIIE1012CS_#264_Kenesei.json"
# 401 Client Error: Unauthorized for url

### ----------------- SENSOR DATA ---------------- ### END
'''
try:

    print(url)
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    #print(response.text)
 
    data = response.json()
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"===> Sikeres művelet Méret = {len(data)}!")

except requests.exceptions.HTTPError as err:
    print(f"=Z=> Request hiba: {err}")

except Exception as ex:
    print(f"=Z=> Egyéb hiba: {ex}")
'''

### ------------------ STATS DATA ---------------- ### BEGIN
# Query Stats Data
# Statistics: Lists recorded metrics for a set of specified parameters and according to supplied filters
# https://docs.connect.catapultsports.com/reference/poststats

#'''
payload = {
    "filters": [
        {
#            "values": ["063bb3d7-30a4-4702-a064-0e9ca93be91e"], #MTKIIE1012CS
#            "values": ["dfca5239-27d2-4f10-a269-2b01e808bacc"], #15E1011SZE_EXT
#            "values": ["730ac34b-324e-4bd8-86d1-e5ee5d34b5da"], #MTKIIE1130CS
            "values": ["71ea2c0e-c71c-4259-9558-83fde24fad07"], #MTKIIE1201P
            "name": "activity_id",
            "comparison": "="
        },
        {
#            "values": ["43ae7760-ea60-4de4-a042-527c62e4dff2"], #264_Kenesei
#            "values": ["f6265230-71ce-48d4-89a6-d75d85a205a0"], #1201_Molnár
            "values": ["bd6c3acb-e707-4086-a610-d3457f686286"], #244 Molnár
            
            "name": "athlete_id",
            "comparison": "="
        }
    ],
#    "group_by": ["activity"],
    "group_by": ["activity", "period"],
    "source": "cached_stats",
    "requested_only": True
}

url = f'{feedurl}/stats'
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1012CS_#264_Kenesei.json"
#fileName = outputRoot + "catapult_SKLA_stats_15E1011SZE_EXT_#1201_Molnár.json"
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1130CS_#264_Kenesei.json"
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1201P_#264_Kenesei.json"
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1130CS_by_periods_#264_Kenesei.json"
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1201P_by_periods_#264_Kenesei.json"
#fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1130CS_by_periods_#244_Molnar.json"
fileName = outputRoot + "catapult_SKLA_stats_MTKIIE1201P_by_periods_#244_Molnar.json"

try:

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    #print(response.text)

    data = response.json()
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"===> Sikeres művelet Méret = {len(data)}!")

except requests.exceptions.HTTPError as err:
    print(f"=Z=> Request hiba: {err}")

except Exception as ex:
    print(f"=Z=> Egyéb hiba: {ex}")


### ------------------ STATS DATA ---------------- ### END
#'''
