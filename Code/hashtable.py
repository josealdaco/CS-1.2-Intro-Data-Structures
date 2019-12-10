#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def unWrapList(self, list, key):
        """ Unwraps List of List to a single List"""
        finalList = []
        for item in list:
            for value in item:
                finalList.append(value[key])
        return finalList

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Running Time is O(n)
        #  Best Running Time: O(n)
        #  Worst Running Time: O(n)
        # Collect all keys in each bucket
        all_keys = []
        print()
        for bucket in self.buckets:
            all_keys.append(bucket.items())  # Get all items of the LinkedList
        all_keys = self.unWrapList(all_keys, 0)  # 0 is key, 1 is value
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Running Time is O(b * L) OR O(n)
        #  Best Running Time: O(n)
        #  Worst Running Time: O(n)
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_keys = []
        for bucket in self.buckets:
            all_keys.append(bucket.items())  # Get all items of the LinkedList
        all_keys = self.unWrapList(all_keys, 1)  #  0 is key, 1 is value
        return all_keys

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        #  Running Time is O(n)
        #  Best Running Time: O(n)
        #  Worst Running Time: O(n)
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        #  Running Time is O(b)
        #  Best Running Time: O(b)
        #  Worst Running Time: O(b)
        sum = 0
        for item in self.buckets:
            sum += item.count
        return sum
        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        #  Running Time is O(1)
        #  Best Running Time: O(l)
        #  Worst Running Time: O(n)

        index = self._bucket_index(key)

        list = self.buckets[index].items()
        for item in list:
            if item[0] == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Running Time is O(n) or O(b * l)
        #  Best Running Time: O(b)
        #  Worst Running Time: O(n)
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)  #  Get index

        for item in self.buckets[index].items():  # Loop over items in linkedList
            if item[0] == key:
                return item[1]
        raise KeyError('Key not found:{}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        #  Running Time is O(l)
        #  Best Running Time: O(1)
        #  Worst Running Time: O(n)
        index = self._bucket_index(key)
        print("Linked List before set", self.buckets[index].items())
        for node in self.buckets[index].items():
            if key == node[0]:
                print("This is the node:", node)
                self.buckets[index].delete(node)
                self.buckets[index].append((key, value))
                return
        return self.buckets[index].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Running Time is O(n) or O(b * l)
        #  Best Running Time: O(b)
        #  Worst Running Time: O(n)
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        try:
            data = self.buckets[index].find(lambda item: item == (key, self.get(key)))
            self.buckets[index].delete(data)
        except ValueError:
            raise KeyError('key not found:{}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
