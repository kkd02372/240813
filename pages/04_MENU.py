import streamlit as st

# 메뉴 추천을 위한 데이터
menu_options = {
    '맑음': {
        '행복': ['아이스크림 🍦', '상큼한 과일 샐러드 🍉'],
        '슬픔': ['편안한 파스타 🍝', '부드러운 크로와상 🥐'],
        '중립': ['신선한 샌드위치 🥪', '산뜻한 주스 🧃']
    },
    '비': {
        '행복': ['핫초코 ☕', '따뜻한 스프 🍲'],
        '슬픔': ['위로의 김밥 🍙', '포근한 덮밥 🍚'],
        '중립': ['부드러운 수프 🍜', '고소한 베이커리 🍰']
    },
    '눈': {
        '행복': ['따뜻한 카푸치노 ☕', '달콤한 핫케이크 🥞'],
        '슬픔': ['훈훈한 라면 🍜', '따뜻한 빵 🥖'],
        '중립': ['클래식 샐러드 🥗', '건강한 스무디 🥤']
    },
    '바람': {
        '행복': ['상큼한 아이스티 🍹', '가벼운 쌈밥 🍲'],
        '슬픔': ['편안한 수프 🍲', '부드러운 떡볶이 🍢'],
        '중립': ['신선한 과일 🍎', '부드러운 요거트 🍶']
    }
}

st.title('🍽️ 오늘의 메뉴 추천기! 🌟')

# 사용자 입력
name = st.text_input('이름을 입력해주세요: ')
weather = st.selectbox('현재 날씨를 선택해주세요:', ['맑음 ☀️', '비 🌧️', '눈 ❄️', '바람 💨'])
mood = st.selectbox('현재 기분을 선택해주세요:', ['행복 😊', '슬픔 😢', '중립 😐'])
situation = st.selectbox('현재 상황을 선택해주세요:', ['공부 🧠', '일 💼', '여가 🏖️'])

if st.button('메뉴 추천 받기! 🥳'):
    if weather in menu_options and mood in menu_options[weather]:
        menu_suggestions = menu_options[weather][mood]
        st.write(f'안녕하세요, {name}님! 👋')
        st.write(f'현재 날씨: {weather}')
        st.write(f'현재 기분: {mood}')
        st.write(f'현재 상황: {situation}')
        st.write('🍴 **추천 메뉴**:')
        for menu in menu_suggestions:
            st.write(f'- {menu}')
    else:
        st.write('⚠️ 날씨, 기분, 상황이 제대로 선택되지 않았습니다. 다시 시도해 주세요!')
