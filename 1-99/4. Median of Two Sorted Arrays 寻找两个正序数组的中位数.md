
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：数组，中位数，题解，leetcode, 力扣，python, c++, java

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/median-of-two-sorted-arrays/

## 题目描述

There are two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively.

Find the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.

You may assume `nums1` and `nums2` cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5

## 题目大意

找两个各自有序数组的中位数。

## 解题方法

### 二分查找

题目给了一个很强的提示：O(log(m + n))的时间复杂度，基本确定了要使用二分查找。

说实话，想了很久不知道怎么解决，最后参考的是[花花酱][1]和[另外一个大神][2]的做法，我觉得自己表述会很乏力，因此推荐大家看上面这两个视频。

核心思想是找到nums1的一个划分位置m1，与nums2中的另一个位置m2 = k - m1，使得两个数组的左边全部都比两个数组的右边小。如果理解了这个题，应该会对二分查找有了深刻的理解。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190915164003921.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

C++代码如下：

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int M = nums1.size();
        int N = nums2.size();
        if (M > N) return findMedianSortedArrays(nums2, nums1);
        int L = M + N;
        int k = (L + 1) / 2; //总共左边需要多少个元素
        int l = 0, r = M; // 对于nums1而言
        int m1 = 0, m2 = 0;
        while (l < r) {
            m1 = l + (r - l) / 2; // nums1的分割位置，左边的元素个数
            m2 = k - m1; // nums2的分割位置，左边的元素个数
            if (nums1[m1] < nums2[m2 - 1]) {
                l = m1 + 1;
            } else {
                r = m1;
            }
        }
        m1 = l;
        m2 = k - l;
        double c1 = max(m1 <= 0 ? INT_MIN : nums1[m1 - 1],
                        m2 <= 0 ? INT_MIN : nums2[m2 - 1]);
        if (L & 1)
            return c1;
        double c2 = min(m1 >= M ? INT_MAX : nums1[m1],
                        m2 >= N ? INT_MAX : nums2[m2]);
        return (c1 + c2 ) / 2;
    }
};
```

参考资料：
https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-4-median-of-two-sorted-arrays/
https://www.youtube.com/watch?v=LPFhl65R7ww

## 日期

2019 年 9 月 15 日 —— 中秋假期的最后一天啦，刷题加油~


  [1]: https://www.youtube.com/watch?v=KB9IcSCDQ9k
  [2]: https://www.youtube.com/watch?v=LPFhl65R7ww
