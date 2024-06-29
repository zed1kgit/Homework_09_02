import unittest
from LinkedListClass import LinkedList


class MyTestCase(unittest.TestCase):
    llist = LinkedList()

    def test_1_insert_at_head(self):
        self.assertEqual(self.llist.insert_at_head("test_data1"), "Узел с данными test_data1 добавлен в начало списка")

    def test_2_insert_at_end(self):
        self.llist.remove_node_position(1)
        self.assertEqual(self.llist.insert_at_end("test_data2"), None)
        self.assertEqual(self.llist.insert_at_end("test_data3"), "Узел с данными test_data3 добавлен в конец списка")
        self.assertEqual(self.llist.insert_at_end("test_data4"), "Узел с данными test_data4 добавлен в конец списка")

    def test_3_remove_node_position(self):
        self.assertEqual(self.llist.remove_node_position(1), "Удален узел с данными test_data2 позиции 1")
        self.assertEqual(self.llist.insert_at_end("test_data5"), "Узел с данными test_data5 добавлен в конец списка")
        self.assertEqual(self.llist.remove_node_position(3), "Удален узел с данными test_data5 позиции 3")
        self.assertEqual(self.llist.remove_node_position(3), "Ничего не удалено")

    def test_4_insert_at_position(self):
        self.assertEqual(self.llist.insert_at_position("test_data4", 1), "Узел с данными test_data4 добавлен на позицию 1")

    def test_5_print_ll(self):
        self.assertEqual(self.llist.print_ll(), "Данные списка выведены")

    def test_6_get(self):
        self.assertEqual(self.llist.get("test_data2")[0], False)
        self.assertEqual(self.llist.get("test_data4")[0], True)

    def test_7_change_data(self):
        self.assertEqual(self.llist.change_data("test_data2", "test_data5"), "Данные не обнаружены")
        self.assertEqual(self.llist.change_data("test_data4", "test_data5"), "Заменены данные в узле № 1")