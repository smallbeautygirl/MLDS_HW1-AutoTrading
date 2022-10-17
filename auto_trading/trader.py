import argparse
import csv

import pandas as pd


def calculate_sma(lookback_price_list: list) -> float:
    """calculate_sma

    Args:
        lookback_price_list (list): _description_

    Returns:
        float: sma
    """
    return sum(lookback_price_list) / len(lookback_price_list)


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

    # You can modify it at will.
    # read csv (change the testing csv column name)
    testing_data = pd.read_csv(args.testing)

    if list(testing_data.columns.values) != ['open', 'high', 'low', 'close']:
        testing_data = pd.read_csv(
            args.testing, names=[
                'open', 'high', 'low', 'close'])
    print(testing_data.columns.values)

    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        lookback_number = 5
        current_action = 0
        hold = 0
        buy_price = 0
        ratio = 1.02
        for i in range(len(testing_data)):
            lookback_price_list = []
            current_close_data = testing_data.values[i][-1]

            print(f"current close price: {current_close_data}")

            if i - lookback_number > 0:
                # 檢查前n天的平均
                lookback_price_list = [testing_data.values[i - j][-1]
                                       for j in range(1, lookback_number + 1)]
                sma = calculate_sma(lookback_price_list)
                print(f"sma: {sma}")

                if hold in [0, 1] and current_close_data > sma and current_close_data > (
                        buy_price * ratio):
                    # sell
                    print("sell")
                    current_action = -1
                    hold = hold - 1
                elif hold in [0, -1] and current_close_data < sma:
                    # buy
                    print("buy")
                    current_action = 1
                    hold = hold + 1
                    buy_price = current_close_data
                else:
                    current_action = 0
            else:
                current_action = 0

            if i != len(testing_data) - 1:
                writer.writerow([current_action])

            print('-' * 50)
    csvfile.close()
