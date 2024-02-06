import pandas as pd
import pandera as pa
from pandera import dtypes
from datetime import datetime
import time

from create_data import timer_decorator
from create_data import DataCreator

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__}関数の実行時間: {end_time - start_time}秒")
#         return result
#     return wrapper


dc = DataCreator(1000000)
data = dc.create_dic()

df = pd.DataFrame(data)


# define schema
schema = pa.DataFrameSchema({
    "name": pa.Column(str, checks=pa.Check.str_startswith("name_")),  # 先頭文字列name_
    "age": pa.Column(int, checks=pa.Check.le(100)),  # 100以下
    "height": pa.Column(float, checks=pa.Check(lambda x: (x >= 100) & (x <= 200))),  # 100~200
    # "birthday": pa.Column(dtypes.DateTime),
    "birthday": pa.Column(str),
})


# 関数
@timer_decorator
def func(df, schema):
    validated_df = schema(df)
    return validated_df

# start_time = time.time()
print(func(df, schema))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"実行時間: {elapsed_time}秒")