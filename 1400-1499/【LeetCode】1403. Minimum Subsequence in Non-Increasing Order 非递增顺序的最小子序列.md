
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order/

# 题目描述

给你一个数组 nums，请你从中抽取一个子序列，满足该子序列的元素之和 严格 大于未包含在该子序列中的各元素之和。

如果存在多个解决方案，只需返回 长度最小 的子序列。如果仍然有多个解决方案，则返回 元素之和最大 的子序列。

与子数组不同的地方在于，「数组的子序列」不强调元素在原数组中的连续性，也就是说，它可以通过从数组中分离一些（也可能不分离）元素得到。

注意，题目数据保证满足所有约束条件的解决方案是 唯一 的。同时，返回的答案应当按 非递增顺序 排列。
 

示例 1：

    输入：nums = [4,3,10,9,8]
    输出：[10,9] 
    解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。 

示例 2：

    输入：nums = [4,4,7,6,7]
    输出：[7,7,6] 
    解释：子序列 [7,7] 的和为 14 ，不严格大于剩下的其他元素之和（14 = 4 + 4 + 6）。因此，[7,6,7] 是满足题意的最小子序列。注意，元素按非递增顺序返回。  

示例 3：

    输入：nums = [6]
    输出：[6]
 

提示：

1. `1 <= nums.length <= 500`
1. `1 <= nums[i] <= 100`



# 题目大意

从数组中抽取最少的数字，使得这部分 数字的和 比剩下 所有的数字和 更大。


# 解题方法

## 贪心

这个题的题目比较长，其实求法很简单，我们优先拿大的数字，当 拿走的数字和 比 剩下的数字和更大时就停止。

1. 排序
2. 优先拿大的数字，直到 拿走的数字之和 大于 剩余的数字之和。

C++代码如下。

```cpp
class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        sort(nums.rbegin(), nums.rend());
        vector<int> res;
        int sum_res = 0;
        int i = 0;
        while (sum_res <= sum - sum_res && i < nums.size()) {
            res.push_back(nums[i]);
            sum_res += nums[i];
            i ++;
        }
        return res;
    }
    
};
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png
