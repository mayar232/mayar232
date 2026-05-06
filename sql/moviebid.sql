CREATE DATABASE MovieDBN;
USE MovieDBN;

-- =========================
-- 1. Production Table
-- =========================
CREATE TABLE Production (
    p_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    address VARCHAR(100)
);

-- =========================
-- 2. Movie Table
-- =========================
CREATE TABLE Movie (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    year DATE,
    product_id INT,
    duration INT,
    FOREIGN KEY (product_id) REFERENCES Production(p_id)
);

-- =========================
-- 3. Actor Table
-- =========================
CREATE TABLE Actor (
    actor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date_of_birth DATE
);

ALTER TABLE Actor
MODIFY name VARCHAR(50) NOT NULL;

-- =========================
-- 4. Director Table
-- =========================
CREATE TABLE Director (
    director_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date_of_birth DATE,
    direct VARCHAR(100),
    acts_in VARCHAR(100),
    age2 INT,
    address VARCHAR(44)
);

-- =========================
-- 5. Genre Table
-- =========================
CREATE TABLE Genre (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    name_type VARCHAR(100)
);

-- =========================
-- 6. Movie_Actor Table
-- =========================
CREATE TABLE Movie_Actor (
    movie_id INT,
    actor_id INT,
    role VARCHAR(100),
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);

-- =========================
-- 7. Director_Movie Table
-- =========================
CREATE TABLE Director_Movie (
    movie_id INT,
    director_id INT,
    role VARCHAR(100),
    PRIMARY KEY (movie_id, director_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (director_id) REFERENCES Director(director_id)
);

-- =========================
-- 8. Movie_Genre Table
-- =========================
CREATE TABLE Movie_Genre (
    genre_id INT,
    movie_id INT,
    PRIMARY KEY (genre_id, movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

-- =========================
-- 9. Quotes Table
-- =========================
CREATE TABLE Quotes (
    quote_id INT PRIMARY KEY AUTO_INCREMENT,
    text VARCHAR(255),
    movie_id INT,
    actor_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);

-- =========================
-- DATA INSERTS
-- =========================

-- Production
INSERT INTO Production (name, address) VALUES
('DreamWorks','USA'), ('Warner Bros','USA'), ('Universal','USA'),
('Paramount','USA'), ('Disney','USA'), ('Sony','USA'),
('Legendary','USA'), ('Lionsgate','USA'), ('Studio Ghibli','Japan'),
('BBC Films','UK');

-- Movie
INSERT INTO Movie (title, year, product_id, duration) VALUES
('Inception','2010-01-01',2,148),
('Avatar','2009-01-01',3,162),
('Titanic','1997-01-01',4,195),
('Interstellar','2014-01-01',2,169),
('Frozen','2013-01-01',5,102),
('Joker','2019-01-01',6,122),
('Dune','2021-01-01',7,155),
('John Wick','2014-01-01',8,101),
('Spirited Away','2001-01-01',9,125),
('Skyfall','2012-01-01',10,143);

-- Actor
INSERT INTO Actor (name, date_of_birth) VALUES
('Leonardo DiCaprio','1974-11-11'),
('Kate Winslet','1975-10-05'),
('Brad Pitt','1963-12-18'),
('Johnny Depp','1963-06-09'),
('Emma Watson','1990-04-15'),
('Robert Downey Jr','1965-04-04'),
('Tom Hardy','1977-09-15'),
('Chris Hemsworth','1983-08-11'),
('Scarlett Johansson','1984-11-22'),
('Keanu Reeves','1964-09-02');

-- Director
INSERT INTO Director (name,date_of_birth,direct,acts_in,age2,address) VALUES
('Christopher Nolan','1970-07-30','Inception','None',54,'UK'),
('James Cameron','1954-08-16','Avatar','None',70,'Canada'),
('Steven Spielberg','1946-12-18','Jurassic Park','None',77,'USA'),
('Quentin Tarantino','1963-03-27','Pulp Fiction','None',61,'USA'),
('Peter Jackson','1961-10-31','LOTR','None',62,'New Zealand'),
('Denis Villeneuve','1967-10-03','Dune','None',57,'Canada'),
('Todd Phillips','1970-12-20','Joker','None',54,'USA'),
('David Yates','1963-10-08','Harry Potter','None',61,'UK'),
('Hayao Miyazaki','1941-01-05','Spirited Away','None',83,'Japan'),
('Sam Mendes','1965-08-01','Skyfall','None',59,'UK');

-- Genre
INSERT INTO Genre (name_type) VALUES
('Action'),('Drama'),('Comedy'),('Sci-Fi'),('Fantasy'),
('Thriller'),('Romance'),('Animation'),('Adventure'),('Crime');

-- Movie_Actor
INSERT INTO Movie_Actor VALUES
(1,1,'Cobb'),(2,1,'Jake'),(3,2,'Rose'),(4,7,'Cooper'),
(5,5,'Anna'),(6,6,'Joker'),(7,7,'Paul'),(8,10,'John Wick'),
(9,9,'Chihiro'),(10,8,'James Bond');

-- Director_Movie
INSERT INTO Director_Movie VALUES
(1,1,'Director'),(2,2,'Director'),(3,3,'Director'),
(4,1,'Director'),(5,9,'Director'),(6,7,'Director'),
(7,6,'Director'),(8,8,'Director'),(9,9,'Director'),(10,10,'Director');

-- Movie_Genre
INSERT INTO Movie_Genre VALUES
(4,1),(4,2),(2,3),(4,4),(8,5),
(10,6),(4,7),(1,8),(8,9),(1,10);

-- Quotes
INSERT INTO Quotes (text,movie_id,actor_id) VALUES
('Dreams feel real',1,1),
('King of the world',3,2),
('Why so serious?',6,6),
('I will find you',8,10),
('Never saying sorry',3,2),
('Time is relative',4,7),
('I am Iron Man',5,6),
('Family is everything',8,10),
('We must go deeper',1,1),
('Adventure awaits',2,1);


-- show the unique address
select distinct address from production;
-- to retrive the first  5 rows
select* from movie limit 5;
 select * from movie where duration>180;

 select * from movie where duration>100 and duration<192;
  select * from movie where duration between 120 and 192;
   select * 
   from movie
   where movie_id> any (select movie_id
						from movie
							where movie_id in(2,3,4));
    select * 
   from movie
   where movie_id> all (select movie_id
						from movie
							where movie_id in(2,3,4));                            
SELECT * FROM Production
WHERE name LIKE '_o%';
SELECT * FROM Actor
WHERE date_of_birth IS NULL;
-- order
SELECT * FROM Movie
ORDER BY title ASC;

-- Retrieve movies whose duration is greater than ANY Sci-Fi movie duration.

select * from genre;


SELECT *FROM Movie
WHERE duration > ANY (
    SELECT duration
    FROM Movie
   where movie_id in(
   select  movie_id
   
        FROM movie_Genre
        WHERE genre_id = (
            SELECT genre_id
            FROM Genre
            WHERE name_type =' Sci-Fi'
	))
    
); 
  SELECT *FROM Movie;