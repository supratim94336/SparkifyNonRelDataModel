from cassandra.cluster import Cluster
from sql_queries import create_table_queries, drop_table_queries


def create_database(session, keyspace):
    """
    This function creates a keyspace
    :return: session
    """
    # create keyspace
    try:
        session.execute("""
                        CREATE KEYSPACE IF NOT EXISTS {} 
                        WITH REPLICATION = 
                        { 'class' : 'SimpleStrategy', 
                          'replication_factor' : 1 };
                        """
                        .format(keyspace))

    except Exception as e:
        print(e)

    # set the keyspace with the session
    try:
        session.set_keyspace(keyspace)
    except Exception as e:
        print(e)
    return session


def drop_tables(session, keyspace):
    """
    This function drops all the tables in the database
    :param session:
    :return:
    """
    # if not found, set the keyspace for safety
    session.set_keyspace(keyspace)

    # drop the tables
    for query in drop_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session, keyspace):
    """
    This function creates all the tables in the database
    :param session:
    :return:
    """
    # if not found set the keyspace for safety
    session.set_keyspace(keyspace)

    # create the tables
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def main():
    cluster = Cluster()
    session = cluster.connect()
    keyspace = "sparkify"
    # create the database
    session = create_database(session, keyspace)
    # drop the tables
    drop_tables(session, keyspace)
    # create the tables
    create_tables(session, keyspace)
    # close the connection
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()
