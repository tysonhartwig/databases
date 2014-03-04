/* Delete the tables if they already exist */
drop table if exists Auctions;
drop table if exists Users;
drop table if exists Bids;
drop table if exists CurrentBid;
drop table if exists Category;
drop table if exists Temp;

/* Create the schema for our tables */
create table Auctions(itemID integer primary key, name text, 
             minBid decimal(10,2), startDate date, endDate date, 
             userID text, description text);
.separator <>
.import auctions.txt Auctions 
/* .import users.txt Temp 
.import bids.txt Bids 
create table Users(userID text primary key, rating integer, 
             locale text, country text);
create table Temp(userID text, rating integer, locale text, 
             country text);
create table Bids(itemID integer, userID text, bidDate date, 
             bid decimal(10,2));
create table CurrentBid(itemID integer primary key, numBids integer, 
             bid decimal(10,2));
create table Category(itemID integer, category text);*/

/* Bulk import from files */
/* 
.import current.txt CurrentBid 
.import category.txt Category 


insert into Users
select distinct *
from Temp
group by userID;

update Users 
set locale = null 
where locale = 'NULL';

update Users 
set country = null 
where country = 'NULL';
*/
update Auctions
set description = null 
where description = 'NULL';
