class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для создания очереди"""
    def __init__(self,size=3, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = size

    def is_empty(self):
        """Проверяет есть ли ноды в экземпляре"""
        if self.head is None:
            return True
        else:
            return False

    def is_full(self):
        """Проверяет заполнена ли очередь в экземпляре"""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            if count == self.size:
                return True
            current_node = current_node.next_node
        return False

    def enqueue(self, data):
        """Добавить ноду в очередь экземпляра"""
        new_node = Node(data)
        if not self.is_full():
            if self.head is None:
                self.head = new_node
            else:
                self.tail.next_node = new_node
            self.tail = new_node
            return True
        else:
            return False

    def dequeue(self):
        """Удалить ноду из очереди экземпляра и возвращает data удаленной ноды"""
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data

    def show(self):
        """Выводит data всех нод в консоли"""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Готово"


