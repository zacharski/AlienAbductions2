DROP DATABASE IF EXISTS music;
CREATE DATABASE  music;
\c music;
DROP TABLE IF EXISTS albums;
CREATE TABLE albums (
  id serial NOT NULL,
  artist varchar(35)  NOT NULL default '',
  name varchar(40) NOT NULL,
  rank int);

INSERT INTO albums (artist, name, rank) VALUES ('Jason Aldean', 'Old Boots, New Dirt', 1);
INSERT INTO albums (artist, name, rank) VALUES ('Taylor Swift', '1989', 37);
INSERT INTO albums (artist, name, rank) VALUES ('Hozier', 'Hozier', 2);
INSERT INTO albums (artist, name, rank) VALUES ('Flying Lotus', 'You''re Dead', 19);
INSERT INTO albums (artist, name, rank) VALUES ('Frozen', 'Soundtrack', 18);
INSERT INTO albums (artist, name, rank) VALUES ('Ariana Grande', 'My Everything', 30);