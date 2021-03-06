#what is a database?

#Tabels
  Tables should store data related to one thing, such as customers
  If the database belongs to a larger entity, such as a business, thin it may store related data in separate tables
  For example: customers, items, purchases, stores, etc.

#Related data
  We can model these relationships between tabels and columns in database systems designed for it.
  There are other database systems which do not allow for relational data
  They have other advantages, such as increased speed or simpler scalability

#Scalability
  A database management system is installed and runs on a computer
  Application connect ot hat computer and ask it to retrieve data for them
  If there are too many requests for data, the computer can end up unable to cope with the load.
  Relational database management systems (RDBMSs) tend to not scale as well as non-relational database management systems
  Scalability is important becuase it enables the servers to serve more clients (applications)
  However, RDBMSs allow you to interact and retrieve data easily.
  For example, using the tables shown earlier, it is easy to get "revenue generated per customer" using an RDBMNS than a non-relational system.

## THE SELECT COMMAND
SELECT * FROM customers;

SELECT customers.first_name FROM customers;

## multiple queries separated by commas also using the alias command AS to rename the columns

SELECT customers.first_name AS "First Name", customers.last_name AS "Last Name" FROM customers;

## THE WHERE COMMAND
    # This will get any customer's from the customers table if they have the first name 'Rolf' 
 SELECT customers.first_name AS "First Name", customers.last_name AS "Last Name" FROM customers
 WHERE customers.first_name = 'Rolf';


## THE OR/AND COMMANDS

SELECT customers.first_name, customers.last_name FROM customers
WHERE customers.first_name = 'Rolf' OR customers.last_name = 'Watson';

## LIMITING - create a limit of the amount of rows to return
SELECT customers.first_name, customers.last_name FROM customers LIMIT 1;

## THE UPDATE COMMAND
UPDATE {tablename} SET {columnname and value} WHERE {filterparameter};

## THE DELETE COMMAND
DELETE FROM items WHERE id=4;

## THE LIKE COMMAND and also WILDCARDS
 The percent symbol is a wildcard or everything
 The underscore symbol is an arbitrary placeholder
// Gets any customers with a last name that has 5 letters and an o in the middle.
SELECT * FROM customers WHERE last_name LIKE '__o__'; 

// Gets any customers with a last name that has any number of letters and has a t in it.
// will return Smith and Scott.
SELECT * FROM customers WHERE last_name LIKE '%t_'; 


# WHAT IS A JOIN
JOINs are one of the key element of relational DBs
They allow us to retrieve data from multiple tables at once
Essential to relational data, as it lets us get data from various tabels.
JOINs are quick.
The most common JOINs are INNER JOIN, followed by LEFT JOIN.


