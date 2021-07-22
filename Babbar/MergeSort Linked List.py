#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
def split(p):
    if not p:
        return p
    s,f = p,p
    while s and f and f.next:
        s = s.next        
        f = f.next.next
    return s
def merge(l,r):
    if not l:
        return r
    elif not r:
        return r
    res = Node(0)
    ans = res
    while l and r:
        if l.data < r.data:
            res.next = l
            l = l.next
        else:
            res.next = r
            r = r.next
        res = res.next
        if l:
            res.next = l
        elif r:
            res.next = r
    return ans.next
            
            
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, p):
        if not p:
            return p
        middle = split(p)
        nextMiddle = middle.next
        middle.next = None
        l = self.mergeSort(p)
        r = self.mergeSort(nextMiddle)
        ans = merge(l,r)
        return ans
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))
