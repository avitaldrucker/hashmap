import unittest
from hash_map import HashMap

class TestHashMapMethods(unittest.TestCase):
    def setUp(self):
        self.hash = HashMap()
        self.hash.set("first", 1)
        self.hash.set("second", 2)
        self.hash.set("third", 3)
        return self.hash

    def test_get_gets_by_key(self):
        self.assertEqual(self.hash.get("first"), 1)
        self.assertEqual(self.hash.get("second"), 2)
        self.assertEqual(self.hash.get("third"), 3)

    def test_sets_key_value_pair(self):
        self.hash.set("fourth", 4)
        self.assertEqual(self.hash.get(4), None)
        self.assertEqual(self.hash.get("fourth"), 4)

    def test_set_overwrites_value(self):
        self.hash.set("one", 1)
        self.hash.set("one", "one")
        self.assertEqual(self.hash.get("one"), "one")

    def test_set_works_with_various_data_types(self):
        self.hash.set("fourth", 4)
        self.hash.set(5, 5)
        self.assertEqual(self.hash.get("fourth"), 4)
        self.assertEqual(self.hash.get(5), 5)

    def test_include(self):
        self.assertTrue(self.hash.include("first"))
        self.assertFalse(self.hash.include("fourth"))

    def test_delete(self):
        self.assertEqual(self.hash.get("first"), 1)
        self.hash.delete("first")
        self.assertEqual(self.hash.get("first"), None)

    def test_count_keeps_count(self):
        self.assertEqual(self.hash.count, 3)

    def test_count_does_not_change_with_update(self):
        self.hash.set("first", 1)
        self.assertEqual(self.hash.count, 3)

    def test_count_keeps_count_with_deletions(self):
        self.hash.delete("first")
        self.assertEqual(self.hash.count, 2)






if __name__ == '__main__':
    unittest.main()
