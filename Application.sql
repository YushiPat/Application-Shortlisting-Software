create database Application;
use Application;
show databases;

create table Resumemain(Fullname char(40),
 DOB char(40),
 Nationality char(40),
 School char(40),
 Dept char(60),
 SAT int,
 SATSubject int,
 Gender char(10),
 Overall int,
 ClassRank int);
desc resumemain;
select * from resumemain;
drop database Application;