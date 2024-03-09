import random


# https://www.geeksforgeeks.org/python-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f'data={self.data} next_node={self.next_node}'


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node

    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next_node = self.head
            self.head = node

    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        cur_node = self.head
        while cur_node.next_node:
            cur_node = cur_node.next_node

        cur_node.next_node = node

    def __str__(self):
        output_str = ''
        cur_node = self.head
        index = 0
        while cur_node.next_node:
            output_str += f'{index}: {cur_node.data}\n'
            index += 1
            cur_node = cur_node.next_node
        output_str += f'{index}: {cur_node.data}'

        return output_str

    def __len__(self):
        if self.head is None:
            return 0

        length = 1
        cur_node = self.head
        while cur_node.next_node:
            length += 1
            cur_node = cur_node.next_node

        return length

    class Iterator:
        # https://www.geeksforgeeks.org/implementing-iterator-pattern-of-a-single-linked-list/
        def __init__(self, cur_node):
            self.cur_node = cur_node

        def __iter__(self):
            return self

        def __next__(self):
            while self.cur_node:
                data = self.cur_node.data
                self.cur_node = self.cur_node.next_node
                return data

            raise StopIteration

    def __iter__(self):
        return self.Iterator(self.head)


def main():
    linked_list = LinkedList()

    input_amount = 5
    rand_min = 0
    rand_max = 20

    for i in range(input_amount):
        linked_list.insert_end(random.randint(rand_min, rand_max))

    for i in range(input_amount):
        linked_list.insert_begin(random.randint(rand_min, rand_max))

    print(f'{linked_list}')
    print(f'{len(linked_list)=}')

    print(f'#' * 30)
    for i in linked_list:
        print(i, end=" ")


if __name__ == '__main__':
    main()
