from pickle import TRUE
import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path
import warnings
import glob


def add_datapoints():
    import shutil

    dataset2 = pd.read_csv('data/processed.csv', sep=',')
    csv_files = glob.glob(os.path.join('data/', "*.csv"))
    print(csv_files)
    i = 0

    model_pkl = glob.glob(os.path.join('model/', "*.pkl"))

    batches = []

    for file in csv_files:
        if 'batch' in file:
            i += 1
            batches.append(file)

    batches.append('data/processed.csv')

    print(batches)
    test = pd.concat(map(pd.read_csv, batches), ignore_index=True)

    dst = "data/used_batches/"
    name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S.csv")
    previous_file = 'data/processed.csv'
    print(name, previous_file)
    dst_new = dst + name
    shutil.move(previous_file, dst_new)

    test_final = test.drop_duplicates()
    test_final.to_csv('data/processed.csv', index=False)

    for file in batches:
        if 'batch' in file:
            import shutil

            dst = "data/used_batches"
            shutil.move(file, dst)

def move_model():
    import shutil
    name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S.pkl")
    prev_model ='model/classifier.pkl'
    dst = "model/previous_models/"+name
    shutil.move(prev_model, dst)

def detect():
    drift = False
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Read model evaluation results
    eval_results = pd.read_csv('evaluation/model_eval.csv', parse_dates=['time_stamp'], dayfirst=True)

    last_run = eval_results['time_stamp'].max()
    model_version = eval_results[eval_results['time_stamp'] == last_run]['version'].values[0]

    # Prepare data for tests
    F1_logs = eval_results[eval_results['metric']=='F1']
    recall_logs = eval_results[eval_results['metric']=='recall']

    last_F1 = F1_logs[F1_logs['time_stamp']==last_run]['score'].values[0]
    all_other_F1 = F1_logs[F1_logs['time_stamp']!=last_run]['score'].values

    last_recall = recall_logs[recall_logs['time_stamp']==last_run]['score'].values[0]
    all_other_recall = recall_logs[recall_logs['time_stamp']!=last_run]['score'].values


    ### Hard test ###

    hard_test_F1 = last_F1 < 0.65 #np.mean(all_other_F1)
    # hard_test_recall = last_recall < np.mean(all_other_recall)


    hard_test_recall = last_recall < 0.62

    print('\nLegend: \nTRUE means the model has drifted. FALSE means the model has not.')

    print('\n.. Hard test ..')
    print('F1: ', hard_test_F1, '  recall: ', hard_test_recall)
    print(last_F1)

    # Re-training signal
    drift_df = pd.DataFrame()
    drift_signal_file = 'evaluation/model_drift.csv'
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print('\n  --- DRIFT DETECTION ---')

    actual_tests = {
                                'hard_test_F1': hard_test_F1,
                                'hard_test_recall': hard_test_recall
                            }


    # print('----',set(actual_tests.values()))

    drift_detected = False
    if True in set(actual_tests.values()):
        drift_detected = True

    if drift_detected:
        print('There is a DRIFT detected in...')
        for a in actual_tests:
            if actual_tests[a]:
                print(a)
        drift_df = drift_df.append({'time_stamp': now, 'model_name': model_version,
                                'hard_test_F1': str(hard_test_F1),
                                'hard_test_recall': str(hard_test_recall),
                                }, ignore_index=True)

        # Save drift signal to file
        if os.path.isfile(drift_signal_file):
            drift_df.to_csv(drift_signal_file, mode='a', header=False, index=False)
        else:
            drift_df.to_csv(drift_signal_file, index=False)
    else:
        print('There is NO DRIFT detected.')

    if drift_detected:
        import subprocess
        print('\n  --- RE-TRAINING ---\n')
        add_datapoints()
        move_model()
        subprocess.call(['python', 'wine_classifier_mod2.py'])