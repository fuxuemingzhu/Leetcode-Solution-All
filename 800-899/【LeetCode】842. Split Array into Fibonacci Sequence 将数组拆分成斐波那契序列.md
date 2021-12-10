
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

## 题目描述

Given a string S of digits, such as S = ``"123456579"``, we can split it into a Fibonacci-like sequence ``[123, 456, 579]``.

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

1. 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
1. F.length >= 3;
1. and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.


Example 1:

    Input: "123456579"
    Output: [123,456,579]

Example 2:

    Input: "11235813"
    Output: [1,1,2,3,5,8,13]

Example 3:

    Input: "112358130"
    Output: []
    Explanation: The task is impossible.

Example 4:

    Input: "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

    Input: "1101111"
    Output: [110, 1, 111]
    Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

1. 1 <= S.length <= 200
1. S contains only digits.

## 题目大意

给出了一个有0-9数字组成的纯数字字符串。判断能否组成所谓的费布拉奇数列。注意这个题注重点在不管你几位数字去划分，只要满足后面的数字等于前两个的和即可。最终要返回的是任何一个组合即可。

## 解题方法

按照Tag说就是快啊，这个题和[306. Additive Number][1]一个一模一样啊，306题是要返回True和False，这个是要求返回具体的一个例子。

因为只要判断能否构成即可，所以不需要res数组保存结果。回溯法仍然是对剩余的数字进行切片，看该部分切片能否满足条件。剪枝的方法是判断数组是否长度超过3，如果超过那么判断是否满足费布拉奇数列的规则。不超过3或者已经满足的条件下继续进行回溯切片。最后当所有的字符串被切片完毕，要判断下数组长度是否大于等于3，这是题目要求。

因为题目要求返回任意一个就好了，因此，只要找到一个满足条件的，那么就返回True，再结束循环就好了。所以整个题都是在306的基础上做出来的。

第一遍提交的时候出了个错，第一遍竟然没看出来：

    输入："539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    输出：[539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]

仔细一想，是最后的数字超过了2**31，python不会报错。。如果是c++或者java应该还是挺容易看出来的。


代码如下：

```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        self.dfs(S, [], res)
        return res
        
    def dfs(self, num_str, path, res):
        if len(path) >= 3 and  path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            res.extend(path)
            return True
        for i in range(len(num_str)):
            curr = num_str[:i+1]
            if (curr[0] == '0' and len(curr) != 1) or int(curr) >= 2**31:
                continue
            if self.dfs(num_str[i+1:], path + [int(curr)], res):
                return True
        return False
```

二刷使用C++代码如下：

```cpp
class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        vector<int> path;
        helper(S, path, 0);
        return path;
    }
    // [start, S.size())
    bool helper(string& num, vector<int>& path, int start) {
        if (start >= num.size() && path.size() >= 3)
            return true;
        for (int i = 1; start + i <= num.size(); i++) {
            if (num[start] == '0' && i > 1) break;
            long long subll = stoll(num.substr(start, i));
            if (subll > INT_MAX) 
                return false;
            if (path.size() >= 2 && subll > path[path.size() - 1] + path[path.size() - 2])
                return false;
            if (path.size() <= 1 || subll == path[path.size() - 1] + path[path.size() - 2]) {
                path.push_back((int)subll);
                if (helper(num, path, start + i)) {
                    return true;
                }
                path.pop_back();
            }
        }
        return false;
    }
};
```

## 日期

2018 年 6 月 12 日 —— 实验室上午放假2333刷题吧
2018 年 12 月 22 日 —— 今天冬至

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80661715
