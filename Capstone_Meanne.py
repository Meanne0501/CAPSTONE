import matplotlib.pyplot as plt
import streamlit as st
st.title ("THIS IS OUR SALES")
st.subheader("It is always good to be here!")
st.write("Join us and earn more sales")
st.image("pic.jpg")

import pandas
import streamlit as st
import pandas as pd

data=pd.read_csv("CAPSTONEDATA.csv")

st.write("Sales Report")

st.bar_chart(data,x="COUNTRY",y="GROSSSALES", color="#EAE77D")

st.write("NET SALES")

st.scatter_chart(data,x="CATEGORY",y="DIVIDEND",color="#0000C0")

st.write("COUNTRY")

st.line_chart(data,x="PROJDATE",y="DIVIDEND",color="#33BB94")


