##  Version Control System (VCS)
A version control system (VCS) is a set of tools that keeps track of the changes we make to our files over time so that you can recall specific versions later. This allows you to revert files back to previous versions of the files if necessary, or compare changes over time. Version control systems are most commonly used for source code files, but they can be used for any type of file, including code, images, and documents.<br>
Common version control systems include Git, Mercurial, and Subversion. In this course we chose Git for its popularity, multi platform support, and robust set of features.

### Git
Git is a VCS created in 2005 by Linus Torvalds, the developer who started the Linux kernel. Git is now one of the most popular version control systems out there and is used in millions of projects. Unlike some version control systems that are centralized around a single server, Git has a distributed architecture. This means that every person contributing to a repository has full copy of the repository on their own development machines. Repositories can be used by as many developers as needed.

### What characteristics make Git particularly powerful?<br>
The ability to work offline, the ability to easily revert changes, and the ability to branch and merge are all characteristics that make Git particularly powerful.

### More Information About Git
Check out the following links for more information:

* https://git-scm.com/doc

* https://www.mercurial-scm.org/

* https://subversion.apache.org/

* https://en.wikipedia.org/wiki/Version_control

Let's install Git on the system:<br>
Check whether you already have it installed by running:
<code> git --version</code> <br>

If you have not already, you can download it from the website and install it.<br>
* (Git download page)[https://git-scm.com/downloads]
* (Git installation instructions for each platform)[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]

Once installed, you will be able to use it from the command line just like any other tool. Make sure that you are running a current version!<br>
One interesting thing about the Windows installation is that it comes preloaded with an environment called MinGW64. This environment lets us operate on Windows with the same commands and tools available on Linux. So you can practice some Linux command line tools on your Windows machine. After installing Git on your Windows machine, you'll be able to use Git from the Linux command line. If you selected the default option for the path environment question during installation, you'll be able to also run it from the PowerShell command line.

<pre>
git config --global user.name "Your Name" 
git config --global user.email "youremail@example.com"
</pre>
The first two lines set the author name and email address respectively. These are used to populate the author field of commit messages.<br>
The --global flag tells git to use the configuration setting for all repostories we use.

**Any Git project consists of 3 sections**:<br>
The *Git directory*, the *working tree* and the *staging area*.

The **git directory** contains all the changes and their history. It acts as a database for all the changes tracked in Git.<br> 
The **working tree** contains the current versions of the files. It acts as a sandbox where we can edit the current versions of the files.<br>
The **staging area** which is also known as the *index* is a file maintained by Git that contains all of the information about what files and changes are going to go into your next command.

When we operate with Git, our files can be either tracked or untracked. Tracked files are part of the snapshots, while untracked files aren't a part of snapshots yet. This is the usual case for new files.<br> 
Each track file can be in one of three main states, *modified,* *staged* or *committed*.

- Modified state is when a file has been changed but the changes have not been staged for commit.
- Staged state is when a file has been changed and the changes have been staged but not committed.
- Committed state is when a file has been changed and the changes have been committed. The changes made to it are safely stored in a snapshot in the *Git directory*. <br>

This means that typically a file tracked by Git, will first be modified when we change it in any way. Then it becomes staged when we mark those changes for tracking. And finally it will get committed when we store those changes in the VCS.

### Conclusion
Version control is a powerful concept that can bring many benefits. By understanding and utilizing the diff and patch commands, you can automate the process of differentiating and editing files. Git is a powerful tool that can bring even more benefits. By installing Git on your machine and utilizing it to create and clone repositories, add code, check the status of code, and commit code, you can take advantage of all that Git has to offer.