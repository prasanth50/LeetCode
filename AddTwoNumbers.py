# 2. ADD Two Numbers
# Medium

# 17694

# 3669

# ADD to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. ADD the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


def ADDTwoNumbers(l1,l2): # This change is from new branch.
    l,m = 0,0
    for i in range(len(l1)-1,-1,-1):
        l *= 10
        l += l1[i]
        
    for j in range(len(l1)-1,-1,-1):
        m *= 10
        m += l2[j]
        
    return l+m

print(ADDTwoNumbers([2,4,3],[5,6,4]))
        
