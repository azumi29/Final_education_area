import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV呼び出し、必要な行の抽出
df_final_education_area = pd.read_csv('final_education_area.csv', encoding='ANSI', header=8, usecols=[2,3,5,7,9,11,13])
# '-'をNaNへ変換してその行を削除
df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】'] = pd.to_numeric(df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】'], errors="coerce")
df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'] = pd.to_numeric(df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'], errors="coerce")
df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】'] = pd.to_numeric(df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】'], errors="coerce")
df_final_education_area['E9105_最終学歴人口（短大・高専）【人】'] = pd.to_numeric(df_final_education_area['E9105_最終学歴人口（短大・高専）【人】'], errors="coerce")
df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = pd.to_numeric(df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】'], errors="coerce")
df_final_education_area = df_final_education_area.dropna() 

# 最終学歴【%】列の追加
df_final_education_area['最終学歴人口（小学校・中学校）【%】'] = df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'] / df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（高校・旧中）【%】'] = df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（短大・高専）【%】'] = df_final_education_area['E9105_最終学歴人口（短大・高専）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（大学・大学院）【%】'] = df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100

# 都道府県列の追加(groupbyのため)
df_final_education_area['都道府県'] = df_final_education_area['地域'].str.split(' ', expand=True)[0]

# 都道府県No.列の追加(groupbyのため)
df_final_education_area['都道府県No.'] = df_final_education_area['地域 コード']/1000
df_final_education_area['都道府県No.'] = np.floor(df_final_education_area['都道府県No.']) # 小数点切り捨て

# 不要な列の削除
df_final_education_area = df_final_education_area.drop('地域 コード', axis=1)
df_final_education_area = df_final_education_area.drop('地域', axis=1)
df_final_education_area = df_final_education_area.drop('E9101_最終学歴人口（卒業者総数）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9102_最終学歴人口（小学校・中学校）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9103_最終学歴人口（高校・旧中）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9105_最終学歴人口（短大・高専）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9106_最終学歴人口（大学・大学院）【人】', axis=1)

# groupby
df_final_education_area = df_final_education_area.groupby(['都道府県No.', '都道府県'], as_index=False) # ['都道府県No.']と['都道府県']をインデックスにしない。（X軸として使えなくなるため）
df_final_education_area = df_final_education_area.mean()
df_final_education_area = df_final_education_area.round(1)
print(df_final_education_area)


# 積み上げ棒グラフ
fig, ax = plt.subplots()

x = df_final_education_area['都道府県No.']
height1 = df_final_education_area['最終学歴人口（小学校・中学校）【%】']
height2 = df_final_education_area['最終学歴人口（高校・旧中）【%】']
height3 = df_final_education_area['最終学歴人口（短大・高専）【%】']
height4 = df_final_education_area['最終学歴人口（大学・大学院）【%】']
label_x = df_final_education_area['都道府県No.']
sum = height1 + height2 + height3 + height4

ax.set_xticks(x) # x軸に都道府県No.をセット
ax.set_xticklabels(df_final_education_area['都道府県'] ,fontname="MS Gothic", fontsize=5, rotation=45) # 都道府県No.を都道府県に置換

# 100%の積み上げのための計算
ax.bar(x, (height1 / sum) * 100)
ax.bar(x, (height2 / sum) * 100, bottom = (height1 / sum) * 100)
ax.bar(x, (height3 / sum) * 100, bottom = ((height1 + height2) / sum) * 100)
ax.bar(x, (height4 / sum) * 100, bottom = ((height1 + height2 + height3) / sum) * 100)

# タイトル、ラベル、凡例の表示
ax.set_title('都道府県ごとの最終学歴の割合', fontname="MS Gothic")
ax.set_ylabel('割合【%】', fontname="MS Gothic")
ax.legend(df_final_education_area.columns[2:6].tolist(), loc='lower right', borderaxespad=2, prop={"family":"MS Gothic"})

# グラフをpngに保存
plt.savefig("final_education_area.png")

plt.show()



# グラフの中に数値を表示
# for i in range(len(height1)):
#     ax.text(i, height1[i]/2, height1[i], fontsize=5)
#     ax.text(i, height1[i]+height2[i]/2, height2[i])
#     ax.text(i, height1[i]+height2[i]+height3[i]/2, height3[i])