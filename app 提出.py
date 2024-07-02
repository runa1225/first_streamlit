import japanize_matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import  pandas as pd


st.title("データ連携")


st.header("1つ目の課題")


age = []

for i in range(25,61):
  age.append(i)

print(age)

savings=[]

for i in range(1,37):
  savings.append(i*60)

print(savings)

import pandas as pd

df = pd.DataFrame({'age':age,'savings':savings})

st.write(df)

fig, ax = plt.subplots() #←figとaxを１つ作成する。
ax.bar(df['age'], df['savings'])
ax.set_xlabel('年齢')
ax.set_ylabel('貯金額（万円）')
ax.set_title('年齢ごとの預金額（毎月5万円）')
#plt.show() #←colaboratory上にグラフを描画
st.pyplot(fig) #←Streamlit上にグラフを描画

# 棒グラフの描画２
st.bar_chart(df,x='age',y='savings')


st.header("2つ目の課題")

saving_per_month = st.number_input("毎月の預金額を入力してください（単位：万円）",value=5.0,format="%.1f")

ages = st.slider(
    '預金開始年齢と終了年齢を指定してください',
    0, 100, (25, 60))

age = []

for i in range(ages[0],ages[1]+1):
	age.append(i)

#リスト内表記だと以下
#age = [i for i in range(ages[0],ages[1]+1)]

if saving_per_month:
  saving = saving_per_month * 12
  savings = [(i+1)*saving  for i in range(ages[1]-ages[0]+1)]

  df2 = pd.DataFrame({'age':age,'savings':savings})

  st.write(df2)

  # 棒グラフの描画
  fig2, ax2 = plt.subplots()
  ax2.bar(df2['age'], df2['savings'])
  ax2.set_xlabel('年齢')
  ax2.set_ylabel('預金額（万円）')
  ax2.set_title(f'年齢ごとの預金額(毎月{saving_per_month}万円)')
  ax2.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
  # Streamlitにグラフを表示
  st.pyplot(fig2)


  # 棒グラフの描画２
  st.bar_chart(df2,x='age',y='savings')

nen=[]

for i in range(30):
  nen.append(str(i+1)+"年後")

ganpon=[]

for i in range(30):
  ganpon.append(100)

sum_interest=[]

for i in range(30):
  sum_interest.append((i+1)*5)

df=pd.DataFrame({'nen':nen,'元本':ganpon,'利子の総額':sum_interest})
st.write(df)


# 積み上げ棒グラフの描画
fig, ax = plt.subplots()

df.plot(kind='bar', stacked=True, x='nen', y=['元本', '利子の総額'], ax=ax)

ax.set_xticklabels(df['nen'], rotation=45)
ax.legend()
ax.set_xlabel('年後')
ax.set_ylabel('総額')
ax.set_title(f'元本と利子の総額')
ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
# Streamlitにグラフを表示
st.pyplot(fig)

st.header("５つ目の課題")
#毎月５万円を１２カ月
saving = 5 * 12

#２５歳から６０歳までのリスト
age = [i for i in range(25,61)]
#print(age)

#投資期間の作成
#１年目から３６年目までのリスト
period = [i + 1 for i in range(60-25+1)]
#print(period)

#投資額の作成
#１年目から３６年目までの総投資額
savings = [(i+1)*saving  for i in range(60-25+1)]
#print(savings)

#複利によるトータル資産の作成
total = [5 * (((1+(0.05/12))**(i*12)-1)/(0.05/12)) for i in period]

df3 = pd.DataFrame({'age':age,'period':period,'savings':savings,'total':total})

#利子分の算出
df3['interest']=df3['total']-df3['savings']
st.write(df3)


# 棒グラフの描画
fig3, ax3 = plt.subplots()
df3.plot(kind='bar', stacked=True, x='age', y=['savings', 'interest'], ax=ax3)


ax3.set_xlabel('年齢')
ax3.set_ylabel('資産額')
ax3.set_title('年齢ごとの資産額(毎月5万円、年利5%)')
ax3.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
# Streamlitにグラフを表示
st.pyplot(fig3)

# 棒グラフの描画２
st.bar_chart(df3,x='age',y=['savings','interest'])
st.divider()


st.header("６つ目の課題")

invest_per_month = st.number_input("毎月の投資額を入力してください（単位：万円）",value=5.0,format="%.1f")

ages2 = st.slider(
    '投資開始年齢と終了年齢を指定してください',
    0, 100, (25, 60))


interest_rate = st.number_input("想定利回りを入力してください。（単位：%）",value=5.0,format="%.1f")


if invest_per_month and interest_rate:
  #年間投資額
  saving2 = invest_per_month * 12

  #年齢のリスト
  age2 = [i for i in range(ages2[0],ages2[1]+1)]

  #投資期間の作成
  period2 = [i + 1 for i in range(len(age2))]
  #print(period)

  #総投資額の作成
  savings2 = [(i+1)*saving2  for i in range(len(age2))]
  #print(savings)

  #複利によるトータル資産の作成
  total2 = [invest_per_month * (((1+(interest_rate/100/12))**(i*12)-1)/(interest_rate/100/12)) for i in period2]

  df4 = pd.DataFrame({'age':age2,'period':period2,'savings':savings2,'total':total2})

  #利子分の算出
  df4['interest']=df4['total']-df4['savings']
  st.write(df4)


  # 棒グラフの描画
  fig4, ax4 = plt.subplots()
  df4.plot(kind='bar', stacked=True, x='age', y=['savings', 'interest'], ax=ax4)


  ax4.set_xlabel('年齢')
  ax4.set_ylabel('資産額')
  ax4.set_title(f'年齢ごとの資産額(毎月{invest_per_month}万円、年利{interest_rate}%)')
  ax4.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
  # Streamlitにグラフを表示
  st.pyplot(fig4)


  # 棒グラフの描画２
  st.bar_chart(df4,x='age',y=['savings','interest'])

  st.write("投資終了時点の資産額：",int(total2[-1]*10000),"円")

st.divider()











