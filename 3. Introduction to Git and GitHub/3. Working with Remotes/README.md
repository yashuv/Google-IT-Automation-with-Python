## Working with Remotes
In this module, we'll learn a load of new things related to GitHub and remote repositories. We'll first talk about what GitHub is and why it matters, and then we'll dive into how to work with GitHub and other remote repositories.

In earlier modules, we called out that Git is a distributed version control system. Distributed means that each developer has a copy of the whole repository on their local machine.

### What is Github?
GitHub is a web-based Git repository hosting service. On top of the version control functionality of Git, GitHub includes extra features like bug tracking, wikis, and task management. GitHub lets us share and access repositories on the web and copy or clone them to our local computer, so we can work on them. GitHub is a popular choice with a robust feature set, but it's not the only one. Other services that provide similar functionality are BitBucket, and GitLab.

We'll be using GitHub for our examples in the rest of this module.
GitHub provides free access to a Git server for public and private repositories. We'll be using a free repository for our examples, which is fine for educational use, small personal projects, or open source development.

### Basic Interaction with Github**
To use it, you first need to create an account on the site. Once you have your account, you're ready to create your brand new repository on GitHub. Using the wizard, we can create the repo and have a fresh remote repository ready to go.

Now, the first step is to create a local copy of the repository. We'll do that by using the following command:
* git clone "URL of the repo" 
\- GitHub conveniently lets us copy the URL from our repo from the interface so that we don't have to type it.
	
Our repo is basically empty. It only has the README file that GitHub created for us. Let's add a bit more content to it, and once changed we need to *stage the change and commit it*, using single command:

* git commit -a -m "Add one more line to README.md"
\- stage and commit the modified file
	
We've modified our README file. We got to remote repository set up on GitHub. So let's use it to send our changes to that remote repository by using:
* git push 
\- gather all the snapshots taken and send them to the remote repository.i.e: push commits from your local repo to a remote repo.
	
So if we check our repository on GitHub, we should see the updated message.

You've probably noticed that we had to enter our password both when retrieving the repo and when pushing changes to the repo. There are a couple ways to avoid having to do this. One way is to create an *SSH key pair and store the public key in our profile* so that GitHub recognizes our computer. Another option is to use a *credential helper which caches our credentials for a time window* so that we don't need to enter our password with every interaction. Git already comes with a credential helper baked in. We just need to enable it by calling:
* git config --global credential.helper cache
\- enable the credential helper
	
We can also pull changes from remote repository by calling:
* git pull
\- fetch the newest updates from a remote repository
	
## Using a Remote Repository

When we clone the newly created GitHub repository, we had our local Git Repo interact with a remote repository. Remote repositories are a big part of the distributed nature of Git collaboration. It let lots of developers contribute to a project from their own workstations making changes to local copies of the project independently of one another. When they need to share their changes, they can issue git commands to pull code from a remote repository or push code into one.<br>
When working with remotes the workflow for making changes has some extra steps. We'll still modify, stage and commit our local changes. After committing, we'll fetch any new changes from the remote repo and manually merge if necessary and only then will push our changes to the remote repo. <br>
Git supports a variety of ways to connect to a remote repository. Some of the most common are using the HTTP, HTTPS and SSH protocols and their corresponding URLs. HTTP is generally used to allow read only access to a repository. In other words, it lets people clone the contents of your repo without letting them push new contents to it. Conversely HTTPS and SSH, both provide methods of authenticating users so you can control who gets permission to push.

By now you have an idea of what a remote repository is and how it interacts with local Git repositories.

### Working with remotes
When we call a git clone to get a local copy of a remote repository, Git sets up that remote repository with the default **origin** name. We can look at the configuration for that remote by running:
* git remote -v 	(in the directory of the repo)
\- gives the URLs associated with the origin remote
	
Remote repositories have a name assigned to them, by default, the assigned name is *origin*. This lets us track more than one remote in the same Git directory.

If we want to get even *more information about our remote*, we can call:
* git remote show origin

<!-- Once you start having more branches, especially different branches in the local and remote repo, this information starts becoming more complex. -->
**So what's remote branches?**
Whenever we're operating with remotes, Git uses remote branches to keep copies of the data that's stored in the remote repository. We could have a look at the remote branches that our Git repo is currently tracking by running:
* git branch -r
	
