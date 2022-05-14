CREATE TABLE users(id Serial, name text, email text, age int);

INSERT INTO users(name, email, age) VALUES
    ('Daniel', 'varmilo.blue@protonmail.com', 15);

select * from users;	