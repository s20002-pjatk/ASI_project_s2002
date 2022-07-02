import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import recall_score, f1_score
from datetime import date, datetime
from pycaret.classification import *
from pycaret.utils import check_metric
import process_raw_data

import os.path

import argparse

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

def go(batch_number,model_type):

    # Load model
    print('---evaluation')

    model_name = "model/" + model_type
    # model = pickle.load(open(model_name, 'rb'))
    model = load_model(model_name)

    # Read test data
    batch_no = batch_number
    process_raw_data.transform_raw_data("data/batch " + str(batch_no) + ".csv")
    test_data = pd.read_csv("data/batch " + str(batch_no) + ".csv")


    # print(model)
    print("Shape",test_data.shape)


    predictions = predict_model(model,test_data)

    # print(predictions)


    f1 = check_metric(predictions['points'], predictions['Label'], metric='F1')
    recall = check_metric(predictions['points'], predictions['Label'],metric = 'Recall')
    # print(f1)
    # print(recall)

    print('test')

    print('F1 on test data: ', f1)
    print('recall on test data: ', recall)
    #
    # Create the evaluation dataframe
    eval_df = pd.DataFrame()

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'F1', 'score': f1}, ignore_index=True)
    eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'recall', 'score': recall}, ignore_index=True)

    # Save evaluation to file
    evaluation_file_name = 'evaluation/model_eval.csv'

    if os.path.isfile(evaluation_file_name):
        eval_df.to_csv('evaluation/model_eval.csv', mode='a', index=False, header=False)
    else:
        eval_df.to_csv('evaluation/model_eval.csv', index=False)