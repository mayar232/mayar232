CREATE database movie2;
use movie2;
create table production(p_id int primary key,
p_name varchar(50),
address varchar(100) 
);

show tables;
show databases;
describe production;
desc production;
rename table production to production_new;
create table movie(movie_id int primary key ,
title varchar(50) , year1 date, duration int);

rename table production_new to product;
alter table movie
add pid int,
modify movie_id int;
DESCRIBE movie;
create table gener(g_id int(6) ,
 name_type varchar(50),
 constraint gener_g_id_pk primary key (g_id));
SHOW TABLES;
DROP TABLE gener;
CREATE TABLE gener (
  g_id INT(6),
  name_type VARCHAR(50),
  CONSTRAINT gener_g_id_pk PRIMARY KEY (g_id)
);
SHOW TABLES;
alter table movie 
add (CONSTRAINT id foreign key(pid)
references product(p_id)on delete cascade);
CREATE TABLE movie_gener (
  movie_id INT,
  g_id INT,

  CONSTRAINT movie_gener_pk PRIMARY KEY (movie_id, g_id),

  CONSTRAINT fk_movie_gener_movie
    FOREIGN KEY (movie_id)
    REFERENCES movie(movie_id),
    CONSTRAINT fk_movie_gener_gener
    FOREIGN KEY (g_id)
    REFERENCES gener(g_id)
 );

SELECT 
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'movie';
CREATE TABLE director_movie (
  rolee VARCHAR(60),
  movie_id INT,
  director_id INT,


  CONSTRAINT director_movie_pk 
    PRIMARY KEY (movie_id, director_id),

  CONSTRAINT fk_director_movie_movie
    FOREIGN KEY (movie_id)
    REFERENCES movie(movie_id),

  CONSTRAINT fk_director_movie_director
    FOREIGN KEY (director_id)
    REFERENCES director(director_id)
    
);
CREATE TABLE actor (
  actor_id INT PRIMARY KEY,
  namee VARCHAR(50),
  date_of_birth DATE
); 
alter table actor
add age int;
SELECT 
  actor_id,
  namee,
  date_of_birth,
  TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS age
FROM actor;
CREATE TABLE movie_actor(
  rolee VARCHAR(60),
  movie_id INT, 
  actor_id INT,

  CONSTRAINT actor_movie_pk 
    PRIMARY KEY (movie_id, actor_id),

  CONSTRAINT fk_actor_movie_movie
    FOREIGN KEY (movie_id)
    REFERENCES movie(movie_id),

  CONSTRAINT fk_actor_movie_actor
    FOREIGN KEY (actor_id)
    REFERENCES actor(actor_id)
);
CREATE TABLE quotes (
  quote_id INT AUTO_INCREMENT PRIMARY KEY,
  textt VARCHAR(250),
  movie_id INT,
  actor_id INT,

  CONSTRAINT fk_quotes_movie
    FOREIGN KEY (movie_id)
    REFERENCES movie(movie_id),

  CONSTRAINT fk_quotes_actor
    FOREIGN KEY (actor_id)
    REFERENCES actor(actor_id)
);
alter table movie
add CONSTRAINT uni_title unique(title); 
SELECT 
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'movie2';

ALTER TABLE equip
DROP CONSTRAINT equip_retairn_ck;
ALTER TABLE equip
DROP PRIMARY KEY ; 
CREATE TABLE products (
    tags SET('new', 'sale', 'popular')
);
SELECT FORMAT(12345.6789, 2) AS result;

CREATE TABLE sizes (
    size ENUM('small', 'medium', 'large')
);

CREATE TABLE products (
    tags SET('new', 'sale', 'popular')
);
INSERT INTO production
VALUES(1,'p1','ts');

INSERT INTO actor
VALUES(01,'ali','1992-04-10',30);

INSERT INTO director
VALUES('ahmad','1989-02-05',103,'no acts');

INSERT INTO gener
VALUES(110,'drama');

INSERT INTO quotes
VALUES(112,'mack today count',1123,01);

INSERT INTO production
(P_id,p_name,address)
VALUES
(2, 'p2','ts');
INSERT INTO movie
VALUES(101,'dreams','2020-02-01',120,2);


