## 【LeetCode】386. Lexicographical Numbers 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/lexicographical-numbers/description/

## 题目描述：

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.



## 题目大意

给了一个数字n,找出1～n的所有数字的字典序排列。

## 解题方法

题目中说了输入可能是5百万，那么只能用O(N)的时间复杂度。

这个题的思路我是参考的[Lexicographical Numbers 字典顺序的数字][1]，不太好想。

1. 如果curr乘以10小于等于n，那么下个数字应该是curr末尾补0；
2. 如果curr已经到达了n，那么说明各位数字已经到头了，应该变化十位数字了，所以除以10，再加一。这时可能会出现恰好进位的情况，而字典序可能是从末尾没有0的数字开始的，所以要把末尾的0去掉。

比如``n=300``时，会有这个队列``1,10,100,101,102...198,199,2,20,200,201...299,3,30,300``

代码如下：

```python3
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cur = 1
        ans = []
        for i in range(n):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return ans
```

## 日期

2018 年 8 月 17 日 ———— 别人七夕，我在刷题。。


  [1]: http://www.cnblogs.com/grandyang/p/5798275.html