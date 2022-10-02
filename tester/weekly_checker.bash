# !/bin/bash

git config --global advice.detachedHead false
git branch -a > branches.txt

while read line
do 
	git stash
	git checkout --track $line
	user=`echo $line | cut -d '/' -f3`
	commit_count=$(git log --since=2.weeks --pretty=format:"%cr : %s" --grep "\[" | sort -k 3 | wc -l)
	if [ $commit_count -gt 7 ]; then
		echo -e "\033[32m commit_count is: $commit_count $user passed over8\033[0m"
	else
		echo -e "\033[35m commit_count is: $commit_count $user goes vacation\033[0m"
	fi
	git checkout master
	git stash pop
done < branches.txt