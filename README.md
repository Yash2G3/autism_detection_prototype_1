# ML based autism detector

Step 1: collect organize and clean datasets from different sources
Here we were able to collect data from 4 different sources 

One of the datasets had quite a lot of discrepancies like negative values 
We studied all the discrepancies and came to a conclusion to replace the result value with the sum of all the answers in form of a yes/no 

Step2: we initialized our research for appropriate models and finalized with logistic regression and naive bayes

But recent changes have shown that gradient boosting algorithm and ADA boost classifier are working more efficiently on the dataset

Step 3: Creating a streamlit web-application for our model

This web-app will take some personal details from the user and based then the user will be asked to answer a set of clinically advised questions 

Based upon the personal information and the questions we will predict whether the patient needs further diagnosis or not

The web-app will also provide the patient with the opportunity to download a detailed report for his diagnosis 

Page 1: landing page will welcome the user to the application 

Page2: The user will be asked to enter their personal details

Page 3: The clinical questionnaire will diagnose the patient and the responses will be stored in a database

The chosen model will inject these inputs in itself to give a prediction for further diagnosis or not

Page 4: the final page will give a brief result to the patient for their diagnosis and they will also have the option to download a report
