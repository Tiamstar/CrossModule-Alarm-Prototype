# data_processor.py


class DataProcessor:
    """负责处理和评分数据的类。"""

    def __init__(self, data_set: list):
        self.data = data_set
        self._cache_is_valid = False 

    def process(self):
        """执行主要的公共处理流程。"""
        self._calculate_score()
        self._cache_is_valid = True
        return sum(self.data)

    def _calculate_score(self):

        print(">>> [Internal] Calculating score...")
        # 实际可能是一个复杂计算
        return len(self.data)