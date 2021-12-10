

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/odd-even-jump/


## 题目描述

You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

- During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
- During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
- (It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.


Example 1:

    Input: [10,13,12,14,15]
    Output: 2
    Explanation: 
    From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
    From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
    From starting index i = 3, we can jump to i = 4, so we've reached the end.
    From starting index i = 4, we've reached the end already.
    In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.

Example 2:

    Input: [2,3,1,1,4]
    Output: 3
    Explanation: 
    From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
    
    During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].
    
    During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.
    
    During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].
    
    We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
    
    In a similar manner, we can deduce that:
    From starting index i = 1, we jump to i = 4, so we reach the end.
    From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
    From starting index i = 3, we jump to i = 4, so we reach the end.
    From starting index i = 4, we are already at the end.
    In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.

Example 3:

    Input: [5,1,3,4,2]
    Output: 3
    Explanation: 
    We can reach the end from starting indexes 1, 2, and 4.
     

Note:

1. 1 <= A.length <= 20000
1. 0 <= A[i] < 100000

## 题目大意

第奇数次跳可以跳到后面的所有不比当前数字小的的数字中，最小的那个数字的位置上；
第偶数次跳可以跳到后面的所有不比当前数字大的的数字中，最大的那个数字的位置上；
如果跳到最后的一个位置，就相当于成功了。问有多少个位置可以成功。

## 解题方法

### 动态规划

我们是调高、跳低轮流跳的，一直到最后的一个位置。参考lee215的例子：

```
Take [5,1,3,4,2] as example.

If we start at 2,
we can jump either higher first or lower first to the end,
because we are already at the end.
higher(2) = true
lower(2) = true

If we start at 4,
we can't jump higher, higher(4) = false
we can jump lower to 2, lower(4) = higher(2) = true

If we start at 3,
we can jump higher to 4, higher(3) = lower(4) = true
we can jump lower to 2, lower(3) = higher(2) = true

If we start at 1,
we can jump higher to 2, higher(1) = lower(2) = true
we can't jump lower, lower(1) = false

If we start at 5,
we can't jump higher, higher(5) = false
we can jump lower to 4, lower(5) = higher(4) = false
```

所以，我们可以看出，从后向前进行遍历，找出每个位置能不能跳到最终的位置。由于跳高、跳低是轮流的，所以，当前的跳高跳低都要维护，而且分别后面一个跳低、跳高状态。

另外就是，这个题让我们找到最小或者最大的数字的位置，最简单的方法当然是查找，这里对查找的要求就大了。如果是线性查找，那么时间复杂度是O(N)，同时由于不是有序的，所以不能二分。一个优化的策略就是C++的map，和Java的TreeMap，即红黑树的实现版本。这个查找同样能达到O(NlogN)的时间复杂度。

定义了连个数组higher,lower分别表示当前位置开始跳高或者跳低能不能达到结尾。定义了基于红黑树的m变量来保存每个数字的位置。对于每个位置都去查找就好了，由于题目限定的条件，我们每次只会查找到一个确定的结果。对应的更新当前的跳高和跳低的状态。

注意，在C++中，lower_bound找到的是第一个满足条件的位置，而upper_bound指向的是第一个不满足的位置，即[low, high)是满足条件的所有范围。

题外话：有没有感觉这个题像不像买卖股票问题？

c++代码如下：

```cpp
class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        const int N = A.size();
        vector<bool> higher(N), lower(N);
        // higher[i] means if we jump higher, can we get N - 1?
        higher[N - 1] = lower[N - 1] = true;
        int res = 1;
        // map[i] means the pos of number i
        map<int, int> m;
        m[A[N - 1]] = N - 1;
        for (int i = N - 2; i >= 0; --i) {
            auto hi = m.lower_bound(A[i]);
            auto lo = m.upper_bound(A[i]);
            if (hi != m.end()) higher[i] = lower[hi->second];
            if (lo != m.begin()) lower[i] = higher[(--lo)->second];
            if (higher[i])
                ++res;
            m[A[i]] = i;
        }
        return res;
    }
};
```

参考资料：

https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-idea-Using-TreeMap-or-Stack

## 日期

2019 年 1 月 13 日 —— 时间太快了


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
