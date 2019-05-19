from config import session_table, user_table, song_table, \
    session_id_type, user_id_type, song_title_type, song_duration_type,\
    user_first_name_type, user_last_name_type, item_in_session_type, \
    artist_type, session_table_primary_key, user_table_primary_key, \
    song_table_primary_key

# DROP TABLES

session_table_drop = "DROP TABLE IF EXISTS {};".format(session_table)
user_table_drop = "DROP TABLE IF EXISTS {};".format(user_table)
song_table_drop = "DROP TABLE IF EXISTS {};".format(song_table)

# CREATE TABLES

session_table_create = ("""
CREATE TABLE IF NOT EXISTS {} 
 (session_id {}, item_in_session {}, artist {}, song_title {}, 
 song_duration {}, 
 PRIMARY KEY {});
""".format(session_table, session_id_type, item_in_session_type,
           artist_type, song_title_type, song_duration_type,
           session_table_primary_key))

user_table_create = ("""
CREATE TABLE IF NOT EXISTS {}
 (user_id {}, session_id {}, item_in_session {}, artist {}, 
 song_title {}, user_first_name {}, user_last_name {}, 
 PRIMARY KEY {});
""".format(user_table, user_id_type, session_id_type,
           item_in_session_type, artist_type, song_title_type,
           user_first_name_type, user_last_name_type,
           user_table_primary_key))

song_table_create = ("""
CREATE TABLE IF NOT EXISTS {} 
(song_title {}, user_id {}, user_first_name {}, user_last_name {}, 
 PRIMARY KEY {});
""".format(song_table, song_title_type, user_id_type,
           user_first_name_type, user_last_name_type,
           song_table_primary_key))

# INSERT RECORDS

session_table_insert = ("""
INSERT INTO {} (session_id, item_in_session, artist, song_title, 
song_duration) 
VALUES (%s, %s, %s, %s, %s);
""".format(session_table))

user_table_insert = ("""
INSERT INTO {} (user_id, session_id, item_in_session, artist, 
song_title, user_first_name, user_last_name) 
VALUES (%s, %s, %s, %s, %s, %s, %s);
""".format(user_table))

song_table_insert = ("""
INSERT INTO {} (song_title, user_id, user_first_name, user_last_name) 
VALUES (%s, %s, %s, %s);
""".format(song_table))

# QUERY LISTS

create_table_queries = [session_table_create, user_table_create,
                        song_table_create]
drop_table_queries = [session_table_drop, user_table_drop,
                      song_table_drop]
