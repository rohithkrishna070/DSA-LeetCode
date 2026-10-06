class Solution(object):
    def rotateRight(self, head, k):

        if head == None:
            return None

        # Find length
        current = head
        length = 0

        while current != None:
            length += 1
            current = current.next

        k = k % length

        if k == 0:
            return head

        # Rotate k times
        for i in range(k):

            previous = None
            current = head

            while current.next != None:
                previous = current
                current = current.next

            current.next = head
            previous.next = None
            head = current

        return head