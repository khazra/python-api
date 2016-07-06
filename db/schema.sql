create database python_api;
use python_api;

create table users(
    id int not null auto_increment,
    username varchar(100) not null,
    password varchar(100) not null,
    primary key (id)
);

insert into users values(null, 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
