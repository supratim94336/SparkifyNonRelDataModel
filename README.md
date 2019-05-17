## Sparkify Non-Relational Data Model

Data Modelling with Cassandra (based on User Activity Logs)

### Getting Started
Download the project:
You can download it as zip and unpack the files or you can clone this 
repository

#### Prerequisites
- Apache Cassandra from *Datastax*
(https://academy.datastax.com/planet-cassandra/cassandra) or
- Apache Cassandra from *Apache* (http://cassandra.apache.org/download/)
- Python 3.5 or above (https://www.python.org/downloads/)

#### Installing and starting Apache Cassandra
If you are downloading Cassandra from Apache foundation Website
* Step 1: Install Java
* Step 2: Download and extract Cassandra
* Step 3: Start Terminal
* Step 4:   
        - $ gedit .bashrc (update .bashrc)   
        - add lines:   
          - Line 1. EXPORT CASSANDRA_HOME = 
          cassandra_extracted_directory    
          - Line 2. EXPORT PATH = $PATH:$CASSANDRA_HOME/bin  
        - save and close .bashrc
* Step 5: $ cassandra -f (start)

or

If you are downloading Cassandra from Datastax Website
* Step 1: Install Java
* Step 2: Download and extract Cassandra v3.9.0/v3.8.0 Tarball
* Step 3: Extract the tarball file into a directory   
* Step 4: run Terminal
* Step 5:   
        - $ cd cassandra_extracted_directory/bin  
        - $ ./cassandra

#### Installing Python Dependencies
You need to install this python dependencies
In Terminal/CommandPrompt:
```
$ pip install -r requirements.txt
```
or (*optional:You can always create a virtual environment and install 
all the 
dependencies for python inside your virtual environment*)
```
$ python3 -m venv virtual-env-name
$ source virtual-env-name/bin/activate
$ pip install -r requirements.txt
```
#### Executing the creation and extraction scripts
In Terminal/CommandPrompt:
Go inside the project directory
```
$ cd project_dir_name
```
Run the pre-processing script (you need it only once)
```
$ python preprocess_files.py
```
Run the table creation script (resetting the tables)
```
$ python create_tables.py
```
Run the database population script (inserting the records)
```
$ python etl.py
```
Test the queries
```
$ jupyter notebook test.ipynb
```
### View and Analyze
You can you use the test.ipynb notebook to query according to your needs

### About the data
You can dump your user_activity_log in terms of .csv formatted files 
inside the data folder

### Example Queries
Once you are done setting up you can get started with some exciting 
queries like:  
Who were the artist, song, and its duration in a particular session and
in order 4th
```
SELECT artist, song_title, song_duration FROM music_app_session_history 
WHERE session_id=338 AND item_in_session=4
```

What artist and his/her song did a user hear in particular session
```
SELECT artist, song, user_first_name, user_last_name FROM 
music_app_user_history WHERE user_id=10 AND session_id=182
```

Who were the users, listened to a particular song
```
SELECT user_first_name, user_last_name FROM music_app_song_history WHERE
 song='All Hands Against His Own'"
```
### Authors
* **Supratim Das** - *Initial work*
