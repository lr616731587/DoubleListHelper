# 创建结点类
class Node():
    def __init__(self, value, next=None):
        self.value = value  # 有用数据
        self.next = next  # 下一个结点地址


# 链表操作
class LinkList():
    def __init__(self):
        self.head = None  # 首结点

    def init_list(self, data):
        # 链表头
        self.head = Node(None)
        # 位置指针
        p = self.head
        for val in data:
            # a.next = b
            p.next = Node(val)
            # 指针跳向下一个结点
            p = p.next

    def show(self):
        p = self.head
        while p:
            print(p.value, end=' -> ')
            p = p.next

    def insert_end(self, data):
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(data)

    def insert_head(self, data):
        p = self.head
        p.value = data
        self.head = Node(None)
        self.head.next = p

    def get_length(self):
        p = self.head
        num = 0
        while p.next:
            num += 1
            p = p.next
        return num

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    def get_item(self, data):
        p = self.head
        count = 0
        while count <= data and p:
            count += 1
            p = p.next
        if p is None:
            raise IndexError
        else:
            return p.value

    def insert(self, index, data):
        """
        随机位置插入数据
        :param index:索引
        :param data:数据
        :return:
        """
        p = self.head
        count = 0
        if index < 0 or index > self.get_length():
            raise IndexError('越界')
        else:
            while count < index:
                count += 1
                p = p.next
        q = Node(data)
        q.next = p.next
        p.next = q

    def delete(self, value):
        p = self.head
        while p.next:
            if p.next.value == value:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError(value, 'is not in link')


