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
        generator(user_prompt, max_length=user_length, num_return_sequences=10, truncation=True)

### Print all 10 completions:
for i in range(10):
  st.write(response.choices[i].message.content)
