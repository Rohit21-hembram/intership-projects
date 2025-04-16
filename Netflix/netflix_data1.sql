# Creating database as netflix.
create database netflix;
use netflix;

# Table created as netflix1 using Table Data Import Wizard.
select * from netflix1;

# Creating a duplicate table.
create table dub_netflix
like netflix1;

# Inserting te same datas here
insert dub_netflix
select * from netflix1;

# Checking values
select * from dub_netflix;

# Remove duplicates.
select *,
ROW_NUMBER() OVER(
PARTITION BY show_id, type, title, director, country, date_added, release_year, rating, duration, listed_in) AS row_num
 from dub_netflix;
 
 WITH duplicates as
 (
 select *,
ROW_NUMBER() OVER(
PARTITION BY show_id, type, title, director, country, date_added, release_year, rating, duration, listed_in) AS row_num
 from dub_netflix
 )
 select * from duplicates where row_num > 1;
 # No duplicates found.
 
# Standardize data.

select date_added from dub_netflix;
select date_added, 
STR_TO_DATE(date_added, '%m/%d/%Y') from dub_netflix;

UPDATE dub_netflix
SET date_added = STR_TO_DATE(date_added, '%m/%d/%Y');

ALTER TABLE dub_netflix
MODIFY COLUMN date_added DATE;

# lets check the dataset.
select * from dub_netflix;

# Exploratory data analysis.
SELECT type, COUNT(*) AS count
FROM dub_netflix
GROUP BY type;

# adding column as year, month and day.
ALTER TABLE dub_netflix
ADD COLUMN year INT,
ADD COLUMN month INT,
ADD COLUMN day INT;

# updating year, month and day.
UPDATE dub_netflix
SET year = YEAR(date_added),
    month = MONTH(date_added),
    day = DAY(date_added);

select date_added, year, month, day from dub_netflix limit 10;



