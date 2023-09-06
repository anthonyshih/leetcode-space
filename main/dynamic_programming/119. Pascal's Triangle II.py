'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

'''
'''
Note from Anthony
From problem 118 we can know:
A new row is " [1] + [ the sum of neighboring elements from row[-1] from 2nd position ] + [1]
For rowIndex = 0 return [ 1 ], from rowIndex = 1 we can start our for loop
We can update our row by row =new_row to avoid to build the triangle and find the last array 
'''


def getRow(rowIndex): 
    if rowIndex == 0:
        return [1]
    
    row = [1] # 因爲 rowIndex = 0 =>[1] 因此設置row=[1]
    
    for i in range(1, rowIndex + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        row = new_row
    
    return row


