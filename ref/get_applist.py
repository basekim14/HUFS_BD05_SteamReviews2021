# -*- coding:utf-8 -*-

import pandas as pd

dataset = "..\dataset\original_dataset\steam_reviews.csv"

pd.set_option("display.max_rows", 350)
df = pd.read_csv(dataset, encoding="utf-8")

# app_id는 해당 게임의 스팀 구매 페이지 url에 활용
# https://store.steampowered.com/app/{app_id}
df_step1 = df.drop_duplicates(["app_id"], ignore_index = True)
df_step2 = df_step1.loc[:, ["app_id", "app_name"]]

# jupyter notebook
# display(df_step2)

# python idle
print(df_step2)
