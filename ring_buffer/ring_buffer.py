from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if storage is full

        # if not at capacity
        # add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        else:
            # if storage is full or last item in list
            if not self.current or not self.current.next:
                # assign storage head to current
                self.current = self.storage.head

            # else assign the next of current to current
            else:
                self.current = self.current.next
            
            self.current.value = item


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node != None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
