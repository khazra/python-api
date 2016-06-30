create database python_api;
use python_api;

create table users(
    id int not null auto_increment,
    username varchar(100) not null,
    password varchar(100) not null,
    primary key (id)
);

insert into users values(null, 'admin', 'admin');
