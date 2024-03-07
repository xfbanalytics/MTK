


def new_dict(old_dict, key_to_pop):
    new_dict = old_dict.copy()
    new_dict.pop(key_to_pop,None)
    return new_dict

#def insert_dictionary_to_table(cursor, dictionary, target_table):

    

def list_replace(list,from_,to_):
    return [to_ if x==from_ else x for x in list]