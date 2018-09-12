# Write your MySQL query statement below

# 别人的代码：使用group by
# http://www.runoob.com/mysql/mysql-group-by-statement.html
select `Email` from `Person` group by `Email` having count(`Email`)>=2;