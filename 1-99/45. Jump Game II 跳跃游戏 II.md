作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reach-a-number/description/


## 题目描述

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
    
    Input: [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.

## 题目大意

每次可以向后面跳跃的格子数等于当前的点数。求最少需要多少步就能调大最后的格子。


## 解题方法

### 贪心

这个题和[55. Jump Game][1]很像，都是求怎么能跳到最后的位置，只不过这个题加了一个条件，就是我们需要的最小的步数，使用的策略是贪心。

我们每次贪心的找在自己当前能到达的几个位置里面，跳到哪个位置的时候，在下一步能跳的最远。然后，我们当前步就跳到这个位置上去，所以我们在这一步的跳跃时，给下一步留下了最好的结果。

所以，使用一个cur表示当前步能到达的最远位置，使用pre表示上一次能到达的最远位置。所以，我们应该遍历在上一步的覆盖范围内，当前能跳的最远位置来更新cur。一个节省计算资源的方式是，保存以前已经检查了的位置为Pos，这样每次检查的范围是pos~pre。

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        cur = 0
        N = len(nums)
        count = 0
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count
```

C++版本的代码如下：


```cpp

class Solution {
public:
    int jump(vector<int>& nums) {
        int N = nums.size();
        int pos = 0;
        int count = 0;
        int pre = 0, cur = 0;
        while (cur < N - 1) {
            count ++;
            pre = cur;
            while (pos <= pre) {
                cur = max(cur, pos + nums[pos]);
                pos ++;
            }
        }
        return count;
    }
};
```

## 日期

2018 年 11 月 28 日 —— 听说楼下有传染病。。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83504437
