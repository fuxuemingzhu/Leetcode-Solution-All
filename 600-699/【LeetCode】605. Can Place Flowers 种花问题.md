
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/can-place-flowers/description/


## 题目描述

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

Example 2:

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Note:

1. The input array won't violate no-adjacent-flowers rule.
1. The input array size is in the range of [1, 20000].
1. n is a non-negative integer which won't exceed the input array size.


## 解题方法

### 贪婪算法

这个题做的方式很蠢，就是一次遍历，看每个位置能不能种花，如果可以就种上，否则就判断下一个节点。

不能种花的条件是：

1. 已经有花
2. 当``i>0``时，右边有花
3. 当``i<len-1``时，左边有花

注意两点：

1. 遍历的时候如果该位置能种花，则种上，否则会影响下一个位置的判断；
2. 最后的条件是``n<=0``，即能种花的位置比给出的n多。

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, num in enumerate(flowerbed):
            if num == 1: continue
            if i > 0 and flowerbed[i - 1] == 1: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1: continue
            flowerbed[i] = 1
            n -= 1
        return n <= 0
```

二刷，做法思路一样：有连续的三个0的话，中间的这个位置种上一朵花。

python代码：

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        N = len(flowerbed)
        res = 0
        for i in range(1, N - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                res += 1
                flowerbed[i] = 1
        return res >= n
```

C++代码如下：

```cpp
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);
        int N = flowerbed.size();
        int res = 0;
        for (int i = 1; i < N - 1; ++i) {
            if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                ++res;
                flowerbed[i] = 1;
            }
        }
        return res >= n;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 26 日 —— 11月最后一周！
