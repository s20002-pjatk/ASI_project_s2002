#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from pycaret.classification import *
import os
import glob
import process_raw_data
import evaluate
import argparse
import drift_mod
import re


def prepare_sets():
  import shutil
  process_raw_data.transform_raw_data('data/processed.csv')
  dataset2 = pd.read_csv('data/processed.csv', sep=',')

  csv_files = glob.glob(os.path.join('data/', "*.csv"))
  # print(csv_files)
  i =0

  model_pkl = glob.glob(os.path.join('model/', "*.pkl"))
  batches = []

  for file in csv_files:
    if 'batch' in file:
      i += 1
      batches.append(file)

  return dataset2,len(model_pkl),batches


def train(data,model_pkl):
  if model_pkl==0:
    exp1 = setup(data=data, target='points', session_id=122, log_experiment=True, silent = True)
    best = compare_models()
    lightgbm = create_model(best)
    tuned_lightgbm = tune_model(lightgbm)
    plot_model(tuned_lightgbm, save=True)
    plot_model(tuned_lightgbm, plot='error',save = True)
    plot_model(tuned_lightgbm, plot='feature',save = True)
    evaluate_model(tuned_lightgbm)
    final = finalize_model(tuned_lightgbm)
    predict_model(final)
    save_model(final, model_name='model/classifier')
  else:
    print('current model active')

def monitor(batches):
  print('wine')
  print(batches)
  if len(batches)>0:
    batches_no = []
    for file in batches:
      number = re.findall(r'\d+', file)
      if len(number) > 0 and number[0] not in batches_no:
        batches_no.append(int(number[0]))

    print(batches_no)
    for i in batches_no:
      print(i, max(batches_no))
      if i == max(batches_no):
        print('Detected')
        evaluate.go(max(batches_no),'classifier')
        drift_mod.detect()

  else:
    print('no new data')

if __name__ == "__main__":
  print('test')
  data, model_pkl, batches = prepare_sets()
  print(f'Training dataset: {data.shape}')
  print(set(data['points']))
  train(data,model_pkl)
  monitor(batches)





