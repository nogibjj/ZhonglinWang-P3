## Set up: import required modules
import csv
import sqlite3

## Step 1: Do SQL queries via a cursor after connecting to superstore database
connects = sqlite3.connect("superstore.db")
cursor = connects.cursor()

## Step 2: Create a new table called superstore (new_table)
new_table = """CREATE TABLE superstore111(
 				unique_id VAR PRIMARY KEY,
                Ship-Mode VAR,
                Segment VAR,
 				Country VAR,
 				City VAR,
 				State VAR,
 				Postal-Code VAR,
 				Region VAR,
                Category VAR,
				Sub-Category VAR,
				Sales VAR,
				Quantity VAR,
				Discount VAR,
				Profit VAR
 				);
 				"""
## Step 3: Insert the new table into the original database, then insert data into table superstore by using SQL query
cursor.execute(new_table)
insert_data = "INSERT INTO superstore111 (unique_id,Ship-Mode,Segment,Country,City,State,Postal-Code,Region,Category,Sub-Category,Sales,Quantity,Discount,Profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

## Step 4: Read each record from superstore.csv file and import the data to new table
file = open("superstore.csv")
records = csv.reader(file)
cursor.executemany(insert_data, records)

### Query 1: Find the top ten states who has the most consumer customers in superstore
query1 = """SELECT Distinct State, count(Segment) 
		   FROM superstore111
		   WHERE State != '' AND Segment='Consumer'
		   Group by State
		   Order by count(Segment) DESC
		   LIMIT 10;"""
top10_consumer = cursor.execute(query1).fetchall()

### Query 2: Find the top ten states who has the most corporate customers in superstore
query2 = """SELECT Distinct State, count(Segment) 
		   FROM superstore111
		   WHERE State != '' AND Segment='Corporate'
		   Group by State
		   Order by count(Segment) DESC
		   LIMIT 10;"""
top10_corporate = cursor.execute(query2).fetchall()

### Query 3: Find the top ten cities who has the most profit in superstore
query3 = """SELECT Distinct City, sum(Profit) 
		   FROM superstore111
		   WHERE City != '' 
		   Group by City
		   Order by count(Profit) DESC
		   LIMIT 10;"""
top10_city = cursor.execute(query3).fetchall()

## Step 5: Show all the results after quering data to the terminal
###Query 1
print("#" * 50)
print(f"Top ten states who has the most consumer customers in superstore:")
for i in top10_consumer:
    print(i)

###Query 2
print("#" * 50)
print(f"Top ten states who has the most corporate customers in superstore:")
for j in top10_corporate:
    print(j)

###Query 3
print("#" * 50)
print(f"Top ten cities who has the most profit in superstore:")
for k in top10_city:
    print(k)

## Finally: Commit all changes and close the database connection
connects.commit()
connects.close()
