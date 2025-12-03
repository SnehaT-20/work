create database cust_db;
create table customer(
 cid int,
 cname varchar(20),
 address varchar(20),
 email varchar(30),
 contact int(12));
  insert into customer( cid, cname, address, email, contact) values
  (1, 'sneha', 'okha', 'sneha@gmail.com', 9022237845),
  (2, 'mona', 'baroda', 'mona@gmail.com', 9022245698),
  (3, 'mohnish', 'ahemdabad', 'mohnish@gmail.com', 9012548845),
  (4, 'monu', 'okha', 'monu@gmail.com', 9020258145),
  (5, 'senu', 'dwarka', 'senu@gmail.com', 9892347845),
  (6, 'nitin', 'mundra', 'nitin@gmail.com', 9005148845),
  (7, 'parth', 'rajkot', 'parth@gmail.com', 9789457845),
  (8, 'samarth', 'dwarka', 'samarth@gmail.com', 9020594625),
  (9, 'yash', 'mithapur', 'yash@gmail.com', 9022302565),
  (10, 'dhviti', 'mithapur', 'dhviti@gmail.com', 9022512346);
  
  -- 15 nov
	alter table customer
    modify column cid int primary key;
    
    alter table customer
    modify column cname varchar(20) not null;
    
    alter table customer
    add column salary int(10) check(salary>2000);
    
    alter table customer
    add column b_date date default('2004-11-20');
    
    