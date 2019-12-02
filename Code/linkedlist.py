#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""

        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        return self.count
        #  Running time is O(1)

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new_node = Node(item)  # Create node using Node class
        if self.tail is not None:  # check if tail does exist
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
            return
        else:  # If no tail found assume LinkedList is empty
            self.head = new_node
            self.tail = new_node
            self.count += 1
        return
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        # Running Time is O(1) for best and worsr case

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        if self.head is not None:
            new_node.next = self.head  # Have the previous head node be saved in the new node
            self.head = new_node  # Now assing the head node to the new node
            self.count += 1
            return       #  ['B'] next [A]->[B]
        else:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return
        # TODO: Prepend node before head, if it exists
        # Running time is O(1) for best and worst case

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        start = self.head
        while(start):  # O(n) through items
            if quality(start.data):  # check is node data and quality match
                return start.data  # If match return the node data
            start = start.next
        return None  # Otherwise return None
        # Running Time is O(n) for worst case, Best is O(1) if first node found is a match

    def delete(self, item):

        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        # Store head node
        if self.head is not None:  # Check is LinkedList is not empty
            node = self.head  # If not start node at HEAD
        else:
            raise ValueError('Item not found: {}'.format(item))
        last_node = None  # last node will be default None
        #  Here we are trying to detach the connections of the previous node and connect it with the future node, Skipping the node being 'deleted'. We have several if statements to check edge cases
        while True:
            if node.data == item:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                elif node == self.head:
                    if node.next is not None:
                        self.head = node.next
                    else:
                        self.head = None
                elif node == self.tail:
                    last_node.next = None
                    self.tail = last_node
                else:
                    last_node.next = node.next
                break
            elif node.next is None:
                raise ValueError('Item not found: {}'.format(item))
            last_node = node
            node = node.next
        self.count -= 1
            #  Best Running Time is O(1), if we just delete the head node, Worst is Running Time O(n) if last node is the desired item


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))
    try:
        ll.delete("C")

    except(ValueError):
        print("Did not find C in the list")  # A quick try except block to test not found edge case


if __name__ == '__main__':
    test_linked_list()
