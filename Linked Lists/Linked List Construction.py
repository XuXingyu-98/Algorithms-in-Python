class Node:
    def _init_(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def _ini_(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None:
            setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next = node.next
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPos = 1
        while node is not None and currentPos != position:
            node = node.next
            currentPos += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, nodeToRemove):
        if nodeToRemove == self.head:
            self.head = self.head.next
        if nodeToRemove == self.tail:
            self.tail = self.tail.prev
        if nodeToRemove.prev is not None:
            nodeToRemove.prev.next = nodeToRemove.next
        if nodeToRemove.next is not None:
            nodeToRemove.next.prev = nodeToRemove.prev
        nodeToRemove.prev = None
        nodeToRemove.next = None

    def containValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
        




        

   