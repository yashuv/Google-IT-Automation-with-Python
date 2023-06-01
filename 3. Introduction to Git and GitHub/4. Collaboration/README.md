## Collaboration
In this module, you’ll continue to explore the collaboration tools available in Git. You’ll learn about the tools that are available to help improve the quality of your code and to better track your code. This includes an overview of pull requests and how the typical workflow of a pull request looks like on GitHub. Next, you’ll dive into how you can squash changes in your code. We’ll finish up by providing you with a cheat sheet on fork and pull requests. Next up, we’ll cover what code reviews are and what the code review workflow looks like. Then, you’ll learn about how to use code reviews on GitHub. The final lesson of this module will focus on managing projects. We’ll take a rundown of best practices on managing projects and how to manage collaboration within those projects. We’ll explore different ways of tracking issues and finish up by discussing the concept of continuous integration with your projects.

### Learning Objectives
* Utilize the code review workflow
* Create, update, and execute pull requests on GitHub
* Explain what a code review is
* Use code reviews in GitHub
* Explain the importance of managing projects and accepting or rejecting changes
* Utilize issue trackers
* Describe the methodology behind continuous integration

### Intro
GitHub has become a super popular platform for collaboration across many projects. It's used heavily for open-source projects. These are projects that allow anyone to use, copy, and modify their code. Having the code published online means that anybody in the world can learn from what the project is doing, and even collaborate on fixes and extra features.<br>
If you're trying to learn a new technology, it's a great idea to practice your skills by contributing to a project that uses that technology. To do that, you'll need to know how to interact with the project. This includes how to send bug fixes, how to make sure that your fixes are applied, and even how to figure out which fixes are needed.

### Pull Request 
#### A Simple Pull Request on Github
Forking a repository on GitHub allows you to freely experiment with changes without affecting the original project. Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.
In GitHub, a pull request is a method of submitting contributions to an open development project. Pull requests are a means of submitting proposed changes to a project through its GitHub repository.<br>
We a click on the `little pencil icon` which let's us edit the file directly from the web interface of Github. We can edit a file in a project that we don't have a right access to. GitHub tells us it created a fork of the project for us, which we can commit our changes to. And if we submit changes to this file, it will create a new branch so that we can send a `pull request`.<br>
`Forking` is a way of creating a copy of the given repository so that it belongs to our user. In other words, our user will be able to push changes to the forked copy, even when we can't push changes to the other repo. When collaborating on projects hosted on GitHub, the typical workflows, first, create a fork of the repo, and then work on that local fork. A forked repo is just like a normal repo, except Github knows which repo it forked from. So we can eventually merge our changes back into the main repo by creating a pull request. A `pull request` is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree. <br>
Hence, we can create pull request directly on GitHub by using the web interface to edit files.

### The Typical Pull Request Workflow on GitHub
Createing pull request directly on GitHub by using the web interface to edit files works for simple changes like fixing typos or adding documentation to a function, but it's not so great for making larger changes that we want to preview or test. To do that, we'll normally have a local copy of the repo in our computer and work with the forked repo as a remote. We'd need to use all the Git commands that we've learned up till now to do this. Let's check out this process by creating a fork of another repo.
<!-- <a href ="https://www.coursera.org/learn/introduction-git-github/lecture/8mpDb/the-typical-pull-request-workflow-on-github">Click here for video demo</a> -->

### Updating an Existing Pull Request
It is quite common doing updates to an existing pull requests for some improvements. The improvement could be to add documentation or tests, or maybe we need to make sure that change works for all cases or that it follows the project style guidelines.<br>
If you need to update an existing pull request, you can simply `commit` additional changes to your same feature branch and `push` them to GitHub. The new commits will automatically be added to the existing pull request.

### Squashing Changes
Squashing changes together combines multiple commits into a single commit. This is useful for cleaning up a messy commit history or for getting rid of commits that are no longer relevant.<br>
So say the project maintainers ask us to create a single commit that includes multiple changes and a more detailed description than the one we submitted. We can do that by using the interactive version of the rebase command called `rebase-i`, as the parameter to the command will pass the `master` branch. So we'll call:

* git rebase-i master

When we call an interactive rebase, a text editor opens with a list of all the selected commits from the oldest to the most recent(reverse chronological order). To squash a commit, change the word `pick` to `squash` next to the commit you want to squash. Save and close the file, and your commits will be squashed together.

