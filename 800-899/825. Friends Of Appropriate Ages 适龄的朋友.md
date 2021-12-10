作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/friends-of-appropriate-ages/description/


## 题目描述：

Some people will make friend requests. The list of their ages is given and ``ages[i]`` is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

- age[B] <= 0.5 * age[A] + 7
- age[B] > age[A]
- age[B] > 100 && age[A] < 100

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

    Input: [16,16]
    Output: 2
    Explanation: 2 people friend request each other.

Example 2:

    Input: [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

    Input: [20,30,100,110,120]
    Output: 
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1. 1 <= ages.length <= 20000.
1. 1 <= ages[i] <= 120.

## 题目大意

这个题让我们找出有多少个好友申请。好友申请不能成立的条件：

- age[B] <= 0.5 * age[A] + 7
- age[B] > age[A]
- age[B] > 100 && age[A] < 100

总结一下：A只能向年龄小于等于自己的人(B)申请，并且也不能太小，总之要满足``0.5 * age[A] + 7 < B <= A``.

第三个条件是第二个条件的子集，只要满足条件二一定满足条件三。

## 解题方法

把上面的约束条件理解清楚之后就很简单了。首先我们需要统计个数，然后肯定需要进行排序，然后遍历标记为A，查找满足他的申请条件的B有多少。

对于A,B他们之间有多少对申请？如果A!=B，那么A要向每个B进行申请；如果A==B，那么A要向和他年龄一样大的其他人申请。

时间复杂度是O(120 * N)，空间复杂度是O(120).

```python
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = collections.Counter(ages)
        ages = sorted(count.keys())
        N = len(ages)
        res = 0
        for A in ages:
            for B in range(int(0.5 * A) + 7 + 1, A + 1):
                res += count[A] * (count[B] - int(A == B))
        return res
```

## 日期

2018 年 10 月 19 日 —— 自古逢秋悲寂寥，我言秋日胜春朝
