# Write your MySQL query statement below
select firstName, lastName, city, state 
from Person P left outer join Address A
on P.personId=A.personId