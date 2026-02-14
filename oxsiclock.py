import time
from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st  # IPython 대신 Streamlit 임포트

# 시계가 표시될 빈 공간(Placeholder) 생성
clock_placeholder = st.empty()

try:
    while True:
        # --- [기존 로직 유지] 시간 계산 ---
        reference_time = datetime(2009, 11, 30, 0, 0, 0, tzinfo=ZoneInfo("Asia/Seoul"))
        current_earth_time = datetime.now(ZoneInfo("Asia/Seoul"))

        earth_elapsed_seconds = (current_earth_time - reference_time).total_seconds()
        oxsi_elapsed_seconds = earth_elapsed_seconds / 0.27

        oxsi_sec_per_min = 60
        oxsi_sec_per_hour = 60 * 60
        oxsi_sec_per_day = 24 * oxsi_sec_per_hour
        oxsi_sec_per_month = 23 * oxsi_sec_per_day
        oxsi_sec_per_year = 9 * oxsi_sec_per_month

        years_elapsed = int(oxsi_elapsed_seconds // oxsi_sec_per_year)
        rem = oxsi_elapsed_seconds % oxsi_sec_per_year
        months_elapsed = int(rem // oxsi_sec_per_month)
        rem %= oxsi_sec_per_month
        days_elapsed = int(rem // oxsi_sec_per_day)
        rem %= oxsi_sec_per_day
        hours = int(rem // oxsi_sec_per_hour)
        rem %= oxsi_sec_per_hour
        minutes = int(rem // oxsi_sec_per_min)
        seconds = int(rem % oxsi_sec_per_min)

        # 문자열 포맷팅
        earth_time_str = current_earth_time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
        oxsi_time_str = f"{1+years_elapsed}년 {1+months_elapsed:02d}월 {1+days_elapsed:02d}일 {hours:02d}시 {minutes:02d}분 {seconds:02d}초"

        # --- [수정된 부분] 화면 출력 ---
        # print()와 clear_output() 대신 placeholder에 덮어쓰기
        with clock_placeholder.container():
            st.metric(label="현재 지구 시간", value=earth_time_str)
            st.metric(label="현재 OXSI 시간", value=oxsi_time_str)
            
            # 단순 텍스트로 보고 싶다면 아래 주석을 해제하고 위 metric을 주석 처리하세요
            # st.write(f"현재 지구 시간: {earth_time_str}")
            # st.write(f"현재 oxsi 시간: {oxsi_time_str}")

        # 0.05초 대기
        time.sleep(0.05)

except KeyboardInterrupt:
    st.write("시계가 종료되었습니다.")