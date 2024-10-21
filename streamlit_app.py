from transformers import pipeline
import streamlit as st

with st.form("my_form"):
    st.write("Please enter your values")
    user_prompt = st.text_input("What is your prompt?")
    user_length = st.text_input("Expected length of the response, in tokens?")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        generator = pipeline('text-generation', model='gpt2')
        st.write(generator(user_prompt, max_length=int(user_length), num_return_sequences=1, truncation=True, temperature=0.2))
        st.write(generator(user_prompt, max_length=int(user_length), num_return_sequences=1, truncation=True, temperature=0.9))

