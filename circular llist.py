#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
def Circular(head):
    if head is None:
        return True
    
    i=0
    node=head.next
    while((node is not None)and(node is not head)):
        node=node.next
        i+=1
        
    return(node==head)


if __name__=='__main__':
    llist=Linkedlist()
    llist.head=Node(1)
    second=Node(2)
    Third=Node(3)
    Fourth=Node(4)
    
    llist.head.next=second
    second.next=Third
    Third.next=Fourth
    
    if Circular(llist.head):
        print('yes')
        
    else:
        print('no')
        
    Fourth.next=llist.head
    
    if Circular(llist.head):
        print('yes')
        
    else:
        print('no')
    
            
        


# In[ ]:




