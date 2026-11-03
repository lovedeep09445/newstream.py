import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Hindustan Times")
st.header('BREAKING NEWS')
st.subheader('IND VS PAK')
st.write('VIRAT KOHLI')
st.markdown('BABAR AZAM')
st.caption('NO BALL DRAMA')

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROiurosT3G1Yrt_SO4Gxcut_z6qV_LgIKrmLEU7ABwAA&s=10')

st.checkbox('checkbox')
st.button('Click Button')
st.radio('Pick your city',['DELHI','PUNE','MUMBAI','AFGHANISTAN'])
st.selectbox('Pick your city',['DELHI','PUNE','MUMBAI','AFGHANISTAN'])

st.multiselect('Pick favourite sports',['cricket','football','basketball'])
st.select_slider('Give a Remark',['Bad','Good','Excellent'])
st.slider('Your Marks',0,100)

on=st.toggle("Activate Feature")
if on:
    st.write('Feature activated!')

number=st.number_input('Insert a number')
st.write('The current number is',number)

d=st.date_input("When's your birthday",value=None)
st.write('Your birthday is:',d)

t=st.time_input("Set an alarm for",value=None)
st.write("Alarm is set for",t)

st.number_input('Enter your marks',0,100)
st.text_input('Enter TEXt')
st.date_input('Exam Date')
st.time_input('Exam time')

st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success('Success')
st.error('Error')
st.warning('Warning')
st.info('Information')
st.exception(RuntimeError('RuntimeError exception'))

st.sidebar.title('5 Minutes Engineering')

st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROiurosT3G1Yrt_SO4Gxcut_z6qV_LgIKrmLEU7ABwAA&s=10')

df=pd.DataFrame(np.random.randn(50,20),columns=('col%d'% i for i in range(20)))

st.dataframe(df)

df=pd.DataFrame(np.random.randn(10,5),columns=('col %d'%i for i in range(5)))

st.table(df)

col1,col2,col3=st.columns(3)

col1.metric("Temperature","70 F","1.2 F")
col2.metric("Wind","9mph","-8%")
col3.metric("Humidity","86%","4%")

prompt=st.chat_input("say SOMETHING")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

with st.status('Step 1'):
    st.write('Step 2')
    time.sleep(1)
    st.write('Step 3')
    time.sleep(1)
    st.write('Step 4')
    time.sleep(1)

st.button("RErun")

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.area_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.bar_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)

df=pd.DataFrame({'lat':[],'lon':[]})
st.map(df)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.scatter_chart(chart_data)

with st.chat_message('user'):
    st.write("Hello ji")