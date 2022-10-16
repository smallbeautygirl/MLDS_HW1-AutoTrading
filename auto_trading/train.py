import argparse
import csv

import pandas as pd


def read_csv(csv_with_path:str) -> list:
    """read a csv file

    Args:
        csv_with_path (str): csv file with path

    Returns:
        list: _description_
    """
    with open(csv_with_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

if __name__ == '__main__':
# You should not modify this part.

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
    default='training_data.csv',
    help='input training data file name')

    parser.add_argument('--testing',
    default='testing_data.csv',
    help='input testing data file name')

    parser.add_argument('--output',
    default='output.csv',
    help='output file name')

    args = parser.parse_args()
    # # The following part is an example.
    # # You can modify it at will.
    # training_data = load_data(args.training)

    # trader = Trader()
    # trader.train(training_data)
    # testing_data = load_data(args.testing)

    # read csv
    # testing_data = pd.read_csv(args.testing)

    testing_data = read_csv(args.testing)
    print(testing_data)
    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in testing_data:
            print(row)
            # method 1: (no action)
            writer.writerow([0])
    csvfile.close()

    #         # We will perform your action as the open price in the next day.
    #         action = trader.predict_action(row)
    #         output_file.write(action)
