作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/jump-game/description/


## 题目描述

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.



## 题目大意

每个位置上的数字代表了最多可以向右跳多少步，问能不能跳到最右边的位置。

## 解题方法

### 贪心

这个题的tag是贪心，贪心策略是我们每次都选取最优的策略，然后前面已经选好了的就不用管了。

这个题的贪心方法是，我们使用一个变量reach保存当前能到达的最后位置索引，那么在每个位置的时候判断这个位置能不能到达，即位置的索引大于了reach说明前面无论怎么走也走不到这个位置，就返回False好了。如果这个位置可以到达，那么要维护一下这个reach，更新策略是当前位置索引+这个数字代表的能向右走多少步，这个代表了到达当前位置的时候向右能到达的最远距离，在这个最远距离以内的任何位置都能到，因为每次跳的步数可以变小的。那么进行了这么一次循环以后，每个位置都判断为能到达，所以结果返回True就好了。

时间复杂度是O(N)，空间复杂度是O(1).

Python代码如下：

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True
```

C++代码如下：

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        const int M = nums.size();
        int reach = 0;
        for (int i = 0; i < M; ++i) {
            if (i > reach) return false;
            reach = max(nums[i] + i, reach);
        }
        return reach >= M - 1;
    }
};
```


[贪心和DP的比较][1]：

贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来最好的选择。也就是说，不从整体最优上加以考虑，他所作出的是在某种意义上的局部最优解。贪心算法和动态规划算法都是由局部最优导出全局最优，这里不得不比较下二者的区别。

贪心算法：
1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由``上一步``的最优解推导``下一步``的最优解，而上一步之前的最优解则不作保留；
2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解。

动态规划算法：
1.全局最优解中一定包含``某个局部最优解``，但不一定包含前一个局部最优解，因此需要记录之前的``所有最优解``；
2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解；
3.边界条件：即最简单的，可以直接得出的局部最优解。


参考资料：

[贪心和DP的比较][1]

## 日期

2018 年 10 月 28 日 —— 10月份最后一个周一
2019 年 1 月 11 日 —— 小光棍节？

  [1]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51636861
