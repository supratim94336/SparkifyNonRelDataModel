import json


with open('config.json', 'r') as f:
    config = json.load(f, encoding='utf-8')

# FILE
file_path = config["file_path"]

# KEYSPACE
keyspace = config["keyspace"]

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