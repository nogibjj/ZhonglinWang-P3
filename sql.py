## Set up: import required modules
import csv
import sqlite3

## Step 1: Do SQL queries via a cursor after connecting to zomato database
connects = sqlite3.connect("zomato.db")
cursor = connects.cursor()

## Step 2: Create a new table called netflix_type1
new_table = """CREATE TABLE zomato111(
 				Restaurant ID PRIMARY KEY,
                Restaurant Name,
                Country Code,
 				City,
 				Address,
 				Locality,
 				Locality Verbose,
 				Longitude,
 				Latitude DATE,
 				Cuisines DATE,
 				Average Cost for two,
 				Currency,
 				Has Table booking,
 				Has Online delivery,
                Is delivering now,
                Switch to order menu,
                Price range,
                Aggregate rating,
                Rating color,
                Rating text,
                Votes
 				);
 				"""
## Step 3: Insert the new table into the original database, then insert data into table zomato by using SQL query
cursor.execute(new_table)
insert_data = "INSERT INTO zomato111 (Restaurant ID, Restaurant Name,Country Code,City,Address,Locality,Locality Verbose,Longitude,Latitude DATE,Cuisines DATE,Average Cost for two,Currency,Has Table booking,Has Online delivery,Is delivering now,Switch to order menu,Price range,Aggregate rating,Rating color,Rating text,Votes) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?);"

## Step 4: Read each record from netflix_titles.csv file and import its records to new table netflix_type
file = open("zomato.csv")
records = csv.reader(file)
cursor.executemany(insert_data, records)

### Query 1: Find the top five countries who have the most TV Shows in zomato
query1 = """SELECT Distinct country, count(type) 
		   FROM zomato111
		   WHERE country != '' AND type='TV Show'
		   Group by country
		   Order by count(type) DESC
		   LIMIT 5;"""
top5_tv_country = cursor.execute(query1).fetchall()

### Query 2: Find the top five countries who have the most movies in Netlfix
query2 = """SELECT Distinct country, count(type) 
		   FROM zomato111
		   WHERE country != '' AND type='Movie'
		   Group by country
		   Order by count(type) DESC
		   LIMIT 5;"""
top5_movie_country = cursor.execute(query2).fetchall()

### Query 3: Find the top five directors who directed the most movies or TV shows in Netlfix
query3 = """SELECT Distinct director, count(title) 
		   FROM zomato111
		   WHERE director != '' 
		   Group by director
		   Order by count(title) DESC
		   LIMIT 5;"""
top5_director = cursor.execute(query3).fetchall()

### Query 4: Find the top five directors who have the most movies or TV shows in Netlfix are listed in Documentaries
query4 = """SELECT Distinct director, count(listed_in) 
		   FROM zomato111
		   WHERE director != '' AND listed_in = 'Documentaries'
		   Group by director
		   Order by count(listed_in) DESC
		   LIMIT 5;"""
top5_director_documentaries = cursor.execute(query4).fetchall()

### Query 5: Find the top five directors who have the most adult movies or TV shows in Netlfix
query5 = """SELECT Distinct director, count(rating) 
		   FROM zomato111
		   WHERE director != '' AND rating in ('R', 'TV-MA', 'NC-17')
		   Group by director
		   Order by count(rating) DESC
		   LIMIT 5;"""
top5_director_adult = cursor.execute(query5).fetchall()

## Step 5: Show all the results after quering data to the terminal
###Query 1
print("#" * 50)
print(f"Top five countries who have the most TV Shows in Netlfix:")
for i in top5_tv_country:
    print(i)

###Query 2
print("#" * 50)
print(f"Top five countries who have the most movies in Netlfix:")
for j in top5_movie_country:
    print(j)

###Query 3
print("#" * 50)
print(f"Top five directors who directed the most movies or TV shows in Netlfix:")
for k in top5_director:
    print(k)

###Query 4
print("#" * 50)
print(
    f"Top five directors who have the most movies or TV shows in Netlfix are listed in Documentaries at Netlfix:"
)
for l in top5_director_documentaries:
    print(l)

###Query 5
print("#" * 50)
print(f"Top five directors who have the most adult movies or TV shows in Netlfix:")
for m in top5_director_adult:
    print(m)

## Finally: Commit all changes and close the database connection
connects.commit()
connects.close()
