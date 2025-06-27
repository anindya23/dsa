class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        str = ""
        obj = self.head
        while obj:
            str += obj.data + "---->"
            obj = obj.next
        print(str)

    def get_length(self):
        length = 0
        obj = self.head
        while obj:
            length += 1
            obj = obj.next
        return length

    def insert_beg(self, data):
        if self.head is None:
            obj = Node(data)
            self.head = obj
        else:
            obj = Node(data, None, self.head)
            self.head = obj

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        obj = self.head
        while obj:
            if obj.next is None:
                obj.next = Node(data, obj)
                break
            obj = obj.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            obj = Node(data)
            self.head.prev = obj
            obj.next = self.head
            self.head = obj

        count = 0
        obj = self.head
        while obj:
            if count == index - 1:
                new = Node(data, obj, obj.next)
                obj.next.prev = new
                obj.next = new
                break
            obj = obj.next
            count += 1

    def insert_values(self, data):
        for value in data:
            self.insert_end(value)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            if self.head.next is None:
                self.head = None
                return
            else:
                self.head.next.prev = None
                self.head = self.head.next
                return
        else:
            obj = self.head
            count = 0
            while obj:
                if count == index:
                    if obj.next:
                        obj.prev.next = obj.next
                        obj.next.prev = obj.prev
                        return
                    else:
                        obj.prev.next = None
                        return

                obj = obj.next
                count += 1
