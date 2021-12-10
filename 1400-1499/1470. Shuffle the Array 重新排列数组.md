# 

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/shuffle-the-array/


# 题目描述


给你一个数组 `nums` ，数组中有 `2n` 个元素，按 `[x1,x2,...,xn,y1,y2,...,yn]` 的格式排列。

请你将数组按 `[x1,y1,x2,y2,...,xn,yn]` 格式重新排列，返回重排后的数组。

示例 1：

    输入：nums = [2,5,1,3,4,7], n = 3
    输出：[2,3,5,4,1,7] 
    解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

示例 2：

    输入：nums = [1,2,3,4,4,3,2,1], n = 4
    输出：[1,4,2,3,3,2,4,1]

示例 3：

    输入：nums = [1,1,2,2], n = 2
    输出：[1,2,1,2]

提示：

1. `1 <= n <= 500`
1. `nums.length == 2n`
1. `1 <= nums[i] <= 10^3`


# 题目大意

略。

# 解题方法

本题比较简单，可以重拳出击。

用一个新的数组按照 `nums[0], nums[n], nums[1], nums[n + 1], ...` 的顺序依次保存所有的排列即可。

Python 代码如下：

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**



# 日期

2020 年 6 月 14 日 —— 今晚争取也直播讲题


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png
