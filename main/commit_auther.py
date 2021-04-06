from pydriller import RepositoryMining
from func_lib import *

url = "https://github.com/signalapp/Signal-Server" 
#url = "https://github.com/spartensor/hamsi-mf.git"
#url = input("Pls enter url or path of the git project: ")

def get_key(val,hash_dictionary): 
    for key, value in hash_dictionary.items(): 
        if val == value: 
            return key 

#creating the dictionary for hash of the commits and index the commits (key: index, value: hash)
commits = RepositoryMining(url).traverse_commits()
hash_dict = {}
idx = 0
for commit in commits:
  hash_dict[idx] = commit.hash
  idx +=1

key_list = list(hash_dict.keys()) 
val_list = list(hash_dict.values())


#commit - author relationship
commits = RepositoryMining(url).traverse_commits()
author_list = []
for commit in commits:
  commit_index = get_key(commit.hash,hash_dict)
  author = commit.author.name
  temp = str(commit_index) + " " + str(author) + "\n"
  author_list.append(temp)


  #writing to file
f = open("commit_author.txt", "x")
line = f.writelines( author_list )
f.close()