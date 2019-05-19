import json


with open('config.json', 'r') as f:
    config = json.load(f, encoding='utf-8')

# TABLE NAMES

session_table = config["tables"]["session_table"]["NAME"]
user_table = config["tables"]["users_table"]["NAME"]
song_table = config["tables"]["songs_table"]["NAME"]

# COLUMN TYPES

session_id_type = config["table_column_type"]["session_id"]
user_id_type = config["table_column_type"]["user_id"]
item_in_session_type = config["table_column_type"]["item_in_session"]
artist_type = config["table_column_type"]["artist"]
song_title_type = config["table_column_type"]["song_title"]
song_duration_type = config["table_column_type"]["song_duration"]
user_first_name_type = config["table_column_type"]["user_first_name"]
user_last_name_type = config["table_column_type"]["user_last_name"]

# PRIMARY KEYS

session_table_primary_key = config["tables"]["session_table"]\
["PRIMARY KEY"]
user_table_primary_key = config["tables"]["users_table"]["PRIMARY KEY"]
song_table_primary_key = config["tables"]["songs_table"]["PRIMARY KEY"]

# COLUMN NUMBERS IN CSV
session_id = config["csv_column"]["session_id"]
user_id = config["csv_column"]["user_id"]
item_in_session = config["csv_column"]["item_in_session"]
artist = config["csv_column"]["artist"]
song_title = config["csv_column"]["song_title"]
song_duration = config["csv_column"]["song_duration"]
user_first_name = config["csv_column"]["user_first_name"]
user_last_name = config["csv_column"]["user_last_name"]

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
