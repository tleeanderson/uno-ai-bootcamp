import streamlit as st
import openai

def set_api_key():
    with open('key.txt', 'r') as file:
        openai.api_key = file.read().strip()

def streamlit_app():
    # Streamlit app
    st.title('Python Code Editor with AI Suggestions')

    # Text input box for Python code
    code_input = st.text_area('Write your Python code here:', height=200)

    if st.button('Run Code'):
        try:
            exec_globals = {}
            exec(code_input, exec_globals)
            st.success('Code executed successfully!')
            st.write(exec_globals)
        except Exception as e:
            st.error(f'Error: {e}')

    # AI-based code suggestions
    if st.button('Get AI Suggestions'):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Provide suggestions for the following Python code:\n\n{code_input}',
            max_tokens=150
        )
        suggestions = response.choices[0].text.strip()
        st.subheader('AI Suggestions')
        st.write(suggestions)


if __name__ == '__main__':
    set_api_key()
    streamlit_app()