#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:41:35 2023

@author: aaahmad
"""

import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df)