We can check the output of:
* git show
\- to see the latest commit and the changes in it.
	
* git status
\- to check the info that git gives us about the current state

* git log --graph --oneline --all -4
\- to see the graph history of our commits 
\- --all for all branches, and -4 for just the latest four commits

Now, when we call:
* git push
Git doesn't like us trying to push our change because it can't be fast-forwarded.i.e: failing to push because of non-fast-forward.

But in this case, we don't want to create a merge. Instead, we want to replace the old commits with the new one. To do this, we will call:
* git push -f
\- to `force` git to push the current snapshot into the repo as is
	
This time, our push completed successfully.<br>

Let's look once again our history graph by running:
* git log -- graph --oneline --all -4
This time, it's just one commit on top of master.

Now looking at the contents of the pull request, we've managed to combine both are commits into one by using the interactive version of git rebase.

## Git Fork and Pull Request Cheat Sheet
Check out the following link for more information:

* https://help.github.com/en/articles/about-pull-request-merges

## Code Reviews
A code review means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns. The goal of a code review is to improve the project by making sure that changes are high quality. It also helps us make sure that the contents are easy to understand. That the style is consistent with the overall project. And that we don't forget any important cases. Reviews increased the number of eyes that have checked the code. This increases the code quality and reduces the amount of bugs. It doesn't mean that there'll be no bugs, but at least the most obvious bugs will be caught. Also, this helps spread knowledge since both the code writers and the code reviewers now know what the code is doing.

Goals of code review are:
- Make sure that the contents are easy to understand
- Ensure consistent style
- Ensure we don't forget any important cases

Some Common code issues that might be addressed in a code review are:<br>
- Using unclear names
- Forgetting to handle a specific condition that could cause a problem
- Forgetting to add tests

### More Information on Code Reviews
Check out the following links for more information:

* http://google.github.io/styleguide/

* https://help.github.com/en/articles/about-pull-request-reviews

* https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31

* https://smartbear.com/learn/code-review/what-is-code-review/

## Managing Projects

### Managing Colaborations
If you are using GitHub to manage your project, you can use the issue tracker to track collaboration and issues. When an issue is created, you can assign it to a specific person and add labels to track the issue. GitHub also offers a number of features that can help you manage your project. For example, you can use the Issues feature to track bugs or features that need to be addressed. 

### Tracking Issues
When working on a project with others, it is important to keep track of who is doing what and where the project stands. GitHub's issue tracker is a great way to do this. By creating an issue, assigning it to specific people, and adding labels and milestones, you can easily keep track of progress and ensure that everyone is on the same page.

### Continuous Integration
We can write automated tests to test the code for us and then use a continuous integration (CI) system to run those tests automatically. A `continuous integration system` will build and test our code every time there's a change. This means that it will run whenever there's a new commit in the main branch of our code. It will also run for any changes that come in through pull request. In other words, if we have continuous integration configured for our project, we can automatically run our tests using the code in a pull request. This way, we can verify that the test will pass after the new changes get merged back into the tree and that means instead of hoping our collaborators will remember to properly test their code, we can rely on our automated testing system to do it for us. Once we have our code automatically built and tested, the next automation step is `continuous deployment`, which is sometimes called `continuous delivery (CD)`. Continuous deployment means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time. This allows errors to be caught and fixed early. Typical configurations include deploying a new version whenever a commit is merged into the main tree or whenever a branch is tagged for release.<br>
There's a large world of tools and platforms related to CI/CD which is what the whole system is usually called. One popular option is Jenkins which can be used to automate lots of different types of projects. Some repository hosting services like GitLab provide their own infrastructure for doing continuous integration. GitHub doesn't offer an integrated solution. Instead, the popular alternative is to use Travis which communicates with GitHub and can access the information from GitHub projects to know which integrations to run.

### Additional Tools
Check out the following links for more information:

* https://arp242.net/diy.html 

* https://help.github.com/en/articles/closing-issues-using-keywords

* https://help.github.com/en/articles/setting-guidelines-for-repository-contributors 

* https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html

* https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/

* https://docs.travis-ci.com/user/tutorial/

* https://docs.travis-ci.com/user/build-stages/ 

## Conclusion
I've checked out a lot of tools for better collaboration through GitHub. I studied the typical workflow for pull requests, how to update and squash changes. I learnt how code reviews help us improve our code by catching bugs, typos, and other issues. Finally, I looked into more advanced collaboration technologies, such as issue trackers and continuous integration services.