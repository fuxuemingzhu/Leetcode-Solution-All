

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/lemonade-change/description/

## 题目描述

At a lemonade stand, each lemonade costs ``$5``. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by ``bills``).

Each customer will only buy one lemonade and pay with either a ``$5``, ``$10``, or ``$20`` bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

 

Example 1:

    Input: [5,5,5,10,20]
    Output: true
    Explanation: 
    From the first 3 customers, we collect three $5 bills in order.
    From the fourth customer, we collect a $10 bill and give back a $5.
    From the fifth customer, we give a $10 bill and a $5 bill.
    Since all customers got correct change, we output true.

Example 2:

    Input: [5,5,10]
    Output: true

Example 3:

    Input: [10,10]
    Output: false

Example 4:

    Input: [5,5,10,10,20]
    Output: false
    Explanation: 
    From the first two customers in order, we collect two $5 bills.
    For the next two customers in order, we collect a $10 bill and give back a $5 bill.
    For the last customer, we can't give change of $15 back because we only have two $10 bills.
    Since not every customer received correct change, the answer is false.
 

Note:

- 0 <= bills.length <= 10000
- bills[i] will be either 5, 10, or 20.

## 题目大意

假如你是卖柠檬水的，现在要给顾客找零钱。一杯柠檬水的售价是5刀，顾客给的钱有5刀，10刀，20刀三种情况。刚开始的时候柜台没有零钱。每个顾客买一杯水。判断给出bills的情况下，能否完成卖柠檬水找零钱的任务。

## 解题方法

这个一看就是很明显的贪心算法，其实大家都知道，如果要找零钱的话，肯定先按照给大的零钱开始，不够再用小的零钱。

这个题目还是有点简单，题目中的零钱其实只有两种：5块和10块。

当给的是10块的时候，肯定找一张5块的就够了。
当给的是20块的时候，如果有10块的，先找10块的零钱，然后再找一张5块的。如果没有10块的，只能找三张5块的了。

代码如下：

```python3
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False
                else:
                    changes[10] += 1
                    changes[5] -= 1
            elif bill == 20:
                if changes[10] != 0:
                    if changes[5] == 0:
                        return False
                    else:
                        changes[5] -= 1
                        changes[10] -= 1
                else:
                    if changes[5] < 3:
                        return False
                    else:
                        changes[5] -= 3
        return True
```

## 日期

2018 年 7 月 4 日 ———— 夏天挺热的，记得吃饭，防止低血糖
2018 年 11 月 13 日 —— 时间有点快
