- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together/

## 题目描述

Given a binary array data, return the **minimum** number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:
    
    Input: [1,0,1,0,1]
    Output: 1
    Explanation: 
    There are 3 ways to group all 1's together:
    [1,1,1,0,0] using 1 swap.
    [0,1,1,1,0] using 2 swaps.
    [0,0,1,1,1] using 1 swap.
    The minimum is 1.

Example 2:

    Input: [0,0,0,1,0]
    Output: 0
    Explanation: 
    Since there is only one 1 in the array, no swaps needed.

Example 3:

    Input: [1,0,1,0,1,0,0,1,1,0,1]
    Output: 3
    Explanation: 
    One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

Note:

1 <= data.length <= 10^5
0 <= data[i] <= 1

## 题目大意

给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

## 解题方法

### 滑动窗口

1. 首先统计总的有N个1
2. 设置大小为N的滑动窗口，统计该滑动窗口中的1的个数最大值是K
3. 需要交换N - K次使得该滑动窗口内的0变成1

C++代码如下：

```cpp
class Solution {
public:
    int minSwaps(vector<int>& data) {
        int N = accumulate(data.begin(), data.end(), 0);
        int left = -N;
        int right = 0;
        int one_counts = 0;
        int K = 0;
        while (right < data.size()) {
            if (data[right] == 1) {
                one_counts ++;
            }
            if (left >= 0 && data[left] == 1) {
                one_counts --;
            }
            K = max(K, one_counts);
            left ++;
            right ++;
        }
        return N - K;
    }
};
```

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
