# Getting Your Python On

In this module, you’ll learn about the different types of operating systems, and how you can get your python code ready to interact with the operating system. We’ll learn about getting your environment set up and installing additional Python modules that will help you along the way. We’ll rundown interpreted versus compiled language, and how they differ from each other. We’ll dive into the benefits of automation, and point out common pitfalls so you can avoid them. Finally, we’ll learn about Qwiklabs, which will be used for graded assessments.

### Learning Objectives
Identify the characteristics of different operating systems
Use the Python environment to create programs
Install additional Python modules in the Python environment
Install and run Python on a local machine
List the benefits and pitfalls of automation

## Getting Familiar with the Operating System
An operating system (OS) is a system software that manages computer hardware and software resources and provides common services for computer programs. The operating system is the most important type of system software in a computer system. Without an operating system, a user cannot run an application program on their computer.

There are actually two main parts in operating system:<br>
The *kernel* and the *user space*. <br>
The kernel is the main core of an operating system. It talks directly to our hardware and manages our systems resources. As users, we don't interact with the kernel directly. Instead, we interact with the other part of the operating system called the user space.<br>
The User space is basically everything outside of the kernel. These are things that we interact with directly, like the system programs and user interface. So when we say operating system, we're referring to both the kernel and the user space. 
The major operating systems using IT today are Windows, Mac OS, and Linux. The Windows operating system is developed by Microsoft, and is widely used in the business and consumer space. Most PCs come with Windows as the default operating system. Mac OS is developed by Apple and is mainly used in the consumer space. If you purchase any Apple computer, they'll come with Mac OS preloaded. Linux is an open source operating system. Open source software is free to share, modify, and distribute. Linux is used heavily in business infrastructure. Most servers in the world today are running Linux.

In this module, we'll use Python to interact with the operating system. Python is a cross-platform language. You can use it on Windows, Mac OS, Linux, and even lesser known Unix variants like FreeBSD. It's even available on mobile phones. Since it's cross-platform, we can use the same Python code to get to our goal on any operating system, whether the goal is opening files, processing text, or managing running processes. This makes Python a great tool for IT specialists who needs to interact with different operating systems.

## Getting Your Computer Ready for Python
As an IT specialist, it's important to know how to install and uninstall software in different operating systems. To run Python locally, you either have it installed on your computer. You can use Python on all major operating systems. So it doesn't matter if you're running Windows, macOS or Linux, you should be able to run Python locally on your computer. It may even already be installed in your system. To check whether you already have Python installed on your computer, open a terminal or command prompt and execute the Python command:
	* python --version

It could say it doesn't recognize the command, which means you don't have Python installed.  It could return a version that starts with the number ,eg:three which means, you have Python 3 installed. For this course, we'll be using Python 3.

If you don't have Python installed yet, it is recommended that you visit the <a href="http://www.python.org/">official Python website</a> and download the installer that corresponds to your operating system.

After checking that you have Python 3 installed, we'll also learn about installing additional modules that aren't part of the Python Standard Library. 
When developers write a Python module that they think others might find useful, they publish it in PyPI, also known as the Python Package Index. We can browse as repository of Python modules to find the module we need. It includes thousands of projects which are classified by different categories, like topic, development studies, and intended audience. These external modules are generally managed with a command line tool called pip. This is a cross-platform tool so you can use it to install, update, and remove external modules on whichever operating system you're running on your computer.

## Running Python Locally
**Interpreted vs. Compiled Languages**
A compiler is a computer program(a piece of software) that translates computer code written in one programming language into another programming language. Compilers are typically used to translate code written in high-level programming languages into code written in low-level programming languages, which can be run on a computer. The computer can read and execute the machine level code directly. Some examples of commonly use compiled programming languages are C, C++, Go and Rust.
<img src="compiler"/>

An interpreter is a computer program that executes code written in a programming language on a computer. Interpreters are typically used to execute code written in high-level programming languages on a computer. Programs written in interpreted language generally rely on an intermediary program called an interpreter. These programs use interpreters to execute the instructions specified in the code, rather than running them through a compiler first. So this makes the development cycle for a program written in an interpreted language much faster. Because its developer doesn't need to wait for the code to be compiled to execute it, and the same code can be read by interpreters running on different operating systems without needing to make any additional changes. The tradeoff is that interpreted languages generally run slower than compiled ones. Python, Ruby, JavaScript, Bash, and PowerShell are all examples of interpreted programming languages.
<img src="interpreter"/>

**IDE**
The term IDE stands for Integrated Development Environment, and usually refers to a code editor with some handy extra capabilities that make writing scripts a lot easier. It is a software application that provides a complete set of tools for software development. We do most of our programming work in code editors and IDEs. 

You can go with whatever is already installed on your computer like Notepad, TextEditor on Windows, TextEdit on Mac OS or nano on Linux. You can choose a more advanced code editor like Atom, Notepad++, or Sublime Text or go for a fully featured graphical IDE like Eclipse or PyCharm. 

## Automating Tasks Through Programming
**Benefits of Automation**
Automation refers to the use of technology to automate tasks or processes. This can include things like using software to automate tasks, using robots to automate manufacturing processes, or using artificial intelligence to make decisions. automation can allow the IT infrastructure to scale, keeping pace with growth and demand. Scalability means that when more work is added to a system, the system can do whatever it needs to complete the work.  for example: Automating the backup and disaster recovery of servers.

**Pitfalls of Automation
 Despite automation has many benefits, when automation is implemented without baffle design, it can cause some serious problems.
1. Over-automation can lead to a loss of control over systems and processes.
2. Automation can create new security risks and vulnerabilities.
3. Automation can increase the complexity of systems and processes, making them more difficult to understand and manage.
4. Automation can lead to unexpected or undesirable outcomes.
5. Automation can create dependencies on specific tools, technologies, or personnel.

If we estimate that it would take less time to automate the tasks than it would to do it manually, chances are, it's a good candidate for automation. So, the time to write the automation is less than time to perform the task multiply by the amount of times you do it, then automate the task. 

A concept called the Pareto Principle can also be a useful guideline to help you decide which tasks to automate. When applied to automation in IT, the Pareto Principle states that 20% of the system administration tasks that you perform are responsible for 80% of your work. If you can identify and automate those 20% of your tasks, you could save yourself a whole lot of time.

Automation, it's an incredibly powerful tool that saves time, reduces mistakes, and facilitates growth and scalability. But we need to apply it thoughtfully to avoid some of the pitfalls that can arise from its use. Keep these things in mind, and automation can be a valuable asset in your toolbox.

** Safety measures of automation in IT
1. Implement a system of regular backups and disaster recovery procedures to ensure that data and critical systems can be recovered in the event of an automation failure.
2. Conduct thorough testing of automation systems before putting them into production to ensure that they will work as intended.
3. Put in place monitoring and logging systems for automation systems to help identify and diagnose problems when they occur.
4. Implement security controls for automation systems to help prevent unauthorized access and misuse.
5. Develop and maintain documentation for automation systems to help ensure that they can be properly used and maintained.
6. Train users on how to properly use and maintain automation systems.
7. Establish procedures for handling errors and exceptions that occur.

### Conclusion:
In this course, I learned how to use Python to perform system administration tasks and interact with a computer’s operating system.