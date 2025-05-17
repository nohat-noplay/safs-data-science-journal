![[Pasted image 20240815105125.png]]
Use `varchar(*integer*)` instead of `char` to store a string 
`drop table TEST` to delete entire table
`alter table TEST drop *Zipcode*` to drop column/variable
`update` age `set` age = age + 1 `where` age > 30

Benefits of Relational DB: + avoid duplications + queries across multiple files is slow
Using `AND` with `OR`:
`WHERE (year = '2017' AND semester = 'Fall') OR (year = '2018' AND semester = 'Spring');`