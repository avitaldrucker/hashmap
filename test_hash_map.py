import unittest
from hash_map import HashMap



class TestHashMapMethods(unittest.TestCase):


    def setUp(self):
        self.hash = HashMap()
        self.hash["first"] = 1
        self.hash["second"] = 2
        self.hash["third"] = 3


    def test_get_gets_by_key(self):
        self.assertEqual(self.hash["first"], 1)
        self.assertEqual(self.hash["second"], 2)
        self.assertEqual(self.hash["third"], 3)


    def test_get_returns_none_for_absent_keys(self):
        self.assertIsNone(self.hash["fourth"])


    def test_set_sets_key_value_pair(self):
        self.hash["fourth"] = 4
        self.assertIsNone(self.hash[4])
        self.assertEqual(self.hash["fourth"], 4)


    def test_set_overwrites_value(self):
        self.hash["one"] = 1
        self.hash["one"] = "one"
        self.assertEqual(self.hash["one"], "one")


    def test_set_works_with_various_data_types(self):
        self.hash["fourth"] = 4
        self.hash[5] = 5
        self.assertEqual(self.hash["fourth"], 4)
        self.assertEqual(self.hash[5], 5)


    def test_include(self):
        self.assertTrue(self.hash.include("first"))
        self.assertFalse(self.hash.include("fourth"))


    def test_delete(self):
        self.assertEqual(self.hash["first"], 1)
        self.hash.delete("first")
        self.assertIsNone(self.hash["first"])


    def test_count_keeps_count_with_insertions(self):
        self.assertEqual(self.hash.count, 3)
        self.hash["fifth"] = 5
        self.assertEqual(self.hash.count, 4)


    def test_count_does_not_change_with_update(self):
        self.hash["first"] = 2
        self.assertEqual(self.hash.count, 3)


    def test_count_keeps_count_with_deletions(self):
        self.hash.delete("first")
        self.assertEqual(self.hash.count, 2)


    def test_resize_increases_length_of_store(self):
        i = 10
        while i < 17:
            self.hash[i] = i + 1
            i += 1

        self.assertEqual(len(self.hash.store), 16)


    def test_resize_rehashes_values(self):
        contents = []
        keys = ["first", "second", "third"]
        for key in keys:
            contents.append([key, self.hash[key]])
        self.hash.resize()

        for pair in contents:
            key, val = pair
            self.assertEqual(val, self.hash[key])


    def test___str__(self):
        expected_pairs = ["'first': 1", "'second': 2", "'third': 3"]
        actual_pairs = str(self.hash).split(", ")
        self.assertEqual(actual_pairs.sort(), expected_pairs.sort())



if __name__ == '__main__':
    unittest.main()
