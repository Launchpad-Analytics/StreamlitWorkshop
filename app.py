import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import re

data_url = "https://raw.githubusercontent.com/labrijisaad/exploratory-data-analysis-in-Python/main/airbnb.csv"

st.title("Airbnb Listings Dataset")

@st.cache
def clean_listings_data(url):
    df = pd.read_csv(
        url,
        dtype= {
            "listing_id": "string",
            "name": "string",
            "host_id": "string",
            "host_id": "string",
            "host_name": "string",
            "neighborhood_full": "string",
            "room_type": "category"
        },
    )
    df = df.loc[:, "listing_id":"listing_added"]
    df['last_review'] = pd.to_datetime(df['last_review'])
    df['listing_added'] = pd.to_datetime(df['listing_added'])
    df['room_type'] = df['room_type'].str.strip().str.lower().replace({"private":"private room"})
    coords = df['coordinates'].str.split(",", expand=True).replace("[()]", "", regex=True)
    df[["lat", "lon"]] = coords
    df[["lat", "lon"]] = df[["lat", "lon"]].astype("float").fillna(0)
    df['price'] = df['price'].str.replace("$", "", regex=False).fillna(0).astype('float')
    
    return df
    
listings = clean_listings_data(data_url)
listings
st.write(listings["room_type"].value_counts())

st.subheader("Breakdown by Room Type")
st.bar_chart(listings["room_type"].value_counts())

st.write(np.histogram(listings['price']))