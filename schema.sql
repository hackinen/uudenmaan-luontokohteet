CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, username TEXT, password TEXT, admin BOOLEAN);
CREATE TABLE destinations (id SERIAL PRIMARY KEY, name TEXT, town TEXT, ranking INT);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, destinationId FOREIGN KEY, username TEXT, ranking INT, comment TEXT);
CREATE TABLE attractions (id SERIAL PRIMARY KEY, destinationId INT, name TEXT, info TEXT);
CREATE TABLE favourites (id SERIAL PRIMARY KEY, userId INT, destinationId INT);