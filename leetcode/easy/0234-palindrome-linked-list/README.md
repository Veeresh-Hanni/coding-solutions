# Palindrome Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a singly linked list, return `true` *if it is a  **palindrome**  or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: head = [1,2,2,1]
Output: true

```

 **Example 2:** 

```
Input: head = [1,2]
Output: false

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9

 

 **Follow up:**  Could you do it in `O(n)` time and `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-08-31T01:04:07.056Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Approach 1 using stack
        """stack = []
        curr = head

        # Push all values onto stack
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # Compare front of list with stack (LIFO = reverse order)
        # curr = head
        # while curr:
        #     if curr.val != stack.pop():
        #         return False
        #     curr = curr.next

        # return True

        # simple using list slice
        return stack == stack[::-1]"""



        # Approach 2 using stack and add only half data
        # Step 1: Find length
        
        """length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Push only FIRST half onto stack
        stack = []
        curr = head
        for _ in range(length // 2):
            stack.append(curr.val)
            curr = curr.next

        # Step 3: Skip middle element if odd length
        if length % 2 != 0:
            curr = curr.next

        # Step 4: Compare second half with stack
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next

        return True"""



        # approach 3 find middle and reverse second half and compare
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if head and head.next is None:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow)
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/)