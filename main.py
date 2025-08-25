<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수유초 졸업식 D-Day 학습코치</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 600px;
            width: 90%;
        }
        
        .quote {
            font-size: 18px;
            font-weight: 300;
            margin-bottom: 30px;
            line-height: 1.6;
            opacity: 0.9;
            font-style: italic;
        }
        
        .school-info {
            font-size: 24px;
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        .dday {
            font-size: 120px;
            font-weight: bold;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin: 30px 0;
            line-height: 1;
        }
        
        .graduation-date {
            font-size: 20px;
            margin-bottom: 20px;
            opacity: 0.8;
        }
        
        .encouragement {
            font-size: 16px;
            margin-top: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            line-height: 1.5;
        }
        
        .floating-emoji {
            position: absolute;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .emoji-1 { top: 10%; left: 10%; animation-delay: 0s; font-size: 30px; }
        .emoji-2 { top: 20%; right: 15%; animation-delay: 1s; font-size: 25px; }
        .emoji-3 { bottom: 15%; left: 20%; animation-delay: 2s; font-size: 35px; }
        .emoji-4 { bottom: 25%; right: 10%; animation-delay: 1.5s; font-size: 28px; }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="floating-emoji emoji-1">📚</div>
    <div class="floating-emoji emoji-2">⭐</div>
    <div class="floating-emoji emoji-3">🎓</div>
    <div class="floating-emoji emoji-4">🌟</div>
    
    <div class="container">
        <div class="quote" id="dailyQuote">
            💫 "꿈을 가지고 있다면 그 꿈을 지켜라. 사람들이 무언가를 할 수 없다고 말할 때, 그건 그들이 할 수 없다는 뜻이지 당신이 할 수 없다는 뜻이 아니다." - 크리스 가드너
        </div>
        
        <div class="school-info">
            🏫 수유초등학교 졸업식 🎊
        </div>
        
        <div class="dday pulse" id="ddayCounter">
            D-169
        </div>
        
        <div class="graduation-date">
            📅 2026년 2월 10일
        </div>
        
        <div class="encouragement">
            🌈 초등학교 마지막 학기, 소중한 추억을 많이 만들어가세요! <br>
            📖 매일매일 조금씩 성장하는 여러분을 응원합니다! 💪✨
        </div>
    </div>

    <script>
        // 명사들의 명언 모음
        const quotes = [
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
        ];

        function updateDDay() {
            const today = new Date();
            const graduationDate = new Date('2026-02-10');
            const timeDiff = graduationDate - today;
            const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
            
            document.getElementById('ddayCounter').textContent = `D-${daysDiff}`;
        }

        function updateDailyQuote() {
            const today = new Date();
            const dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24));
            const quoteIndex = dayOfYear % quotes.length;
            document.getElementById('dailyQuote').innerHTML = quotes[quoteIndex];
        }

        // 페이지 로드 시 실행
        updateDDay();
        updateDailyQuote();

        // 매일 자정에 업데이트 (실제 환경에서는 서버 사이드에서 처리하는 것이 좋음)
        setInterval(updateDDay, 1000 * 60 * 60); // 1시간마다 체크
    </script>
</body>
</html>
