# About Project - Log Analysis
Building an informative summary from logs is a real task that comes up very often in software engineering.In this project we are working with real time application database which contains the data of http server logs.

In this project we are trying to answer three most frequently asked questions.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# How it works?
# Step 1 : Downloading the data
We need to download the data to the PostgreSQL database. Run the below command
psql -d <databasename> -f <filename>
Running the above command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

# Step 2 : Creating reporting tool using Python
Run the command
python loganalysis.py
Running the above command will execute the file loganalysis.py and print the required results of the SQL queries in plain text. 

We may have to create and use views in the above program as some of the queries are little complex.

Syntax for creation of views
CREATE OR REPLACE <View Name>
AS
<.....
       SELECT STATEMENT
 .....>

