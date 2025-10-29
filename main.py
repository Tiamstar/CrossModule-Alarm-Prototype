# main.py


from data_processor import DataProcessor

def generate_report(data):
    """
    创建处理器并生成报告。
    """
    processor = DataProcessor(data)
    
    result = processor.process()
    print(f"Total result: {result}")

    score = processor._calculate_score()
    print(f"Directly accessed score: {score}")

if __name__ == "__main__":
    sample_data = [10, 20, 30]
    generate_report(sample_data)