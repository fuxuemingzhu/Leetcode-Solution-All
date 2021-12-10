- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/max-consecutive-ones-ii/

## 题目描述

Given a binary array, find the maximum number of consecutive `1`s in this array if you can flip at most one `0`.

Example 1:

    Input: [1,0,1,1,0]
    Output: 4
    Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
        After flipping, the maximum number of consecutive 1s is 4.

Note:

1. The input array will only contain 0 and 1.
1. The length of input array is a positive integer and will not exceed 10,000

Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


## 题目大意

最多可以把数组中的一个0翻转成1，求能够成的最长连续1有多少。

## 解题方法

### 动态规划

我第一遍做这个题的时候，使用的是从左向右和从右向左两次遍历，找出每个0的左右两部分连续1的个数相加。这样也能过，但是有点麻烦。

比较好的解决方案是动态规划，定义两个变量left, right。

1. left的含义是：遇到了0，并翻转了该0时，包含该0的位置和其左侧连续的1的的长度。
2. right的含义是：从上次遇到0之后，累加得到的连续1的个数。

举例说明：

|1  |0  |1  |1  |0  |
|--|--|--| -- | -- |
|left start| left end|right start|right end, `i`|    |

维护两个变量：

1. 当遇到1时，用right保存已经遇到的连续的1（不含翻转0得到的1）。
1. 当遇到0时，把这个0翻转，更新left为right + 1（把位置的0翻转为1），更新right为0。

`left+right`的最大值即为所求。

C++代码如下：

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        const int N = nums.size();
        if (N == 0) return 0;
        int left = 0, right = 0;
        int res = 0;
        for (int i = 0; i < N; ++i) {
            if (nums[i] == 1) {
                right++;
            } else {
                left = right + 1;
                right = 0;
            }
            res = max(res, left + right);
        }
        return res;
    }
};
```

参考资料：https://www.cnblogs.com/grandyang/p/6376115.html

## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
