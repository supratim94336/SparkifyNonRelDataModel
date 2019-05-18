from cassandra.cluster import Cluster
import pandas as pd
from sql_queries import session_table_insert, user_table_insert, \
    song_table_insert


def process_session_data(session, query, data):
    """
    This function processes all the data and inserts records into
    session history table
    :param session:
    :param query:
    :param data:
    :return:
    """

    # read and insert records
    for index, row in data.iterrows():
        session.execute(query, (row[8], row[3], row[0], row[9], row[5]))


def process_user_data(session, query, data):
    """
    This function processes all the data and inserts records into
    user history table
    :param session:
    :param query:
    :param data:
    :return:
    """

    for index, row in data.iterrows():
        session.execute(query, (row[10], row[8], row[3], row[9], row[0],
                                row[1], row[4]))


def process_song_data(session, query, data):
    """
    This function processes all the data and inserts records into
    song history table
    :param session:
    :param query:
    :param data:
    :return:
    """

    for index, row in data.iterrows():
        session.execute(query, (row[9], row[10], row[1], row[4]))


def main():
    # connect to the keyspace
    cluster = Cluster()
    session = cluster.connect()

    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)

    # define file path of records
    file_path = "events_data_new.csv"

    # define dataframe
    data = pd.read_csv(file_path, encoding='utf-8')
    print("No of rows present: {}".format(str(data.shape[0])))

    # process the files
    try:
        process_session_data(session, session_table_insert, data)
        process_user_data(session, user_table_insert, data)
        process_song_data(session, song_table_insert, data)
    except Exception as e:
        print(e)

    # close the connection
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
