import os
import pytz
import pyowm
import streamlit as st

# def barchart(days,temp_min,temp_max):
#     plt.bar(days,temp_min)
#     plt.bar(days,temp_max)

page_bg_img = '''
<style>
body {
background-image: url("https://19yw4b240vb03ws8qm25h366-wpengine.netdna-ssl.com/wp-content/uploads/5-Best-Free-and-Paid-Weather-APIs-2019-e1587582023501.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



owm=pyowm.OWM("6d7c60c7816604809419b93b2ab3adc0")
mgr=owm.weather_manager()

#st.title("5 Day Weather Forecast")
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Weather Forecast</p>', unsafe_allow_html=True)

st.write("### Write the name of a City to see weather details")

place=st.text_input("NAME OF THE CITY :", "")

if place == None:
    st.write("Input a CITY!")

unit=st.selectbox("Select Temperature Unit",("celsius","fahrenheit"))


try:
    wr=mgr.weather_at_place(place)
    w=wr.weather

    st.title("Status: ")
    st.write(w.detailed_status)         # 'clouds'
    st.title("Wind: ")
    for qw in w.wind():
        st.write(qw,w.wind()[qw])                  # {'speed': 4.6, 'deg': 330}
    st.title("Humidity: ")
    st.write(w.humidity)                # 87
    st.title("Temperature: ")
    for qw in w.temperature(unit):
        st.write(qw,w.temperature(unit)[qw])                                                 # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    st.title("Rain: ")
    if len(w.rain)==0:
        st.write("No Rain")
    else:
        st.write(w.rain)                    # {}
    st.title("Precipitation Probability: ")
    st.write(w.precipitation_probability)   
    st.title("Visibility Distance:")  
    st.write(w.visibility_distance) 
except:
    st.title("City Not Found!!!")



