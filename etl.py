import csv
from cassandra.cluster import Cluster


def process_session_data(session, file_path, table):
    """
    This function processes all the data and inserts records into
    session history table
    :param session:
    :param file_path:
    :param table:
    :return:
    """
    # get total number of records found
    with open(file_path, 'r', encoding='utf8') as f:
        num_rows = sum(1 for _ in f)

    print('{} rows found in {}'.format(num_rows, file_path))

    # counter
    count = 0

    # read and insert records
    with open(file_path, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            count += 1
            if count % 1000 == 0:
                print("{} rows out of {} have been processed"
                      .format(count, num_rows))
            query = "INSERT INTO " + table + \
                    "(session_id, " \
                    "item_in_session, " \
                    "artist, " \
                    "song_title, " \
                    "song_duration)"
            query = query + " VALUES (%s, %s, %s, %s, %s)"
            session.execute(query, (int(line[8]), int(line[3]), line[0],
                                    line[9], float(line[5])))


def process_user_data(session, file_path, table):
    """
    This function processes all the data and inserts records into
    user history table
    :param session:
    :param file_path:
    :param table:
    :return:
    """
    # get total number of records found
    with open(file_path, 'r', encoding='utf8') as f:
        num_rows = sum(1 for _ in f)

    print('{} rows found in {}'.format(num_rows, file_path))

    # counter
    count = 0

    # read and insert records
    with open(file_path, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            count += 1
            if count % 1000 == 0:
                print("{} rows out of {} have been processed"
                      .format(count, num_rows))
            query = "INSERT INTO " + table + \
                    "(user_id, " \
                    "session_id, " \
                    "item_in_" \
                    "session, " \
                    "artist, " \
                    "song, " \
                    "user_first_name, " \
                    "user_last_name)"
            query = query + " VALUES (%s, %s, %s, %s, %s, %s, %s)"
            session.execute(query, (
            int(line[10]), int(line[8]), int(line[3]), line[9], line[0],
            line[1], line[4]))


def process_song_data(session, file_path, table):
    """
    This function processes all the data and inserts records into
    song history table
    :param session:
    :param file_path:
    :param table:
    :return:
    """
    # get total number of records found
    with open(file_path, 'r', encoding='utf8') as f:
        num_rows = sum(1 for _ in f)

    print('{} rows found in {}'.format(num_rows, file_path))

    # counter
    count = 0

    # read and insert records
    with open(file_path, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            count += 1
            if count % 1000 == 0:
                print("{} rows out of {} have been processed"
                      .format(count, num_rows))
            query = "INSERT INTO " + table + \
                    " (song, " \
                    "user_id, " \
                    "session_id, " \
                    "user_first_name, " \
                    "user_last_name)"
            query = query + " VALUES (%s, %s, %s, %s, %s)"
            session.execute(query, (
            line[9], int(line[10]), int(line[8]), line[1], line[4]))


def main():
    # connect to the keyspace
    cluster = Cluster()
    session = cluster.connect()

    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)

    # define file path of records
    file_path = "all_events_file.csv"

    # process the files
    try:
        process_session_data(session, file_path,
                             table='music_app_session_history')
        process_user_data(session, file_path,
                          table='music_app_user_history')
        process_song_data(session, file_path,
                          table='music_app_song_history')
    except Exception as e:
        print(e)

    # close the connection
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
