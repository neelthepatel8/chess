class LinkedList:
    def __init__(self, head):
        self.head = head
        self.count = 0
    
    def append(self, data):
        new_node = Node(data, None)
        head = self.head

        while (head.next != None):
            head = head.next
        
        head.next = new_node
    
    def search_and_remove(self, data):
        head = self.head
        prev = None
        while (head.next != None):
            if (head.data == data):
                prev.next = head.next.next
            prev = head
            head = head.next
        
    def peek(self):
        head = self.head
        while (head.next != None):
            head = head.next
        
        return head.data

    def print(self):
        head = self.head
        while head != None:
            print(f"{head.data} -> ", end="")
            head = head.next
        print("None")


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
def main():
    head = Node(10, None)
    
    list = LinkedList(head)

    list.append(20)

    list.print()

if __name__ == "__main__":
    main()



