# Phase3_Code-challenge3

## OBJECT RELATIONS CODE CHALLENGE - CONCERTS
- For this assignment, we'll be working with a Concert domain.

- We have three tables: `Band` (name and hometown), `Venue` (title and city), and `Concert`.

- For our purposes, a **Band** has many concerts, a **Venue** has many concerts, and a **Concert** belongs to a band and to a venue. **Band-Venue** is a many-to-many relationship

- You will need to create the schema for the concerts table, using the attributes specified in the deliverables below. You will also need to create the migrations for the above tables, following the same structure.

## Getting Started
- Create a directory where you will be working on this file.

- The run `pipenv install` while inside the directory.Then run `pipenv shell` so as to open up your virtual environment

- Then you will need to `pip install ipdb` inside your virtual environment this will help in debugging your code.

- Step by step work your way through the deliverables and try your best to tackle the challenges.

## Deliverables
- You will be writing methods that execute `raw SQL`queries to interact with your database. Use Python’s `sqlite3` or `psycopg2` library to run SQL commands.

- Make sure to set up your database and tables using `raw SQL` commands before working on the deliverables.
 
- Create the classes required and add the following methodsand properties.

### Classes
1. `Band`:Represents a music band with the following attributes `name` and `hometown`.
 
- `create_table`:Creates the `bands` table.
- `drop_table`:Drops the  `bands` table 
- `save`:Saves a new band to the database and retrieves the `id`.
- `create`:Class method that combines creating a `Band` object and saving it.
- `concerts`:Retrieves all concerts related to the Band.

- `venues`:Retrieves all venues where the band has performed in concerts.

2. `Venue`:Represents a venue where concerts are held,with attributes `title` and `city`.
- `create_table` : Creates the `venues` table.
- `dropt_table`:Drops the `venues` table.
- `save`:Saves a new venue to the database and retrives the `id`.
- `create`: Class method that combines creating a Venue object and saving it.
- `concerts`: Retrieves all concerts held at this venue.
- `bands`: Retrieves all bands that have performed at this venue.

3. `Concerts`:Represents a concert with a `band_id`,`venue_id` and `date`.
- `create_table`: Creates the concerts table with foreign key references to bands and venues.
- `drop_table`: Drops the concerts table.
- `save`: Saves a concert to the database.
- `create`: Class method to create and save a concert.
- `band`: Retrieves the Band instance associated with the concert.
- `venue`: Retrieves the Venue instance associated with the concert.

## Object Relationship Methods
- For the following methods, write SQL queries to retrieve the necessary data from the database.

 **Concert**

- `Concert.band()`: should return the Band instance for this concert.
- `Concert.venue()`: should return the Venue instance for this concert.

**Venue**

- `Venue.concerts()`: returns a collection of all concerts for the venue.
- `Venue.bands()`: returns a collection of all bands who performed at the venue.

**Band**

- `Band.concerts()`: should return a collection of all concerts the band has played.
- `Band.venues()`: should return a collection of all venues the band has performed at.

## Aggregate and Relationship Methods

**Concert**

- `Concert.hometown_show()`: returns true if the concert is in the band's hometown, false if it is not. Use SQL joins to compare the band's hometown with the concert's venue city.

- `Concert.introduction()`: returns a string with the band's introduction for this concert:
```python
"Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
```
**Band**

- `Band.play_in_venue(venue, date)`: takes a venue (venue title) and date (as a string) as arguments, and creates a new concert for the band at that venue on that date. Insert the concert using raw SQL.

- `Band.all_introductions()`: returns an array of strings representing all the introductions for this band.

   - Each introduction is in the form: `"Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"`

- `Band.most_performances()`: returns the Band that has played the most concerts. Use SQL GROUP BY and COUNT to identify the band with the most concerts.

**Venue**

- `Venue.concert_on(date)`: takes a date (string) as an argument and finds the first concert on that date at the venue.

- `Venue.most_frequent_band()`: returns the band that has performed the most at the venue. You will need to count how many times each band has performed at this venue using a SQL GROUP BY query.

## Authors

[Jeremy Gitau](https://github.com/Jeremy-3)