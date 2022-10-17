import argparse
import csv
from cgi import print_arguments

status = 0
openPrice = []
minPrice = []
maxPrice = []
endPrice = []
total = []


def read_csv(csv_with_path: str) -> list:
    """read a csv file

    Args:
        csv_with_path (str): csv file with path

    Returns:
        list: _description_
    """
    with open(csv_with_path, 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def stockStrategy():
    global status
    # print("openPrice", openPrice)
    # print("endPrice", endPrice)
    if len(total) < 2:
        return 0
    else:
        # if status == 0:
        if abs(float(endPrice[len(endPrice) - 1]) - float(openPrice[len(openPrice) - 1])) < abs(
                float(endPrice[len(endPrice) - 2]) - float(openPrice[len(openPrice) - 2])):
            if float(endPrice[len(endPrice) - 2]) - \
                    float(openPrice[len(openPrice) - 2]) > 0 and status != -1:
                status -= 1
                return -1
            elif float(endPrice[len(endPrice) - 2]) - float(openPrice[len(openPrice) - 2]) < 0 and status != 1:
                status += 1
                return 1
            else:
                return 0
        else:
            return 0
        # else:
        #     if status == 1 and endPrice[len(
        #             endPrice) - 1] < endPrice[len(endPrice) - 2]:
        #         status -= 1
        #         return -1
        #     elif status == -1 and endPrice[len(endPrice) - 1] > endPrice[len(endPrice) - 2]:
        #         status += 1
        #         return 1
        #     else:
        #         return 0

        # else:
        #     return 0


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
    # print(testing_data)
    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in testing_data:
            # print(row)
            if (len(total) != len(testing_data) - 1):
                result = stockStrategy()
                # method 1: (no action)
                writer.writerow([result])
                total.append(result)
                openPrice.append(row[0])
                maxPrice.append(row[1])
                minPrice.append(row[2])
                endPrice.append(row[3])
        print("end", total)
        print("count", len(total))
    csvfile.close()

    #         # We will perform your action as the open price in the next day.
    #         action = trader.predict_action(row)
    #         output_file.write(action)
