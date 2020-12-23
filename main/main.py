from pydriller import RepositoryMining
#from .functions import get_key


#creating the dictionary for hash of the commits and index the commits (key: index, value: hash)
url = "https://github.com/tensorflow/tensorflow" 
commits = RepositoryMining(url).traverse_commits()
hash_dict = {}
idx = 0
for commit in commits:
  hash_dict[idx] = commit.hash
  idx +=1

print(hash_dict)
key_list = list(hash_dict.keys()) 
val_list = list(hash_dict.values())

def get_key(val,hash_dictionary): 
    for key, value in hash_dictionary.items(): 
        if val == value: 
            return key 

#commit - parent relationship
# url = "https://github.com/tensorflow/tensorflow" 
# commits = RepositoryMining(url).traverse_commits()
# mylist = []
# for commit in commits:
#   for parent in commit.parents:
#     commit_index = get_key(commit.hash,hash_dict)
#     parent_index = get_key(parent,hash_dict)
#     temp = str(commit_index) + " " + str(parent_index) + "\n" 
#     mylist.append(temp)

# print(mylist)