"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


note from William

when you draw the decision tree
you will find that this is a DP question
try to do the buttom-up trace back 
in the below is the case that n=5

   _ _ _ _ _ _
   8 5 3 2 1 1 

so the key is to define the last one and two
the keep rolling to the left 
and you can notice this is a fib
in this case is n-1
we can keep updating the array till the end of the array

 
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        one, two = 1, 1

        for i in range(n-1):
            temp = one # you save this with tme so you don't miss it
            one = one + two
            two = temp #then you got the two in temp and going going
        
        return one