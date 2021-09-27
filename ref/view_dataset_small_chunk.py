import pandas as pd
import os

# 한 조각에 담을 행의 수
size = 10 ** 5
dataset = "..\dataset\original_dataset\steam_reviews.csv"

df = pd.read_csv(dataset, encoding="utf-8", chunksize=size)

if not os.path.exists("chunk"):
    os.makedirs("chunk")
    
os.chdir(os.getcwd()+"\chunk")

for num, chunk in enumerate(df):
    chunk.to_csv(f"{os.getcwd()}\chunk{num+1}.csv", index=False, encoding="utf-8-sig")
