# Owen Fish
# 10/15/17
# ocfish@email.wm.edu
# 703-915-1306
# 
# Python implementation of a basic linked-list class with various methods 
# designed for flexible data storage
#

class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.value = val
      self._next = None
      self._previous = None
      

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.header = Linked_List._Node(None)
    self.trailer = Linked_List._Node(None)
    self.header._next = self.trailer
    self.trailer._previous = self.header
    self.size = 0
    

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    return self.size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.

    new = Linked_List._Node(val)
    new._previous = self.trailer._previous
    self.trailer._previous = new
    new._next = self.trailer
    new._previous._next = new
    self.size += 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    
    if self.size == 0 and index == 0:
      raise IndexError
    elif (index >= 0 and index <= self.size -1) or index == 0:
      #Use ._next or ._previous, whichever is shorter
      if index -1 < self.size/2:
        current = self.header
        for i in range(index):
          current = current._next
  
      else:
        current = self.trailer
        for i in range(self.size - index + 2):
          current = current._previous 
              
      new = Linked_List._Node(val)
      new._next = current._next
      current._next = new
      new._previous = current
      new._next._previous = new
      self.size += 1        
      
    else:
      raise IndexError
        

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index >= 0 and index < self.size:
      #Use ._next or ._previous, whichever is faster
      if index - 1 <= self.size/2:
        current = self.header
        for i in range(index):
          current = current._next
      else:
        current = self.trailer
        current = current._previous
        for i in range(self.size - index):
          current = current._previous
        
        
        
      val = current._next.value
      current._next = current._next._next
      current._next._previous = current._next._previous._previous
      self.size -= 1  
    else:
      raise IndexError
    return val
        

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    
    #Use ._next or ._previous, whichever is faster
    if index >= 0 and index < self.size:
      if index - 1 <= self.size / 2:
        current = self.header
        for i in range(index):
          current = current._next
        val = current._next.value
      else:
        current = self.trailer
        for i in range(self.size - 1 - index):
          current = current._previous
        val = current._previous.value  
    else:
      raise IndexError
    return val

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    string = '['
    current = self.header
    current = current._next
    for i in range(self.size):
      val = current.value
      string = string + ' ' + str(val)
      if i < self.size - 1:
        string = string + ','    
      current = current._next
    string = string + ' ]'
    return string
      

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    current = self.header
    self._iter_node = current._next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    
    while self._iter_node is not self.trailer:
      to_return = self._iter_node.value
      self._iter_node = self._iter_node._next
      return to_return
    
    raise StopIteration
  
  def reverse(self):
    result = Linked_List()
    if self.size == 0:
      return result
    current = self.header._next
    result.append_element(current.value)
    while current._next is not self.trailer:
      current = current._next
      result.insert_element_at(current.value, 0)
    return result  
    
      
    


    
     
    
      
      
    
    
    
