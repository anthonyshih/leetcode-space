'''

https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''


'''
Solution from Hottari

Sol. I
1. For each x belonging to 2^m, there must be a '1' (1, 10, 100, 10000...)
2. Any y from 0 to n can be decomposed into 2^m + p.

So, we can create a temporary integer called 'update' 
and double it when i == update*2 (since 2^m must have a '1')

Step 0: ans[0] = 0
Step 1: Check 'update' (Is i == update*2?)
Step 2: ans[i] = 1 + ans[i - update] (any y from 0 to n can be decomposed into 2^m + p)



Sol. II
1. The binary representation of an even number ends in xxxxx0, while that of an odd number ends in xxxxx1
2. The fundamental method to find a binary representation is division by 2. ( "/2" ) 

so,
step 0: ans[0] = 0
step 1: ans[i] = ans[int(i/2)] + i%2

'''

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(n+1)                             # faster than list.append() and [0 for i in range(n+1)]
        update = 1
        for i in range(1, n+1):
            if i == update*2:                       # the binary representation of power(2, n1) must be 1 
                update = i
                ans[i] = 1
            else: ans[i] = 1 + ans[i - update]      # i = update + n2 (update < n2 < update*2) 
                                                    # ( use previous value in the list -> dynamic ) 
        return ans