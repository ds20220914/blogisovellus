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


CREATE TABLE Admin (
    id SERIAL PRIMARY KEY,
    admin_id TEXT REFERENCES Users ON DELETE CASCADE
);

CREATE TABLE Private_blogs (
    id SERIAL PRIMARY KEY,
    private_blog_id TEXT REFERENCES Blogs ON DELETE CASCADE,
    salasana TEXT
);
