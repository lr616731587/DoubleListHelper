"""
针对列表的自定义工具
"""


class ListHelper():
    """
    列表助手
    """

    @staticmethod
    def find_all(target, func_condition):
        """
        查找所有满足条件的元素
        :param target: 列表
        :param func_condition: 条件： 函数/方法类型  参数：列表中的元素
        :return: 是否满足条件，布尔型
        """
        for item in target:
            if func_condition(item):
                yield item
        # return (item for item in target if func_condition(item))

    @staticmethod
    def fist(target, func_condition):
        """
        返回满足条件的第一个数据
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func_condition):
        """
        筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
        """
        # list = [func_condition(item) for item in target]
        # return list

        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        """
        计算列表中指定条件的所有元素和
        :param target:
        :param func_condition:
        :return:
        """
        num_sum = 0
        for item in target:
            num_sum += func_condition(item)
        return num_sum

    @staticmethod
    def statistics(target, func_condition):
        """
        统计个数
        :param target:
        :param func_condition:
        :return:
        """
        stat_num = 0
        for item in target:
            if func_condition(item):
                stat_num += 1
        return stat_num

    @staticmethod
    def exists(target, func_condition):
        """
        判断
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def last(target, func_condition):
        """
        满足条件的最后一个元素
        :param target:列表
        :param func_condition:条件
        :return:
        """
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                return target[i]

    @staticmethod
    def delete_all(target, func_condition):
        """
        删除指定条件的元素
        :param target:
        :param func_condition:
        :return:
        """
        del_count = 0
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                del target[i]
                del_count += 1
                # target.remove(target[i])
        return del_count

    @staticmethod
    def max_all(target, func_condition):
        """
        获取最大的元素
        :param target:
        :param func_condition:
        :return:
        """
        max_value = target[0]
        for i in range(1, len(target)):
            if func_condition(target[i]) > func_condition(max_value):
                max_value = target[i]
        return max_value

    @staticmethod
    def order_by(target, func_condition):
        """
        根据指定条件进行升序排列
        :param target:
        :param func_condition:
        :return:
        """
        for i in range(len(target) - 1):
            if func_condition(target[i]) > func_condition(target[i + 1]):
                target[i], target[i + 1] = target[i + 1], target[i]
        # return target
