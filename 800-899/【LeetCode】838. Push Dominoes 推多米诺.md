# 【LeetCode】838. Push Dominoes 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/push-dominoes/description/

## 题目描述：

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

![此处输入图片的描述][1]

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

    Example 1:
    
    Input: ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."
    
    Example 2:
    
    Input: "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.

Note:

1. 0 <= N <= 10^5
1. String dominoes contains only 'L', 'R' and '.'



## 题目大意

推多米诺骨牌。在起始的时候，都是站着的，然后同时像某些方向推，L代表向左边推，R代表向右边推,.代表不推。如果左右撞在一起，那么就受力平衡。另外，很重要的一点，如果一个牌倒在了另外一个已经倒了的牌上，不会给它施加任何力。换句话说，一个推倒了的牌只能对另一个站着的牌起作用。

## 解题方法

如果理解了一个推倒了的牌只能对另一个站着的牌起作用这句话那么基本上就能做出来这个题了，否则是做不出来的。

我们对这个题的理解应该是找出最近的两个被推倒了的牌，然后判断这两个牌是什么样子的即可，不用考虑这个区间以外的牌，因为这两张牌被推倒了，而这个区间外的其他牌不会对推倒了的牌起作用。所以使用双指针的方式解决。

所以在两个被推倒了的区间里：

    'R......R' => 'RRRRRRRR'
    'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
    'L......R' => 'L......R'
    'L......L' => 'LLLLLLLL'

使用双指针即可解决掉。

代码如下：

```python
class Solution(object):
    def pushDominoes(self, d):
        """
        :type dominoes: str
        :rtype: str
        """
        d = "L" + d + "R"
        res = []
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            mid = r - l - 1
            if l:
                res.append(d[l])
            if d[l] == d[r]:
                res.append(d[l] * mid)
            elif d[l] == 'L' and d[r] == 'R':
                res.append('.' * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return "".join(res)
```

参考资料：

https://leetcode.com/problems/push-dominoes/discuss/132332/C++JavaPython-Two-Pointers

## 日期

2018 年 9 月 15 日 ———— 天气转冷，小心着凉


  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png