import pandas as pd
import random
import string
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class DataCreator:
    rand_len: int = 10

    # ランダムな文字列を生成する関数
    @staticmethod
    def __generate_random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    # ランダムな日付文字列を生成する関数
    @staticmethod
    def __generate_random_date():
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2023, 12, 31)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        date_object = random_date.strftime('%Y-%m-%d') # 日付フォーマットを指定

        # str を　datetime型に変更
        date_object = datetime.strptime(date_object, '%Y-%m-%d')

        return date_object

    def create_dic(self):
        # ランダムな文字列と数値を含むDataFrameを作成
        data = {
            'name': [f"name_{self.__generate_random_string(4)}" for _ in range(self.rand_len)],
            'age': [random.randint(1, 100) for _ in range(self.rand_len)],
            'height': [random.uniform(100.0, 200.0) for _ in range(self.rand_len)],
            'birthday': [self.__generate_random_date() for _ in range(self.rand_len)],
        }
        return data

