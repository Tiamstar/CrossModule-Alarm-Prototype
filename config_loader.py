# config_loader.py

"""
文件 B: 动态加载配置
这是告警的“根因”和“修复点”。
"""

class Config:
    """一个动态配置类。"""
    
    def __init__(self, config_dict: dict):
        """
        使用 setattr 动态设置属性。
        Pylint 的静态分析无法跟踪这里设置了什么。
        """
        self._data = config_dict
        for key, value in self._data.items():
            # !! 这就是“根因” !!
            # Pylint 看不懂 setattr 内部的逻辑
            setattr(self, key, value)

def get_config() -> Config:
    """获取配置实例。"""
    # 实际中这可能是从 .ini 或 .env 文件加载的
    settings = {
        "api_key": "abc-123-xyz",
        "timeout": 30
    }
    return Config(settings)