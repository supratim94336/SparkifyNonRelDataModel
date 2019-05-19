from cassandra.cluster import Cluster
from sql_queries import create_table_queries, drop_table_queries
from config import file_path, keyspace, session_id, user_id, \
    song_title, song_duration, user_first_name, user_last_name, \
    item_in_session, artist
from sql_queries import session_table_insert, user_table_insert, \
    song_table_insert
import pandas as pd
import logging


class CassandaraDataModel:
    def __init__(self, file, session, keyspace):
        self.file = file
        self.session = session
        self.keyspace = keyspace

    def create_database(self):
        """
        This function creates a keyspace
        :return:
        """
        # create keyspace
        try:
            self.session.execute("""CREATE KEYSPACE IF NOT EXISTS {} 
            WITH REPLICATION = {'class' : 'SimpleStrategy', 
            'replication_factor' : 1 };""".format(self.keyspace))

        except Exception as e:
            logging.info(e)

        # set the keyspace with the session
        try:
            self.session.set_keyspace(keyspace)
        except Exception as e:
            logging.info(e)

    def create_tables(self):
        """
        This function creates all the tables in the database
        :param
        :return:
        """

        # create the tables
        for query in create_table_queries:
            try:
                self.session.execute(query)
            except Exception as e:
                logging.info(e)

    def drop_tables(self):
        """
        This function drops all the tables in the database
        :param
        :return:
        """

        # drop the tables
        for query in drop_table_queries:
            try:
                self.session.execute(query)
            except Exception as e:
                logging.info(e)

    def process_session_data(self, query, data):
        """
        This function processes all the data and inserts records into
        session history table
        :param query:
        :param data:
        :return:
        """

        # read and insert records
        for index, row in data.iterrows():
            try:
                self.session.execute(query, (row[session_id],
                                             row[item_in_session],
                                             row[artist],
                                             row[song_title],
                                             row[song_duration]))
            except Exception as e:
                logging.info(e)

    def process_user_data(self, query, data):
        """
        This function processes all the data and inserts records into
        user history table
        :param query:
        :param data:
        :return:
        """

        # read and insert records
        for index, row in data.iterrows():
            try:
                self.session.execute(query, (row[user_id],
                                             row[session_id],
                                             row[item_in_session],
                                             row[artist],
                                             row[song_title],
                                             row[user_first_name],
                                             row[user_last_name]))
            except Exception as e:
                logging.info(e)

    def process_song_data(self, query, data):
        """
        This function processes all the data and inserts records into
        song history table
        :param query:
        :param data:
        :return:
        """

        # read and insert records
        for index, row in data.iterrows():
            try:
                self.session.execute(query, (row[song_title],
                                             row[user_id],
                                             row[user_first_name],
                                             row[user_last_name]))
            except Exception as e:
                logging.info(e)


def main():
    cluster = Cluster()
    session = cluster.connect()
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.INFO)

    # create the database
    cassandra_model = CassandaraDataModel(file=file_path,
                                          session=session,
                                          keyspace=keyspace)

    logging.info("Creating Data Model")
    cassandra_model.create_database()

    # drop the tables
    logging.info("Dropping Existing Tables")
    cassandra_model.drop_tables()

    # create the tables
    logging.info("Creating New Tables")
    cassandra_model.create_tables()

    # define dataframe
    logging.info("Reading Data File")
    data = pd.read_csv(file_path, encoding='utf-8')
    logging.info("Total No. of Rows Present: {}".format(str(data.shape[0])))

    # process the files
    logging.info("Processing Data and Inserting into Session Table")
    cassandra_model.process_session_data(session_table_insert, data)
    logging.info("Processing Data and Inserting into User Table")
    cassandra_model.process_user_data(user_table_insert, data)
    logging.info("Processing Data and Inserting into Song Table")
    cassandra_model.process_song_data(song_table_insert, data)

    # close the connection
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
