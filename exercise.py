import streamlit as st
import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from PIL import Image

#Title
st.title("Data Science Project")

#Image
image = Image.open(r'C:\Users\Siddhi\Downloads\image.png')
st.image(image,use_column_width=True)

st.write(""" # A Single Data App with Streamlit""")#more  # you will use the more lighter the text will be written

st.write(""" ### Let's explore different classifiers and datasets""")

#Sidebar

dataset_name = st.sidebar.selectbox('Select dataset',('Breast Cancer','Iris','Wine'))

classifier_name = st.sidebar.selectbox('Select Classifier',('KNN','SVM'))

def get_dataset(name):
	if name=='Iris':
		data=datasets.load_iris()
	elif name=='Breast Cancer':
		data=datasets.load_breast_cancer()
	else:
		data=datasets.load_wine()
	x=data.data #independent variables
	y=data.target #dependent variables

	return x,y

x,y=get_dataset(dataset_name)
st.dataframe(x) #independent variables
#st.dataframe(y) dependent variables
st.write('Shape of your dataset is: ',x.shape)
st.write('Unique target variables: ',len(np.unique(y)))

plt.figure()
sns.boxplot(data=x,orient='h')
st.pyplot()


plt.hist(x)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False) #to disable warning coming as leaving st.pyplot empty

#Building Algorithm

def add_parameter(name_of_clf):
	params=dict()
	if name_of_clf=='SVM':
		c=st.sidebar.slider('C',0.1,15.0)
		params['C']=c
	else:
		name_of_clf=='KNN'
		k=st.sidebar.slider('K',1,15)
		params['K']=k
	return params

params=add_parameter(classifier_name)


def get_classifier(name_of_clf,params):
	clf=None  
	if name_of_clf=='SVM':
		clf=SVC(C=params['C'])
	else:
		clf=KNeighborsClassifier(n_neighbors=params['K'])
	return clf

clf=get_classifier(classifier_name,params)

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=10)

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

st.write(y_pred)

accuracy=accuracy_score(y_test,y_pred)

st.write("Classifier name: ",classifier_name)
st.write('Accuracy of algortithum is: ',accuracy)