These branches are read only. We can look at the commit history, like we would with local branches, but we can't make any changes to them directly. To modify their contents, we'll have to go through the workflow we called out before.

First, we *pull* any new changes to our local branch, then *merge* them with our changes and *push* our changes to the repo.
We've been using git status to check the status of our changes. We can also use:
* git status
\- to check the status of our changes in remote branches as well.
\- tells us that our branch is up to date or not with the origin/master branch
	
The *master branch in the remote repository* called **origin**.

### Fetching New Changes
Suppose there are some files added to our repo. We could always use the GitHub website to browse the changes that were submitted. But we want to learn how to do it by interacting through the command line because you might need to do it this way at your job, and it'll work the same no matter which platform you use to interact with Git. So first, let's look at the output of the command: 
* git remote show origin

It says that the local branches out of date. This happens when there were commits done to the repo that aren't yet reflected locally. Git doesn't keep remote and local branches in sync automatically, it waits until we execute commands to move data around when we're ready. To sync the data, we use the command:
* git fetch 

This command copies the commits done in the remote repository to the remote branches, so we can see what other people have committed. Fetched content is downloaded to the remote branches on our repository. So it's not automatically mirrored to our local branches. We can run *git checkout* on these branches to see the working tree, and we can run git log to see the commit history.

Let's look at the current commits in the remote repo by running:
* git log origin/master
	
Looking at this output, we can see that the *remote origin/branch* is pointing to the latest commit. While the *local master branch* is pointing to the previous commit we made earlier on.

Let's see what happens if we run: 
* git status
	
Git status helpfully tells us that there's a commit that we don't have in our branch. It does this by letting us know our branches behind their remote origin/master branch. <br>
If we want to integrate the branches into our master branch, we can perform a *merge operation*, which merges the origin/master branch into our local master branch. To do that, we'll call:
* git merge origin/master
\- merge the changes of the master branch of the remote repository into our local branch

If we look at the *log output* on our branch now:
* git log
	
we should see the new commit. We see that now our master branch is up to date with the remote origin/master branch. With that, we've updated our branch to the latest changes. 

We can use *git fetch* to review the changes that happen in the remote repository. If we're happy with them, we can use *git merge* to integrate them into the local branch. Fetching commits from a remote repository and merging them into your local repository is such a common operation in Git that there's a handy command to let us do it all in one action. We'll check that out next.

#### What’s the main difference between git fetch and git pull?
- git fetch fetches remote updates but doesn't merge;  
- git pull fetchs the remote copy of the current branch and automatically try to merge it into the current local branch.

###  Updating the Local Repository
Since fetching and merging are so common, Git gives us the *git pull* command that does both for us. Running git pull will fetch the remote copy of the current branch and automatically try to merge it into the current local branch.

Let's check if our colleague has made any new changes to the repo. We'll run git pull and see what changes we get.
* git pull
\- it includes the output of the fetch and merge commands 
	
Then, look at the changes by using:
* git log -p -1
\- see changes made by colleague
	
When we called git pull, we might also see a new remote branch called, for eg:,"experimental", as if our colleague started working on a new feature in that branch. Let's check out the output of:
* git remote show origin
	
And see what it says about that new branch. We might see that there's a new remote branch called experimental, which we don't have a local branch for yet. To create a local branch for it, we can run:
* git checkout experimental
\- Git automatically copies the contents of the remote branch into the local branch. 
The working tree should have been updated to the contents of the experimental branch.

Now we're all set to work on the "experimental" feature together with our colleague.
	
But, If we want to get the contents of remote branches without automatically merging any contents into the local branches, we can call:
* git remote update
 
This will fetch the contents of all remote branches, so that we can just call checkout or merge as needed.

In our past examples, we've only looked at what happens with changes when they can be solved through *fast forward*. In upcoming section, we'll look at what happens when we try to push changes, especially when our changes generate conflicts.

### Solving Conflicts
<u>**The Pull-Merge-Push Workflow**</u>
We've now looked at the details of fetching and pulling data from a remote repositories without any local changes. We saw earlier how we can use the git push command to send our changes to the remote repo. But what if when we go to push our changes, there are new changes to the remote repo? To find it out, suppose we start by making a change to our *xyz.py* script.

