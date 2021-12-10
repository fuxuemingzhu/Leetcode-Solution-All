
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/employee-importance/description/][1]


## 题目描述

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11
    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:

1. One employee has at most one direct leader and may have several subordinates.
2. The maximum number of employees won't exceed 2000.

## 题目大意

给的数据结构是[1, 5, [2, 3]]表示的是1号员工的重要性是5，有两个下属2和3。

输入一个员工的Id,求它自己和它所有的下属的重要性之和。

## 解题方法

### 方法一：DFS

题目意思是找出每个节点与其子节点的所有重要性之和。

为了快速查询每个节点的id与其对应，建立了map。

然后采用dfs遍历。当某个子节点不再有子节点的时候会自动终止该分支的遍历。

我觉得这个题应该背下来。

```python
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employee_dict = {employee.id : employee for employee in employees}
        def dfs(id):
            return employee_dict[id].importance + sum(dfs(id) for id in employee_dict[id].subordinates)
        return dfs(id)
```

---

二刷，换了一个写法，没有新定义dfs，而是直接使用了题目给的函数。效率竟然提高了不少。

```python
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {employee.id : employee for employee in employees}
        res = emap[id].importance
        for sub in emap[id].subordinates:
            res += self.getImportance(employees, sub)
        return res
```

## 日期

2018 年 1 月 17 日 
2018 年 11 月 10 日 —— 这么快就到双十一了？？

  [1]: https://leetcode.com/problems/employee-importance/description/
