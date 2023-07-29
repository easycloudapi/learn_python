

## GitHub Repo Auth:
1. Ref: 
    1. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
2. Follow below steps -
    ```shell
    git remote -v
    git remote set-url origin https://<TOKEN>@github.com/<USERNAME>/<REPOSITORYNAME>.git
    ```
    >
    > origin  https://github.com/easycloudapi/learn_python.git (fetch)
    >
    > origin  https://github.com/easycloudapi/learn_python.git (push)
    >
    > upstream        https://github.com/easycloudapi/learn_python.git (fetch)
    >
    > upstream        https://github.com/easycloudapi/learn_python.git (push)
    >
3. 

## Git Clone from Main branch:
```shell
git clone 
```

## Git checkout to new branch
```shell
git checkout -b <new_local_branch>
git checkout <other_local_branch>

```

## Initial Commit on local and push to remote:
```shell
git pull origin <remote_branch>
git status
git add .
git commit -m "[jira_issue_id] <comment>"
git push -u origin <remote_branch>
```

## Git Delete branch
```shell
# delete local branch, goto checkout another branch
git branch --delete <local_branch_name>

# delete remote branch if merged already
git push --delete origin/<remote_branch>

# delete remote branch if not merged
git push -D origin/<remote_branch>
```