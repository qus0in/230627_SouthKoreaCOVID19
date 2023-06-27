import streamlit as st
import common

common.page_config()

st.title("South Korea COVID-19")
st.caption("""
"South Korea COVID-19 Dataset" 데이터셋:
한국 내 COVID-19 확진자 수, 사망자 수, 격리해제 수 등과 같은
대한민국 COVID-19 관련 정보를 제공하는 데이터 세트입니다.
이 데이터는 지역별로 구분되어 있으며, 시간에 따라 업데이트됩니다.
""")
st.image("img/welcome.png")

st.write("[Data](/Data)")