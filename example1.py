a=5
b=6
c = a+b
print(c)

# Working Directory
# git init
# git add example1.py , git add . => add all files in the working directory
# git status
# git commit -m "Initial commit"
# git status
# git remote add origin <remote_repository_URL>
# git remote -v => check the remote repository URL
# git branch -M main
# git pull --rebase origin main => in simple words, it means to fetch the latest changes from the remote repository and apply your local changes on top of them. 
# git push -u origin main
# # To check the status of the repository
# git log => check the commit history


# git clone <remote_repository_URL> => to clone the remote repository to your local machine

# git switch <branch_name> => to switch to a different branch in the repository
# git switch -c <new_branch_name> => to create a new branch and switch to it

# git merge <branch_name> => to merge changes from one branch into another
# Example:
# git merge feature-branch => merge changes from the feature-branch into the current branch

# git branch -d <branch_name> => to delete a branch locally
# git push origin --delete <branch_name> => to delete a branch from the remote repository

# git push -u origin <branch_name> => to push a new branch to the remote repository and set the upstream tracking reference



# git diff
# example 
# - print("Hello")
# + print("Hello GitHub")
