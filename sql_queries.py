# DROP TABLES

session_table_drop = "DROP TABLE IF EXISTS music_app_session_history;"
user_table_drop = "DROP TABLE IF EXISTS music_app_user_history;"
song_table_drop = "DROP TABLE IF EXISTS music_app_song_history;"

# CREATE TABLES

session_table_create = ("""
CREATE TABLE IF NOT EXISTS music_app_session_history 
 (session_id int, item_in_session int, artist text, song_title text, 
 song_duration float, PRIMARY KEY (session_id, item_in_session));
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS music_app_user_history
 (user_id int, session_id int, item_in_session int, artist text, 
 song text, user_first_name text, user_last_name text, 
 PRIMARY KEY ((user_id, session_id), item_in_session));
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS music_app_song_history (song text, 
 user_id int, session_id int, user_first_name text, user_last_name text, 
 PRIMARY KEY (song, user_id, session_id));
""")


# INSERT RECORDS

session_table_insert = ("""
INSERT INTO music_app_session_history (session_id, item_in_session, 
artist, song_title, song_duration) VALUES (%s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO music_app_user_history (user_id, session_id, 
item_in_session, artist, song, user_first_name, user_last_name) 
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO music_app_song_history (song, user_id, session_id, 
user_first_name, user_last_name) VALUES (%s, %s, %s, %s, %s);
""")

# QUERY LISTS

create_table_queries = [session_table_create, user_table_create,
                        song_table_create]
drop_table_queries = [session_table_drop, user_table_drop,
                      song_table_drop]
