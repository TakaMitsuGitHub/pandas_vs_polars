from typing import Literal

import patito as pt
import polars as pl
import pandas as pd

from create_data import DataCreator

dc = DataCreator()
data = dc.create_dic()

df = pl.DataFrame(data)

from datetime import timedelta
class Valid(pt.Model):
    name: str
    age: int
    height: float
    birthday: str

print(Valid.validate(df))