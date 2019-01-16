DROP DATABASE IF EXISTS twitter;
CREATE DATABASE IF NOT EXISTS twitter;
USE twitter;

DROP TABLE IF EXISTS contacts,

CREATE TABLE contacts (
    name     VARCHAR(40)         NOT NULL,
    url   VARCHAR(40)     NOT NULL,
    tweet_volume   VARCHAR(40)     NOT NULL);
