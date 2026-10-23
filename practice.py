class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traver(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def insert(self, val, position):
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0

            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count += 1

            if prev_node is None:
                print("Invalid position")
                return

            prev_node.next = new_node
            new_node.next = curr

    def delete(self):
        curr = self.head

        while curr is not None and curr.next is not None:
            curr.next = curr.next.next
            curr = curr.next


sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print("Before insertion:")
sll.traver()

sll.insert(25, 2)

print("After insertion:")
sll.traver()

sll.delete()

print("After deleting alternate nodes:")
sll.traver()