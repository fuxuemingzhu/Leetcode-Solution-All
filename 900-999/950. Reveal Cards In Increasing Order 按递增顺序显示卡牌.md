

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reveal-cards-in-increasing-order/description/


## 题目描述
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

1， Take the top card of the deck, reveal it, and take it out of the deck.
1. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
1. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in ``increasing order``.

The first entry in the answer is considered to be the top of the deck.

 

Example 1:

    Input: [17,13,11,2,3,5,7]
    Output: [2,13,3,11,5,17,7]
    Explanation: 
    We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
    After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
    We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
    We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
    We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
    We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
    We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
    We reveal 13, and move 17 to the bottom.  The deck is now [17].
    We reveal 17.
    Since all the cards revealed are in increasing order, the answer is correct.
 

Note:

1. 1 <= A.length <= 1000
1. 1 <= A[i] <= 10^6
1. A[i] != A[j] for all i != j


## 题目大意

对一堆面朝下的牌进行如下操作：

1. 把最上面的牌翻开
2. 如果还有牌，把最上面的牌放到最下面
3. 如果还有牌，重复1和2

问初始状况如何排列牌，才能使得翻开牌的顺序是有序的。

## 解题方法

### 模拟

这个世界太有意思了，看似超级困难的游戏，在计算机的帮助下，很快就能求解。但这也是对程序设计的一个挑战。

我最初的想法是进行模拟，但是我想到的是用list模拟，那么每次插入操作很费时，应该不能通过，所以我就去找规律去了！惭愧啊！

正确的方法是使用链表！因为链表在前后进行插入删除的时间复杂度都是O(1)，所以比list强多了。

使用链表的话，我们需要把整个的顺序倒着看，也就是说把题目给出的翻牌的顺序从下向上看。那么我们得出了规律：

第一步，先把最大的数字放入链表里；

第二步，每次把剩余的最大值放到链表的开头，同时把链表的最后一个元素放入到链表最前面。

只要还有剩余数字，重复第一和第二步。

python的代码其实很简单。

```python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        N = len(deck)
        res = [0] * N
        que = collections.deque()
        for i in range(N):
            if que:
                que.appendleft(que.pop())
            que.appendleft(deck.pop())
        return list(que)
```


## 日期

2018 年 12 月 2 日 —— 又到了周日


  [1]: https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png
