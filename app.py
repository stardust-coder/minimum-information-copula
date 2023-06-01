import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from main import *
from MIC.statistics import *


with st.sidebar:
    st.write("Created by Issey Sukeda")
    st.write("Email: sukeda-issei006[at]g.ecc.u-tokyo.ac.jp")

    st.write("### References")
    st.write("T. Bedford, K. J. Wilson, On the construction of minimum information bivariate copula families, Annals of the Institute of Statistical Mathematics 66 (2014) 703–7")
    st.write("T. Sei, 最小情報コピュラとその周辺 (2021)")



st.title("Analysis using minimum information copula")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

option = st.selectbox(
    'How would you like to extract information?',
    ('Spearman ρ (MICS)', 'Kendall τ (MICK)'))
option_dict = {"Spearman ρ (MICS)":"rho","Kendall τ (MICK)":"tau"}
const = option_dict[option]

size = st.slider("Gridsize", min_value=5, max_value=50, value=20, step=1)


if st.button('Start modeling'):
    st.write('You selected:', option)

    if df is not None:
        fig1, ax1 = plt.subplots()
        ax1.plot(df["X"],label="X")
        ax1.plot(df["Y"],label="Y")
        ax1.legend()
        st.write("### Data")
        st.pyplot(fig1)
        fig2, ax2 = plt.subplots()
        ax2.scatter(df["X"],df["Y"])
        st.write("### X vs Y (before preprocessing)")
        st.pyplot(fig2)
        st.write("### X vs Y (after preprocessing)")
        st.write("Transformed to order statistics. [0,1] x [0,1].")
        fig3, ax3 = plt.subplots()
        df, _ = preprocessing(df)
        ax3.scatter(df["X-os"],df["Y-os"])
        st.pyplot(fig3)

        st.write("### Statistics of Data")
        rho, tau, ll5, ll1, lu5, lu1 = calc_bivar_stats(df) #modify later
        st.write(f"Spearman's ρ (sample version) : {rho}")
        st.write(f"Kendall's τ (sample version) : {tau}")
        st.write(f"Lower tail dependence λL (sample version) : 5% {ll5}, 1% {ll1}")
        st.write(f"Upper tail dependence λU (sample version) : 5% {lu5}, 1% {lu1}")

    
    if option == 'Kendall τ (MICK)':
        plot(size,const,tau,mode="greedy")
        image = Image.open('result/temp.png')
        st.write("### Suggested MICK")
        st.image(image, caption='MICK result')

    else:
        st.write("preparing ...")