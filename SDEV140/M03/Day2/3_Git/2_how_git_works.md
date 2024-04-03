# How Git Works

# Installing git:

If you have a package manager, it should be as easy as running:
```
<package-manager> install git
```
Some package managers use 'add' instead of 'install', but you hopefully know the difference!
Now, if you would like package manager, look at the following package managers per operating systems:

- MacOS:   [Homebrew](https://brew.sh/)
- Windows: [Chocolatey](https://chocolatey.org/install)

### ***Otherwise, you can just install git from their website [HERE](https://git-scm.com/downloads).***

---

## Timeline

![git_workflow.png](..%2Fassets%2Fgit_workflow.png)

---

# Commands

![git_cmds.png](..%2Fassets%2Fgit_cmds.png)


## Git Init

To get started using git on a project, you need to initialize git!
To do so, just use the following command in the project's directory:
```
git init
```

This creates the .git folder in your project with no changes added to it. Without doing anything else, 
it has recorded nothing concerning your project, but, we can change that.

## Add and commit

To actually have files added to a project, you need to add them using the add command (lots of adds). 
Do that like this:
```
git add <specific file you are adding>
```
This file will be added to a staging area. It hasn't yet been added to your
project, and if you want to remove it from the staging area, you can use the reset command:
```
git reset <specfic file you are removing>
```

To add all the files in a project, you can use:
```
git add -A
```

To remove all files in the staging area, you can use the reset command with nothing else:
```
git reset
```


When you have made a meaningful number of changes and added the files you would like, you can make a commit!
Commits are snapshots of a project at given points of time. It essentially ends up being versions of a project, 
although some people may not refer to them as that. 

So, if you made a bug fix or added a new feature to a project, it is very much time to add the changed files and 
make a commit. When you make a commit, you ought to give it a meaningful message describing the changes you made.
Here is the command to make your commit!
```
git commit -m "<A message>"
```

To see the difference that you have made since the latest commit, you can use the following command:
```
git diff
```

## Pushing to main

Once you have made commit(s) and they are ready to be put into your main code, you should push to main




## Creating a branch and Pull Request


## Updating your project

## Merge Conflicts

What happens when two individuals both change the same file and push it at the same time?
A merge conflict!

