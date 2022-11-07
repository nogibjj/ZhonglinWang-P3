# ZhonglinWang-P3

## Abstract
In this project 3, our primary goal is to create a sql script doing sql-quarying data from the dataset "superstore.csv". The dataset is downloaded from Kaggle dataset website: https://www.kaggle.com/datasets/roopacalistus/superstore?resource=download. It includes superstore information across the US. There are 13 variables: Ship Mode, Segment, Country, City, State, Postal code, Region, Category, Sub-category, Sales, Quantity, Discount, and Profit. I add another unique_id variable as the unique identification code of each store. This project aimed at building a connection from original data, insert all records, and read them into the file called superstore.db. The built-in SQL statements will be used for answer my three reseach questions:  

* What are the top ten states who has the most superstores whose majority customers is consumer?
* What are the top ten states who has the most superstores whose majority customers is corporate?
* What are top ten cities who has the most profit of superstores?


## Querying data via Sqlite.

## Generate a script that queries a database via Sqlite
### Query 1: Find the top ten states who has the most superstores whose majority of customers is consumer.
### Query 2: Find the top ten states who has the most superstores whose majority of customers is corporate.
### Query 3: Find the top ten cities who has the most profit in superstore.
<img width="703" alt="截屏2022-11-06 下午7 09 53" src="https://user-images.githubusercontent.com/112585430/200203718-1f7c6e49-102e-4e14-9876-6b768508981d.png">


### Type: `python sql.py` on Terminal to see answers of five research questions, and print the results:
<img width="527" alt="截屏2022-11-06 下午7 09 08" src="https://user-images.githubusercontent.com/112585430/200203258-46ea5262-c05f-438f-b106-58e4ecb7cfb3.png">


## Finally: Commit all changes and then close the database connection
* `connects.commit()`
* `connects.close()`

