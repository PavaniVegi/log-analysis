# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:48:33 2018

@author: Pavani vegi
"""

import psycopg2
import re

dbname = 'news'

"""
print_results prints the query result 
"""
def print_results(result):
    reslength = len(result);
    for i in range(0,reslength):
        print(result[i])
       # print(re.sub(r"[\\(\\)]","",str(result[i])))
    print("\n\n")


#What are the most popular three articles of all time?

query1Text = " \
SELECT \
    b.title, count(a.*) AS Views \
FROM  \
    log a INNER JOIN articles b ON a.path = CONCAT('/article/', b.slug) \
GROUP BY b.title \
ORDER BY views DESC \
LIMIT 3 ;" 


db = psycopg2.connect(database = dbname)
c = db.cursor()
c.execute(query1Text)
print("Most popular three articles of all time")
print_results(c.fetchall())

# Who are the most popular article authors of all time?

query2Text = " \
SELECT \
    c.name, count(a.*) as views \
FROM \
    log a inner join articles b ON a.path = CONCAT('/article/',b.slug) \
    inner join authors c ON b.author = c.id \
GROUP BY c.name ORDER BY views DESC ;"

c.execute(query2Text)
print("most popular article authors of all time")
print_results(c.fetchall())

# On which days did more than 1% of requests lead to errors?

query3TextCreateView = "\
CREATE OR REPLACE VIEW Error_Logs \
AS \
SELECT \
    SUBSTRING(CAST (time AS VARCHAR),1,10) AS date , (COUNT(*) * 1.0 * 100 )/(SELECT COUNT(*) FROM log WHERE status = '404 NOT FOUND' ) AS error \
FROM \
    log \
WHERE \
    status = '404 NOT FOUND' \
GROUP BY SUBSTRING(CAST (time AS VARCHAR),1,10); "

query3Text = "\
SELECT \
date,error \
from Error_Logs \
where  error >1;"

c.execute(query3TextCreateView)
c.execute(query3Text)
print("days which leads to more than 1% errors")
print_results(c.fetchall())
db.close()

