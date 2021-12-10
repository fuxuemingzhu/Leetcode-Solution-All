
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

## 题目描述

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:
    
    Input:
    [1,2,3]
    
    Output:
    2
    
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

## 题目大意

题目短的一般都不难。题意是求把一个数组所有的数都弄相等最少需要多少步。一步可以是把某个数字增加1或者把某个数字减少1.

## 解题方法

### 方法一：排序

题意已经明确了，把数字调整相等的最小步数，一定是把大数变小，把小数变大，最后都达到其``中位数``（注意不是均值）。最小化全部/平均距离是中位数的一个显著的性质。

> Minimizing the total/average distance is just a prominent property of a median. 

可以举例来看：

    对于 [1, 5, 6]，其均值是4， 中位数是5.
    
    如果把所有的数字都移动到4，需要sum([3,1,2])=6步；
    
    如果把所有的数字都移动到5，需要sum([4,0,1])=5步。

我的理解是，移动到均值容易受到极端值的影响，而移动到中位数则不存在这个问题。具体的数学证明我不会。。当做定理记住好了。

代码：

```python
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) / 2]
        return sum([abs(num - median) for num in nums])
```

同样使用排序去做。新学会了``~i``运算。即求反。python支持负数索引，所以这个运算符很实用啊。

> The ~ operator is the same as in C++, so 0, 1, 2, ... get turned into -1, -2, -3, .... But C++ doesn’t support negative indexing. In Python, index -1 means the last element, index -2 means the next-to-last element, etc.

代码：

```python
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[~i] - nums[i] for i in range(len(nums) / 2)])
```

C++排序解法同样很简单。

排序找中位数的方法如下：

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        const int N = nums.size();
        int mid = nums[N / 2];
        int res = 0;
        for (int n : nums) {
            res += abs(n - mid);
        }
        return res;
    }
};
```

### 方法二：直接找中位数

C++有直接找中位数的函数nth_element()，参数设置成N/2就能把中位数的位置给固定了。这种做法可以不用排序了，速度也更快。

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        const int N = nums.size();
        int mi = N / 2;
        nth_element(nums.begin(), nums.begin() + mi, nums.end());
        int res = 0;
        for (int n : nums) {
            res += abs(n - nums[mi]);
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 4 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始
