
import json
import folium
import pandas as pd
geo_path = './seoul_map.json'
geo_str = json.load(open(geo_path, encoding='UTF-8'))
map = folium.Map(location=[37.5502,126.982], 
                 zoom_start=12
                 #,tiles='Stamen Toner'
                 )

police_norm = pd.read_csv('./crime_in_seoul_final.csv',sep=',',encoding='utf-8')
police_norm.head()

map_data = police_norm['범죄']
#station_name.append('서울'+str(name[:-1])+'경찰서') # -1 전부
map.choropleth(
    geo_data = geo_str,
    name = 'choropleth',
    data = map_data,#police_norm['범죄'],
    columns =  [police['구별'], map_data],
    key_on = 'feature.id',
    fill_color = 'PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name = '범죄발생율(%)'
    )
folium.LayerControl().add_to(map)
map.save('./Crime_MAP.html')