Suppose we make our code clearer by renaming our parameter of function inside our script, and we make the code invocation clearer by using the name of the parameters in the call to the function, such that our code would still work.

All right, we've made the change. Let's stage it and commit it as usual. We'll first use:
* git add -p
\- to look at the changes we made and accept them
Then we'll create a commit message to show that we've renamed our parameter, and that we're using parameter names for the invocation as:
* git commit -m "Rename parameter, use parameter names for invocation"
	
We've made our change, staged it, and committed it. We should be ready to push into the remote repo, except now we have a collaborator also making changes.	
 Let's see what happens when we try running push:
* git push
	
When we tried to push, Git *rejected our change*, that's because the remote repository contains changes that we don't have in our local branch that Git *can't fast-forward*. Maybe you remember when we talked about Git's merging algorithms? As usual, Git gives us some helpful information along with the error message, especially the part about integrating remote changes with git pull.

This means we need to sync our local remote branch with the remote repository before we can push. We learned earlier that we can do this with:
* git pull
	
Git tried to automatically merge the local and remote changes to xyz.py, but *found a conflict*.

Let's first look at the tree of commits on all branches as represented by:
* git log --graph --oneline --all

This graph shows us the different commits and positions in the tree. We can see the master branch, the origin/master branch, and the experimental branch. The graph indicates that our current commit and the commit in the origin/master branch share a common ancestor, but they don't follow one another.

This means that we'll need to do a *three-way merge*. To do this, let's look at the actual changes in that commit by running:
* git log -p origin/master.
	
So our colleague decided to reorder the conditional clauses in the function to match the order that the parameters are passed to the function. They happen to *change in the same line that we changed* when we renamed the parameter variable, which caused the conflict that Git couldn't resolve.<br>
Let's fix it by editing the file to remove the conflict.
* atom xyz.py
	
We need to decide which line to keep to fix conflict(remove all of the conflict markers and only leave the code as it should be after the merge) which lets us check that there are no unresolved conflicts left. For example, we can keep the new order, but use renamed variable.

One thing to notice is that Git will try to do all possible automatic merges and only leave manual conflicts for us to resolve when the automatic merge fails.

In this case, we can see that the other changes we made were merged successfully without intervention. Only the change that happened in the same line of the file needed our input. 

Nice, now that we fixed the conflict, you can finish the merge.<br>
To do this, we need to add the xyz.py file, and then call git commit to finish the merge. 
* git add xyz.py
	
* git commit

The *editor message* shows that it's performing a merge of the remote branch with the local branch. We can *add extra information to this message*. For example, we can say that we fixed line in the function to use the new variable name and the new order.<br>
Our merge is finally ready, we can try pushing to the remote again:
* git push
\- push our work to the remote repo
	
Yes, after fixing the conflict, we were able to push our work to the remote repo. Let's look at the commit history of the master branch now, by calling:
* git log --graph --oneline

We see that the *latest commit is the merge*, followed by the two commits that caused the merge conflict, which are on split paths in our graph. As we called out before, when Git needs to do a three-way merge, we end up with a separate commit for merging the branches back into the main tree. 

Now we know how to successfully complete a pull, merge, and push cycle, even when it means doing some manual merges. <br>
Up next, we'll talk about using branches with a remote repositories.

### Pushing Remote Branches
Pushing remote branches is the process of sending the local changes on a remote branch to the remote repository. This is done using the git push command. 
	
If you are pushing the remote branch for first time, use: 
* git push -u origin <branch>
\- push a branch to a remote repo
	The -u option is used to set the upstream branch.
	
If you have a branch that you want to share with collaborators, you can push it to a remote server using:
* git push origin <branch>
 
Once our branch is pushed to the remote repo, our collaborators can view the code, test it, and let us know if it's ready for merging.

Assuming they say it's okay, how should this branch get merged back into the master branch? We'll talk about that next.

### Rebasing Your Changes
As mentioned earlier, that once our branch has been properly reviewed and tested, it can get merged back into the master branch. This can be done by us or by someone else. One option is to use the git merge command that we discussed earlier. Another option is to use the git rebase command. <br>
Rebasing means changing the base commit that's used for our branch.

