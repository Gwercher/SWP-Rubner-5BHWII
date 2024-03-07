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
        while cur_node.next_node:
            output_str += f'{cur_node.data}\n'
            cur_node = cur_node.next_node
        output_str += f'{cur_node.data}'

        return output_str

if __name__ == '__main__':
    linked_list = LinkedList(Node(1))
    linked_list.insert_end(2)
    linked_list.insert_end(3)
    linked_list.insert_end(4)
    linked_list.insert_begin(0)

    print(linked_list)