# JOINs are like sets
  - Unordered groups of unique elements
  - JOINs treat rows of data as if they were Sets

  # INTERSECT Set intersection is the elements common to two sets

  # INNER JOIN is akin to Set Intersection

  # INNER JOIN selects rows from table1 and table2 where they match the selecting column

    SELECT * FROM customers 
    INNER JOIN purchases
    ON customers.id = purchases.customer_id;

  # LEFT JOIN selects all rows from table1, on the left, the rows from table2, on the right, if they match
   
    SELECT * FROM customers
    LEFT JOIN purchases
    ON customers.id = purchases.customer_id;

  #RIGHT JOIN selects all rows from table1, on the right, the rows from table2, on the left, if they match
   
    SELECT * FROM customers
    RIGHT JOIN purchases
    ON customers.id = purchases.customer_id;
  
  # FULL JOIN selects all rows from both tables, matching them if there is a match on the selecting column
  Similar to a LEFT and a RIGHT JOIN
    
    SELECT * FROM customers
    FULL JOIN purchases
    ON customers.id = purchases.customer_id;

  # PERFORMING MULTIPLE JOINS IS POSSIBLE!
    
    SELECT first_name, last_name FROM items
    INNER JOIN purchases
    ON items.id = purchases.item_id
    INNER JOIN customers ON purchases.customer_id = customers.id;

  # GROUP BY - groups up the data to form relevant information 
    
    SELECT customers.first_name, customers.last_name, COUNT(purchases.id) FROM customers
    LEFT JOIN purchases ON customers.id = purchases.customer_id
    GROUP BY customers.id;

  # SUM - 
    SELECT customers.first_name, customers.last_name, SUM(items.price) FROM items 
    INNER JOIN purchases ON items.id = purchases.item_id
    INNER JOIN customers ON purchases.customer_id = customers.id
    GROUP BY customers.id;

    SELECT SUM(items.price) FROM purchases
    INNER JOIN items ON purchases.item_id = items.id;

  # ORDER BY, more SUM, more AS, and DESC and ASC

    SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" from customers
    INNER JOIN purchases ON customers.id = purchases.customer_id
    INNER JOIN items ON purchases.item_id = items.id
    GROUP BY customers.id
    ORDER BY total_spent DESC
    LIMIT 1;
  
  # CREATE A TABLE - learn about primary key,
    Primary keys are unique values used to identify the row. Primary keys are unique by default.
    
    CREATE TABLE public.users (
      id integer,
      name character varying(100) NOT NULL #max characters is 100 the name cannot be empty (NOT NULL)
      CONSTRAINT users_id_pkey PRIMARY KEY (id) #
    )

  # INSERT A USER
    
    INSERT INTO public.users(id, name)
    VALUES (1, 'enterloper');

  # column names as arguments are not needed if you intend to add value to every column
  # specifying the columns is necessary only if you want to omit data

    INSERT INTO public.users
    VALUES (2, 'kossel')

    CREATE TABLE public.videos (
      id integer PRIMARY KEY,
      user_id integer REFERENCES public.users, #make sure user_id is a valid row in public.users
      title character varying(255) NOT NULL,
    )

  # INSERT INTO public.videos

    INSERT INTO public.videos
    VALUES (4, 3, 'War Dogs');

  # LOOK UP THE VALUES YOU ENTERED WITH AN INNER JOIN
      
    SELECT * FROM public.videos INNER JOIN public.users ON public.users.id = public.videos.user_id;

  # AUTO INCREMENT with a SEQUENCE
      
    CREATE SEQUENCE users_id_seq; # starts with 1
    CREATE SEQUENCE users_id_seq START 4; # starts at 4
  
  # ALTER THE TABLE THAT WILL USE THE SEQUENCE
    
    ALTER TABLE public.users
    ALTER COLUMN id
    SET DEFAULT nextval('users_id_seq')
  
  # ATTACH SEQUENCE to a TABLE (this way the sequence is deleted with the table when the table is dropped)
    
    ALTER SEQUENCE users_id_seq OWNED BY public.users.id;

  # CREATE AN INDEX (indexes speed up searches when you have huge tables, this creates a binary tree. Because a tree is made, this does slow down insertion of data because the table and now the tree has to both be updated, but Indexes are still valuable.)

    CREATE INDEX users_name_index ON public.users(name);

  # CREATE MULTI-COLUMN INDEXES

    CREATE INDEX index_name ON public.videos(id, user_id)

  # If an index becomes corrupted because sometimes they do. 
    # this reduces the size of the index if the index grows too large.
    # https://www.postgresql.org/docs/9.5/static/sql-reindex.html

    REINDEX INDEX index_name
    REINDEX TABLE table_name
    REINDEX DATABASE database_name
          
  # DROP A TABLE
    
    DROP TABLE public.users CASCADE;

    # to avoid errors, you can do the following
    DROP TABLE IF EXISTS public.videos;

    DROP DATABASE/SEQUENCE/INDEX

  # SQL VIEWS - A view is a result of a query that you can do various things
    
    CREATE VIEW total_revenue_per_customer AS
    SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM customers
    INNER JOIN purchases ON customers.id = purchases.customer_id
    INNER JOIN items ON purchases.item_id = items.id
    GROUP BY customers.id;

    # Then to reference the view we can do: 

      SELECT * FROM total_revenue_per_customer;

    #To DROP the view: 

      DROP VIEW total_revenue_per_customer;

  # another view just with customer_id added:

    CREATE VIEW total_revenue_per_customer AS
    SELECT customers.id, customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM customers
    INNER JOIN purchases ON customers.id = purchases.customer_id
    INNER JOIN items ON purchases.item_id = items.id
    GROUP BY customers.id; 
    
  # WHY VIEWS ARE VALUABLE ( The query is saved so additional data can be referenced from the return )

    SELECT * FROM total_revenue_per_customer WHERE total_spent > 150;

    - Then create the view
      
      CREATE VIEW awesome_customers AS
      SELECT * FROM total_revenue_per_customer WHERE total_spent > 150;
    
    - then reference the view of the previous view and do whatever you like for display

      SELECT * FROM awesome_customers ORDER BY total_spent DESC;
  
  # INSERT INTO A VIEW (cannot be done if VIEW has a group by clause, due to losing granularity)
    -create the view
      CREATE VIEW expensive_items AS
      SELECT * FROM items WHERE price > 100;

    -insert the desired value to the view
      INSERT INTO expensive_items(id, name, price)
      VALUES (10, 'laptop', 400.00);

      #drop the view above to make a new view with a local check
      -DROP VIEW expensive_items;

  # WITH LOCAL CHECK OPTION makes sure that items can not be added to the view if they don't meet the requirements
    
    CREATE VIEW expensive_items AS
    SELECT * FROM items WHERE price > 100
    WITH LOCAL CHECK OPTION;
    
    #this now throws an error
    INSERT INTO expensive_items(id, name, price)
    VALUES (11, 'Pencil', 2.00)
  
  # FUNCTIONS IN SQL
      -COUNT()
        SELECT customers.first_name, customers.last_name, COUNT(purchases.id) AS purchase_count
        FROM customers
        INNER JOIN purchases ON customers.id = purchases.customer_id
        GROUP BY customers.id;
      -SUM()
      -AVG()
        SELECT AVG(items.price) FROM items;
          *ANOTHER *
        SELECT AVG(items.price) FROM ITEMS
        INNER JOIN purchases ON items.id = purchases.item_id; 
      -MAX()
        this:      
          SELECT items.name, items.price FROM ITEMS
          INNER JOIN purchases ON items.id = purchases.item_id
          ORDER BY items.price DESC
          LIMIT 1;
        is similar to this:
          SELECT MAX(items.price) FROM items
          INNER JOIN purchases ON items.id = purchases.item_id;
        the difference is you lose some meta data in the returned query
      -HAVING
        SELECT customers.first_name, customers.last_name, COUNT(purchases.id) AS purchase_count
        FROM customers
        INNER JOIN purchases ON customers.id = purchases.customer_id
        GROUP BY customers.id
        HAVING COUNT(purchases.id) > 2;
  ## DATES
    -DEFAULT DATE - 2017-04-16 05:16:45 ISO
    SELECT NOW(); - returns the date
    SELECT TO_CHAR(NOW(), 'DD/MM/YYYY'); returns a formatted version of the date.
    SELECT TO_CHAR(NOW(), 'FMDay, DDth FMMONTH, DD/MM/YYYY HH:MM:SS');
    SELECT TO_CHAR(NOW(), 'FMDay DDth FMMonth, DD/MM/YYYY HH:MM:SS'); - Saturday 09th September, 09/09/2017 10:09:04
    SELECT TO_TIMESTAMP('Saturday 09th September, 09/09/2017 10:09:04', 'FMDay DDth FMMonth, YYYY HH:MI:SS');
    SELECT TO_TIMESTAMP('1983-04-16 01:02:02', 'YYYY-MM-DD HH:MI:SS')
  ## OTHER TYPES 
    - STORING IMAGES using the data type BYTEA 
    - ENUM -> CREATE TYPE mood AS ENUM('extremely unhappy', 'unhappy', 'ok', 'happy', 'extremely happy');
      -then create a table:
        CREATE TABLE students (
        name character varying(255),
        current_mood mood
        );
      -then enter the value with the appropriate value from the ENUM above
        INSERT INTO students VALUES ('Moe', 'happy');
      -because ENUMS are lists, the values can be compared using >(=) or <(=)
        SELECT * FROM students WHERE current_mood > 'ok';      
  ## NESTED SELECT
    SELECT * FROM items 
    WHERE price > (SELECT AVG(items.price) FROM items);
    SELECT items.name, items.price - (
      SELECT AVG(items.price) FROM items
    ) From items;
    CREATE VIEW expensive_items_diff AS
    SELECT *, items.price - (
    SELECT AVG(items.price) From items WHERE price > 100) AS "average_diff"
    FROM items WHERE price > 100;
  # SEQUENCE - a way to auto increment values like ids
    CREATE TABLE test (
      id SERIAL PRIMARY KEY,
      name character varying(255)
    );
    INSERT INTO test(name) VALUES ('rich');
  # DELETE
    DELETE * FROM users WHERE id != 1; 
