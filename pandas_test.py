import pandas as pd
import pandera as pa
from pandera import dtypes
from datetime import datetime

from create_data import DataCreator


dc = DataCreator()
data = dc.create_dic()

df = pd.DataFrame(data)


# df = pd.DataFrame({
#     "column1": [1, 4, 0, 10, 9],
#     "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
#     "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
# })

# define schema
schema = pa.DataFrameSchema({
    "name": pa.Column(str, checks=pa.Check.str_startswith("name_")),  # 先頭文字列name_
    "age": pa.Column(int, checks=pa.Check.le(100)),  # 100以下
    "height": pa.Column(float, checks=pa.Check(lambda x: (x >= 100) & (x <= 200))),  # 100~200
    "birthday": pa.Column(dtypes.DateTime),
})

validated_df = schema(df)
print("##################")
print(validated_df)
