from cassandra.cluster import Cluster
import pandas as pd
from config import file_path, keyspace, session_id, user_id, \
    song_title, song_duration, user_first_name, user_last_name, \
    item_in_session, artist
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
        session.execute(query, (row[session_id], row[item_in_session],
                                row[artist], row[song_title],
                                row[song_duration]))


def process_user_data(session, query, data):
    """
    This function processes all the data and inserts records into
    user history table
    :param session:
    :param query:
    :param data:
    :return:
    """

    # read and insert records
    for index, row in data.iterrows():
        session.execute(query, (row[user_id], row[session_id],
                                row[item_in_session], row[artist],
                                row[song_title], row[user_first_name],
                                row[user_last_name]))


def process_song_data(session, query, data):
    """
    This function processes all the data and inserts records into
    song history table
    :param session:
    :param query:
    :param data:
    :return:
    """

    # read and insert records
    for index, row in data.iterrows():
        session.execute(query, (row[song_title], row[user_id],
                                row[user_first_name],
                                row[user_last_name]))


def main():
    # connect to the keyspace
    cluster = Cluster()
    session = cluster.connect()

    try:
        session.set_keyspace(keyspace=keyspace)
    except Exception as e:
        print(e)

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
