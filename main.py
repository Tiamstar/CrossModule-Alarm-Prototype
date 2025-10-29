# main.py

"""
文件 A: 使用配置的主程序
这是Pylint将报告告警的“位置”文件。
"""

from config_loader import get_config

def connect_to_api():
    """
    使用配置连接API。
    """
    app_config = get_config()
    
    print("Connecting to API...")
    
    # !! Pylint 将在这里报告告警 !!
    # E1101: Instance of 'Config' has no 'api_key' member
    if app_config.api_key:
        print(f"Using key: {app_config.api_key[:3]}...")
    else:
        print("API key is missing!")

if __name__ == "__main__":
    connect_to_api()