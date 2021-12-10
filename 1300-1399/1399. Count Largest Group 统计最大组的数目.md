- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/count-largest-group/

# 题目描述

Given an integer `n`. Each number from `1` to `n` is grouped according to the sum of its digits. 

Return how many groups have the largest size.

Example 1:

    Input: n = 13
    Output: 4
    Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
    [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:

    Input: n = 2
    Output: 2
    Explanation: There are 2 groups [1], [2] of size 1.

Example 3:

    Input: n = 15
    Output: 6

Example 4:

    Input: n = 24
    Output: 5
     

Constraints:

1. `1 <= n <= 10^4`

# 题目大意

给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。

请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

# 解题方法

## 直接求

第一感觉：直接按照题目说的求。

第二感觉：应该会有规律出现的，但是提交bug了一次之后反应过来，所有的数字不止在 1~10 之间，比如当 n = 9999 时，所有数字的和是 4 * 9 = 36. 因此规律不好找，还是直接求吧。

直接求的方式就是按照题目说的，把 1 ~ n 中所有的数字，各个位的和加在一起。用一个数组（或者字典）保存各个`数位和`出现的次数，然后统计最多出现的次数共有多少个。

由于`数位和`最大也就是 当 n = 9999 时，`数字和`为 36，所以我开了一个 100 的数组来保存`数字和`。


C++代码如下。

```cpp
class Solution {
public:
    int countLargestGroup(int n) {
        vector<int> count(100, 0);
        for (int i = 1; i <= n; ++i) {
            count[sum_digit(i)] ++;
        }
        int max = *max_element(count.begin(), count.end());
        int res = 0;
        for (int i = 0; i < 100; ++i) {
            if (count[i] == max) {
                res ++;
            }
        }
        return res;
    }
    int sum_digit(int i) {
        int sum = 0;
        while (i > 0) {
            sum += i % 10;
            i /= 10;
        }
        return sum;
    }
};
```


 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
  [2]: https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-diao-zhan-jie-jue-jie-yu-shui-wen-ti-by-sweeti/
  [3]: https://pic.leetcode-cn.com/7d5ff9af88634d417d7925e8987b7db92d3a26766bd9078215ab63df424fa745-water.gif
  [4]: https://pic.leetcode-cn.com/1d1c62807d886ac9a10229cbae229465989bd6aa707449e9620a639772ba3f07-image.png
