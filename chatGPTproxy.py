import openai
import streamlit as st

openai_key_input = st.text_input("Enter your openai.api_key:")
openai.api_key = openai_key_input

# Define GPT-3 completion function
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens= 1500,
        n=1,
        stop=None,
        temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message['content']
    return message.strip()

# Set up Streamlit app
def main():
    st.title("Proxy Demo")
    
    input_key = "input_key"
    user_input = st.text_area("Enter your message:", key=input_key)  # Use st.text_input instead of st.text_area
    
    if st.button("Submit"):
        output = generate_text(user_input)
        st.write("AI Response:")
        st.write(output)

if __name__ == "__main__":
    main()
