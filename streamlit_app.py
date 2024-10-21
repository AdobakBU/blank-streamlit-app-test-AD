from transformers import pipeline

### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Generate the answer to the question "Damascus is a"
generator("Damascus is a", max_length=20, num_return_sequences=10, truncation=True)

### Print all 10 completions:
for i in range(10):
  st.write(response.choices[i].message.content)
