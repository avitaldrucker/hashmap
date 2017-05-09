import unittest
from link import Link


class TestLinkMethods(unittest.TestCase):

    def setUp(self):
        self.empty_link = Link()
        self.link = Link("one", 1)

    def test_init_with_link(self):
        self.assertEqual(self.link.key, "one")
        self.assertEqual(self.link.val, 1)
        self.assertIsNone(self.link.next)
        self.assertIsNone(self.link.prev)

    def test_init_with_empty_link(self):
        self.assertIsNone(self.empty_link.key)
        self.assertIsNone(self.empty_link.val)
        self.assertIsNone(self.empty_link.next)
        self.assertIsNone(self.empty_link.prev)

    def test_remove(self):
        self.empty_link.next = self.link
        self.link.prev = self.empty_link
        third_link = Link()
        self.link.next = third_link
        third_link.prev = self.link.next
        self.link.remove()
        self.assertEqual(self.empty_link.next, third_link)
        self.assertEqual(third_link.prev, self.empty_link)
        self.assertIsNone(self.empty_link.prev)
        self.assertIsNone(third_link.next)

    def test___str__(self):
        self.assertEqual(str(self.empty_link), "[None, None]")
        self.assertEqual(str(self.link), "['one', 1]")


if __name__ == '__main__':
    unittest.main()
