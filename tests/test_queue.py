import unittest
from Queue import Queue


class MyTestCase(unittest.TestCase):
    queue = Queue()

    def test_1_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue("test_data1")
        self.assertEqual(self.queue.is_empty(), False)

    def test_2_is_full(self):
        self.assertEqual(self.queue.is_full(), False)
        self.queue.enqueue("test_data2")
        self.queue.enqueue("test_data3")
        self.assertEqual(self.queue.is_full(), True)
