# ex2tron's blog:
# http://ex2tron.wang

# Write your MySQL query statement below
select distinct Salary as SecondHighestSalary from Employee order by Salary desc limit 1 offset 1

select(select distinct Salary from Employee order by Salary desc limit 1 offset 1) as SecondHighestSalary
