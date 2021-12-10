
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/total-hamming-distance/description/

## 题目描述

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

    Example:
    Input: 4, 14, 2
    
    Output: 6
    
    Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
    showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:

1. Elements of the given array are in the range of 0 to 10^9
1. Length of the array will not exceed 10^4.

## 题目大意

计算数组中所有数字之间的汉明距离。

## 解题方法

### 位运算

汉明距离可以通过异或操作去算。

数组长度会达到10^4， 暴力解法不可取。

思路：计算数组中每个数的二进制每一位中为1的个数和为0的个数，两者相乘即为总的不同的个数。

巧妙地把数组中两两数字的比较变化成了32位的二进制数字的比较。时间复杂度O(n)。

参考：http://www.cnblogs.com/grandyang/p/6208062.html

找规律：

>     4:     0 1 0 0
>     
>     14:    1 1 1 0
>     
>     2:     0 0 1 0
>     
>     1:     0 0 0 1
> 
> 我们先看最后一列，有三个0和一个1，那么它们之间相互的汉明距离就是3，即1和其他三个0分别的距离累加，然后在看第三列，累加汉明距离为4，因为每个1都会跟两个0产生两个汉明距离，同理第二列也是4，第一列是3。我们仔细观察累计汉明距离和0跟1的个数，我们可以发现其实就是0的个数乘以1的个数，发现了这个重要的规律，那么整道题就迎刃而解了，只要统计出每一位的1的个数即可。

Python代码：

```python
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for pos in range(32):
            bitCount = 0
            for i in range(len(nums)):
                bitCount += (nums[i] >> pos) & 1
            res += bitCount * (len(nums) - bitCount)
        return res
```

二刷的时候选择C++，这次一眼就看出这个题的套路了：把每个位的1和0进行统计，这个位能够成的不同 = 1的个数×0的个数。累加每一位的不同即可。

```cpp
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            int count0 = 0, count1 = 0;
            int mask = 1 << i;
            for (int n : nums) {
                if (n & mask) {
                    ++count1;
                } else {
                    ++count0;
                }
            }
            res += count0 * count1;
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 9 日 
2019 年 2 月 26 日 —— 二月就要完了
