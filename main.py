import streamlit as st
from datetime import datetime, date
import time

# 페이지 설정
st.set_page_config(
    page_title="수유초 졸업식 D-Day 학습코치",
    page_icon="🎓",
    layout="centered"
)

# 명사들의 명언 모음
quotes = [
    "\"꿈을 가지고 있다면 그 꿈을 지켜라.\" - 크리스 가드너",
    "\"성공의 비밀은 시작하는 것이다.\" - 마크 트웨인",
    "\"미래는 자신의 꿈의 아름다움을 믿는 사람들의 것이다.\" - 엘리너 루즈벨트",
    "\"배움에는 끝이 없다. 오늘 배운 것이 내일의 힘이 된다.\" - 넬슨 만델라",
    "\"어려움 속에서 기회가 숨어있다.\" - 알버트 아인슈타인",
    "\"포기하지 않으면 실패하지 않는다.\" - 윈스턴 처칠",
    "\"작은 걸음도 앞으로 나아가는 것이다.\" - 공자",
    "\"목표를 세우는 것은 보이지 않는 것을 보이게 만드는 첫 걸음이다.\" - 토니 로빈스",
    "\"오늘의 나보다 내일의 내가 더 나아지도록 노력하라.\" - 소크라테스",
    "\"할 수 있다고 믿든 할 수 없다고 믿든, 당신이 맞다.\" - 헨리 포드",
    "\"지식은 힘이다. 하지만 지식을 행동으로 옮기는 것이 진정한 힘이다.\" - 프랜시스 베이컨",
    "\"창의성은 지식보다 중요하다.\" - 알버트 아인슈타인",
    "\"좋은 습관은 성공의 열쇠다.\" - 아리스토텔레스",
    "\"실패는 성공으로 가는 징검다리다.\" - 토머스 에디슨",
    "\"인생은 자전거 타기와 같다. 균형을 잡으려면 계속 움직여야 한다.\" - 알버트 아인슈타인"
]

# 현재 날짜와 시간으로 D-Day 실시간 계산
def calculate_dday():
    now = datetime.now()
    today = now.date()
    graduation_date = date(2026, 2, 10)
    days_remaining = (graduation_date - today).days
    return days_remaining, today

# D-Day 계산
days_remaining, current_date = calculate_dday()

# 오늘의 명언 선택 (날짜 기반으로 일관성 유지)
quote_index = current_date.timetuple().tm_yday % len(quotes)
today_quote = quotes[quote_index]

# CSS 스타일링 (블랙 앤 화이트 컨셉)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    
    .stApp {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Comic Neue', cursive;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    .quote-box {
        background-color: #ffffff;
        color: #000000;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 3px solid #000000;
        text-align: center;
        box-shadow: 0 8px 16px rgba(255, 255, 255, 0.1);
    }
    
    .dday-box {
        background-color: #000000;
        color: #ffffff;
        border: 5px solid #ffffff;
        border-radius: 30px;
        padding: 50px;
        margin: 40px 0;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.3);
    }
    
    .info-box {
        background-color: #ffffff;
        color: #000000;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border: 2px solid #000000;
        text-align: center;
    }
    
    .section-box {
        background-color: #000000;
        color: #ffffff;
        border: 2px solid #ffffff;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        text-align: center;
    }
    
    h1, h2, h3 {
        font-family: 'Comic Neue', cursive !important;
        font-weight: 700 !important;
    }
    
    p, div {
        font-family: 'Comic Neue', cursive !important;
    }
    
    .big-number {
        font-size: 150px !important;
        font-weight: 900 !important;
        font-family: 'Comic Neue', cursive !important;
        text-shadow: 3px 3px 0px #666666;
        margin: 30px 0 !important;
        line-height: 1 !important;
    }
    
    .update-time {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: rgba(255, 255, 255, 0.9);
        color: #000000;
        padding: 8px 12px;
        border-radius: 10px;
        font-size: 12px;
        font-family: 'Comic Neue', cursive;
    }
