# ASI_project_s2002
# Table of contents
## 1. [General](#general)
## 2. [Architecture](#architecture)
## 3. [Instruction](#instruction)
## 4. [Authors](#authors)

## 1. General <a name="general"></a>
The application was designed to support choice of wine. It can help non-expert customers to select quqlity wine. It can be a part of bigger software as well as stand-alone application. Besides, the pipeline should also work in a loop that: 
creates ML model, 
eveluates the model using new batches of data
detectcts data drift
in case of the data drift retraines and updates the model

Data to construct machine learning model were downlowaded from Kaggle.

## 2. Architecture <a name="architecture"></a>
The architecture of the application is described by the diagram shown in the Figure 1.

![Alt](architecture.drawio.svg)


## 3.Installation <a name="installation"></a>

The easiest way to run the application is to use Anaconda Navigator. It can be download from: https://anaconda.org/ 

After installation of the anaconda software, create a new virtual evironment in Anaconda Navigator. Recommended python version is 3.8.13.

To activate new environmet , type in the fllowing command in Anaconda Prompt:

(base) C:\Users\saras>conda activate ASI

Neccessary libraries to run the application were listed below:
- numpy 
- pandas
- pycaret

They can be installed in the new virtual environement by typing in the Anaconda Prompt the following command:

(ASI) C:\Users\saras> pip install name_of_the_library

To run the application type in  Anaconda Prompt the following command:
(ASI) C:\Users\saras> python wine_classifier_mod2.py

Make sure that Anaconda Prompt points the correct location where the file is stored. 


## 5. Authors <a name="authors"></a>
Sara Szymkuć is the only author of the application.
