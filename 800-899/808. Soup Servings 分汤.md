作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/soup-servings/description/

## 题目描述：

There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

1. Serve 100 ml of soup A and 0 ml of soup B
1. Serve 75 ml of soup A and 25 ml of soup B
1. Serve 50 ml of soup A and 50 ml of soup B
1. Serve 25 ml of soup A and 75 ml of soup B

When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

 

Example:

    Input: N = 50
    Output: 0.625
    Explanation: 
    If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

1. 0 <= N <= 10^9. 
1. Answers within 10^-6 of the true value will be accepted as correct.



## 题目大意

有A，B两种汤。初始每种汤各有N毫升，现有4种操作：

    1. A倒出100ml，B倒出0ml
    2. A倒出75ml， B倒出25ml
    3. A倒出50ml， B倒出50ml
    4. A倒出25ml， B倒出75ml

每种操作的概率均等为0.25。如果汤的剩余容量不足完成某次操作，则有多少倒多少。当每一种汤都倒完时停止操作。

求A先倒完的概率，加上A和B同时倒完的概率*0.5。

## 解题方法

这个题是个简单的记忆化搜索问题。

使用solve(A, B)函数表示当A, B分别是两者的数量的时候，A先倒完的概率，加上A和B同时倒完的概率*0.5。同时使用memo来保存这个结果。

    if A <= 0 and B > 0: return 1 // A先倒完，结果是1
    if A <= 0 and B <= 0: return 0.5 // A和B同时倒完，结果是题目设定的0.5
    if A > 0 and B <= 0: return 0 // B先倒完，结果是0

由于四个操作发生的概率是相等的，所以，当A,B同时剩余的时候，其结果是4个操作获得概率的平均数。

另外就是题目给了提示，B没有每次倒100的情况，所以，A先倒完的概率更大。当N很大的时候，我们会做很多次操作，最后肯定是A先结束。题目要求小数点后6位，所以当N > 5600 直接 return 1.0。

另外在测试中发现，如果把(A,B)是否在记忆化数组中放到所有判断的前面，速度会加快。

时间复杂度是O(N^2)，空间复杂度是O(N^2). 

代码如下：

```python
class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        self.memo = dict()
        if N > 5600: return 1.0
        return self.solve(N, N)
    
    def solve(self, A, B):
        if (A, B) in self.memo:
            return self.memo[(A, B)]
        if A <= 0 and B > 0: return 1
        if A <= 0 and B <= 0: return 0.5
        if A > 0 and B <= 0: return 0
        prob = 0.25 * (self.solve(A - 100, B) + self.solve(A - 75, B - 25)
                       + self.solve(A - 50, B - 50) + self.solve(A - 25, B - 75))
        self.memo[(A, B)] = prob
        return prob
```

参考资料：

http://bookshadow.com/weblog/2018/04/02/leetcode-soup-servings/
https://leetcode.com/problems/soup-servings/discuss/121711/C%2B%2BJavaPython-When-N-greater-4800-just-return-1/185112

## 日期

2018 年 10 月 10 日 ———— 冻成狗


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291936
