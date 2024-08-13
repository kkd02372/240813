import streamlit as st

# 제목과 소개
st.title('📚 초등학생을 위한 수학 디지털 교과서 ✏️')
st.write('환영합니다! 여기서 수학 문제를 풀고, 직접 필기해보세요. 😊')

# 문제 목록
problems = {
    '문제 1️⃣': '5 + 3 = ?',
    '문제 2️⃣': '12 - 7 = ?',
    '문제 3️⃣': '8 × 6 = ?',
    '문제 4️⃣': '15 ÷ 3 = ?'
}

# 문제 선택
st.sidebar.title('문제 선택 📖')
selected_problem = st.sidebar.radio('문제를 선택하세요:', list(problems.keys()))

# 선택된 문제 출력
st.subheader(f'🔢 {selected_problem}')
st.write(problems[selected_problem])

# 답안 입력
answer = st.text_input('답을 입력해보세요: ', '')

# 필기 영역
st.subheader('✏️ 필기 영역')
st.write('문제를 해결한 후 이곳에 필기를 해보세요.')

# 필기판 구현
st.write('필기 영역 📝')
st.text_area('필기 내용을 입력하세요:', '', height=150)

# 제출 버튼
if st.button('답 제출 🚀'):
    st.write('답이 제출되었습니다! 🎉')

# 피드백
if answer:
    st.write(f'입력한 답: {answer}')
    # 정답 확인 (간단한 예제, 실제로는 정답을 확인하는 로직이 필요합니다)
    correct_answers = {'문제 1️⃣': '8', '문제 2️⃣': '5', '문제 3️⃣': '48', '문제 4️⃣': '5'}
    if answer == correct_answers.get(selected_problem, ''):
        st.write('정답입니다! 👍')
    else:
        st.write('정답이 아닙니다. 다시 시도해보세요. 🤔')

