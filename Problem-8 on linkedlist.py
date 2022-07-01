class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Single_Linked_List:
    def __init__(self):
        self.head=None

    def insert_At_Begin(self,data):
        node_beg=Node(data)
        node_beg.next=self.head
        self.head=node_beg

    def insert_At_End(self,data):
        node_end=Node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=node_end

    def insert_At_Pos(self,pos,data):
        node_pos=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        node_pos.next=temp.next
        temp.next=node_pos

    def delete_At_Begin(self):
        temp=self.head
        self.head=temp.next
        temp=None

    def delete_At_End(self):
        prev=self.head
        temp=prev.next
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def delete_At_Pos(self,pos):
        prev=self.head
        temp=prev.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp=None

    def display(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print()

def main():

    obj=Single_Linked_List()
    n1=Node(10)
    obj.head=n1
    n2=Node(20)
    n1.next=n2
    n3=Node(30)
    n2.next=n3
    n4=Node(40)
    n3.next=n4
    n5=Node(50)
    n4.next=n5

    print("The list is : ")
    obj.display()

    obj.insert_At_Begin(5)
    print("Element inserted at begin : ")
    obj.display()

    obj.insert_At_End(60)
    print("Element inserted at end : ")
    obj.display()

    obj.insert_At_Pos(4,25)
    print("Element inserted at given postion : ")
    obj.display()

    obj.delete_At_Begin()
    print("Element deleted at beginning : ")
    obj.display()

    obj.delete_At_End()
    print("Element deleted at end : ")
    obj.display()

    obj.delete_At_Pos(4)
    print("Element deleted at given position : ")
    obj.display()

if __name__=='__main__':
    main()