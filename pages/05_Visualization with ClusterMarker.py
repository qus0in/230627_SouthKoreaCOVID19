import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import common

common.page_config()

st.title("Visualization with ClusterMarker")

data = common.get_sales()

# 지도 초기화
map_korea = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 클러스터링을 위한 MarkerCluster 객체 생성
marker_cluster = MarkerCluster().add_to(map_korea)

# 데이터 시각화
for idx, row in data.iterrows():
    lat, lon = row['latitude'], row['longitude']
    
    # MarkerCluster에 Marker 추가
    folium.Marker(
        location=[lat, lon]
    ).add_to(marker_cluster)

# https://github.com/randyzwitch/streamlit-folium/blob/master/examples/streamlit_app.py
# 지도 출력
st_folium(map_korea)