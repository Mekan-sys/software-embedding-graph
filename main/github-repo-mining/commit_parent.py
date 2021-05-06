from pydriller import RepositoryMining
from func_lib import *

url="https://github.com/signalapp/Signal-Server"
#url = input("Pls enter url or path of the git project: ")


#creating the dictionary for hash of the commits and index the commits (key: index, value: hash)
commits = RepositoryMining(url).traverse_commits()
hash_dict = {}
idx = 0
for commit in commits:
  hash_dict[idx] = commit.hash
  idx +=1

key_list = list(hash_dict.keys()) 
val_list = list(hash_dict.values())


#commit - parent relationship
commits = RepositoryMining(url).traverse_commits()
mylist = []
for commit in commits:
  for parent in commit.parents:
    commit_index = get_key(commit.hash,hash_dict)
    parent_index = get_key(parent,hash_dict)
    temp = str(commit_index) + " " + str(parent_index) + "\n" 
    mylist.append(temp)


#writing to txt file
f = open("commit_parent.txt", "x")
line = f.writelines( mylist )
f.close()