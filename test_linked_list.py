import unittest
from linked_list import LinkedList

class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.empty_list = LinkedList()
        self.linked_list = LinkedList()
        self.linked_list.append("first", 1)
        self.linked_list.append("second", 2)
        self.linked_list.append("third", 3)

    def test_empty(self):
        self.assertTrue(self.empty_list.empty())
        self.assertFalse(self.linked_list.empty())

    def test_append(self):
        self.empty_list.append("first", 1)
        self.assertFalse(self.empty_list.empty())

    def test_append_in_order(self):
        self.assertEqual(self.linked_list.first().key, "first")
        self.assertEqual(self.linked_list.last().key, "third")

    def test_update(self):
        self.empty_list.append("first", 1)
        self.empty_list.update("first", 2)
        self.assertEqual(self.empty_list.first().val, 2)

    def test_update_does_not_add_new_links(self):
        self.empty_list.update("first", 2)
        self.assertTrue(self.empty_list.empty())

    def test_get_gets_by_key(self):
        self.assertEqual(self.linked_list.get("first"), 1)
        self.assertEqual(self.linked_list.get("second"), 2)
        self.assertEqual(self.linked_list.get("third"), 3)

    def test_get_returns_none_for_absent_keys(self):
        self.assertEqual(self.linked_list.get("absent key"), None)

    def test_remove_by_key(self):
        self.assertEqual(self.linked_list.get("first"), 1)
        self.linked_list.remove("first")
        self.assertEqual(self.linked_list.get("first"), None)

    def test_remove_reassigns_pointers(self):
        self.linked_list.remove("second")
        self.assertEqual(self.linked_list.first().next.key, "third")
        self.assertEqual(self.linked_list.last().prev.key, "first")

    def test_include(self):
        self.assertTrue(self.linked_list.include("first"))
        self.assertFalse(self.linked_list.include("fourth"))

if __name__ == '__main__':
    unittest.main()
