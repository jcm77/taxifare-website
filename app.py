import streamlit as st
import requests
import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown("""
            # NY TAXI
            """
)

# Get pickup date
date = st.date_input(
    "Pickup date",
    datetime.date(2023, 12, 1))

# Get pickup time
time = st.time_input('Pickup time', datetime.time(8,45 ))
# Date time concatenation
date_time_pickup = str(date)+" "+str(time)

# Getting lat & long parameters. Piickup & dropoff
pickup_long = st.text_input('Enter pickup longitude', 40.7614327)
pickup_lat = st.text_input('Enter pickup latitude', -73.9798156)
dropoff_long = st.text_input('Enter dropoff longitude', 40.6513111)
dropoff_lat = st.text_input('Enter dropoff latitude', -73.8803331)

# Passenger count
def get_select_box_data():
    return pd.DataFrame({
          'num_passenger': list(range(1,8))
        })
df = get_select_box_data()
num_passengers = st.selectbox('Number of Passengers', df['num_passenger'])



url = 'https://taxifare.lewagon.ai/predict'
# Build a dictionary containing the parameters for our API
params = {
'pickup_datetime':date_time_pickup,
'pickup_longitude': pickup_long,
'pickup_latitude': pickup_lat,
'dropoff_longitude': dropoff_long,
'dropoff_latitude': dropoff_lat,
'passenger_count' : num_passengers,
}

# Button for triggering the request
if st.button('Get fare'):
    # print is visible in the server output, not in the page
    print('fare requested!')
    # st.write('Fare requested ... ')
    response = requests.get(url,params=params).json()
    st.write(f"Your estimated fare is: {round(response['fare'],2)} USD.")
else:
    st.write('Please enter full data and make request.')
