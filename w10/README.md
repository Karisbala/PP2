## Lab 10

### 1. Based on PostgreSQL tutorial create PhoneBook:

1. Design tables for PhoneBook.
2. Implement two ways of inserting data into the PhoneBook.
    * upload data from csv file
    * entering user name, phone from console  
4. Implement updating data in the table (change user first name or phone)
5. Querying data from the tables (with different filters)
6. Implement deleting data from tables by username of phone



### 2. User and his score in snake game.
1. Create user and user_score tables.
2. Before starting snake game, user should enter his username
3. If user exists, you should show current level of user. (You should create several levels, with different walls, speed etc.)
4. Implement shortcut for pause and save your current state and score to database.



## Lab 11

### 1. Based on previous task 'PhoneBook' implement following, using functions and stored procedures:
1. Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
2. Create procedure to insert new user by name and phone, update phone if user already exists 
3. Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
4. Create function to querying data from the tables with pagination (by limit and offset)
5. Implement procedure to deleting data from tables by username or phone