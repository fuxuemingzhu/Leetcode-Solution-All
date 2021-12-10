作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


[LeetCode]

题目地址：[https://leetcode.com/problems/add-digits/](https://leetcode.com/problems/add-digits/)

Total Accepted: 33351 Total Submissions: 71187 Difficulty: Easy


## 题目描述


Given a non-negative integer ``num``, repeatedly add all its digits until the result has only one digit.

Example:

	Input: 38
	Output: 2 
	Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
	             Since 2 has only one digit, return it.

Follow up:

- Could you do it without any loop/recursion in O(1) runtime?

## 题目大意

如果一个数字不是个位数，那么就一直把它的各个位上的数字加在一起形成新的这个数字，然后继续这个操作。问最后的结果是多少。

## 解题方法

### 方法一：递归

直接模拟题目的操作，一直进行这个操作直至只剩下个数数字。所以是两个循环，第一个循环是判断是不是只剩下个位数字，第二个循环是把每位数字加在一起，形成新的数字。

时间复杂度是O(1)，空间复杂度是O(1)。因为整数最多32位，所以循环的次数上限是确定的。

Python代码如下：

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num:
                temp += num % 10
                num /= 10
            num = temp
        return num
```


### 方法二：减1模9

另一个方法比较简单，可以举例说明一下。假设输入的数字是一个5位数字num，则num的各位分别为a、b、c、d、e。

有如下关系：num = a * 10000 + b * 1000 + c * 100 + d * 10 + e

即：num = (a + b + c + d + e) + (a * 9999 + b * 999 + c * 99 + d * 9)

因为 a * 9999 + b * 999 + c * 99 + d * 9 一定可以被9整除，因此num模除9的结果与 a + b + c + d + e 模除9的结果是一样的。

对数字 a + b + c + d + e 反复执行同类操作，最后的结果就是一个 1-9 的数字加上一串数字，最左边的数字是 1-9 之间的，右侧的数字永远都是可以被9整除的。

这道题最后的目标，就是不断将各位相加，相加到最后，当结果小于10时返回。因为最后结果在1-9之间，得到9之后将不会再对各位进行相加，因此不会出现结果为0的情况。因为 (x + y) % z = (x % z + y % z) % z，又因为 x % z % z = x % z，因此结果为 (num - 1) % 9 + 1，只模除9一次，并将模除后的结果加一返回。

```java
/**
 * 给定整数不断将它的各位相加，直到相加的结果小于10，返回结果
 * @param num
 * @return
 */
public int addDigits(int num) {
    return (num - 1) % 9 + 1;
}
```

二刷的python写法如下：

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
```

### 方法三：直接模9

根据方法二的启发。把这个数直接取9的模，余数就是这个答案。

但是，在实际运行中发现，如果这个数是9的倍数，那么，计算结果为0，而实际答案为9.故加上对是否为9的倍数的判断。

同时，如果输入为0，也要进行判断。

```java
/**
 * 给定整数不断将它的各位相加，直到相加的结果小于10，返回结果
 *
 * @param num
 * @return
 */
public int addDigits4(int num) {
	return (num != 0 && num % 9 == 0) ? 9 : num % 9;
}
```

## 日期

2015/10/15 23:50:44 
2018 年 11 月 10 日 —— 这么快就到双十一了？？
