作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/card-flipping-game/description/

## 题目描述：

On a table are ``N`` cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number ``X`` on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, ``fronts[i]`` and ``backs[i]`` represent the number on the front and back of card i. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

    Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
    Output: 2
    Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
    We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
 

Note:

1. 1 <= fronts.length == backs.length <= 1000.
1. 1 <= fronts[i] <= 2000.
1. 1 <= backs[i] <= 2000.


## 题目大意

有一些正反面都有数字的牌，我们可以做很多次翻转操作，每次翻转时如果这个牌背面的数字没有在这群牌的正面出现过，那么就可以把这个牌翻转过来。求翻转哪个牌可以之后，可以使得所有牌正面中的最小值最小。

## 解题方法

这个题的英文描述不清，我尽量翻译的清楚了。

所以，如果一个牌正反面相等，那么翻转不翻转没什么意义。否则可以翻转，求翻哪些之后会得到最小，就是如果不翻转的最小值和翻转了之后的最小值的最小值。使用set保存一下正反面相等的数字，这些是一定不能在正面出现的，然后找出不在这个set里面的正反面的最小值即可。

怎么理解？首先正反面相同的翻转没有意义，然后找在正反面的最小值把它翻转到正面来。那么有人会想，如果翻转这个牌和其他的正面的牌有冲突怎么办？其实，如果和set里面的牌有冲突没有意义，如果和不在set里面的正面的牌有冲突就把这个冲突的牌也翻转即可。所以，不用考虑这么多。。

时间复杂度是O(N)，空间复杂度最坏是O(N).

代码如下：

```python
class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        s = set()
        res = float('inf')
        for f, b in zip(fronts, backs):
            if f == b:
                s.add(f)
        for f in fronts:
            if f not in s:
                res = min(res, f)
        for b in backs:
            if b not in s:
                res = min(res, b)
        return 0 if res == float('inf') else res
```


参考资料：

https://zxi.mytechroad.com/blog/hashtable/leetcode-822-card-flipping-game/

## 日期

2018 年 9 月 27 日 ———— 今天起得格外早
