作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/hand-of-straights/description/

## 题目描述

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

    Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
    Output: true
    Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

    Input: hand = [1,2,3,4,5], W = 4
    Output: false
    Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1. 1 <= hand.length <= 10000
1. 0 <= hand[i] <= 10^9
1. 1 <= W <= hand.length

## 题目大意

给出了一堆扑克牌，也给出了一个数字W，看这堆扑克牌能不能恰好全部拼成长度为W的顺子。

## 解题方法

这个思路可以说很暴力了。先做个统计，得出手里都有哪些牌，然后找出最小的牌，从这个牌开始长度为W的遍历，判断能否构成长度为W的顺子，就这样求下去即可，直到所有的牌都结束。

做了一个优化的地方，找出最小的牌的个数，因为这个最小的牌只能和比它大的牌构成顺子，所以我们可以在遍历的时候把后面的牌的个数全部剪掉这个数字。

代码如下：

```python
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        cards = collections.Counter(hand)
        while cards:
            start = min(cards.keys()) 
            start_val = cards[start]
            for card in range(start, start + W):
                if card not in cards:
                    return False
                cards[card] -= start_val
                if cards[card] == 0:
                    cards.pop(card)
                elif cards[card] < 0:
                    return False
        return not cards
```

同样的做法，如果提前做一个排序还是能加快这个运算的，这样就不用每次都去求min了。里面用到的一个技巧是range(W)之后做了一个翻转，也就是说先从大的值开始减，这样能保证cards[start]不受干扰。


```python
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        cards = collections.Counter(hand)
        for start in sorted(cards):
            if cards[start] > 0:
                for j in range(W)[::-1]:
                    if start + j not in cards:
                        return False
                    cards[start + j] -= cards[start]
                    if cards[start + j] < 0:
                        return False
        return True
```


用C++刷题的时候，使用Map保存每个数字的数量，因为map是自动排好序的。所以少了排序的步骤。统计个数之后，直接进行遍历，对于每个数字都向他后面搜索W - 1个数字。方法比较直白。

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        map<int, int> count;
        for (int h : hand) {
            ++count[h];
        }
        for (auto c : count) {
            int cur = c.first;
            int n = c.second;
            if (n > 0) {
                for (int i = 1; i < W; ++i) {
                    if (!count.count(cur + i)) {
                        return false;
                    }
                    count[cur + i] -= n;
                    if (count[cur + i] < 0)
                        return false;
                }
            }
        }
        return true;
    }
};
```

## 日期

2018 年 9 月 8 日 —— 美好的周末，从刷题开始
2019 年 2 月 27 日 —— 二月就要完了

  [1]: https://leetcode.com/static/images/problemset/diagonal_traverse.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/82390672
