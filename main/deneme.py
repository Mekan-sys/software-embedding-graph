from pydriller import RepositoryMining


url="https://github.com/signalapp/Signal-Server"
f= open("deneme.txt","w")

for commit in RepositoryMining(url).traverse_commits():
    for modification in commit.modifications:
        f.write('Author {} modified {} in commit {}'.format(commit.author.name, modification.filename, commit.hash)+"\n")

#writing to txt file`
#f = open("deneme", "x")
#line = f.writelines( hash_dict )
#f.close()