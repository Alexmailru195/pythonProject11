class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        previous  = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def display(self):
        current  = self.head
        elements = []
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def replace(self, old_data, new_data):
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return

def menu():
    linked_list = SinglyLinkedList()

    user_input = input("Введите набор чисел, разделенных пробелами: ")
    for num in user_input.split():
        linked_list.add(int(num))

    while True:
        print("\nВыберите действие:")
        print("1. Добавить элемент в список")
        print("2. Удалить элемент из списка")
        print("3. Показать содержимое списка")
        print("4. Проверить есть ли значение в списке")
        print("5. Заменить значение в списке")

        choice = input("Ваш выбор: ")

        if choice == '1':
            value = int(input("Введите число для добавления: "))
            linked_list.add(value)
        elif choice == '2':
            value = int(input("Введите число для удаления: "))
            linked_list.remove(value)
        elif choice == '3':
            print("Содержимое списка:", linked_list.display())
        elif choice == '4':
            value = int(input("Введите число для проверки: "))
            if linked_list.contains(value):
                print("Число есть в списке.")
            else:
                print("Числа нет в списке.")
        elif choice == '5':
            old_value = int(input("Введите заменяемое значение: "))
            new_value = int(input("Введите новое значение: "))
            linked_list.replace(old_value, new_value)

menu()
