CREATE TABLE Person(
    id          int                   PRIMARY KEY,
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30),
    patronymic  varchar(30),
    birth_year  int,
    birth_month int,
    birth_day   int,
    mob_number  int
);
CREATE TABLE VK_acc(
    id          int         PRIMARY KEY,
    city        varchar(30),
    school      varchar(30),
    university  varchar(50),
    id_person   int         REFERENCES Person(id)
);
CREATE TABLE VK_net(
    id      int PRIMARY KEY,
    who     int REFERENCES VK_acc(id),
    on_whom int REFERENCES VK_acc(id)
);
CREATE TABLE VK_group(
    id int PRIMARY KEY
);
CREATE TABLE VK_group_TO_VK_acc(
    id          int PRIMARY KEY,
    id_VK_acc   int REFERENCES VK_acc(id),
    id_VK_group int REFERENCES VK_group(id)
);
CREATE TABLE Instagram_acc(
    id          int PRIMARY KEY,
    id_person   int REFERENCES Person(id)
);
CREATE TABLE Instagram_net(
    id      int PRIMARY KEY,
    who     int REFERENCES Instagram_acc(id),
    on_whom int REFERENCES Instagram_acc(id)
);
