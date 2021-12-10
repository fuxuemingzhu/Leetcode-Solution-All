# 【LeetCode】738. Monotone Increasing Digits 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/monotone-increasing-digits/description/

## 题目描述：

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:

    Input: N = 10
    Output: 9

Example 2:

    Input: N = 1234
    Output: 1234

Example 3:

    Input: N = 332
    Output: 299

Note: N is an integer in the range [0, 10^9].

## 题目大意

找出一个比这个数字小的，每位数字都是递增的最大数字。

## 解题方法

把题目给出的数字拆分成数组进行理解。如果这么理解之后，那我们就是要找到一个最大的递增数组。

做的方法是找出第一个降序的位置，有两种情况：

case 1:
对于 14267 , 第一个出现下降的位置是4，所以把4变成3，把4后面的数字全部改成9.得到13999；

case 2:
对于1444267, 第一个降序的位置是最后一个4，如果只把最后一个4按照case1处理，那么得到的是1443999，仍然不满足题意。所以需要找到第一个位置的4，然后做case1操作，这样得到的是1399999。

写代码的时候我是逆序过来做的，然后我犯了一个错误，写成了num[i] > num[i - 1] or (ind != -1 and num[i] == num[i - 1])。为什么不能是num[i] == num[i - 1]呢？因为这样会找到最后的一个相等的位置，而我们只需要找到最先出现相等的位置即可。

时间复杂度是O(n)，空间复杂度是O(n).

代码如下：

```python
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10: return N
        num = [int(n) for n in str(N)[::-1]]
        n = len(num)
        ind = -1
        for i in range(1, n):
            if num[i] > num[i - 1] or (ind != -1 and num[i] == num[ind]):
                ind = i
        if ind == -1:
            return N
        res = '9' * ind + str(num[ind] - 1) + "".join(map(str, num[ind + 1:]))
        return int(res[::-1])
```

如果不使用逆序，也可以做：

```python3
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10: return N
        num = [int(n) for n in str(N)]
        n = len(num)
        ind = n - 1
        for i in range(n - 2, -1, -1):
            if num[i] > num[i + 1] or (ind != n - 1 and num[i] == num[ind]):
                ind = i
        if ind == n - 1:
            return N
        num[ind] -= 1
        for i in range(ind + 1, n):
            num[i] = 9
        return int("".join(map(str, num)))
```

参考资料：

https://leetcode.com/problems/monotone-increasing-digits/discuss/109794/Simple-Python-solution-w-Explanation

## 日期

2018 年 9 月 16 日 ———— 天朗气清，惠风和畅