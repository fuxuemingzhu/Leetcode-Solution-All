
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

## 题目描述

Given a non-empty array of numbers, ``a0, a1, a2, … , an-1``, where ``0 ≤ ai < 2^31``.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:
    
    Input: [3, 10, 5, 25, 2, 8]
    
    Output: 28
    
    Explanation: The maximum result is 5 ^ 25 = 28.



## 解题方法

### 依次遍历每一位

这个题不是很会，不过学到了异或操作的一个重要性质：a^b = c, 则有 a^c = b，且 b^c = a;

因此如果相求最大的c，可以把c设成1，看b存在不存在给定的数组当中。

下面的内容来自：https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/  这个文章很好，讲的很详细大体能明白。

> 我们还需要用上一个异或的特性，假设a和b产生了最终的答案max，即a ^ b = x，那么根据异或的特性，a ^ x = b。同理，a和b的最高位（前n位）也有相同的性质。
>      先以最高位为例子，我们可以把所有的数字的最高位放到一个HashSet里面，然后使用1与set里面的所有数字进行异或，如果得出的结果仍然在set里面，那么最终结果的最高位必然为1，否则为0。也即，先假定结果为1，然后与set中所有数字异或，假定a与1异或得到结果b（a ^ 1 = b），而b仍然在set里面，那么说明set中有两个数字异或能得到1（a ^ b = 1）。否则，set中没有两个数字能够异或得到1，那么最终结果的最高位为1的假设失败，说明最终结果的最高位为0。以此类推可以得到第二位、第三位。。。的数字。
>      再做一下推广，我们将所有数字的前N位放到一个HashSet里面，然后使用之前N-1位得到的最大值前缀prefix与set里面的所有数字进行异或，如果得出的结果仍然在set中，那么第N位必然为1，否则为0。
>      举个例子，给定数组[14, 11, 7, 2]，二进制表示分别为[1110, 1011, 0111, 0010]。题目说了，数字最长不会超过32位，所以应从i = 31开始，但是所有数字中最多位4位数，简单起见，我直接从最高位i=3开始

```
1. i = 3, set = {1000, 0000} => max = 1000
2. i = 2, set = {1100, 1000, 0100, 0000} => max = 1100
3. i = 1, set = {1110, 1010, 0110, 0010} => max = 1100
4. i = 0, set = {1110, 1011, 0111, 0010} => max = 1100
```

Python代码：

```python
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        for x in range(32)[::-1]:
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])
            temp = ans | 1 << x
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    ans = temp
                    break
        return ans
```

C++代码：

```cpp
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int res = 0;
        int mask = 0;
        unordered_set<int> s;
        for (int i = 31; i >= 0; i--) {
            s.clear();
            mask |= 1 << i;
            for (int num : nums) {
                s.insert(num & mask);
            }
            int tmp = res | (1 << i);
            for (int pre : s) {
                if (s.count(tmp ^ pre)) {
                    res = tmp;
                    break;
                }
            }
        }
        return res;
    }
};
```

### 前缀树

使用Trie也能做，但是我还没有想明白。。

## 日期

2018 年 3 月 7 日 
2018 年 12 月 19 日 —— 感冒了，好难受
