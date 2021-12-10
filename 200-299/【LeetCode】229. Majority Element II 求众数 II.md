作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/majority-element-ii/description/

## 题目描述

Given an integer array of size n, find all elements that appear more than ``⌊ n/3 ⌋`` times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

    Input: [3,2,3]
    Output: [3]

Example 2:

    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]

## 题目大意

找出一个数组中出现次数超过``⌊ n/3 ⌋``次的所有数字。

## 解题方法

### hashmap统计次数

虽然不符合题目的要求，但是一般情况下，对空间复杂度要求的题目都不用管它的空间要求。这样很快就能写出来。

时间复杂度是O(N)，空间复杂度是O(N)。

Python代码如下：

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > N / 3:
                res.append(n)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        const int N = nums.size();
        unordered_map<int, int> count;
        for (int n : nums)
            ++count[n];
        vector<int> res;
        for (auto& c : count) {
            if (c.second > N / 3) {
                res.push_back(c.first);
            }
        }
        return res;
    }
};
```

### 摩尔投票法 Moore Voting

题目要求的是线性时间和常量的空间，和[169. Majority Element][1]基本一样的。169题使用一次遍历就找出了超过出现次数超过一半的数字。这个题需要在这个基础上更进一步。首先我们肯定知道数组中出现次数超过``⌊ n/3 ⌋``次的最多有两个！因为如果3个的话，这三个数字的总次数 > 3×``⌊ n/3 ⌋`` = n，不可能的。所以我们对这个题的做法同样使用摩尔投票法，先使用两个变量分别保存次数最多和次多的就可以了。然后我们还需要再过一遍数组，判断次数最多和次多的是不是超过了``⌊ n/3 ⌋``次，把超过的数字返回就行了。

踩到的坑：

1. 在第一个for循环中，必须先判断是不是已经和已有的相等，如果不满足的情况下才能判断是不是次数为0。比如题目中给的例子``[1,1,1,3,3,2,2,2]``，如果先判断cm和cn的次数是不是0，那么会把m和n分别都设置成了1。而我们的目的是m和n分别代表两个不同的数字，所以应该先做是不是和已有的数字相等的判断。
2. 统计次数的时候需要用if 和else if，不能两个if。这个是因为我们把m和n都初始化成了0，对于``[0,0,0]``这个测试用例，如果两个if会导致结果是``[0,0]``。

时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        m = n = cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
            elif cm == 0:
                m = num
                cm = 1
            elif cn == 0:
                n = num
                cn = 1
            else:
                cm -= 1
                cn -= 1
        cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
        res = []
        if cm > N / 3:
            res.append(m)
        if cn > N / 3:
            res.append(n)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int m = 0, n = 0, cm = 0, cn = 0;
        for (int i : nums) {
            if (m == i) {
                ++cm;
            } else if (n == i) {
                ++cn;
            } else if (cm == 0) {
                m = i;
                cm = 1;
            } else if (cn == 0) {
                n = i;
                cn = 1;
            } else {
                --cm;
                --cn;
            }
        }
        cm = cn = 0;
        for (int i : nums) {
            if (i == m)
                ++cm;
            else if (i == n)
                ++cn;
        }
        vector<int> res;
        const int N = nums.size();
        if (cm > N / 3)
            res.push_back(m);
        if (cn > N / 3)
            res.push_back(n);
        return res;
    }
};
```

## 相似题目

[169. Majority Element][1]

## 参考资料

http://www.cnblogs.com/grandyang/p/4606822.html

## 日期

2018 年 10 月 29 日 —— 美好的一周又开始了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51288749
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/83444553
  [3]: https://mp.weixin.qq.com/s/ILhJ-yahxzXCGrBCES1P0A
