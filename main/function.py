#function for get key from a value from hash_dictionary

#class Funcs:
def get_key(val,hash_dictionary): 
    for key, value in hash_dictionary.items(): 
        if val == value: 
            return key 