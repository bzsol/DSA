class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.lenght = 1
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        return True
    def dequeue(self):
        if self.lenght == 0:
            return None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.lenght -= 1
            if self.lenght == 0:
                self.first= None
                self.last = None
            return temp
            



