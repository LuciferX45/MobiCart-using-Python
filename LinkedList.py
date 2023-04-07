#Represent a node of linked list    
class Node:    
    def __init__(self,data):    
        self.data = data   
        self.previous = None  
        self.next = None  
            
class LinkedList:    
    #Represent the head and tail of the linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
            #Both head and tail will point to newNode    
            self.head = self.tail = newNode;    
            #head's previous will point to None    
            self.head.previous = None;    
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None;    
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
            #newNode's previous will point to tail    
            newNode.previous = self.tail;    
            #newNode will become new tail    
            self.tail = newNode;    
            #As it is last node, tail's next will point to None    
            self.tail.next = None;    
                
    #display() will print out the nodes of the list    
    def display(self):   
        #Node current will point to head    
        current = self.head   
        if(self.head == None):    
            print("List is empty");    
            return   
               
        while(current != None):         
            print(current.data)  
            current = current.next

    #display data from an exact node            
    def Ndisplay(self,counter):
        temp = self.head
        if counter == 0:
            if(temp != None):
                return(temp.data)
        elif counter == 1:
            if(temp != None):
                temp = temp.next
                return(temp.data)
        else:
            for i in range(1, counter-1):  
                if(temp != None):
                    temp = temp.next
            return(temp.data)

    #shows the size of the linked list
    def size(self):
        current = self.head
        count=0
        while current !=None:
            count=count+1
            current=current.next
        return(count)

    #helps search a node in the Linked List
    def SearchElement(self, searchValue):
        temp = self.head
        found = 0
        i = 0 

        if(temp != None):
           while (temp != None):
               i += 1
               if(temp.data == searchValue):
                  found += 1
                  break
               temp = temp.next
        if(found == 1):
           print("Model: ",temp.data,"\nPrice: ",temp.next.data)
           #from here we can return value the model and price for adding it to the cart
        else:
           print(searchValue,"is not found in the list.")




