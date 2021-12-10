
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/distribute-candies/#/description][1]


## 题目描述

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:

    Input: candies = [1,1,2,2,3,3]
    Output: 3
    Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies. 

Example 2:

    Input: candies = [1,1,2,3]
    Output: 2
    Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
    The sister has two different kinds of candies, the brother has only one kind of candies. 

Note:

 1. The length of the given array is in range [2, 10,000], and will be even.
 2. The number in given array is in range [-100,000, 100,000].

## 题目大意

题目的意思是把一堆数字平均分成两堆，其中的一堆的最大的种类个数为多少。


## 解题方法

### Java解法

第一感觉就是HashMap，统计每个数字出现的次数，然后统计就行，如果种类的数目多于总数字的半数，那么只能选半数的，否则不能平均分成两堆，否则就可以选择种类的个数做最多的分类个数。

```java
public class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> kinds = new HashSet<Integer>();
        for(int candy : candies){
            kinds.add(candy);
        }
        return Math.min(kinds.size(), candies.length / 2);
    }
}
```

### Python解法

如果蜡烛的种类够N//2种，那么可以给其中一堆N//2种，否则最多只能给蜡烛种类数个不同种类的蜡烛。

```python
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) // 2)
```

## 日期

2017 年 5 月 8 日 
2018 年 11 月 8 日 —— 项目进展缓慢

  [1]: https://leetcode.com/problems/distribute-candies/#/description
