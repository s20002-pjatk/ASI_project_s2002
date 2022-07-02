import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def transform_raw_data(name):
    # name = sys.argv[1]
    csv_url= name
    dataset_transformed = pd.read_csv(csv_url, sep=',')

    # dataset_smaller = dataset.head(50000)
    # print(dataset_smaller.shape)

    # dataset.info()
    print(f"Quality {set(dataset_transformed['points'])}")

    transformed= len(set(dataset_transformed['points']))
    if transformed > 3:

        dataset_transformed.points = np.where(dataset_transformed['points']>89, 'Good', 'Bad')

        dataset_final = dataset_transformed.drop_duplicates()
        dataset_final.to_csv(name,index=False)

        # plt.title('Rozkład danych "points"')
        # dataset_transformed['points'].hist()
        # plt.savefig('histogram_points')
        #
        # plt.title('Rozkład danych "points"')
        # dataset_transformed['points'].hist()
        # plt.show()
        # plt.savefig('histogram_categorical')

    else:
        print('Data already in good format')

# transform_raw_data('wine_data_regr.csv')

