import streamlit as st
st.title('jagga info')
col1,col2 = st.columns(2)

with col1:
    st.image('image.png')
with col2:
    st.write('Jogender is a driven 28-year-old postgraduate residing in Rewari, Haryana, who holds a Master of Computer Applications degree from Indira Gandhi University, Meerpur. Focused entirely on his ultimate career goal of becoming a Google-level AI Engineer, he spends significant time mastering data science, machine learning algorithms, and exploring cutting-edge computing hardware like RTX laptops and premium mobile devices. Outside of his intense technical studies, Jogender is an avid fan of professional wrestling and mixed martial arts, tracking WWE and UFC closely with a strong preference for icons like Brock Lesnar and Goldberg, though he has a strong aversion to cricket. For entertainment, he prefers gripping action-thrillers and emotional dramas. At home, he shares a close bond with his mother, actively coordinates family milestones with his sister and brother-in-law, and heavily values his reliable circle of true friends, Ankit and Bolt, balancing his high-tech ambitions with meaningful personal connections.')    

st.header('list of skills')
st.subheader('python')
st.subheader('AI and ML')
st.subheader('DSA')
st.subheader('git')
st.subheader('sql')
st.subheader('data structure')
st.subheader('demo how is it good or bad')

st.sidebar.title('Main Menu')
st.sidebar.markdown("""
                    - info
                    - contact
                    - page
                    """)

st.sidebar.selectbox('select one',['jagga','ankit'])
st.sidebar.button('select')
st.title('hello jagga')

option = st.sidebar.selectbox('select one',['jagga','ankit'])
btn = st.sidebar.button('select')

if btn:
    st.title('hello'+option)


