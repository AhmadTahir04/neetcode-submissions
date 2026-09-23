class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode


    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        i = 0
        curr = self.head
        while curr.next:
            if i == index - 1:
                curr.next = curr.next.next
                return True

            i += 1
            curr = curr.next
        return False
                
    def getValues(self) -> List[int]:
        arr = []
        if self.head is None:
            return arr
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
