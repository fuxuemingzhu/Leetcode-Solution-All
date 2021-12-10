# 【LeetCode】870. Advantage Shuffle 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/advantage-shuffle/description/

## 题目描述：

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

    Input: A = [2,7,11,15], B = [1,10,4,11]
    Output: [2,11,7,15]

Example 2:

    Input: A = [12,24,8,32], B = [13,25,32,11]
    Output: [24,32,8,12]
 

Note:

1. 1 <= A.length = B.length <= 10000
1. 0 <= A[i] <= 10^9
1. 0 <= B[i] <= 10^9

## 题目大意

如何安排A的各个数字，使得对于每个位置A[i]>B[i]的情况最多。

## 解题方法

中国人小时候学过的一个故事，叫做田忌赛马，大家应该都知道的，用自己比对方强一点点的马去战胜对方的马，如果对方的马太强了，那么就用自己的最弱的马去参加比赛。这样做的好处就是我们用自己的弱鸡消耗掉对方的精锐，自己获胜的概率就最大。

使用了双向队列解决这个问题。同样是对A,B进行从小到大的排序，排序时需要保存B中的数字原来在数组中的哪个位置。这样我们对A进行一次遍历，每次出动自己的最弱的马，如果这个马能战胜B中最弱的马，那么就这么使用；如果战胜不了的话，那么就用这个最弱的马去和B中最强的马比赛，这样就干掉了对方的精锐。

时间复杂度是O(nlogn)，空间复杂度是O(n).

代码如下：

```python
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(A)
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res
```

参考资料：

https://leetcode.com/problems/advantage-shuffle/discuss/149932/Python-greedy-sol-with-detailed-comment-Chinese-story:-Tian-Ji's-Horse-race

## 日期

2018 年 9 月 21 日 —— 转眼这个月又快过去了
