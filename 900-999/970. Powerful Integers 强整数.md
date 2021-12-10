
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/powerful-integers/


## 题目描述

Given two non-negative integers ``x`` and ``y``, an integer is powerful if it is equal to ``x^i + y^j`` for some integers ``i >= 0`` and ``j >= 0``.

Return a list of all powerful integers that have value less than or equal to ``bound``.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation: 
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2

Example 2:

    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]
 

Note:

1. 1 <= x <= 100
1. 1 <= y <= 100
1. 0 <= bound <= 10^6


## 题目大意

给了两个非负整数x, y，问能组成的`x^i + y^j <= bound`有多少种。其中，i、j非负。

## 解题方法

### 暴力搜索

这个题是一个Easy题，在周赛做的时候，想复杂了，竟然想的是判断bound - x ^ i是不是y的幂。这样确实变复杂了，而且不好写。果断改成对i,j正向的两重循环。

想法是对i从0开始搜索，最多搜到bound，j也是最多搜到bound，判断得到的target = x^i + y^j 是不是<=bound，是的话就放入结果中，并且对j和i进行增长。由于题目要求不能重复，所以使用了set进行去重。

这个题坑爹的是当x或者y是1的时候，由于1的任何次方都是自己，所以有可能造成死循环，我就在这里卡住了。这也是为什么我限制了i和j是要递增的，并且它们的边界是bound的原因。

python代码如下：

```python
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()
        i = 0
        while x ** i <= bound and i <= bound:
            j = 0
            while j <= bound:
                target = x ** i + y ** j
                if target > bound:
                    break
                res.add(target)
                j += 1
            i += 1
        return list(res)
```

上面的做法虽然挺直白的，但是不够好，更好的想法是把x^i和y^j看成一个整体，这个整体每次自乘x或者y，然后判断两个整体相加的和是不是小于等于bound。同样地，也需要对x和y是不是1进行判断，这里的判断更容易一点，即如果等于1的话直接打破循环，不用再自乘x或者y了。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        set<int> res;
        for (int i = 1; i < bound; i *= x) {
            for (int j = 1; i + j <= bound; j *= y) {
                res.insert(i + j);
                if (y == 1) break;
            }
            if (x == 1) break;
        }
        return vector<int>(res.begin(), res.end());
    }
};
```

参考资料：https://leetcode.com/problems/pancake-sorting/discuss/214213/JavaC%2B%2BPython-Straight-Forward

## 日期

2019 年 1 月 6 日 —— 打球打的腰酸背痛


  [1]: https://assets.leetcode.com/uploads/2018/10/12/8-queens.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79517109
