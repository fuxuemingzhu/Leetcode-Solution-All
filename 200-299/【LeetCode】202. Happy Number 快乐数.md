
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)

Total Accepted: 36352 Total Submissions: 109782 Difficulty: Easy


## 题目描述


Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

	Input: 19
	Output: true
	Explanation: 
	1^2 + 9^2 = 82
	8^2 + 2^2 = 68
	6^2 + 8^2 = 100
	1^2 + 0^2 + 0^2 = 1

## 题目大意

判断一个数字是不是开心的数字，所谓开心数字，就是把它的每一位数字求平方和之后构成新数字，然后继续这个操作，看最后能不能到1.

## 解题方法

### 递归

使用递归的方法。

我自己的算法，10以下的Happy Number 只有 1和7 ，如果一个数计算到只有个位数时，如果计算到十位以下，这个数是1或7，返回true,否则，返回false。

```java
public static boolean isHappy(int n) {
	int ans = 0;
	if (n == 1 || n == 7) {
		return true;
	} else if (n > 1 && n < 10) {
		return false;
	} else {
		String numString = "" + n;
		char numChar[] = numString.toCharArray();
		for (char aNumChar : numChar) {
			ans += (aNumChar - '0') * (aNumChar - '0');
		}
	}
	return isHappy2(ans);
}
```

方法一改进：

没必要10以下的数字啊，1到7之间的都是false。直接判断数到1和7之间 就false就好了。

 7通过计算也回到1。
 
```java
public static boolean isHappy(int n) {
	int ans = 0;
	if (n == 1) {
		return true;
	} else if (n > 1 && n < 7) {
		return false;
	} else {
		String numString = "" + n;
		char numChar[] = numString.toCharArray();
		for (char aNumChar : numChar) {
			ans += (aNumChar - '0') * (aNumChar - '0');
		}
	}
	return isHappy5(ans);
}
```
### 迭代

同计算循环小数一样, 如果出现循环, 则无需继续计算,直接返回false即可. 

每次计算时，把已经计算数放到一个集合里面，在计算过程中如果出现循环（集合里已经有这个数字），返回false。否则一直计算。

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            nx = 0
            while n != 0:
                nx += (n % 10) ** 2
                n //= 10
            if nx == 1:
                return True
            n = nx
        return False
```


迭代的C++代码如下：

```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visited;
        visited.insert(n);
        while (n != 1) {
            int pre = n;
            int next = 0;
            while (pre) {
                next += (pre % 10) * (pre % 10);
                pre /= 10;
            }
            n = next;
            if (visited.count(n))
                break;
            visited.insert(n);
        }
        return n == 1;
    }
};
```

## 日期

2015/10/16 16:06:37 
2018 年 11 月 19 日 —— 周一又开始了
2019 年 1 月 14 日 —— 凛冬将至
