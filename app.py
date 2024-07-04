import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("投資シミュレーションツール")

invest_per_month = st.number_input("毎月の投資額を入力してください（単位：万円）", value=5.0, format="%.1f")

ages = st.slider('投資開始年齢と終了年齢を指定してください', 0, 100, (25, 60))

interest_rate = st.number_input("想定利回りを入力してください。（単位：%）", value=5.0, format="%.1f")

# デバッグ用の出力
st.write(f"毎月の投資額: {invest_per_month}万円")
st.write(f"投資開始年齢と終了年齢: {ages}")
st.write(f"想定利回り: {interest_rate}%")

if invest_per_month and interest_rate:
    # 年間投資額
    saving = invest_per_month * 12

    # 年齢のリスト
    age = [i for i in range(ages[0], ages[1] + 1)]

    # 投資期間の作成
    period = [i + 1 for i in range(len(age))]

    # 総投資額の作成
    savings = [(i + 1) * saving for i in range(len(age))]

    # 複利によるトータル資産の作成
    total = [invest_per_month * (((1 + (interest_rate / 100 / 12)) ** (i * 12) - 1) / (interest_rate / 100 / 12)) for i in period]

    # 変数が正しく定義されているか確認
    st.write(f"年齢リスト: {age}")
    st.write(f"投資期間: {period}")
    st.write(f"総投資額: {savings}")
    st.write(f"トータル資産: {total}")

    df = pd.DataFrame({'age': age, 'period': period, 'savings': savings, 'total': total})

    # 利子分の算出
    df['interest'] = df['total'] - df['savings']
    st.write(df)

    # 棒グラフの描画
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, x='age', y=['savings', 'interest'], ax=ax)

    ax.set_xlabel('年齢')
    ax.set_ylabel('資産額')
    ax.set_title(f'年齢ごとの資産額(毎月{invest_per_month}万円、年利{interest_rate}%)')
    ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)

    # Streamlitにグラフを表示
    st.pyplot(fig)

st.divider()
