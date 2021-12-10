作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/random-pick-with-weight/description/

## 题目描述：

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1. ``1 <= w.length <= 10000``
1. ``1 <= w[i] <= 10^5``
1. ``pickIndex`` will be called at most ``10000`` times.

**Example 1:**

    Input: 
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output: [null,0]

**Example 2:**

    Input: 
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output: [null,0,1,1,1,0]

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.


## 题目大意

这个题目不太好理解，是要求按照权重挑选索引。比如[1,99]中，有1%的概率挑选到索引0，有99%的概率挑选到索引1.

## 解题方法

这个题很巧妙，我是想不出来的。做法是把概率分布函数转化为累计概率分布函数。然后通过随机数，进行二分查找。

比如，输入是 `[1,2,3,4]` ，那么概率分布是 `[1/10, 2/10, 3/10, 4/10]`，累积概率分布是` [1/10, 3/10, 6/10, 10/10]` . 总和是 10。如果我们产生一个随机数，在 1~10 之中，然后判断这个数字在哪个区间中就能得到对应的索引。

对于输入 `[1,2,3,4]`，计算出来的 preSum 是 `[1,3,6,10]` ，然后随机选一个 `s`，然后查找 `s` 属于哪个区间，各区间的含义是：

    区间：		[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]
    preSum:  	1,	3,	6,	10
	返回值：		1,	2,	3,	4

相当于找比 s 大的 preSum 值的索引。

如果还不理解，那么就想一想这个 preSum 的间隔，是不是发现这个间隔对应了题目的输入？那么选随机数找 upper_bound 的时候那就不是把一个区间里的数字合并到了某个 preSum 值上，而且 preSum 是不是对应着输入？所以是不是就把这个某个区间内的随机数对应上了一个输入值？

总之，随机的数字在哪个区间当中，那么就返回这个区间对应的数字即可。

这个二分查找也可以好好学习一下。

代码如下：

```python
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.preSum[-1]
        rand = random.randint(0, total - 1)
        left, right = 0, len(self.preSum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if rand >= self.preSum[mid]:
                left = mid
            else:
                right = mid
        if rand < self.preSum[left]:
            return left
        return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

## 日期

2018 年 8 月 18 日 —— 天在下雨
