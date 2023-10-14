CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT,password TEXT
);


CREATE TABLE Blogs (
    id SERIAL PRIMARY KEY,
    Blog_name TEXT,
    content TEXT,
    time    TIMESTAMP,
    user_id TEXT REFERENCES users ON DELETE CASCADE,
    community TEXT
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    Blog_id TEXT REFERENCES Blogs ON DELETE CASCADE,
    content TEXT
);


