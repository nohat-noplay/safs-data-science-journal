Version Control system is a way of tracking complete history of work done so far and have multiple simultaneous versions of the product

It can identify:
- Who made the change 
- What time/date the change was made
- What sort of changes are done
- Ability to go back to previous / other versions


Version control is better than text editor (undo) because:
1. Often you want both old and new versions
2. Editor undo buffer is temporary
3. Too much to remember where to undo


#### GIT
A Repository ("repo") stores the complete project and all it's versions
This is not automated so we need to learn how to do this

Git allows for every team member to have it's own repo (stored on local computer) AND/OR there is a central repo (hosted on Github). 
Allows for different repos that hold the same files to be updated at the same time and intelligent algorithms merge the updates together

Git can:
- Show the lists of commits in order
- Retrieve code as it existed at a point in the past
- Show exact differences between code at different times


#### Local Repository vs. Working Directory

“Working directory” stores the version of the code that you’re currently working on.
- a straightforward ordinary directory 
- usually latest version but branches allow for other options

"Local Repo" stores all versions of the code (that has been committed) into "Working Directory"
- repo is stored in a sub-directory in the working directory (./git)


#### Setting up Git

If you don't have Git on your computer: https://git-scm.com/download/win
I use PowerShell for Git (possibly could do it through VS Code)

Set up identity: 
[user@pc]$ git config --global user.name "Your Name" 
[user@pc]$ git config --global user.email "me@xyz.com"

Check identity:
[user@pc]$ git config user.name

Set Up Local Repo:
To actually create a repository for a project: 
► 1. You can take a local directory that is currently not under version control, and turn it into a Git repository, or
► 2. You can clone an existing Git repository from elsewhere.

Option 1: 
[user@pc]$ mkdir myproject 
[[user@pc]$ cd myproject 
[user@pc]$ git init

Creates and populate the .git directory (hidden) 
[user@pc]$ ls -al


#### Staging and Committing

A commit should represent one thing (small bug fix/small feature). 
You must stage before committing

![[Pasted image 20240429115134.png]]

Staging: 
This starts tracking files
[user@pc]$ git add (filename)

To unstage: 
[user@pc]$ git reset MyCode.py
[user@pc]$ git reset

Committing: 
This allows changes to be stored
g: [user@pc]$ git commit -m “meaningful comment” (if you want a bigger comment: just write git commit)

To uncommit:
You don't. Fix it by making another commit

Any tracked file can be either, committed, staged or being modified.

To list files that are (1) staged, (2) new/modified since the last commit but not staged, or (3) unchanged:
[user@pc]$ git status

To see all un-staged code changes in detail:
[user@pc]$ git diff


#### Logs and Diffs

Get Summary of all commits: 
[user@pc]$ git log --graph

See entire history of a file:
[user@pc]$ git log -p MyCode.py
+ + is line that was added
+ - is line that was deleted
+ @@ - identifies location of changed lines
+ 
How To Exit The Git Log? Step 3: By **pressing the q key on the keyboard**

See differences between two commits:
[user@pc]$ git diff 46b9bc 5f14b6  
((commits look like codes like these))

#### Branches

Branching allows for multiple simultaneous versions
Master Branch is usually for main "it works!" version
Feature Branch(es) for working on adding/fixing - less risk affecting what everyone else is working on / good code


by Default - you in Master Branch

Make new branch - 
[user@pc]$ git branch mynewbranch

Switch Branch
Make sure:
- you commit any uncommited changes first 
- This will delete and replace your code with the latest version in “mynewbranch”.
[user@pc]$ git checkout mynewbranch


Make and Switch Branch (in one line)
[user@pc]$ git checkout -b mynewbranch

You need to switch back to master to see older versions of your code

List existing branches:
[user@pc]$ git branch

Rename Branch: 
[user@pc]$ git branch -m 'mybranch' 'newnameforbranch'

#### Merging

Merging Branches is how we get all the code to go together. 
Often Feature branches is where developers do the work and then Master Branch is where the work all ends up together

1. Go to Master Branch
[user@pc]$ git checkout master
2. Merge feature branch with master
[user@pc]$ git merge mynewbranch

Most merging happens automatically with algorithms. 
However if 2 branches both change the same section of code: this is a merge conflict!

Merge Conflict needs to be solved manually
You must: 
1. Edit Xyz.py, see both changes, and figure out for yourself how to reconcile them. 
	[user@pc]$ git add Xyz.py
2. Stage and commit your new changes.
	[user@pc]$ git commit -m "Merged abc-xyz changes."


#### Remote Repos

#### Cloning

Create a new local repo off an existing central repo:
[user@pc]$ git clone https://xyz.com/myproject.git

We can also create a 2nd local repo.
[user@pc]$ git clone myprojectmyproject2
[user@pc]$ cd myproject2

#### Pushing and Pulling

Push to a remote repo (keeping different repos in sync):

Upload newbranch to origin
[user@pc]$ git push -u origin mynewbranch

Upload the current branch to current remote:
[user@pc]$ git push

Pull from a remote repo (when need to build on the work another had done):

Get Changes and merge with another branch
[user@pc]$ git pull (remote)

NOTE: New commits never overwrite existing ones, they are just added
