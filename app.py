import streamlit as st;
from dotenv import load_dotenv
import os
import openai
import pandas as pd

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

if openai.api_key is None:
    raise ValueError("API key not found! Please set the OPENAI_API_KEY environment variable.")

st.title("nutrition calculator")

st.markdown("Enter your food details to calculate the protein and carbs content.")

st.subheader("Enter the list of cooked: Vegetables, Meat and Carbs you will be eating in grams for one meal")

veg_input = st.text_area("Cooked Vegetables", value="")

non_veg = st.text_area("Meat", value="")

carbs_intake = st.text_area("Carbohyderates", value="")

if st.button("Calculate Nutrition"):
    st.write("calculate nutrition values....")

def parse_user_input(user_input):
    vegetables = []
    for veggies in user_input.splitlines():
        veggies = veggies.strip()
        if not veggies:
            continue
        parts = veggies.split(",")
        if len(parts) != 2:
            st.error(f"Error parsing line: '{veggies}'. Please use the format: Name,Weight")
            return []
        name = parts[0].strip()
        weight_str = parts[1].strip()
        
        try:
            weight = float(weight_str)
        except ValueError:
            st.error(f"Error converting weight to number in line: '{veggies}'")
            return []  # Return empty to signal a parse error
        
        vegetables.append((name,weight))
        
    return vegetables


veg = parse_user_input(veg_input)

nv = parse_user_input(non_veg)

carbs = parse_user_input(carbs_intake)



if veg and nv and carbs:
    st.write(f"""Vegetables Data: {veg}""")
    st.write(f"""Meat Data: {nv}""")
    st.write(f"""Carbs Data: {carbs}""")
    