The problem with three way merges is that because of the split history, it's hard for us to debug when an issue is found in our code, and we need to understand where the problem was introduced. By changing the base where our commits split from the branch history, we can replay the new commits on top of the new base. This allows Git to do a *fast forward merge and keep history linear*.

So, we can do this by running the command *git rebase*, *followed by the branch that we want to set as the new base*. When we do this, Git will try to replay our commits after the latest commit in that branch. This will work automatically if the changes are made in different parts of the files, but will require manual intervention if the changes were made in other files. Let's check out this process by rebasing our 'refactor' branch onto the master branch. First, we'll check out the master branch and pull the latest changes in the remote repo.
* git checkout master
	
* git pull

Git tells us that it's updated the master branch with some changes that our colleague had made. At this point, the changes that we have in the refactor branch can no longer be merged through fast forwarding into the master branch. That's because there's now an extra commit in the master that's not present in the refactor.

Let's see how this looks by asking the log command to show us the current graph of all branches.
* git log --graph --oneline --all

It can be really useful to understand complex history trees. Assume that the 'refactor' branch has *three commits* before the common ancestor, with the current commit that's at the head of the master branch. If we merged our branch now, it would cause a three way merge. But we want to keep our history linear. We'll do this with a rebase of the refactor against master:
* git checkout refactor
	
* git rebase master 

It says that it rewound head and replayed our work on top of it. And luckily, everything succeeded.

Let's look at the output of:
* git log --graph --oneline

Now we can see the master branch and linear history with our list of commits. We're ready to merge our commits back onto the main trunk of our repo and have this fast forwarded. To do that, we'll check out the master branch and merge the refactor branch.
* git checkout master
	
* git merge refactor
	
Awesome, we were able to merge our branch through a fast forward merge and keep our history linear.

We're now done with our refactor and can get rid of that branch, *both remotely and locally*. To remove the remote branch, we'll call:
* git push --delete origin refactor

To remove the local branch, we'll call:
* git branch -d refactor.

Yes, we're done with our refactor. We can now push changes back into the remote repo.
* git push 
\- push changes to remote repo
	
### Best Practices for Collaboration
It's a good idea to always synchronize your branches before starting any work on your own. That way, whenever you start changing code, you know that you're starting from the most recent version and you minimize the chances of conflicts or the need for rebasing.

Another common practice is to try and avoid having very large changes that modify a lot of different things. Instead, try to make changes as small as possible as long as they're self-contained. For example, if you are renaming a variable for clarity reasons, you don't want to have code that adds new functionality in the same commit. It's better if you split it into different commit. This makes it easier to understand what's going on with each commit.

On top of that, if you remember to push your changes often and pull before doing any work, you reduce the chances of getting conflict. We called out already that when working on a big change, it makes sense to have a separate feature branch.

This lets you work on new changes while still enabling you to fix bugs in the other branch. To make the final merge of the feature branch easier, it makes sense to regularly merge changes made on the master branch back onto the feature branch.

This way, we won't end up with a huge number of merge conflicts when the final merge time comes around.

If you need to maintain more than one version of a project at the same time, it's common practice to have the latest version of the project in the master branch and a stable version of the project on a separate branch.

You'll merge your changes into the separate branch whenever you declare a stable release.

Early in our Git journey, we mentioned that having good commit messages is important. It's already important when you're working alone since good commit messages help the future you understand what's going on, but it's even more important when you're collaborating with others since it gives your collaborators more context on why you made the change and can help them understand how to solve conflicts when necessary. So commit to being a good collaborator and remember to add those commit messages.

### Conclusion:
In this module, I have been introduced to GitHub and learned how it works with Git. I created new repositories and cloned those repositories onto my computer. Next, I got to know about what a remote repository is, how we can work with them, and how we can host them. I got familiar with commands like modify, stage, and commit, which was used for local changes, as well as the fetch command, which can pull any changes from remote repositories. I finally focused on learning about conflicts. This allowed me to explore the concepts of pull-merge-push workflows, pushing remote branches and rebasing your changes.