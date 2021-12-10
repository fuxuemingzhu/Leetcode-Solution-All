# 【LeetCode】911. Online Election 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/online-election/description/

## 题目描述：

In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

    Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
    Output: [null,0,1,1,0,0,1]
    Explanation: 
    At time 3, the votes are [0], and 0 is leading.
    At time 12, the votes are [0,1,1], and 1 is leading.
    At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
    This continues for 3 more queries at time 15, 24, and 8.
     

Note:

1. 1 <= persons.length = times.length <= 5000
1. 0 <= persons[i] <= persons.length
1. times is a strictly increasing array with all elements in [0, 10^9].
1. TopVotedCandidate.q is called at most 10000 times per test case.
1. TopVotedCandidate.q(int t) is always called with t >= times[0].


## 题目大意

题目意思是在一个竞选中，在times[i]时刻会投票给persons[i]，然后求t时刻的得票最多的候选人。注意，如果出现票数相等的情况，选择获得最新投票的那个。

## 解题方法

这个题很容易想到实现一个保存了当前出现次数最多数字的栈。类似的题目还有实现一个保存最小值的栈。

如果把这个题目这么抽象出来之后，会发现，只需要再增加一个二分查找代码就好了。

所以这个题使用List保存每个时间点对应的当前的获得票数最多的person。在q(t)中，使用二分查找到第一个小于t的times位置，然后返回这个位置对应的时间得票最多的person即可。

平均的时间复杂度是O(logn)，空间复杂度是O(N).

代码如下：

```python
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p, t in zip(persons, times):
            count[p] = count.get(p, 0) + 1
            if count.get(lead, 0) <= count[p]:
                lead = p
            self.leads.append(lead)
            
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        l, r = 0, len(self.times) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid] == t:
                return self.leads[mid]
            elif self.times[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return self.leads[l - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

参考资料：

https://leetcode.com/problems/online-election/discuss/173382/C++JavaPython-Binary-Search-in-Times

## 日期

2018 年 9 月 24 日 —— 祝大家中秋节快乐
