# CSE2140 Second Language Programming 1 and CSE2110 Procedural Programming 1

## CSE2140 Notes 

### Version Control Systems 

Version control systems are a category of software tools that helps **record changes** to files by keeping track of modifications done to the file. 

Version control systems provides a framework for *external documentation*, where each commit documents what changes were made from previous versions of code. In addition, it provides documentation, such as README files within the project folder. 

Version control contributes to *change management* as data is not lost when personnel leave the project and new recruits that are hired will have documentation about what has already happened. 

When a project is ready for publishing, the version control system can also package the current project and release it. Release schedules vary depending on the project and organization structures. For example, Microsoft does their updates on Tuesday, and Google does their updates on Wednesday. They can either be time based (eg: Microsoft and Google) or feature-based (eg: videos being released for the core game and downloadable content (DLC) being released afterwards). 

There are many version control systems, such as Git, Subversion, Mercurial, and Microsoft Team Foundation Version Control. We are using Git for the computing science program at Lillian Osborne. Git is the most commonly used system, although there are some that are similar. 

#### Git and Git Repositories 

Git is a version control system (VCS) that tracks changes to source code. Git repositories are the online storage platform for projects versioned using Git. One important thing to note is that Git and Git Repos are not on any exams, however you will submit projects through Git. The curriculum doesn't have anything on Git and Git Repositories or VCS because our curriculum was published in 2009. Even so, learning Git and Git Repos are incredibly useful for working and industry standards. 

Cloning a repository takes a copy of the Git repository and places it onto the local computer. The clone also has all versioning and branches of the repository. With a clone on your computer, you do not need an internet connection to work on the code. To create a new version of the source code on Git, the new changes must be **committed** to Git to save a local of the changes. To synchronize the local changes to the online repository, the local committed version must be **pushed** to the online repository. 

* Note that a user can have multiple local commits of a project before pushing all the changes to the Git repository. 

To synchronize changes from the online repository to a local project, the online changes must be **pulled** to the local computer. 

* Note that it is best practice to pull changes to a local repository before adding additional changes. If a pull is not done first there may be conflicts when trying to synchronize changes afterwards. This practice is required for collaborating within a Git repo. 

There are additional features such as collaboration, restoring previous versions, and branching that are covered in CS30.  

## Change Management (IB)

Change management is the process, tools, and techniques to manage the people side of changes to achieve required business outcomes. 

Changing a system can be difficult for a variety of reasons.

* New personnel will need time to become accustomed to the workflow and styles of the project
* Staff usually need to learn new processes and skills
* New personnel must adjust to the culture of the new environments (People need to feel welcome so that they can stay for a long time)
* Staff set in their ways may find adjusting difficult (revolt!)
* Efficiency of the entire team will decrease as they lack experience with certain software and workloads
* There may be downtime between system changeovers
  * Transferring data between systems is complex
  * Data may be lost during the transfer
* Transitioning to new systems requires purchasing new (expensive!) equipment and time for users to adjust
* New systems may omit useful features from the old system 

## Computing Science 10 Review 

### Variables 

Variables are a tool to store data and call data at a later part of the program. When naming variables, there are different formats such as camelCase, snake_case, kebab-case, PascalCase (Capitalized), lowercase, UPPERCASE. (For IB, UPPERCASE is used for **all** variable names.) camelCase is used for function and method names, lowercase is used for local variables, UPPERCASE is used for global variables. 

When naming variables
1. The name of the variables can only have alphanumeric characters, underscores(_), or hyphens(-) 
2. Variable names must be unique (case sensitive)
3. It should be descriptive about the data it stores (so you can remember it)
4. Can't start with a number

