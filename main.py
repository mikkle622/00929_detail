import pandas as pd
import plotly.express as px
import os

folder_path = "./data"
file_names = [
    f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
]
for file_name in file_names:
    print(f"檔案名稱：{file_name}")

fund_vaule_array = []
days = []

for idx in range(0, len(file_names)):
    if idx == len(file_names) - 1:
        break

    excel_name = folder_path + "/" + file_names[idx]
    excel_name_1 = folder_path + "/" + file_names[idx + 1]

    df = pd.read_excel(excel_name)
    df1 = pd.read_excel(excel_name_1)

    start_idx = 10
    end_idx = 50

    print("基金淨值", df1.iat[3, 0])
    fund_vaule_array.append(int(df1.iat[3, 0].replace(",", "")))
    days.append(file_names[idx + 1][19:-5])

    print(excel_name_1, " : 個股進出明細")
    print("==========================================================================")
    for i in range(start_idx, end_idx):
        # print('df-----------', df.iat[i, 0], df.iat[i, 1], df.iat[i, 2], df.iat[i, 3])
        for j in range(start_idx, end_idx):
            if df.iat[i, 0] == df1.iat[j, 0]:
                diff = int(df1.iat[j, 2].replace(",", "")) - int(
                    df.iat[i, 2].replace(",", "")
                )
                print(
                    "代號:",
                    df.iat[i, 0],
                    "名稱:",
                    df.iat[i, 1],
                    #   '買賣股數', diff,
                    "買賣張數",
                    int(diff / 1000),
                    "持有張數",
                    int(int(df1.iat[j, 2].replace(",", "")) / 1000),
                    "權重",
                    df1.iat[j, 4],
                )
                break
    print("==========================================================================")


# 畫出淨值成長趨勢
values = [fund_vaule_array]
labels = days
fig = px.histogram(x=labels, y=values, width=1200, height=400)
fig.show()
