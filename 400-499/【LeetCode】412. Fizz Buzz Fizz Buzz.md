
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

[https://leetcode.com/problems/fizz-buzz/][1]

 - Total Accepted: 31093
 - Total Submissions: 53272
 - Difficulty: Easy

##Question

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output ``“Fizz”`` instead of the number and for the multiples of five output ``“Buzz”``. For numbers which are multiples of both three and five output ``“FizzBuzz”``.

Example:

	n = 15,
	
	Return:
	[
	    "1",
	    "2",
	    "Fizz",
	    "4",
	    "Buzz",
	    "Fizz",
	    "7",
	    "8",
	    "Fizz",
	    "Buzz",
	    "11",
	    "Fizz",
	    "13",
	    "14",
	    "FizzBuzz"
	]

## 题目大意

从1~n这么多数字中中，如果某个位置是3的倍数，把这个数字换成Fizz，如果是5的倍数，把这个数字换成Buzz，如果既是3的倍数又是5的倍数，换成FizzBuzz.

## 解题方法

### 方法一：遍历判断

思路很简单，判断是否能特定位置的数字是否能被3和5整除即可。

```python
class Solution(object):
    def fizzBuzz(self, n):
    	"""
    	:type n: int
    	:rtype: List[str]
    	"""
    	ListReturn = [];
    	x = 1
    	while x <= n:
    		if x % 3 == 0 and x % 5 == 0:
    			ListReturn.append("FizzBuzz")
    		elif x % 3 == 0:
    			ListReturn.append("Fizz")
    		elif x % 5 == 0:
    			ListReturn.append("Buzz")
    		else:
    			ListReturn.append(str(x))
    		x += 1
    	return ListReturn
```

AC:69 ms

感觉好繁琐，python应该可以很简单。所以参考了别人的跟进如下。

```python
class Solution(object):
    def fizzBuzz(self, n):
    	"""
    	:type n: int
    	:rtype: List[str]
    	"""
    	return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) 
    	+ str(i) * (i % 3 != 0 and i % 5 != 0)			
    	for i in range(1, n + 1)]
```
AC:96 ms

嗯。这个看起来舒服多了。

### 方法二：字符串相加

如果是5的倍数，就把结果字符串后面加上Buzz即可。这里不能使用elif的判断，因为是15既是3的倍数又是5的倍数，所以需要加上两个字符串。

```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            pos = ""
            if i % 3 == 0:
                pos += "Fizz"
            if i % 5 == 0:
                pos += "Buzz"
            if not pos:
                pos = str(i)
            res.append(pos)
        return res
```

### 方法三：字典

把方法二的判断进行了优化，使用字典保存3和5的字符串的结果对应。

```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        strmap = {3 : "Fizz", 5 : "Buzz"}
        for i in range(1, n + 1):
            pos = ""
            for j in [3, 5]:
                if i % j == 0:
                    pos += strmap[j]
            if not pos:
                pos = str(i)
            res.append(pos)
        return res
```


## 日期

2017 年 1 月 2 日 
2018 年 11 月 8 日 —— 项目进展缓慢

  [1]: https://leetcode.com/problems/fizz-buzz/
