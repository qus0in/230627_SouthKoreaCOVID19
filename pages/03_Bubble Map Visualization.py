import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Bubble Map Visualization")

data = common.get_sales()

# 지도 초기화
map_korea = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 데이터 시각화
for idx, row in data.iterrows():
    lat, lon = row['latitude'], row['longitude']
    confirmed_cases = row['confirmed']
    
    # CircleMarker를 사용하여 버블맵 표현
    folium.CircleMarker(
        location=[lat, lon],
        radius=confirmed_cases/500,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        tooltip=f"Confirmed Cases: {confirmed_cases}"
    ).add_to(map_korea)

# https://github.com/randyzwitch/streamlit-folium/blob/master/examples/streamlit_app.py
# 지도 출력
st_folium(map_korea)