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