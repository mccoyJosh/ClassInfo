# Unit Testing (In Python)

Now, most langauges do not come built in with a testing framework... but python does.
Now the built-in package technically is 'fine', but if you are doing a serious
project you are probably going to want use something like [PyTest](https://pypi.org/project/pytest/) as it just has way more functionality.


But the idea of when you go about unit testing is to test every possibility in your code. 
If you have some sort of sequence, make sure the case where it may go outside of bounds is covered.
If you have a method that catches an error in a specific circumstance, make a test which sees if it
catches that error properly.

You want to TRY to test every path in your code.

For the sake of this example, I am using the Bank class from before.



# LOOK AT EXAMPLE_TEST_PROJECT

Run this command from root directory:

`python -m unittest SDEV140.M07.Day1.t3_UnitTesting.example_test_project.tests.test`