# Git 101🧑🏻‍🚀

## Exercise 1
  - [ ] Who created git? and what is the essence of git.
   Linus Torvalds
   It is a version control system. It allows developers to keep track of changes in source code

## Exercise 2
  - [ ] What is the difference between git, gitlab and github?
  Github is owned by microsoft and available to the public. Gitlab on the other hand is privately owned
  Git is on the command line . Github is a web based version of git


## Exercise 3
  - [ ] Apart from git, is there any other version control system? If there is, kindly list them.
  Yes
  Mercurial, Monotone

## Exercise 4
  - [ ] What does `git init` and `git status` do?
  git init is used to initialize a net git repository or reinitialize an existing one
  git status is used to display the state of the working directory



## Exercise 5
  - [ ] What is a `commit` in git. Explain and show examples of a commit in the terminal.
  git commit saves the current version of a project into the repository

$ git commit -m "First Commit"
[master (root-commit) 7ec1d6b] First Commit
 Committer: Paa Yaw Fuachie Sobreh <yaw.sobreh@turntabl.io>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit


## Exercise 6
  - [ ] In git, there is a way to ignore file, how is this done.
  - [ ] Create some files and intentionally ignore them.
  You create a gitignore file


## Exercise 7
  - [ ] What does `git log` do? Show examples of `git log` in the terminal.
   git log is used to display a list of commits in a Git repository. It shows the commit history in reverse chronological order by default

   $ git log
commit 7ec1d6b135e0c18ec1ddf2d16e3a0f14a9c5bdd3 (HEAD -> PaaYaw)
Author: Paa Yaw Fuachie Sobreh <yaw.sobreh@turntabl.io>
Date:   Tue Jun 3 09:05:23 2025 +0000

    First Commit



## Exercise 8
  - [ ] What does it mean to do `git add`.
  git add is used to add changes in your working directory to the staging area


## Exercise 9
  - [ ] What is a staging area in git and how do you get items into the staging area.
  - [ ] Illustrate this in the terminal by moving an untracked file to the tracked state and then staging area.
  The staging area is an intermediate area where changes are gathered before they are committed to the repository.
  You get items there with the git add command


## Exercise 10
  - [ ] How do you commit in git with the message on the same line?
  $ git commit -m "First Commit"



## Exercise 11
  - [ ] What is the difference between the `pull`,`push` and `fetch` command in git.
  The git fetch command is used to fetch all changes from the remote repository to the local repository without making any changes to the current working directory. 

  The git pull command is used to fetch all changes from the remote repository and automatically merge or rebase them into your current working directory

  The git push command is used to upload local branch commits to the corresponding remote branch.


## Exercise 12
  - [ ] What command do you run in git, if you want to see more information about a remote in git. Illustrate this in the terminal and try and understand the output. Please contact Caleb, if you do not.
   git remote show remote

## Exercise 13
  - [ ] What is the difference between rebase and merge in git. Illustrate with examples.
  Merging is a way to combine the changes from one branch into another.
  Rebasing is a process of moving or combining a sequence of commits to a new base commit. It allows you to take the changes from one branch and reapply them on top of another branch.

## Exercise 14
  - [ ] What is `git checkout`?
    - [ ] `git checkout` has another alias. What is it?
    - [ ] Show that both checkout and its alias are doing the same thing in the terminal.

  The git checkout command is used to switch branches or restore working tree files in Git
   git switch
  $ git switch testBranch
  Switched to branch 'testBranch'


## Exercise 15
- [ ] What are tags in git, and what types of tags are there?
Tags in Git are used to mark specific points in a repository's history
annotated tags and lightweight tags.

## Exercise 16
- [ ] Do you know that, you can delete a branch in git?
  - [ ] Create a branch and delete it.
  - [ ] Wait....what is the difference between deleteing with `-d` and `-D` arguments in git?
  git branch -d is for deleting branches that are fully merged in its upstream branch or to HEAD
  git branch -D deletes the branch even if it's not merged.

## Exercise 17
- [ ] Can you change a branch name? If yes what is the command? Illustrate this in the terminal.
git branch -m old-branch-name new-branch-name


## Exercise 18
- [ ] What does it mean to revert a commit resetting to a previous commit?
- [ ] What does it to reset to a previous commit?
- [ ] What is the difference between the reset and revert?
reverting a commit creates a new commit that undoes the changes done by the previous commit
resetting moves the current commit pointer to an earlier commit (Like how you delete a node in a linked list)

reverting keeps the changes although they are not visible but resetting deletes altogether

## Exercise 19
- [ ] Resolving Conflicts
Scenario:
  * In the main-branch, create a file and name it calculator.py
  * Add 4 functions into this file, the functions are: add,subtract,multiply and divide.
  * Implement these functions and test them to see if it works.
  * Create two branches from main: feature-a and feature-b
  * In feature-a, modify the same line in your calculator.py file
  * Commit the change
  * Switch to feature-b and modify the SAME line differently
  * Commit this change too
  * Try to merge both branches into main (one will conflict)
  * Resolve the conflict manually by accepting both changes
  * Complete the merge.

## Exercise 20
- [ ] Beatrice should create a repo named[how-we-collaborate].
- [ ] Beatrice should then create three branches(`main`,`dev` and `beatrice`(this is where she adds her stuff)).
- [ ] The stuff can be anything random, but it should be at least 5 files.
- [ ] After Beatrice has created the repo, she can share a link to Paa Yaw, who should then fork the repo Beatrice created.[You need to know what forking is.]
- [ ] In the forked repo, Paa Yaw should create 5 different files and push his changes to his branch for Beatrice to merge.
- [ ] After merging, Beatrice should cherry-pick changes from Paa Yaw's branch and put it in her branch.
- [ ] Also, Paa Yaw should cherry-pick changes from Beatrice's branch and put it in his branch.
- [ ] How many commits do each of you have at the end of the exercise.(Hint: it should be the same number.)
