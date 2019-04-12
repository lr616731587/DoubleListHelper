class Vector2:
    """
    2维向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def lift():
        return Vector2(0, -1)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def left_up():
        return Vector2(-1, -1)

    @staticmethod
    def left_down():
        return Vector2(1, -1)

    @staticmethod
    def right_up():
        return Vector2(-1, 1)

    @staticmethod
    def right_down():
        return Vector2(1, 1)


class DoubleListHelper:
    """
    而为列表助手
        定义：在开发过程中所有对二维列表的仓用操作
    """
    @staticmethod
    def get_elements(li, v_pos, v_dir, count):
        """
        某个方向获取某个数量
        :param li:
        :param v_pos:
        :param v_dir:
        :param count:
        :return:
        """
        result = []
        #  位置 1 0  -->  方向 0 1

        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(li[v_pos.x][v_pos.y])
        return result


