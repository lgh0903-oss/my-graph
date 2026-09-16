import streamlit as st
import pandas as pd
import plotly.express as px


# ==================================================
# 페이지 설정
# ==================================================

st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)


# ==================================================
# 제목
# ==================================================

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("영화의 일별 관객 수가 시간에 따라 어떻게 변하는지 살펴봅니다.")


# ==================================================
# 데이터 불러오기
# ==================================================

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"


@st.cache_data
def load_data():

    df = pd.read_csv(DATA_URL)

    # 날짜를 실제 날짜 형식으로 변환
    df["날짜"] = pd.to_datetime(
        df["날짜"].astype(str),
        format="%Y%m%d",
        errors="coerce"
    )

    # 숫자형 열 변환
    number_columns = [
        "순위",
        "영화코드",
        "일관객",
        "누적관객",
        "스크린수",
        "상영횟수"
    ]

    for column in number_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df


try:
    df = load_data()

except Exception as e:
    st.error("데이터를 불러오는 중 문제가 발생했습니다.")
    st.exception(e)
    st.stop()


# ==================================================
# 그래프 1
# 영화별 날짜에 따른 일관객 변화
# ==================================================

st.divider()

st.header("📈 그래프 1. 영화별 일관객 변화")

st.write(
    "영화를 하나 선택하면 해당 영화의 날짜별 일관객 변화를 확인할 수 있습니다."
)


# 영화 목록
movie_list = sorted(
    df["영화명"].dropna().unique()
)


# 영화 선택
selected_movie = st.selectbox(
    "영화를 선택하세요.",
    movie_list
)


# 선택한 영화 데이터
movie_df = df[
    df["영화명"] == selected_movie
].copy()


# 날짜순 정렬
movie_df = movie_df.sort_values("날짜")


# 그래프 1
fig1 = px.line(
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


# 마우스를 올렸을 때 표시되는 정보
fig1.update_traces(
    hovertemplate="<b>날짜</b>: %{x|%Y-%m-%d}<br><b>일관객</b>: %{y:,}명<extra></extra>"
)


fig1.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수(명)",
    height=500
)


st.plotly_chart(
    fig1,
    use_container_width=True
)


# 그래프 1 설명 공간
st.subheader("📝 이 그래프로 알 수 있는 것")

st.info(
    "여기에 이 그래프로 알 수 있는 내용을 직접 작성하세요."
)


# ==================================================
# 그래프 2
# 일관객 합계 TOP 5 영화
# ==================================================

st.divider()

st.header("📊 그래프 2. 일관객 합계 TOP 5 영화")

st.write(
    "이 기간 동안 일관객 합계가 가장 큰 5편의 날짜별 일관객 변화를 비교합니다."
)


# --------------------------------------------------
# 영화별 일관객 합계 계산
# --------------------------------------------------

movie_total = df.groupby(
    "영화명",
    as_index=False
)["일관객"].sum()


# 일관객 합계가 큰 순서로 정렬
movie_total = movie_total.sort_values(
    "일관객",
    ascending=False
)


# 상위 5편의 영화명
top5_movies = movie_total.head(5)["영화명"].tolist()


# --------------------------------------------------
# TOP 5 영화 데이터만 가져오기
# --------------------------------------------------

top5_df = df[
    df["영화명"].isin(top5_movies)
].copy()


# 날짜순으로 정렬
top5_df = top5_df.sort_values(
    ["날짜", "영화명"]
)


# --------------------------------------------------
# 그래프 2
# --------------------------------------------------

fig2 = px.line(
    top5_df,
    x="날짜",
    y="일관객",
    color="영화명",
    markers=True,
    title="일관객 합계 상위 5편의 날짜별 일관객 변화",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수",
        "영화명": "영화"
    }
)


# 마우스를 올렸을 때 표시되는 정보
fig2.update_traces(
    hovertemplate="<b>영화</b>: %{fullData.name}<br><b>날짜</b>: %{x|%Y-%m-%d}<br><b>일관객</b>: %{y:,}명<extra></extra>"
)


fig2.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수(명)",
    height=600,
    legend_title="영화"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)


# 그래프 2 설명 공간
st.subheader("📝 이 그래프로 알 수 있는 것")

st.info(
    "여기에 이 그래프로 알 수 있는 내용을 직접 작성하세요."
)


# ==================================================
# 그래프 3
# 앞으로 추가할 그래프 공간
# ==================================================

st.divider()

st.header("📊 그래프 3")

st.info(
    "앞으로 새로운 그래프를 추가할 수 있는 공간입니다."
)


# ==================================================
# 그래프 4
# 앞으로 추가할 그래프 공간
# ==================================================

st.divider()

st.header("📊 그래프 4")

st.info(
    "앞으로 새로운 그래프를 추가할 수 있는 공간입니다."
)
# ── 그래프 2. 흥행 대작들의 곡선 겹쳐 보기 ────────────────────
st.header("2. 흥행 대작 다섯 편의 곡선")
top5 = df.groupby("영화명")["일관객"].sum().nlargest(5).index
five = df[df["영화명"].isin(top5)].sort_values("날짜")
fig2 = px.line(five, x="날짜", y="일관객", color="영화명", markers=True)
st.plotly_chart(fig2, width="stretch")
st.caption("이 그래프로 알 수 있는 것: (한 문장으로 적어 보세요)")
