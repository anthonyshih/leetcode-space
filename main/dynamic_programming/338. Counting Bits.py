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