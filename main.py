import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

Time_Zones=["UTC","Asia/Karachi","Asia/Dubai","Asia/Kolkata","Asia/Tokyo","Australia/Sydney","Europe/London","Europe/Paris","America/New_York","America/Los_Angeles"]

st.title("Time Zone Converter")
selected_time_zone = st.multiselect("Select Time Zones",Time_Zones,default=["UTC","Asia/Karachi"]) # Multiselect widget to select multiple time zones

st.subheader("Selected Timezones")
for tz in selected_time_zone:

    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    st.write(f"**{tz}** : {current_time}")
    
