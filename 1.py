import streamlit as st


st.markdown('**_really_cool** .')
st.markdown(''' ### Streamlitis 
            a''')
st.text('This is sometext.')

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a caption')


st.write("st.write render 東西哦")
st.warning('Thisisawarning')

st.info("hi")

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')


st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
code