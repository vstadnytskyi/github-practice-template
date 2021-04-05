=======
Lessons
=======

Lesson 1
----------------------------
In this lesson, we will fork the repository to create your own copy on GitHub and clone it to the local drive, so you have access to the files locally.

Please see instructions on github.com
https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

Lesson 2
----------------------------

Lesson 3
----------------------------
Let us create a new simple function that multiplies to float numbers. In this repository there is already created file with algorithms: /github_practice_tempalte/numberical/algorithms.py Open it on your local computer and create a new function

.. code-block:: python

  def multiply(num1,num2):
      """
      calculates the product of two numbers

      Parameters
      ----------
      num1 (float)
      num2 (float)

      Returns
      -------
      num (float)

      Examples
      --------
      >>> num = multiply(1,3)
      """
      return num1*num2
I have already added it to the file. You just need to uncomment it. Now, when we are happy with the function, let us create a test. Go github_practice_tempalte/tests/test_numerical.py and inside 'class NumericalTest' add a new test function.

.. code-block:: python

  def test_multiply(self):
      from ..numerical import algorithms
      self.assertEqual(algorithms.multiply(3,4), 12)

I have already added it to the file. You just need to uncomment it. Next lesson we will run a pytest to see if all functions are working correctly.

Lesson 4
----------------------------
In this lesson, we will fix the function that does not work correctly and pytest returns "failed" flag.
