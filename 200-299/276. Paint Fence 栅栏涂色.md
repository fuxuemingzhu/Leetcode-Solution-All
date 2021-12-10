
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/

## 题目描述

There is a fence with `n` posts, each post can be painted with one of the `k` colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:

- n and k are non-negative integers.

Example:

    Input: n = 3, k = 2
    Output: 6
    Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
    
                post1  post2  post3      
     -----      -----  -----  -----       
       1         c1     c1     c2 
       2         c1     c2     c1 
       3         c1     c2     c2 
       4         c2     c1     c1  
       5         c2     c1     c2
       6         c2     c2     c1


## 题目大意

有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱最多连续两个颜色相同。然后，返回所有有效涂色的方案数。


## 解题方法

### 动态规划

设F[n]为到第n个栅栏总的配色方案数，设当前的栅栏为cur，前面一个栅栏为prev，更前面的一个栅栏为pprev. 

当前栅栏cur的涂色方案有两种：

1. 和prev相同，此时说明prev的颜色应与pprev的颜色不同，pprev的涂色方法有 F(n - 2) 种，prev的涂色方式有 (k - 1) 种，所以此时情况应为 F(n - 2) * (k - 1)
1. 和prev不同，prev的涂色方法有 F(n - 1) 种，cur的涂色方式有 (k - 1) 种，此时情况应为 F(n - 1) * (k - 1)

所以递推公式应为 F(n) = F(n - 2) * (k - 1) + F(n - 1) * (k - 1)


C++代码如下：

```cpp
class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0) return 0;
        if (n == 1) return k;
        int pprev = k;
        int prev = k * k;
        int cur = k * k;
        for (int i = 2; i < n; ++i) {
            cur = pprev * (k - 1) + prev * (k - 1);
            pprev = prev;
            prev = cur;
        }
        return cur;
    }
};
```

参考资料：https://leetcode-cn.com/problems/paint-fence/solution/c-dp-zong-jie-yi-xia-liang-chong-si-lu-by-sheng-be/

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
