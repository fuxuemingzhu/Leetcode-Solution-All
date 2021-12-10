
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


# 题目描述


给你一个二进制字符串 s 和一个整数 k 。

如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。


示例 1：

    输入：s = "00110110", k = 2
    输出：true
    解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。

示例 2：

    输入：s = "00110", k = 2
    输出：true

示例 3：

    输入：s = "0110", k = 1
    输出：true
    解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。

示例 4：

    输入：s = "0110", k = 2
    输出：false
    解释：长度为 2 的二进制串 "00" 没有出现在 s 中。

示例 5：

    输入：s = "0000000001011100", k = 4
    输出：false

提示：

1. `1 <= s.length <= 5 * 10^5`
1. `s` 中只含 0 和 1 。
1. `1 <= k <= 20`

# 题目大意

检查一个字符串是否包含所有长度为 K 的二进制子串。

# 解题方法

## 统计长度为 K 的子串个数

第一想法：把长度为 K 的所有二进制全部找出来，然后判断是否都在 s 中出现了。该方法的复杂度是 `O(2^K * len(s))`，大概是 `10 ^ 11`的级别，一定会超时。

所以反过来想， s 中长度为 K 的所有**不同的子串数目**是否有 2 ^ K 个呢。如果是的话，说明 s 中包含所有长度为 K 的二进制子串。

代码是 **set + 子字符串** 实现的。

时间复杂度是 `O(N*k)`，N 是 s 的长度，乘以 k 是截取获得子字符串的操作时间复杂度。 
空间复杂度是 `O(2 ^ k)`。

Python 代码如下：

```python
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        contains = set()
        N = len(s)
        for i in range(N - k + 1):
            contains.add(s[i:i + k])
        return len(contains) == (2 ** k)
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 31 日 —— 转眼 5 月过去了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png
