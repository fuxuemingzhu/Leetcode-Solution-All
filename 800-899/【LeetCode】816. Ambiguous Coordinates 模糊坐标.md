作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/ambiguous-coordinates/description/

## 题目描述：

We had some 2-dimensional coordinates, like ``"(1, 3)"`` or ``"(2, 0.5)"``.  Then, we removed all commas, decimal points, and spaces, and ended up with the string ``S``.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:

    Input: "(123)"
    Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:

    Input: "(00011)"
    Output:  ["(0.001, 1)", "(0, 0.011)"]
    Explanation: 
    0.0, 00, 0001 or 00.01 are not allowed.

Example 3:

    Input: "(0123)"
    Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:

    Input: "(100)"
    Output: [(10, 0)]
    Explanation: 
    1.0 is not allowed.

Note:

1. 4 <= S.length <= 12.
1. S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.

## 题目大意

输入是一个用括号包起来的数字组成的字符串，要对这个数字字符串进行分割，分成两个合理数字。合理数字的定义是整数或者小数。并且整数不能有前导0，小数不能有末尾0.

## 解题方法

这个应该是属于python玩字符串里面比较难的题了。

首先分成两部分还好办，直接用字符串切片即可。其次，难点在于判断分成合理的整数和小数。

1. 看能否组成合理整数：长度为1或者没有前导0
2. 看能否组成合理小数：把数字再次分割成整数部分和小数部分
 - 整数部分可以只有1位并且为0，否则不能有前导0
 - 小数部分结尾不能为0

最后的结果是分成的左右部分能够成的所有整数或者小数的组合。

```python
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        S = S[1:-1]
        for i in range(1, len(S)):
            left, right = S[:i], S[i:]
            left_list = self.get_number(left)
            right_list = self.get_number(right)
            if left_list and right_list:
                for left_number in left_list:
                    for right_number in right_list:
                        ans.append("(" + left_number + ", " + right_number + ")")
        return ans

    def get_number(self, num):
        decimal_list = []
        if len(num) == 1 or num[0] != '0':
            decimal_list.append(num)
        for i in range(1, len(num)):
            integer, fractor = num[:i], num[i:]
            print(integer, fractor)
            if (len(integer) > 1 and integer[0] == '0') or fractor[-1] == '0':
                continue
            decimal_list.append(integer + '.' + fractor)
        return decimal_list
```

## 日期

2018 年 6 月 13 日 ———— 天阴阴，地潮潮


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80661715
