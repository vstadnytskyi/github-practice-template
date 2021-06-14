=======
Lessons
=======

Lesson 1
----------------------------
In this lesson, we will fork the repository to create your own copy on GitHub and clone(meaning to download) it to the local drive, so you have access to the files locally.

Please see instructions on github.com
https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

after finishing this part you should have two remote repositories(repos) connected. One will be origin(that is your forked copy) and the second one is upstream (that point at this practice repo)

git@github.com:vstadnytskyi/github-practice-template.git
or
https://github.com/vstadnytskyi/github-practice-template.git

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

Lesson 5
---------------
creating first pull request.

Go to the file /docs/source/intoduction.rst and delete the phrase "There is a big fat typo in the introducion." add file, commit and create pull request. I will eveluate it, and if everything is good I will comment on it and deny it (so we do not change the practice repo and leave it as it is for future practices).

Note, if you see typos or do want to impove the text elsewhere, please! be my guest and submit pull requests. I am more than happy to get help with making this practice better.
