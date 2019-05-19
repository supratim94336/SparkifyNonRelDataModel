import os
import glob
import csv
from config import file_path


def preprocess_files(all_events_file):
    """
    This function processes all the events csv files and creates a final
    csv file with all the non null records/rows found
    :param all_events_file:
    :return:
    """
    # checking your current working directory
    cur_dir = os.getcwd()

    # Get your current folder and subfolder event data
    data_dir = os.path.join(cur_dir, 'event_data')

    # Create a for loop to create a list of files and collect each
    # file_path
    file_path_list = []
    for root, dirs, files in os.walk(data_dir):
        # join the file path and roots with the subdirectories using
        # glob
        file_path_list = glob.glob(os.path.join(root, '*'))

    full_data_rows_list = []

    # for every file_path in the file path list collect records
    for f in file_path_list:

        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:

            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)

            # extracting each data row one by one and append it
            for line in csvreader:
                full_data_rows_list.append(line)

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)

    # create one file with all the records
    with open(all_events_file, 'w', encoding='utf8',
              newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(
            ['artist', 'firstName', 'gender', 'itemInSession',
             'lastName', 'length', 'level', 'location', 'sessionId',
             'song', 'userId'])
        for row in full_data_rows_list:
            if row[0] == '':
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5],
                             row[6], row[7], row[8], row[12], row[13],
                             row[16]))


def main():
    preprocess_files(all_events_file=file_path)


if __name__ == '__main__':
    main()

