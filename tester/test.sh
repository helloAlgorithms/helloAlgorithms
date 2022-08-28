#!/bin/bash

for user in $*
do
git stash
git checkout $user
git log --since=2.weeks --pretty=format:"%cr : %s" --grep "\[" | sort -k 3
commit_count=$(git log --since=2.weeks --pretty=format:"%cr : %s" --grep "\[" | sort -k 3 | wc -l)
if [ $commit_count -gt 7 ]; then
	echo -e "\033[32m commit_count is: $commit_count $user passed over8\033[0m"
else
	echo -e "\033[35m commit_count is: $commit_count $user goes vacation\033[0m"
fi
git stash
git checkout master
done
