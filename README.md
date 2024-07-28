**INDUSTRIAL ANAMOLY DETECTION MODEL**

**INTRODUCTION**

The  objective is to identify unusual behavior in equipment data and thereby prevent equipment failure, reduce downtime, and improve operational efficiency by prediciting the anamoly well in advance.

**Python Libraries**

The following mentioned libraries are used to build the application

**Scikit-learn**: import sklearn

**IMBlearn**: from imblearn.combine import SMOTEENN

**Pandas, Numpy**:	import pandas as pd, import numpy as np

**Dash board libraries**-**Streamlit, Seaborn, Matplotlib**:	import streamlit as st, import seaborn as sns, from matplotlib import pyplot as plt

**GUIDE** 

**2.	Predict Anamoly** – The streamlit form allows you to input the data and then predicts the anamoly based on the data given by the user.

![image](https://github.com/user-attachments/assets/bd91b00d-d0ff-470c-83a8-8d1580ec8229)



**Data preprocessing and Data Visualization**

Data preprocessing was performed using pandas, numpy and data visualization was performed using seaborn and matplotlib. After the data preprocessing classification model
was built using sklearn. XGBClassifier gave an testing accuracy of 99 % for prediciting the anamoly. Data imbalance in the classification model was handled by using SMOTEENN.






