CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT,password TEXT
);


CREATE TABLE School (
    id SERIAL PRIMARY KEY,
    Blog_name TEXT,
    content TEXT,
    time    TIMESTAMP,
    writer TEXT
);

CREATE TABLE Life (
    id SERIAL PRIMARY KEY,
    Blog_name TEXT,
    content TEXT,
    time    TIMESTAMP,
    writer  TEXT
);


CREATE TABLE Sport (
    id SERIAL PRIMARY KEY,
    Blog_name TEXT,
    content TEXT,
    time   TIMESTAMP,
    writer TEXT
);

CREATE TABLE Game (
    id SERIAL PRIMARY KEY,
    Blog_name TEXT,
    content TEXT,
    time TIMESTAMP,
    writer TEXT
);

CREATE TABLE School_comment (
    id SERIAL PRIMARY KEY,
    Blog_id TEXT,
    content TEXT
);

CREATE TABLE life_comment (
    id SERIAL PRIMARY KEY,
    Blog_id TEXT,
    content TEXT
);

CREATE TABLE sport_comment (
    id SERIAL PRIMARY KEY,
    Blog_id TEXT,
    content TEXT
);

CREATE TABLE game_comment (
    id SERIAL PRIMARY KEY,
    Blog_id TEXT,
    content TEXT
);
