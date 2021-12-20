#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 23:13:07 2021

@author: yiyiwang
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
from datetime import datetime
from datetime import date



### Streamlit Demo

st.title('HHA 507 - Final Assignment - Streamlit')
st.subheader('Yiyi Wang') 
st.write('Streamlit demo for the following questions:')
st.write('1. How does Stony Brook hospital’s overall rating compare to the rest of NY?')
st.write('2. What is the most expensive inpatient DRGs for Stony Brook?')
st.write('3. What is the most expensive outpatient APCs for Stony Brook? ')
st.write('4. What is the Stony Brook average outpatient APCs compares to the average outpatient APCs of NY? ')
st.write('5. What is the Stony Brook average inpatient DRGs compared to the average inpatient DRGs of NY? ')
st.write('6. What is the Stony Brook national outpatient mortality rate compared to New York outpatient national mortality rate? ')

@st.cache
def load_hospitals():
    hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital

@st.cache
def load_inatpatient():
    inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return inpatient

@st.cache
def load_outpatient():
    outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return outpatient

# Load the data:     
hospital = load_hospitals()
inpatient  = load_inatpatient()
outpatient = load_outpatient()

st.title('Hospital Over Rating Stony Brook / NY State')

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(hospital)


# Quickly creating a pivot table 
st.subheader('Hospital Data Pivot Table')
dataframe_pivot = hospital.pivot_table(index=['state','city'],values=['hospital_overall_rating'],aggfunc='mean')
st.dataframe(dataframe_pivot)

hospitals_ny = hospital[hospital['state'] == 'NY']
hospital_sb = hospital[hospital['city'].str.contains('STONY')]

#Bar Chart
st.subheader('Hospital Over All Rating - NY')
bar1 = hospitals_ny['hospital_overall_rating'].value_counts().reset_index()
bar2 = hospitals_sb['hospital_overall_rating'].value_counts().reset_index()
st.dataframe(bar1)

st.markdown("the inpatient DRGs")

inpatient_DRGs = inpatient[inpatient['average_total_payments']]
st.bar_chart(inpatient_DRGs)


st.markdown("outpatient APCs")

outpatient_APCs = outpatient[inpatient['average_total_payments']]
st.bar_chart(outpatient_APCs)

st.markdown("mortality rate comparison")

st.title('mortality rate comparison Stony Brook / NY State')

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(hospital)


# Quickly creating a pivot table 
st.subheader('Hospital Data Pivot Table - mortality')
dataframe_pivot = hospital.pivot_table(index=['state','city'],values=['mortality_national_comparison	'],aggfunc='mean')
st.dataframe(dataframe_pivot)


#Bar Chart
st.subheader('mortality rate comparison - NY')
bar1 = hospitals_ny['mortality rate comparison'].value_counts().reset_index()
bar2 = hospitals_sb['mortality rate comparison'].value_counts().reset_index()
st.dataframe(bar1)

