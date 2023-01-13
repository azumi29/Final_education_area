import pandas as pd
import matplotlib.pyplot as plt

# CSV呼び出し、必要な行の抽出
df_final_education_area = pd.read_csv('final_education_area.csv', encoding='ANSI', header=8, usecols=[2,3,5,7,9,11,13])
# '-'をNaNへ変換してその行を削除
df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】'] = pd.to_numeric(df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】'], errors="coerce")
df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'] = pd.to_numeric(df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'], errors="coerce")
df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】'] = pd.to_numeric(df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】'], errors="coerce")
df_final_education_area['E9105_最終学歴人口（短大・高専）【人】'] = pd.to_numeric(df_final_education_area['E9105_最終学歴人口（短大・高専）【人】'], errors="coerce")
df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = pd.to_numeric(df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】'], errors="coerce")
df_final_education_area = df_final_education_area.dropna() 

# 最終学歴（％）列の追加
df_final_education_area['最終学歴人口（小学校・中学校）【%】'] = df_final_education_area['E9102_最終学歴人口（小学校・中学校）【人】'] / df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（高校・旧中）【%】'] = df_final_education_area['E9103_最終学歴人口（高校・旧中）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（短大・高専）【%】'] = df_final_education_area['E9105_最終学歴人口（短大・高専）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
df_final_education_area['最終学歴人口（大学・大学院）【%】'] = df_final_education_area['E9106_最終学歴人口（大学・大学院）【人】']/ df_final_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100

# 不要な列の削除
df_final_education_area = df_final_education_area.drop('地域 コード', axis=1)
df_final_education_area = df_final_education_area.drop('E9101_最終学歴人口（卒業者総数）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9102_最終学歴人口（小学校・中学校）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9103_最終学歴人口（高校・旧中）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9105_最終学歴人口（短大・高専）【人】', axis=1)
df_final_education_area = df_final_education_area.drop('E9106_最終学歴人口（大学・大学院）【人】', axis=1)


print(df_final_education_area)