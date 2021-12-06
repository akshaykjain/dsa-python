class Node:
    def __init__(self, value):
        self.data = value
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value) :
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, value):
        current = self.head
        while current:
            if current.get_data() == value:
                return current
            current = current.get_next()
        if current is None:
            print("Data not in list")
        return current

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return "Deleted Data"
            prev = current
            current = current.get_next()
        return "Data not found in list"

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.head = prev
        return "List Reversed !"

    def printList(self):
        current = self.head
        print ("List: ")
        while current:
            print (current.get_data())
            current = current.get_next()

    def createLoop(self):
        curr = self.head
        curr.next_node.next_node = curr
        return "Created Loop !"

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.get_next()):
            slow_p = slow_p.get_next()
            fast_p = fast_p.get_next().get_next()
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return "Loop Detected and Eliminated !"
        return "No Loop Detected !"

    def removeLoop(self, loop_node):
        ptr1 = self.head
        while(1):
            ptr2 = loop_node

            while(ptr2.get_next() != ptr1 and ptr2.get_next() != ptr2):
                ptr2 = ptr2.get_next()

            if ptr2.get_next() == ptr1:
                break

            ptr1 = ptr1.get_next()
        ptr2.set_next(None)

def main():
    sL = SinglyLinkedList()
    sL.insert(9)
    sL.insert(10)
    sL.insert(11)
    sL.insert(12)
    sL.printList()
    print (sL.reverse())
    sL.printList()
    print (sL.createLoop())
    print (sL.detectAndRemoveLoop())
    print (sL.detectAndRemoveLoop())

main();


