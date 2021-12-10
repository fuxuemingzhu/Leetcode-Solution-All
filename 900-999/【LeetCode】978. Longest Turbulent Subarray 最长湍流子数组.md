作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/longest-turbulent-subarray/


## 题目描述

A subarray ``A[i], A[i+1], ..., A[j]`` of ``A`` is said to be turbulent if and only if:

- For ``i <= k < j``, ``A[k] > A[k+1]`` when ``k`` is odd, and ``A[k] < A[k+1]`` when ``k`` is even;
- **OR**, for ``i <= k < j``, ``A[k] > A[k+1]`` when ``k`` is even, and ``A[k] < A[k+1]`` when ``k`` is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the **length** of a maximum size turbulent subarray of A.

Example 1:

    Input: [9,4,2,10,7,8,8,1,9]
    Output: 5
    Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

Example 2:

    Input: [4,8,12,16]
    Output: 2

Example 3:

    Input: [100]
    Output: 1
 
Note:

1. 1 <= A.length <= 40000
1. 0 <= A[i] <= 10^9

## 题目大意

如果相邻的两个数字的差在大于0和小于0这两种情况中互相翻转，那么说明这个子数组是符合要求的。求最长的符合要求的子数组。

## 解题方法

### 虫取法

虫取法就是前后指针交替前进的方式。

对于这个题来说，我们先固定左侧的指针left，然后把右侧指针right向右移动，我使用了isde来表示上一次的相邻数字的差的符号，每次把当前的相邻数字符号和上一次的进行判断。需要注意的是题目要求必须翻转，如果连续数字是相等的则不符合要求。

移动的时候需要注意是不是相邻数字的差交替的：

如果是交替的，那么更新现在的相邻数字差的符号并且更新最长子串的长度；

如果不是交替的，那么需要更新left指针，这里的不是交替有两个情况，一是相等，二是连续的递增或者相减。如果right指向的元素是连续两个相等的，那么left指向right当前的位置当做新的起点；如果是A[right - 2]，A[right - 1]，A[right]三者有序的情况，那么把left更新到right-1的位置，此时right不要向右移动，相当于把left = right - 1当做新的数组起始位置。

举个栗子：

[9,4,2,10,7,8,8,1,9]

9,4,2是单调递减的三个数字，此时应该把left移动到4的位置，right仍然指向2，开始新的遍历过程。

当来回翻转，right到了第二个8的时候，此时子数组是4,2,10,7,8,8，已经不满足翻转条件，此时把left指向right为第二个8的位置，然后开始新的遍历过程。


再举个栗子：

[1,1,1,1,1,1,1]

这样都是连续相等的数值，那么A[right] == A[right - 1]会一直成立，所以每次都把left更新到right的位置，则没有一个构成翻转的条件，res不更新。由此也可见，应该把满足要求的最小的子数组的长度res初始化为1.

c++代码如下：

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
        const int N = A.size();
        if (N == 1) return 1;
        int res = 1;
        int left = 0, right = 1;
        bool isde = false;
        while (right < N) {
            if (A[right] == A[right - 1]) {
                left = right;
                right++;
            } else if (right - left == 1 || (A[right] - A[right - 1] < 0 != isde)) {
                isde = A[right] - A[right - 1] < 0;
                res = max(res, right - left + 1);
                right ++;
            } else {
                left = right - 1;
            }
        }
        return res;
    }
};
```


## 日期

2019 年 1 月 20 日 —— 这次周赛有点简单


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
