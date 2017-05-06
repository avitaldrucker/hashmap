import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.empty_list = LinkedList()
        self.linked_list = LinkedList()
        linked_list.append("first", 1)
        linked_list.append("second", 2)
        linked_list.append("third", 3)

    def test_empty(self):
        self.assertTrue(self.empty_list.empty())
        self.assertFalse(self.linked_list.empty())

    def test_append(self):
        self.empty_list.append("first", 1)
        self.assertFalse(empty_list.empty())

    def test_append_in_order(self):
        self.assertEqual(self.linked_list.first(), "first")
        self.assertEqual(self.linked_list.last(), "third")

    def test_update(self):
        self.empty_list.append("first", 1)
        self.empty_list.update("first", 2)
        self.assertEqual(empty_list.first().val, 2)

    def test_update_does_not_add_new_links(self):
        self.empty_list.update("first", 2)
        self.assertTrue(empty_list.empty())

    def test_get_gets_by_key(self):
        self.assertEqual(self.linked_list.get("first"), 1)
        self.assertEqual(self.linked_list.get("second"), 2)
        self.assertEqual(self.linked_list.get("third"), 3)

    def test_get_returns_none_for_absent_keys(self):



print("returns nil for absent keys")
print(linked_list_2.get("absent key") == None)

print("remove")
print("removes a link by key")
linked_list_3 = LinkedList()
linked_list_3.append("first", 1)
linked_list_3.append("second", 2)
linked_list_3.append("third", 3)

print(linked_list_3.get("first") == 1)
linked_list_3.remove("first")
print(linked_list_3.get("first") == None)


print("reassigns pointers when links are removed")
linked_list_4 = LinkedList()
linked_list_4.append("first", 1)
linked_list_4.append("second", 2)
linked_list_4.append("third", 3)
linked_list_4.remove("second")
print(linked_list_4.first().next.key == "third")
print(linked_list_4.last().prev.key == "first")

print("include")
print("returns true if a key is present")
linked_list_5 = LinkedList()
linked_list_5.append("first", 1)
linked_list_5.append("second", 2)
linked_list_5.append("third", 3)
print(linked_list_5.include("first") == True)

print("returns false if a key is not in the list")
print(linked_list_5.include("fourth") == False)
