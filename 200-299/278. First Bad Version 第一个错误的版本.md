
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/first-bad-version/description/


## 题目描述


You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions ``[1, 2, ..., n]`` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool ``isBadVersion(version)`` which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

	Given n = 5, and version = 4 is the first bad version.
	
	call isBadVersion(3) -> false
	call isBadVersion(5) -> true
	call isBadVersion(4) -> true
	
	Then 4 is the first bad version. 

## 解题方法

### 二分查找

找出最开始错的版本。

其实就是二分查找，注意题目求的是版本号，而不是调用了多少次isBadVersion函数。

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
```

C++版本：

```cpp
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 0, right = n; //[left, right]
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 28 日 —— 心无旁骛
