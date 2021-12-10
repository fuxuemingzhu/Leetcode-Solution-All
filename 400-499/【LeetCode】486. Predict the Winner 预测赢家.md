# 【LeetCode】486. Predict the Winner 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/predict-the-winner/description/

## 题目描述：

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

    Input: [1, 5, 2]
    Output: False
    Explanation: Initially, player 1 can choose between 1 and 2. 
    If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
    So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
    Hence, player 1 will never be the winner and you need to return False.

Example 2:

    Input: [1, 5, 233, 7]
    Output: True
    Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
    Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:

1. 1 <= length of the array <= 20.
1. Any scores in the given array are non-negative integers and will not exceed 10,000,000.
1. If the scores of both players are equal, then player 1 is still the winner.



## 题目大意

眼神越来越不好了，看了很多遍题目都看成了预测冬天-_-||

题目的意思很简单，两个玩家可以轮流的从一个数组前面和后面拿数字，每次只能拿一个，被拿走的不能再拿了，最后判断先拿的那个玩家能不能赢。

## 解题方法

这个题要感谢左程云的讲解，使用两个函数代表先发和后发的情况。如果先发，那么应该返回的是拿走前面的数字或者拿走后面的数字能拿到的结果的最大值。但是如果后发，那么应该返回的是前面不拿和后面不拿的最小值。

直接暴力递归会超时，使用记忆化搜索就能通过了。因为使用的python2，除法默认是地板除，这就是我第一次提交失败的原因，这种情况使用浮点数除法就没问题了。

题目和[877. Stone Game][1]做法一样的。

官方解答写了各种方法的对比，包括DP，值得一看：https://leetcode.com/articles/predict-the-winner/

代码如下：

```python
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        self.f_map, self.s_map = dict(), dict()
        player1 = self.f(nums, 0, len(nums)-1, self.f_map)
        print(player1)
        return player1 >= _sum / 2.0
        
    def f(self, nums, start, end, f_map):
        if start == end:
            return nums[start]
        if (start, end) not in f_map:
            f_val = max(nums[start] + self.s(nums, start+1, end, self.s_map), nums[end] + self.s(nums, start, end-1, self.s_map))
            f_map[(start, end)] = f_val
        return f_map[(start, end)]
        
    def s(self, nums, start, end, s_map):
        if start == end:
            return 0
        if (start, end) not in s_map:
            s_val = min(self.f(nums, start+1, end, self.f_map), self.f(nums, start, end-1, self.f_map))
            s_map[(start, end)] = s_val
        return s_map[(start, end)]
```

上面的代码写复杂了，可以简化成下面这样：

```python
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        self.f_map, self.s_map = dict(), dict()
        player1 = self.f(nums, 0, len(nums)-1)
        return player1 >= _sum / 2.0
        
    def f(self, nums, start, end):
        if start == end:
            return nums[start]
        if (start, end) not in self.f_map:
            f_val = max(nums[start] + self.s(nums, start+1, end), nums[end] + self.s(nums, start, end-1))
            self.f_map[(start, end)] = f_val
        return self.f_map[(start, end)]
        
    def s(self, nums, start, end):
        if start == end:
            return 0
        if (start, end) not in self.s_map:
            s_val = min(self.f(nums, start+1, end), self.f(nums, start, end-1))
            self.s_map[(start, end)] = s_val
        return self.s_map[(start, end)]
```

方法二：

DP，未完待续。

参考资料：


## 日期

2018 年 9 月 8 日 ———— 美好的周末，从刷题开始


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82390672