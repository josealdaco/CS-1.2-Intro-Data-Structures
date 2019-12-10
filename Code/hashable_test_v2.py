from hashtable_test import HashTableTest
from hashtable import HashTable
import unittest


class HashTableExtensionTest(HashTableTest):  #  All tests from previous must Pass before going forward
    """ Purpose is to get more points in CS rubric"""

    def sampleHash(self):
        """Sample Hash to reuse for every Test """
        ht = HashTable()
        ht.set('Nothing', 24)
        ht.set('Something', 16)
        ht.set('Nothing', 100)
        ht.set('Something', 50)
        return ht

    def test_valueMethod(self):
        ht = self.sampleHash()
        if 100 in ht.values() and 50 in ht.values():
            response = True
        self.assertEqual(response, True)
        self.assertEqual(len(ht.keys()), 2)  #  Make sure Nothing only appears once

    def test_length_Method(self):
        ht = self.sampleHash()
        self.assertEqual(ht.length(), 2)  # Similar check as before

    def test_containsMethod(self):
        ht = self.sampleHash()
        self.assertEqual(ht.contains('Nothing'), True)
        self.assertEqual(ht.contains('False'), False)

    def test_getMethod(self):
        ht = self.sampleHash()
        self.assertEqual(ht.get('Nothing'), 100)
        with self.assertRaises(KeyError):
            ht.get('Together')  # Raises because Together is non-Existen

    def test_setMethod(self):
        ht = self.sampleHash()
        ht.set('Together', 5)
        self.assertEqual(ht.contains('Together'), True)

    def test_deleteMethod(self):
        ht = self.sampleHash()
        self.assertEqual(ht.length(), 2)  # Length before deletion
        ht.delete('Nothing')
        self.assertEqual(ht.length(), 1)  # Length after deletion

if __name__ == '__main__':
    unittest.main()
