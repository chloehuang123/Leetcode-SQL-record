"""
Input: 
Customers table:
+-------------+------+---------+
| customer_id | year | revenue |
+-------------+------+---------+
| 1           | 2018 | 50      |
| 1           | 2021 | 30      |
| 1           | 2020 | 70      |
| 2           | 2021 | -50     |
| 3           | 2018 | 10      |
| 3           | 2016 | 50      |
| 4           | 2021 | 20      |
+-------------+------+---------+
Output: 
+-------------+
| customer_id |
+-------------+
| 1           |
| 4           |
+-------------+
"""



# Write your MySQL query statement below

select customer_id 
from Customers
where year = 2021 and revenue > 0
