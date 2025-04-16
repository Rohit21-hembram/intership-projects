# creating database named data_coffee.
create database data_coffee;
use data_coffee;

# creating table sales.
create table sales(
	date VARCHAR(10),
    datetime TIME,
    cash_type VARCHAR(10),
    card VARCHAR(50),
    money FLOAT,
    coffee_name VARCHAR(50)
    );
    
# loading data into table sales.
load data infile "D:/Unified mentor Internship projects/Coffee sales/index.csv"
	into table sales
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    ;

# checking the values.
SELECT * FROM sales;

# checking for null values of every columns.
select count(*) as date_null_counts from sales where date is null;
select count(*) as datetime_null_counts from sales where datetime is null;
select count(*) as cash_type_null_counts from sales where cash_type is null;
select count(*) as card from sales where card = '';
select count(*) as money from sales where money is null;
select count(*) as coffee_name_null_counts from sales where coffee_name is null;

 # filling missing value.
 # Finding out the most frequent value in card column.
SELECT card
FROM Sales
GROUP BY card
ORDER BY COUNT(*) DESC
LIMIT 1 OFFSET 1;

UPDATE Sales
JOIN (
    SELECT card
    FROM Sales
    GROUP BY card
    ORDER BY COUNT(*) DESC
    LIMIT 1 OFFSET 1
) AS SecondMostFrequent
ON sales.card IS NULL
SET sales.card = SecondMostFrequent.card;

select * from sales;

# Analyzing distribution of card columns.
SELECT card, COUNT(*) as frequency
FROM sales
GROUP BY card
ORDER BY frequency DESC;















