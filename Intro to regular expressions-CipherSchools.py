'''
Regexp
select * from customers where Contactname regexp 'm';
^ - beginning
$ - ending
| - or
[] - matches any one in the brackets
select * from customers
where City regexp "^M" and city regexp "d$";
select * from customers
where city regexp "^a|ch|d$"
select * from customers
where city regexp "[a-h]e";
'''