class Node:
    def __init__(self, item):
        """
        Constructor for Node class.

        Args:
            item: The value to be stored in the node.
        """
        self.item = item
        self.next = None
        self.prev = None


class CircleDoubleLinkedList:
    def __init__(self):
        """
        Constructor for DoubleLinkedList class.
        Initializes an empty doubly linked list.
        """
        self.begin = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        """
        Checks if the doubly linked list is empty.

        Returns:
            True if the doubly linked list is empty, False otherwise.
        """
        return self.size == 0

    def addFirst(self, item):
        """
        Adds a new node with the given item at the beginning of the doubly linked list.

        Args:
            item: The value to be added to the list.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = self.end = newNode
            self.end.next = self.begin
            self.end.prev = self.begin
            self.begin.next = self.end
            self.begin.prev = self.end
        else:
            self.begin.prev = newNode
            newNode.next = self.begin
            self.begin = newNode
            newNode.prev = self.end
            self.end.next = newNode
        self.size += 1

    def addLast(self, item):
        """
        Adds a new node with the given item at the end of the doubly linked list.

        Args:
            item: The value to be added to the list.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = self.end = newNode
            self.end.next = self.begin
            self.end.prev = self.begin
            self.begin.next = self.end
            self.begin.prev = self.end
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
            self.end.next = self.begin
        self.size += 1

    def removeNode(self, item):
        """
        Removes the first occurrence of the node with the given item from the doubly linked list.

        Args:
            item: The value to be removed from the list.
        """
        if self.isEmpty():
            print(("EMPTY LIST"))
        else:
            nodeRemoved = self.begin
            if self.begin.item == item:
                if self.size == 1:
                    self.begin = self.end = None
                else:
                    self.begin = nodeRemoved.next
                    self.begin.prev = self.end
                    self.end.next = self.begin

            else:
                nodeRemoved = nodeRemoved.next

                while nodeRemoved != self.begin:
                    if nodeRemoved.item == item:
                        nodeRemoved.prev.next = nodeRemoved.next
                        nodeRemoved.next.prev = nodeRemoved.prev
                        break  # Added to exit the loop after removing the node
                    else:
                        nodeRemoved = nodeRemoved.next

            self.size -= 1
            return True

    def showList(self):
        """
        Displays the items in the doubly linked list.
        """
        print("CIRCLE DOUBLE LINKED LIST")
        print(f"SIZE: {self.size}")

        if self.isEmpty():
            print("EMPTY LIST")
        else:
            print("END", end=" <-> ")
            currentNode = self.begin
            while True:
                print(f"[{currentNode.item}]", end=" <-> ")
                currentNode = currentNode.next
                if currentNode == self.begin:
                    break
            print("BEGIN")

    def search(self, item):
        """
        Searches for the first occurrence of the given item in the doubly linked list.

        Args:
            item: The value to be searched in the list.
        """
        currentNode = self.begin
        position = 0
        if (self.isEmpty()):
            print(("EMPTY LIST"))
        else:
            while True:
                if currentNode.item == item:
                    print(f"Item {item} is in position {position}")
                    return
                position += 1
                currentNode = currentNode.next
                if (currentNode == self.begin):
                    break
            print(f"Item {item} isn't in the list")

    def clear(self):
        """
        Deletes all nodes from the doubly linked list.
        """
        currentNode = self.begin.next
        while currentNode != self.begin:
            nextNode = currentNode.next
            self.removeNode(currentNode.item)  # Remove the node from memory
            currentNode = nextNode

        self.begin = None
        self.end = None
        self.size = 0
