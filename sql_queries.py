# TABLE NAMES
session_table = "music_app_session_history"
user_table = "music_app_user_history"
song_table = "music_app_song_history"

# DROP TABLES

session_table_drop = "DROP TABLE IF EXISTS {};".format(session_table)
user_table_drop = "DROP TABLE IF EXISTS {};".format(user_table)
song_table_drop = "DROP TABLE IF EXISTS {};".format(song_table)

# CREATE TABLES

session_table_create = ("""
CREATE TABLE IF NOT EXISTS {} 
 (session_id int, item_in_session int, artist text, song_title text, 
 song_duration float, PRIMARY KEY (session_id, item_in_session));
""".format(session_table))

user_table_create = ("""
CREATE TABLE IF NOT EXISTS {}
 (user_id int, session_id int, item_in_session int, artist text, 
 song text, user_first_name text, user_last_name text, 
 PRIMARY KEY ((user_id, session_id), item_in_session));
""".format(user_table))

song_table_create = ("""
CREATE TABLE IF NOT EXISTS {} (song text, 
 user_id int, user_first_name text, user_last_name text, 
 PRIMARY KEY (song, user_id));
""".format(song_table))


# INSERT RECORDS

session_table_insert = ("""
INSERT INTO {} (session_id, item_in_session, 
artist, song_title, song_duration) VALUES (%s, %s, %s, %s, %s);
""".format(session_table))

user_table_insert = ("""
INSERT INTO {} (user_id, session_id, 
item_in_session, artist, song, user_first_name, user_last_name) 
VALUES (%s, %s, %s, %s, %s, %s, %s);
""".format(user_table))

song_table_insert = ("""
INSERT INTO {} (song, user_id, 
user_first_name, user_last_name) VALUES (%s, %s, %s, %s);
""".format(song_table))

# QUERY LISTS

create_table_queries = [session_table_create, user_table_create,
                        song_table_create]
drop_table_queries = [session_table_drop, user_table_drop,
                      song_table_drop]
