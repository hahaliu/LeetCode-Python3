# ex2tron's blog:
# http://ex2tron.wang

# Write your MySQL query statement below
# 实用mysql中的outer join
select p.FirstName, p.LastName, a.City, a.State from Person p LEFT JOIN Address a on p.PersonId = a.PersonId
