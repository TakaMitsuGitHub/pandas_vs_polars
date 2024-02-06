from typing import Literal
import time

import patito as pt
import polars as pl
import pandas as pd

from create_data import timer_decorator
from create_data import DataCreator

dc = DataCreator(1000000)
data = dc.create_dic()

df = pl.DataFrame(data)

from datetime import timedelta
class Valid(pt.Model):
    name: str
    age: int
    height: float
    birthday: str


@timer_decorator
def func(df, Valid):
    result = Valid.validate(df)
    print(df)
    return result

# start_time = time.time()
print(func(df, Valid))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"実行時間: {elapsed_time}秒")