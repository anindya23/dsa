class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        print("Traverse LinkedList")

        if(self.head is None):
            print("LinkedList is Empty")
        else:
            node = self.head
            while node:
                print(node.data + " ---> ")
                node = node.next

    def insert_beg(self, value):
        print("Insert Item at the Beginning")
        if self.head is None:
            self.head = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def insert_end(self, value):
        print("Insert Item at the end")
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)


    def insert_item_at(self, index, value):
        print("Insert Item at any position")

    def insert_items_at(self, index, values):
        print("Insert Items at position")

    def insert_after_value(self, target, value):
        print("Insert Item at a particular value")

    def remove_item(self, value):
        print("Remove an Item")

    def remove_item_at(self, index, item):
        print("Remove item at particular index")

    def remove_items(self, values):
        print("Remove items from LinkedList")

    def remove_by_value(self, value):
        print("Remove particular item from LinkedList")