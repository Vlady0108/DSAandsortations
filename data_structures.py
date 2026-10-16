# How many jobs the same type

from this import d


def count_marketers(job_titles):
    count = 0
    for job_title in job_titles:
        if job_title.lower() == "marketer":
            count += 1
    return count

# Last job in profile

def last_work_experience(work_experiences):
    if len(work_experiences) == 0:
        return None
    return work_experiences[-1]

# 1st Custom Data Structure : The stack ( like a list but designed more restrictive)
# ( LIFO - last in first out )
# append
# Pop and peek

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items[-1]
        del self.items[-1]
        return val

# Takes a string as input and returns True if the
# parantheses in the string are balanced and Fase otherwise.
# An instance of the provided Stack class in stack.py to keep
# track of the parantheses.

def is_balanced(input_str):
    s = Stack()
    for c in input_str:
        if c == "(":
            s.push("something")
        elif c == ")":
            popped = s.pop()
            if popped is None:
                return False
    val = s.peek()
    return val is None

# Queues:
# push(item)
# pop()
# peek()
# size()
# these queue operations Big O complexity
# is O(1)


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

# Linked list:
# for a faster queue , there is the linked
# list ( instead of a regular List array )
# A linked list is where elements are not stored next to
# each other in memory , instead, each item references the next in chain.

# the yield keyword in Python return a value like the return keyword
# It is used secondly to turn the function into a
# generator function

# A generator function creates a new function object.
# When that function is called, it executes the code in the
# generator function until it hits a yield statement
# At the point, the function pauses and returns the value of the
# yield statement. The next time the function is called,
# it picks up right where it left off.

from node import Node

class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        if self.head is None:
            self.tail = node
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        old_tail.set_next(node)
        self.tail = node
        '''last_node = None
        for n in self:
            last_node = n
        last_node.set_next(node)'''

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

# Linked list queue for having a function running
# at a O(1) complexity. Now we need a way to remove
# the first element from the linked list
# in constant time. When we are finished, our
# LinkedList will fulfill the basic requirements of a Queue:
# add_to_tail : constant time insert
# remove_from_head : constant time pop

# A queue made with a linked list instead of an
# array can have O(1) complexity pushes and pops

# A queue that uses and array does not have O(1) pushes
# and pops because  when elements are added or removed from
# the first index of the array all the items need to shift
# which takes O(n) complexity time.


class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        temp.next = None
        return temp

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
