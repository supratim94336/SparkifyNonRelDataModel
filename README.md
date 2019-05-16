## Sparkify Non-Relational Data Model

Data Modelling with Postgres (based on Songs Metadata and User Activity Logs)

### Getting Started
Download the project:
You can download it as zip and unpack the files or you can clone the 
repository from our github link

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
* Step 4: $ cassandra -f (start)

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
Run the pre-processing script
```
$ python preprocess_files.py
```
Run the table creation script
```
$ python create_tables.py
```
Run the database population script
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
You can dump your user_activity_log .csv formatted files inside the data
 folder

### Example Queries
Once you are done setting up you can get started with some exciting 
queries like:  
Who are the users who heard a particular song
```
Yet to be written
```

What an user heard in a particular session
```
Yet to be written
```

What was the song heard by a user in a particular session
```
Yet to be written
```
### Authors
* **Supratim Das** - *Initial work*
