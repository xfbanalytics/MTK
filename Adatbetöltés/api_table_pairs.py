first_load = False
days_to_load = 7 #hány napra visszamenőleg töltse be

api_dict = {
'threshold_sets':{'table_name':'input_catapult_threshold_sets'},
'parameter_types':{'table_name':'input_catapult_parameter_types'},
 'teams':{'table_name':'input_catapult_teams','extra':['tags']},
 'parameters':{'table_name':'input_catapult_parameters'},
 'parameter_types':{'table_name':'input_catapult_parameter_types'},
 'positions':{'table_name':'input_catapult_positions'},
#'stats':{'table_name':'input_catapult_stats'},
'tags':{'table_name':'input_catapult_tags'},
'tagtype':{'table_name':'input_catapult_tagtypes'},
'venues':{'table_name':'input_catapult_venues'},
# 'periods':{'table_name':'input_catapult_periods','extra':['tags']},
# 'activities':{'table_name':'input_catapult_activities','extra':['owner','periods']},
# 'athletes':{'table_name':'input_catapult_athletes','extra':['tags']},
}


always_load_dict = {
'periods':{'table_name':'input_catapult_periods','extra':['tags']},
 'activities':{'table_name':'input_catapult_activities','extra':['owner','periods','tag_list']},
 'athletes':{'table_name':'input_catapult_athletes','extra':['tags']},
}