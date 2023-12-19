import streamlit as st

st.title('My First Streamlit project')
st.subheader('This is a subheader')

from PIL import Image

image = Image.open(r'C:\Users\Siddhi\Downloads\image.png')
st.image(image,use_column_width=True)

st.write('This the first time I am writing in sublime text using streamlit')

st.markdown('This is a markdown')

st.success('Congratulations for cracking 1 Cr+ Package')

st.info('This is an information for you')

st.warning('This is the last time I am warning you')

st.error('Error!, Please try again later')

st.help(range)

st.text("***"*100)

import numpy as np
import pandas as pd

dataframe = np.random.rand(20,20)#generated random numbers from 0-1
st.dataframe(dataframe)

st.text("***"*100)

df=pd.DataFrame(np.random.randn(10,20),columns=['col %d' % i for i in range(20)])
st.dataframe(df.style.highlight_max(axis=1))

st.text("***"*100)

#Line Chart
chart_data = pd.DataFrame(np.random.rand(20,3), columns=['a','b','c'])
st.line_chart(chart_data)

st.text("***"*100)

#Area Chart
st.area_chart(chart_data)

#Bar Chart
chart_data = pd.DataFrame(np.random.rand(50,3), columns=['a','b','c'])
st.bar_chart(chart_data)

import matplotlib.pyplot as plt

arr = np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
st.pyplot()

st.text("***"*100)

#Distplot

import plotly
import plotly.figure_factory as ff

x1=np.random.randn(200)-2
x2=np.random.randn(200)
x3=np.random.randn(200)-2

hist_data=[x1,x2,x3]
group_label=['Group 1','Group 2','Group 3']

fig = ff.create_distplot(hist_data,group_label,bin_size=[.2,.25,.5])
st.plotly_chart(fig,use_container_width=True)

st.text("***"*100)

df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])
st.map(df)

st.text("***"*100)

if st.button('Say hello'):
	st.write('Hello is there')
else:
	st.write('Why are you here')

st.text("***"*100)

genre=st.radio('what is ur favourite genre?',('Comedy','Drama','Action','None'))

if genre=='Comedy':
	st.write('Oh u like comedy')
elif genre=='Drama':
	st.write('Oh u like drama')
elif genre=='Action' :
	st.write('Oh u like Action')
elif genre=='None':
	st.write('I dont know ur preference')

st.text("***"*100)

option=st.selectbox("How was your day",('really fun','boring','ok'))
st.write('It was ',option)

st.text("***"*100)

option=st.multiselect("How was your day",('really fun','boring','ok'))
st.write('It was ',option)

st.text("***"*100)

age=st.slider('How old are you',0,100,10)#intial,ending,from where to start the slider
st.write("I am ", age, ' year old')

values=st.slider('What is your range',0,100,(10,20))#intial,ending,from where to start the slider
st.write('My range is ',values)

st.text("***"*100)

number=st.number_input("Enter your favourite number")
st.write('Your favourite number is ',number)

st.text("***"*100)
st.text("***"*100)

upload_file=st.file_uploader('Choose a csv file', type='csv')

if upload_file is not None:
	df=pd.read_csv(upload_file)
	st.write(df)
	st.success('File uploaded successfully')
else:
	st.markdown('Please upload a File')

st.text("***"*100)

color = st.color_picker('Whaat is your favourite color? ','#00f900')
st.write('My favourite color is: ',color)	

st.text("***"*100)

add_sidebar = st.sidebar.selectbox('What were your subjects in school in 12th standard',('English','Maths','Physics','Physical Education'))

st.text("***"*100)

import time

my_bar=st.progress(0)
for i in range(100):
	time.sleep(0.1)
	my_bar.progress(i+1)

with st.spinner('Please hold on for a second!'):
	time.sleep(5)
st.success('Loaded successfully')	

st.balloons()