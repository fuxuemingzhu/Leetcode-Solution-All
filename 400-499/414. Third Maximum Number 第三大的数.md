
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/third-maximum-number/description/


## 题目描述

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

    Input: [3, 2, 1]
    
    Output: 1
    
    Explanation: The third maximum is 1.

Example 2:

    Input: [1, 2]
    
    Output: 2
    
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

    Input: [2, 2, 3, 1]
    
    Output: 1

	Explanation: Note that the third maximum here means the third maximum distinct number.
	Both numbers with value 2 are both considered as second maximum.

## 题目大意

找出一个数组中第三大的数字，如果不存在的话，就返回最大数字。

## 解题方法

### 替换最大值数组

最基本的方法，找到最大值，然后每次把最大值移除，这样重复三次就得到了第三大的值。

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def setMax(nums):
            _max = max(nums)
            for i, num in enumerate(nums):
                if num == _max:
                    nums[i] = float('-inf')
            return _max
        max1 = setMax(nums)
        max2 = setMax(nums)
        max3 = setMax(nums)
        return max3 if max3 != float('-inf') else max(max1, max2)
```

### 使用set

用set去算，set的时间复杂度是O(n)。set的remove()方法可以去除某个值，不过每次只能去除一个。

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums_set) < 3:
            return max(nums_set)
        nums_set.remove(max(nums_set))
        nums_set.remove(max(nums_set))
        _max = max(nums_set)
        return _max
```

这个方法的C++版本如下：

```cpp
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s;
        for (int num : nums) {
            s.insert(num);
        }
        if (s.size() < 3) {
            return maxset(s);
        }
        s.erase(maxset(s));
        s.erase(maxset(s));
        return maxset(s);
    }
private:
    int maxset(set<int> &s) {
        int res = INT_MIN;
        for (int c : s) {
            res = max(res, c);
        }
        return res;
    }
};
```

原来C++也有求最大值函数叫做max_element()，参数是起始和结束位置，返回的是指针。

```cpp
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s;
        for (int num : nums) {
            s.insert(num);
        }
        if (s.size() < 3) return *max_element(s.begin(), s.end());
        s.erase(*max_element(s.begin(), s.end()));
        s.erase(*max_element(s.begin(), s.end()));
        return *max_element(s.begin(), s.end());
    }
};
```


### 三个变量

维护三个变量分别保存最大、次大、第三大的值，只需要遍历一次数组，找到这个数字和三个变量的大小关系，就能对应的更新对应的值。

为了去重，elif里面写了当前的Num要处于开区间内。

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s1 > s2 > s3
        s1, s2, s3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > s1:
                s1, s2, s3 = num, s1, s2
            elif num < s1 and num > s2:
                s2, s3 = num, s2
            elif num < s2 and num > s3:
                s3 = num
        return s3 if s3 != float('-inf') else s1
```

这个方法的C++写法如下，为什么需要使用long long 呢？因为当第三大的数字是INT_MIN的话，你如果把三个数字都初始化成了INT_MIN就没法判断了。


```cpp
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long long s1, s2, s3;
        s1 = s2 = s3 = LLONG_MIN;
        for (int num : nums) {
            if (num > s1) {
                s3 = s2;
                s2 = s1;
                s1 = num;
            } else if (num < s1 && num > s2) {
                s3 = s2;
                s2 = num;
            } else if (num < s2 && num > s3) {
                s3 = num;
            }
        }
        return s3 != LLONG_MIN ? s3 : s1;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 27 日 —— 最近的雾霾太可怕
