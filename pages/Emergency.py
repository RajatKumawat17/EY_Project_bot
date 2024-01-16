import folium
import streamlit as st
from streamlit_card import card


from streamlit_folium import st_folium

st.header("EMERGENCY :" , divider = "gray")
res = card(
        title="Call Ambulance 📞",
        text="",
        image="https://www.shutterstock.com/image-illustration/ambulance-car-rides-trough-tunnel-600nw-1159851319.jpg",
        url="/Emergency",
        styles={
            "card": {
                "width": "50%", 
                "height": "100px"
            }
        }
    )

res = card(
        title="Find Nearby Ambulances 🚑",
        text="",
        image="https://www.shutterstock.com/image-vector/call-ambulance-car-via-mobile-600nw-1722854494.jpg",
        url="/Emergency",
        styles={
            "card": {
                "width": "50%", 
                "height": "100px"
            }
        }
    )
st.subheader("🚑NEARBY AMBULANCES :", divider = 'gray')
# center on Liberty Bell, add marker
m = folium.Map(location=[23.199935271719703, 77.42093801304037], zoom_start=16)
folium.Marker(
    [23.198934350397884, 77.41984903619309], popup="Ambulance1", tooltip="Ambulance 1"
).add_to(m)
folium.Marker(
    [23.197558876723264, 77.41839224334319], popup="Ambulance2", tooltip="Ambulance 2"
).add_to(m)
folium.Marker(
    [23.200487690082365, 77.4245935105245], popup="Ambulance3", tooltip="Ambulance 3"
).add_to(m)
folium.Marker(
    [23.20402781982071, 77.41682583387768], popup="Ambulance4", tooltip="Ambulance 4"
).add_to(m)

# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m, width=725, returned_objects=[])