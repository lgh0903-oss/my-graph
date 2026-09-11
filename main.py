import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# 제목
# --------------------------------------------------
st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("영화의 일별 관객 수가 시간에 따라 어떻게 변하는지 살펴봅니다.")

# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
DATA_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/"
    "main/data/kobis_daily.csv"
)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 날짜 열을 실제 날짜 자료형으로 변환
    df["날짜"] = pd.to_datetime(
        df["날짜"].astype(str),
        format="%Y%m%d"
    )

    # 숫자형 열 변환
    numeric_columns = [
        "순위",
        "영화코드",
        "일관객",
        "누적관객",
        "스크린수",
        "상영횟수"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


try:
    df = load_data()

except Exception as e:
    st.error("데이터를 불러오는 중 문제가 발생했습니다.")
    st.exception(e)
    st.stop()


# ==================================================
# 그래프 1. 영화별 날짜에 따른 일관객 변화
# ==================================================

st.divider()
st.header("📈 그래프 1. 영화별 일관객 변화")

st.write(
    "영화를 하나 선택하면 해당 영화의 날짜별 일관객 변화를 확인할 수 있습니다."
)

# 영화 목록
movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
    "영화를 선택하세요.",
    movie_list
)

# 선택한 영화 데이터
movie_df = df[df["영화명"] == selected_movie].copy()

# 날짜순 정렬
movie_df = movie_df.sort_values("날짜")

# 선 그래프
fig = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    title=f"「{selected_movie}」 날짜별 일관객 변화",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수"
    }
)

# 마우스를 올렸을 때 날짜와 관객 수가 보이도록 설정
fig.update_traces(
    hovertemplate=
    "<b>날짜</b>: %{x|%Y-%m-%d}<br>"
    "<b>일관객</b>: %{y:,}명"
    "<extra></extra>"
)

fig.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수(명)",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# 그래프로 알 수 있는 것
# --------------------------------------------------
st.subheader("📝 이 그래프로 알 수 있는 것")

st.info(
    "여기에 이 그래프로 알 수 있는 내용을 직접 작성하세요."
)


# ==================================================
# 그래프 추가 영역
# ==================================================

st.divider()
st.header("📊 그래프 2")

st.info(
    "앞으로 새로운 그래프를 추가할 수 있는 공간입니다."
)

# 새로운 그래프는 아래에 계속 추가하면 됩니다.


# ==================================================
# 그래프 3 추가 영역
# ==================================================

st.divider()
st.header("📊 그래프 3")

st.info(
    "앞으로 새로운 그래프를 추가할 수 있는 공간입니다."
)
