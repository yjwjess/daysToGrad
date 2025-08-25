import streamlit as st
from datetime import datetime, date, timedelta
import pytz

# 페이지 설정
st.set_page_config(
    page_title="수유초 졸업식 D-Day",
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

# 서울 시간 기준으로 현재 날짜 가져오기
def get_korean_date():
    try:
        # 서울 시간대 설정
        kst = pytz.timezone('Asia/Seoul')
        korean_time = datetime.now(kst)
        return korean_time.date()
    except:
        # pytz가 없을 경우 UTC+9 수동 계산
        utc_now = datetime.utcnow()
        korean_time = utc_now + timedelta(hours=9)
        return korean_time.date()

# D-Day 계산
def calculate_dday():
    current_date = get_korean_date()
    graduation_date = date(2026, 2, 10)
    days_remaining = (graduation_date - current_date).days
    return days_remaining, current_date

# 계산 실행
days_remaining, current_date = calculate_dday()

# 오늘의 명언 선택
quote_index = current_date.timetuple().tm_yday % len(quotes)
today_quote = quotes[quote_index]

# Apple 스타일 CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif;
        color: #1d1d1f;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    .ios-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .dday-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 50px 30px;
        margin: 30px 0;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        text-align: center;
    }
    
    .small-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        text-align: center;
    }
    
    .big-number {
        font-size: 140px;
        font-weight: 700;
        color: #007AFF;
        margin: 20px 0;
        line-height: 0.9;
        text-shadow: 0 2px 4px rgba(0, 122, 255, 0.2);
    }
    
    .title-text {
        font-size: 32px;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 10px;
    }
    
    .subtitle-text {
        font-size: 24px;
        font-weight: 500;
        color: #1d1d1f;
        margin: 10px 0;
    }
    
    .body-text {
        font-size: 17px;
        font-weight: 400;
        color: #424245;
        line-height: 1.5;
    }
    
    .quote-text {
        font-size: 18px;
        font-weight: 400;
        color: #1d1d1f;
        line-height: 1.6;
        font-style: italic;
    }
    
    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 12px;
    }
    
    .status-bar {
        position: fixed;
        top: 10px;
        right: 15px;
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        backdrop-filter: blur(10px);
    }
    
    .refresh-button {
        background: #007AFF;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        margin-top: 20px;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# 상태바 (iOS 스타일)
current_time = datetime.now().strftime("%H:%M")
st.markdown(f'<div class="status-bar">🕐 {current_time} | 서울</div>', unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<div style="text-align: center; padding: 20px 0;"><h1 style="color: white; font-size: 36px; font-weight: 300; margin: 0;">🎓 수유초 졸업 카운트다운</h1></div>', unsafe_allow_html=True)

# 오늘의 명언
st.markdown(f'''
<div class="ios-card">
    <div class="section-title">💭 오늘의 명언</div>
    <p class="quote-text">{today_quote}</p>
</div>
''', unsafe_allow_html=True)

# D-Day 메인 카드
st.markdown(f'''
<div class="dday-card">
    <div class="title-text">수유초등학교 졸업식</div>
    <div class="big-number">D-{days_remaining}</div>
    <div class="subtitle-text">2026년 2월 10일</div>
</div>
''', unsafe_allow_html=True)

# 현재 날짜 정보
weekday_korean = {
    'Monday': '월요일', 'Tuesday': '화요일', 'Wednesday': '수요일',
    'Thursday': '목요일', 'Friday': '금요일', 'Saturday': '토요일', 'Sunday': '일요일'
}
korean_weekday = weekday_korean.get(current_date.strftime('%A'), current_date.strftime('%A'))

st.markdown(f'''
<div class="ios-card">
    <div class="section-title">📅 오늘</div>
    <div class="subtitle-text">{current_date.strftime("%Y년 %m월 %d일")} {korean_weekday}</div>
    <p class="body-text">졸업까지 <strong>{days_remaining}일</strong> 남았습니다</p>
</div>
''', unsafe_allow_html=True)

# 정보 카드들
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
    <div class="small-card">
        <div class="section-title">📖 오늘의 목표</div>
        <p class="body-text">{daily_goals[goal_index]}</p>
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
    <div class="small-card">
        <div class="section-title">💡 학습 팁</div>
        <p class="body-text">{tips[tip_index]}</p>
    </div>
    ''', unsafe_allow_html=True)

# 응원 메시지
months_remaining = days_remaining // 30
weeks_remaining = days_remaining // 7

st.markdown(f'''
<div class="ios-card">
    <div class="section-title">⭐ 응원 메시지</div>
    <div class="subtitle-text" style="color: #007AFF;">오늘도 화이팅! 💪</div>
    <p class="body-text">
        약 {months_remaining}개월 {days_remaining % 30}일 | 약 {weeks_remaining}주 남았어요<br>
        매일 조금씩 성장하는 여러분을 응원합니다!
    </p>
</div>
''', unsafe_allow_html=True)

# 하단 정보
st.markdown("---")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(f"""
    <div style="color: white; font-size: 15px; padding: 10px 0;">
        📍 기준 날짜: {current_date.strftime('%Y년 %m월 %d일')} (한국 시간)<br>
        🎯 목표: 2026년 2월 10일 수유초등학교 졸업식
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🔄 새로고침", key="refresh"):
        st.rerun()

# 푸터
st.markdown("""
<div style="text-align: center; padding: 30px 0; color: white;">
    <p style="font-size: 20px; font-weight: 500; margin-bottom: 10px;">
        수유초등학교 6학년 여러분의 꿈을 응원합니다! 🌟
    </p>
    <p style="font-size: 14px; opacity: 0.8;">
        매일 성장하는 여러분이 자랑스러워요
    </p>
</div>
""", unsafe_allow_html=True)
