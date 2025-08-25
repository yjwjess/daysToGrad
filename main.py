import streamlit as st
from datetime import datetime, date

# 페이지 설정
st.set_page_config(
    page_title="수유초 졸업식 D-Day 학습코치",
    page_icon="🎓",
    layout="centered"
)

# 명사들의 명언 모음
quotes = [
    "💫 \"꿈을 가지고 있다면 그 꿈을 지켜라. 사람들이 무언가를 할 수 없다고 말할 때, 그건 그들이 할 수 없다는 뜻이지 당신이 할 수 없다는 뜻이 아니다.\" - 크리스 가드너",
    "🌟 \"성공의 비밀은 시작하는 것이다.\" - 마크 트웨인",
    "🚀 \"미래는 자신의 꿈의 아름다움을 믿는 사람들의 것이다.\" - 엘리너 루즈벨트",
    "📚 \"배움에는 끝이 없다. 오늘 배운 것이 내일의 힘이 된다.\" - 넬슨 만델라",
    "💎 \"어려움 속에서 기회가 숨어있다.\" - 알버트 아인슈타인",
    "🌈 \"포기하지 않으면 실패하지 않는다.\" - 윈스턴 처칠",
    "⭐ \"작은 걸음도 앞으로 나아가는 것이다.\" - 공자",
    "🎯 \"목표를 세우는 것은 보이지 않는 것을 보이게 만드는 첫 걸음이다.\" - 토니 로빈스",
    "🌱 \"오늘의 나보다 내일의 내가 더 나아지도록 노력하라.\" - 소크라테스",
    "💪 \"할 수 있다고 믿든 할 수 없다고 믿든, 당신이 맞다.\" - 헨리 포드",
    "📖 \"지식은 힘이다. 하지만 지식을 행동으로 옮기는 것이 진정한 힘이다.\" - 프랜시스 베이컨",
    "🎨 \"창의성은 지식보다 중요하다.\" - 알버트 아인슈타인",
    "🌸 \"좋은 습관은 성공의 열쇠다.\" - 아리스토텔레스",
    "✨ \"실패는 성공으로 가는 징검다리다.\" - 토머스 에디슨",
    "🎪 \"인생은 자전거 타기와 같다. 균형을 잡으려면 계속 움직여야 한다.\" - 알버트 아인슈타인"
]

# D-Day 계산
today = date.today()
graduation_date = date(2026, 2, 10)
days_remaining = (graduation_date - today).days

# 오늘의 명언 선택 (날짜 기반으로 일관성 유지)
quote_index = today.timetuple().tm_yday % len(quotes)
today_quote = quotes[quote_index]

# CSS로 배경 설정
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .quote-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.4);
        text-align: center;
    }
    
    .dday-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 50px;
        margin: 30px 0;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 15px 45px rgba(31, 38, 135, 0.5);
        text-align: center;
    }
    
    .encouragement-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 오늘의 명언 (상단)
st.markdown(f'''
<div class="quote-box">
    <h3 style="color: white; margin-bottom: 15px;">💭 오늘의 명언</h3>
    <p style="font-size: 18px; font-style: italic; color: white; line-height: 1.6; margin: 0;">
        {today_quote}
    </p>
</div>
''', unsafe_allow_html=True)

# D-Day 메인 섹션 (중앙)
st.markdown(f'''
<div class="dday-box">
    <h2 style="color: white; font-size: 32px; margin-bottom: 20px;">🏫 수유초등학교 졸업식</h2>
    <div style="font-size: 120px; font-weight: bold; color: #FFD700; text-shadow: 3px 3px 8px rgba(0,0,0,0.6); margin: 30px 0; line-height: 1;">
        D-{days_remaining}
    </div>
    <p style="font-size: 24px; color: white; margin: 0;">2026년 2월 10일</p>
</div>
''', unsafe_allow_html=True)

# 격려 메시지
months_remaining = days_remaining // 30
weeks_remaining = days_remaining // 7

st.markdown(f'''
<div class="encouragement-box">
    <h3 style="color: white; margin-bottom: 20px;">🎓 졸업까지</h3>
    <p style="font-size: 18px; color: white; line-height: 1.6; margin-bottom: 15px;">
        초등학교 마지막 학기, 소중한 추억을 만들어가세요!
    </p>
    <p style="font-size: 16px; color: white; line-height: 1.5;">
        약 {months_remaining}개월 {days_remaining % 30}일 | 약 {weeks_remaining}주 | 총 {days_remaining}일
    </p>
    <p style="font-size: 16px; color: white; margin-top: 20px;">
        매일 조금씩 성장하는 여러분을 응원해요! 💪
    </p>
</div>
''', unsafe_allow_html=True)

# 하단 정보
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📖 오늘의 목표")
    daily_goals = [
        "숙제 성실히 완료하기",
        "독서 30분 이상 하기",
        "친구들과 좋은 추억 만들기",
        "새로운 것 하나 배우기",
        "감사한 마음 갖기",
        "건강한 생활 습관 유지하기",
        "창의적인 활동 해보기"
    ]
    goal_index = today.timetuple().tm_yday % len(daily_goals)
    st.write(daily_goals[goal_index])

with col2:
    st.markdown("### 💡 학습 팁")
    tips = [
        "집중할 때는 25분씩 공부하기",
        "필기는 색깔별로 정리하기",
        "모르는 것은 바로 질문하기",
        "계획표 만들어보기",
        "복습이 진짜 공부!",
        "친구와 함께 공부하기",
        "즐겁게 학습하기"
    ]
    tip_index = (today.timetuple().tm_yday + 1) % len(tips)
    st.write(tips[tip_index])

with col3:
    st.markdown("### ⭐ 응원")
    st.write("오늘도 화이팅!")

# 하단 장식
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="font-size: 18px; color: white;">
        <strong>수유초등학교 6학년 여러분의 꿈을 응원합니다!</strong> 🌟
    </p>
    <p style="font-size: 14px; color: rgba(255,255,255,0.8); margin-top: 10px;">
        졸업까지 힘내세요!
    </p>
</div>
""", unsafe_allow_html=True)
