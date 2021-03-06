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

    def __iter__(self):
        """Returns iterables in hashtable."""
        return self._get_iterator()

    def _get_iterator(self):
        """Returns next iterator."""
        for bucket in self.buckets:
            for data in bucket:
                yield data

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        O(n), it needs to check through all the nodes and add the 
        key to the array."""
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        O(n), it needs to check through all the nodes and add the value 
        to the array."""
        all_vals = []
        for bucket in self.buckets:
            for _, val in bucket.items():
                all_vals.append(val)
        return all_vals

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        O(n), it needs to check through all the nodes and add the data to
        the array."""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        O(n) due to it needing to loop through all the buckets."""
        total_size = 0
        for bucket in self.buckets:
            total_size += bucket.length()
        return total_size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        O(n), since the find method is an O(n) operation."""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        value = bucket.find(lambda node: node[0] == key)
        if value is not None:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        O(n), since the find method is an O(n) operation."""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        value = bucket.find(lambda node: node[0] == key)
        if value is not None:
            return value[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        O(n^2), since the find method is an O(n) operation, and so is
        the replace method."""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        original_val = bucket.find(lambda node: node[0] == key)
        if original_val is not None:
            bucket.replace(original_val, (key, value))
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        O(n^2), since the find method is an O(n) operation, and so is
        the delete method."""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        value = bucket.find(lambda node: node[0] == key)
        if value is not None:
            bucket.delete(value)
        else:
            raise KeyError('Key not found: {}'.format(key))


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

    print('\nTesting iterability:')
    for item in ht:
        print(item)

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
