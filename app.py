import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("投資シミュレーションツール")

invest_per_month = st.number_input("毎月の投資額を入力してください（単位：万円）", value=5.0, format="%.1f")
ages = st.slider('投資開始年齢と終了年齢を指定してください', 0, 100, (25, 60))
interest_rate = st.number_input("想定利回りを入力してください。（単位：%）", value=5.0, format="%.1f")
target_amount = st.number_input("目標額を入力してください（単位：万円）", value=5000.0, format="%.1f")

if invest_per_month and interest_rate:
    # 年間投資額
    saving = invest_per_month * 12 * 10000  # 円単位に変換

    # 年齢のリスト
    age = [i for i in range(ages[0], ages[1] + 1)]

    # 投資期間の作成
    period = [i + 1 for i in range(len(age))]

    # 総投資額の作成
    savings = [(i + 1) * saving for i in range(len(age))]

    # 複利によるトータル資産の作成
    total = [invest_per_month * 10000 * (((1 + (interest_rate / 100 / 12)) ** (i * 12) - 1) / (interest_rate / 100 / 12)) for i in period]

    # データフレームの作成
    df = pd.DataFrame({'年齢': age, '期間': period, '総投資額': savings, 'トータル資産': total})

    # 利子分の算出
    df['利子'] = df['トータル資産'] - df['総投資額']
    
    # 目標額を達成する年齢を計算
    df['目標達成'] = df['トータル資産'] >= target_amount * 10000  # 目標額を円単位に変換
    achieved_age = df[df['目標達成']]['年齢'].min() if df['目標達成'].any() else '目標未達成'
    
    st.write(f"目標額 {target_amount} 万円を達成する年齢: {achieved_age}")

    st.write(df)

    # 棒グラフの描画
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, x='年齢', y=['総投資額', '利子'], ax=ax)

    ax.set_xlabel('年齢')
    ax.set_ylabel('資産額')
    ax.set_title(f'年齢ごとの資産額(毎月{invest_per_month}万円、年利{interest_rate}%)')
    ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)

    # Streamlitにグラフを表示
    st.pyplot(fig)

st.divider()
