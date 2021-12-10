# 【LeetCode】649. Dota2 Senate 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/dota2-senate/description/

## 题目描述：

In the world of Dota2, there are two parties: the ``Radiant`` and the ``Dire``.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

1. ``Ban one senator's right``: 
A senator can make another senator lose all his rights in this and all the following rounds.

2. ``Announce the victory``: 
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
Given a string representing each senator's party belonging. The character ``'R'`` and ``'D'`` represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be ``Radiant`` or ``Dire``.

Example 1:

    Input: "RD"
    Output: "Radiant"
    Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
    And the second senator can't exercise any rights any more since his right has been banned. 
    And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:

    Input: "RDD"
    Output: "Dire"
    Explanation: 
    The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
    And the second senator can't exercise any rights anymore since his right has been banned. 
    And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
    And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Note:

1. The length of the given string will in the range [1, 10,000].

## 题目大意

模拟Dota2参议院的获胜规则。题目比较长，简言之就是，有两个角色R和D，每个角色每轮投票都可以ban掉另外一个角色，这个操作一直做下去，直到最后能发言的只是一种角色，那么这类角色就赢了。注意哈，已经Ban掉的，不能投票了。

## 解题方法

看到长度范围是10000，估计只能用时间复杂度O(N)的算法了，但是没想到遍历一遍能怎么做，所以看了别人的方法，还真是模拟这个过程，直至获胜为止。

方法其实还是很简单的，模拟这个过程使用的是两个队列的贪心算法，这个方法是每次只杀掉下一个要发言的对方的参议员。即先把每个角色出现的位置都分别进入各自的队列，然后两个队列都从头pop出来，然后比较一下谁能活下来，然后放到这个队列的最后去。用了一个``+n``的技巧，来说明是这轮已经结束的，给下轮作比较。这个步骤比较重要，如果不``+n``那么这个元素相等于在这一轮投票中一直投票。

这个时间复杂度不好分析，但假设R和D的数量大致相等的话，那么一轮过后，基本剩下的个数就不多了，所以平均的时间复杂度是O(N)，空间复杂度是O(N).

代码如下：

```python
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        q_r, q_d = collections.deque(), collections.deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == "R":
                q_r.append(i)
            else:
                q_d.append(i)
        while q_r and q_d:
            r = q_r.popleft()
            d = q_d.popleft()
            if r < d:
                q_r.append(r + n)
            else:
                q_d.append(d + n)
        return "Radiant" if q_r else "Dire"
```

参考资料：

https://leetcode.com/problems/dota2-senate/discuss/105858/JavaC++-Very-simple-greedy-solution-with-explanation

## 日期

2018 年 9 月 27 日 —— 国庆9天长假就要开始了！
