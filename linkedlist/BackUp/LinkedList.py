class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeg(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            obj = Node(data)
            obj.next = self.head
            self.head = obj

    def insertEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            obj = self.head
            while obj.next:
                obj = obj.next
            obj.next = Node(data)


    def traverse(self):
        str = ''
        obj = self.head
        while obj:
            str += obj.data + '-->'
            print(str)
            obj = obj.next

    def insert_values(self, data):
        for value in data:
            self.insertEnd(value)

    def get_length(self) -> int:
        length = 0
        obj = self.head
        while obj:
            length += 1
            obj = obj.next

        return length

    def remove_item(self, index)->bool:
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
        else:
            obj = self.head
            count = 0
            while obj:
                if count == index - 1:
                    obj.next = obj.next.next
                    break
                obj = obj.next
                count += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            obj = Node(value)
            obj.next = self.head
            self.head = obj
        else:
            count = 0
            obj = self.head
            while obj:
                if count == index - 1:
                    obj.next = Node(value, obj.next)
                    break
                count += 1
                obj = obj.next

    def insert_after_value(self, value, target):
        count = 0
        obj = self.head
        while obj:
            if obj.data.lower() == target.lower():
                obj.next = Node(value, obj.next)
                break
            obj = obj.next
            count += 1

    def remove_by_value(self, value):
        obj = self.head

        if self.head.data.lower() == value.lower():
            self.head = self.head.next
            return

        while obj.next is not None:
            if obj.next.data.lower() == value.lower():
                obj.next = obj.next.next
                break
            obj = obj.next
