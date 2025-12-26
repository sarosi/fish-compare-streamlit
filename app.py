import streamlit as st
import compare_species
import tank_conditions

st.set_page_config(page_title="Aquarium Planner", layout="wide")

st.title("Freshwater Aquarium Planning Tool")

page = st.sidebar.radio(
    "Select Mode",
    [
        "Compare Species Parameters",
        "Find Species by Tank Conditions",
    ]
)

if page == "Compare Species Parameters":
    compare_species.run()

elif page == "Find Species by Tank Conditions":
    tank_conditions.run()
