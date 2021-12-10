- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/missing-ranges/

## 题目描述

Given a sorted integer array nums, where the range of elements are in the **inclusive range `[lower, upper]`**, return its missing ranges.

Example:
    
    Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    Output: ["2", "4->49", "51->74", "76->99"]


## 题目大意

给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

## 解题方法

### 遍历

这个题的坑比较多，比如：

1. 小心整数操作溢出
2. 区间中数据可能有重复
3. 处理第一个和最后一个节点

采用long long类型的数据，然后依次遍历所有的元素，判断这个元素和上一个元素的差值是否>=2。另外需要注意最后一个元素也要判断。

第一次提交的时候，我想在`nums.push_back(upper+1)`，只要一次遍历就行。结果发现哦upper+1可能会超出int范围。所以只能用下面的解法了。

C++代码如下：

```cpp
class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> res;
        long long left = (long long)lower - 1;
        long long val = 0;
        for (long long right : nums) {
            val = right - left;
            if (val == 2) {
                res.push_back(to_string(left + 1));
            } else if (val > 2) {
                res.push_back(to_string(left + 1) + "->" + to_string(right - 1));
            }
            left = right;
        }
        val = upper - left;
        if (val == 1) {
            res.push_back(to_string(upper));
        } else if (val > 1) {
            res.push_back(to_string(left + 1) + "->" + to_string(upper));
        }
        return res;
    }
};
```

参考资料：https://leetcode-cn.com/problems/missing-ranges/solution/cte-shu-qing-kuang-duo-dao-bao-by-liyupi/

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
