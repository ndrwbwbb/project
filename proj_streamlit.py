import streamlit as st
import pandas as pd

df = pd.read_csv('/Users/andreybobua/PycharmProjects/master.csv')

st.set_page_config(page_title="My Webpage", page_icon=":tada")

st.title("World suicide rate statistics")
st.subheader("This dashboard will present the information about suicide statistics all over the world over a 35-year period from 1985 to 2020.")
st.write("Let's display my dataset:")
st.dataframe(df)
st.subheader("Dataset features:")
st.write("country — Name of the country")
st.write("year — Number of year")
st.write("sex — Sex group")
st.write("age — Age group")
st.write("suicides_no — Number of suicides per particular sex-age group")
st.write("population — Population of particular sex-age group")
st.write("suicides_per_100k — Number of suicides per 100k of population of particular sex-age group")
st.write("country-year — Name of the country + number of year")
st.write("HDI_per_year — Human Development Index "
         "(An indicator calculated by the United Nations Development Programme"
         " that characterizes human development, quality and standard of living in all countries of the world)")
st.write("gdp_for_year — Gross domestic product for year in a particular country")
st.write("gdp_per_capital — Gross domestic product for year in a capital of a particular country")
st.write("generation — name of the generation")
st.subheader("Let's display some statistics, which includes mean, median,"
             " standard deviation and some other information about numerical fields")