</style>
""", unsafe_allow_html=True)

# 실시간 업데이트 시간 표시
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f'<div class="update-time">업데이트: {current_time}</div>', unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 style="text-align: center; color: white; font-size: 48px; margin-bottom: 30px;">🎓 수유초 졸업 D-Day</h1>', unsafe_allow_html=True)

# 오늘의 명언 (상단)
st.markdown(f'''
<div class="quote-box">
    <h3 style="margin-bottom: 15px; font-size: 20px;">💭 오늘의 명언</h3>
    <p style="font-size: 18px; font-style: italic; line-height: 1.6; margin: 0; font-weight: 400;">
        {today_quote}
    </p>
</div>
''', unsafe_allow_html=True)

# D-Day 메인 섹션 (중앙)
st.markdown(f'''
<div class="dday-box">
    <h2 style="font-size: 36px; margin-bottom: 20px; font-weight: 700;">수유초등학교 졸업식</h2>
    <div class="big-number">D-{days_remaining}</div>
    <p style="font-size: 28px; margin: 0; font-weight: 700;">2026년 2월 10일</p>
</div>
''', unsafe_allow_html=True)

# 현재 날짜 정보
st.markdown(f'''
<div class="info-box">
    <h3 style="margin-bottom: 15px;">📅 오늘 날짜</h3>
    <p style="font-size: 24px; margin: 0; font-weight: 700;">
        {current_date.strftime("%Y년 %m월 %d일")}
    </p>
    <p style="font-size: 16px; margin-top: 10px;">
        졸업까지 {days_remaining}일 남았어요!
    </p>
</div>
''', unsafe_allow_html=True)

# 하단 정보 섹션
col1, col2 = st.columns(2)

with col1:
    daily_goals = [
        "숙제 성실히 완료하기",
        "독서 30분 이상 하기",
        "친구들과 좋은 추억 만들기",
        "새로운 것 하나 배우기",
        "감사한 마음 갖기",
        "건강한 생활 습관 유지하기",
        "창의적인 활동 해보기"
    ]
    goal_index = current_date.timetuple().tm_yday % len(daily_goals)
    
    st.markdown(f'''
    <div class="section-box">
        <h3 style="margin-bottom: 15px;">📖 오늘의 목표</h3>
        <p style="font-size: 18px; font-weight: 400;">
            {daily_goals[goal_index]}
        </p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    tips = [
        "집중할 때는 25분씩 공부하기",
        "필기는 색깔별로 정리하기",
        "모르는 것은 바로 질문하기",
        "계획표 만들어보기",
        "복습이 진짜 공부예요!",
        "친구와 함께 공부하기",
        "즐겁게 학습하기"
    ]
    tip_index = (current_date.timetuple().tm_yday + 1) % len(tips)
    
    st.markdown(f'''
    <div class="section-box">
        <h3 style="margin-bottom: 15px;">💡 학습 팁</h3>
        <p style="font-size: 18px; font-weight: 400;">
            {tips[tip_index]}
        </p>
    </div>
    ''', unsafe_allow_html=True)

# 응원 메시지
months_remaining = days_remaining // 30
weeks_remaining = days_remaining // 7

st.markdown(f'''
<div class="info-box">
    <h3 style="margin-bottom: 15px;">⭐ 응원 메시지</h3>
    <p style="font-size: 20px; margin-bottom: 15px; font-weight: 700;">
        오늘도 화이팅! 💪
    </p>
    <p style="font-size: 16px; line-height: 1.5;">
        약 {months_remaining}개월 {days_remaining % 30}일 | 약 {weeks_remaining}주 남았어요<br>
        매일 조금씩 성장하는 여러분을 응원합니다!
    </p>
</div>
''', unsafe_allow_html=True)

# 하단 메시지
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: white;">
    <p style="font-size: 20px; font-weight: 700;">
        수유초등학교 6학년 여러분의 꿈을 응원합니다! 🌟
    </p>
    <p style="font-size: 14px; margin-top: 10px; opacity: 0.8;">
        졸업까지 힘내세요!
    </p>
</div>
""", unsafe_allow_html=True)

# 자동 새로고침 (1분마다)
time.sleep(0.1)  # 페이지 로딩 완료 대기
if st.button("🔄 새로고침", key="refresh_button"):
    st.rerun()
