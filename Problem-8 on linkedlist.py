class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Single_Linked_List:
    def __init__(self):
        self.head=None

    def insert_At_Begin(self,data):
        node_beg=Node(data)
        if(self.head==None):
            self.head=node_beg
        else:
            node_beg.next=self.head
            self.head=node_beg

    def insert_At_End(self,data):
        node_end=Node(data)
        if(self.head==None):
            node_end=self.head
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=node_end

    def insert_At_Pos(self,pos,data):
            node_pos=Node(data)
            temp=self.head
            for i in range(1,pos-1):
                temp=temp.next
            if(pos!=1):
                node_pos.next=temp.next
                temp.next=node_pos
            else:
                self.head=node_pos
                node_pos.next=temp
            
    def delete_At_Begin(self):
        if(self.head==None):
            print("Deletion is not posssible")
            return
        temp=self.head
        self.head=temp.next
        temp=None

    def delete_At_End(self):
        if(self.head==None):
            print("Deletion is not posssible")
            return
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
            if(pos==1):
                self.head=temp
                prev=None
            else:
                prev.next=temp.next
                temp=None

    def display(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while temp:
                if temp.next:
                    print(temp.data,"-->",end=" ")
                else:
                    print(temp.data)
                temp=temp.next

            print()
    def count(self):
        temp=self.head
        con=1
        while temp:
            con+=1
            temp=temp.next
        return con

def main():
    obj=Single_Linked_List()
    i=True
    while(i):
        print("Press 1 to insert at begining\n"
        "Press 2 to insert at ending\n"
        "Press 3 to insert at any position\n"
        "Press 4 to delete at begining\n"
        "press 5 to delete at end\n"
        "press 6 to delete at any position\n"
        "Press any other number to exit")
        try:
            n = int(input("Enter your choice : "))

            if(n==1):
                data=int(input("Enter the data : "))
                obj.insert_At_Begin(data)
                print("Element inserted at begin : ")
                obj.display()
            elif(n==2):
                data=int(input("Enter the data : "))
                obj.insert_At_End(data)
                print("Element inserted at end : ")
                obj.display()
            elif(n==3):
                data=int(input("Enter the data : "))
                pos_data=int(input("Enter the position : "))
                if(pos_data>obj.count()):
                    print("Enter the postion  less than the ",(obj.count()+1))
                elif(pos_data==0):
                    print("Enter from 1st position ")
                else:
                    obj.insert_At_Pos(pos_data,data)
                    print("Element inserted at given postion : ")
                    obj.display()
            elif(n==4):
                    obj.delete_At_Begin()
                    print("Element deleted at beginning : ")
                    obj.display()
            elif(n==5):
                    obj.delete_At_End()
                    print("Element deleted at end : ")
                    obj.display()
            elif(n==6):
                    pos_data=int(input("Enter the position to delete  : "))
                    if(pos_data>=obj.count()):  
                        print("Enter the position which is less than ",obj.count())
                    elif(pos_data==0):
                        print("Enter from 1st position ")
                    else:
                        obj.delete_At_Pos(pos_data)
                        print("Element deleted at given position : ")
                        obj.display()
            else:
                    i=False
        except ValueError:
            print("Enter the correct value---!")
            break

if __name__=='__main__':
    main() 