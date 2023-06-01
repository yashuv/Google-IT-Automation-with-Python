# Testing in Python
In this module, you’ll learn how to create tests in Python. We’ll cover what testing is all about and dive into the differences between manual versus automated testing. Next, we’ll explore what unit tests are intended to do and how to write them. Then, we’ll learn about other test concepts like black box versus white box tests and how test-driven development can frame how you design and write your code. Finally, you’ll learn about errors and exceptions, and how to combat them.


## Learning Objectives
* Explain what testing is and the different types of testing available
* Describe the difference between black box and white box testing
* Explain test-driven development
* Apply a try-except construct to catch errors and exceptions

##

##

##

### Unit Test Cheat-Sheet
Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.

**Best of Unit Testing Standard Library Module**

Understand a Basic Example:

* https://docs.python.org/3/library/unittest.html#basic-example

Understand how to run the tests using the Command Line:

* https://docs.python.org/3/library/unittest.html#command-line-interface

Understand various Unit Test Design Patterns:

* https://docs.python.org/3/library/unittest.html#organizing-test-code

* Understand the uses of setUp, tearDown; setUpModule and tearDownModule

Understand basic assertions:
<img src="images/understanding basic assertion.png"/>

Understand more specific assertions such as assertRaises

* https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

## More About Tests
Check out the following links for more information:

* https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/

* https://landing.google.com/sre/sre-book/chapters/testing-reliability/

* https://testing.googleblog.com/2007/10/performance-testing.html

* https://www.guru99.com/smoke-testing.html

* https://www.guru99.com/exploratory-testing.html

* https://testing.googleblog.com/2008/09/test-first-is-fun_08.html

## Handling Errors Cheat-Sheet
Raise allows you to throw an exception at any time.

* https://docs.python.org/3/tutorial/errors.html#raising-exceptions

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

* https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

* https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.

* https://docs.python.org/3/tutorial/errors.html#handling-exceptions

Except is used to catch and handle the exception(s) that are encountered in the try clause.

* https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Other interesting Exception handling readings:

* https://doughellmann.com/posts/python-exception-handling-techniques/