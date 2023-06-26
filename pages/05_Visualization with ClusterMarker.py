import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Choropleth Map Visualization")

data = common.get_sales()

# 지도 초기화
map_korea = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 데이터 시각화
folium.Choropleth(
    # https://github.com/southkorea/southkorea-maps/blob/master/kostat/2013/json/skorea_municipalities_geo_simple.json
    geo_data="https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2013/json/skorea_municipalities_geo_simple.json",
    name='choropleth',
    data=data,
    columns=['city', 'confirmed'],
    key_on='feature.properties.name_eng',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Confirmed Cases'
).add_to(map_korea)

# https://github.com/randyzwitch/streamlit-folium/blob/master/examples/streamlit_app.py
# 지도 출력
st_folium(map_korea)