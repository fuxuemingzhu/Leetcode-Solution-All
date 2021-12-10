
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

## 题目描述

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For ``num = 5`` you should return ``[0,1,1,2,1,2]``.

Follow up:

 - It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
 - Space complexity should be O(n).
 - Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## 题目大意

计算0<=x<=num的所有数字，二进制表示里面的1的个数。

## 解题方法

这个题用DP的方法。

分析规律：
```
   0000    0
-------------
   0001    1
-------------
   0010    1
   0011    2
-------------
   0100    1
   0101    2
   0110    2
   0111    3
-------------
   1000    1
   1001    2
   1010    2
   1011    3
   1100    2
   1101    3
   1110    3
   1111    4
```

把第i个数分成两种情况，如果i是偶数那么，它的二进制1的位数等于i/2中1的位数；如果i是奇数，那么，它的二进制1的位数等于i-1的二进制位数+1，又i-1是偶数，所以奇数i的二进制1的位数等于i/2中二进制1的位数+1. 

所以上面的这些可以很简单的表达成``answer[i] = answer[i >> 1] + (i & 1)``。

Python代码如下：

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i / 2] + i % 2
        return res
```

Java代码如下：

```java
public class Solution {
    public int[] countBits(int num) {
        int[] answer = new int[num+1];
        answer[0] = 0;
        for(int i = 1; i < answer.length; i++){
            answer[i] = answer[i >> 1] + (i & 1);
        }
        return answer;
    }
}
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for (int i = 1; i <= num; i ++) {
            res[i] = res[i / 2] + i % 2;
        }
        return res;
    }
};
```

## 日期

2017 年 4 月 25 日 
2018 年 12 月 4 日 —— 周二啦！

  [1]: https://leetcode.com/problems/counting-bits/#/description
