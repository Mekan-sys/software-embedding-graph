from pydriller import RepositoryMining
import time

#url="/Users/mekan/tensorflow"
#https://github.com/signalapp/Signal-Server
url = input("Pls enter url or path of the git project: ")
name = input("Pls enter name of the project: ")
f= open("../graphs/"+name+"_auther_file.txt","w")

t0= time.time()
for commit in RepositoryMining(url).traverse_commits():
    if isinstance(commit.modifications,list):
        for modification in commit.modifications:
            f.write('{}#{}'.format(commit.author.name, modification.filename)+"\n")
    else:
        print(commit.modifications)
        #f.write('{}#{}'.format(commit.author.name, modification.filename)+"\n")
t1= time.time() - t0
print("Time elapsed: ", t1)