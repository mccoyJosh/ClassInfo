# Unit Testing Introduction

Unit testing is the process of laying out tests
that your code must pass. Typically, when done correctly, you end up
with pressing a single button which will test all of your code
and tell you how many of your tests passed/failed.

Some good reasons why you ought to do this are:

- ## Identifying Bugs Early:
  - Unit tests can catch bugs early in the development process, which makes them cheaper and easier to fix.
  
- ## Maintaining Code Quality:
  - Writing tests ensures that your code meets the expected behavior and maintains its quality throughout its lifecycle.

- ## Supporting Continuous Integration (CI) and Continuous Deployment (CD):
  - Unit tests can be integrated into CI/CD pipelines to automate the testing process and ensure that changes are thoroughly tested before being deployed to production.
    Having tests ready to go, when new features are implemented into your code, you can make sure none of your
    previous work broke due to your changes.
  
- ## Improving Design:
  - Writing tests often leads to better code design, as it encourages you to write modular code that is easier to test.

- ## Time Savings:
  - While writing tests initially takes time, it can save time in the long run by reducing the time spent debugging and fixing bugs.
    With well written tests, you should be able to find exactly where in your code you are experiencing an error.
  
