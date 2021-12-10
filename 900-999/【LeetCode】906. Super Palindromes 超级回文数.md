
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/super-palindromes/description/


## 题目描述

Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers ``L`` and ``R`` (represented as strings), return the number of superpalindromes in the inclusive range ``[L, R]``.

 

Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
 

Note:

1. ``1 <= len(L) <= 18``
1. ``1 <= len(R) <= 18``
1. ``L`` and ``R`` are strings representing integers in the range ``[1, 10^18)``.
1. ``int(L) <= int(R)``

## 题目大意

找出在``[L, R]``双闭区间内，所有的超级回文数个数。超级回文数是指本身是回文数，并且它的算数平方根也是回文数。

## 解题方法

### BFS解法

暴力求解的话一定超时，很明显超级回文数是很稀少的，我们还是想想怎么能找规律吧。这是一些超级回文数：

    # n, n^2
    (1, 1)
    (2, 4)
    (3, 9)
    (11, 121)
    (22, 484)
    (101, 10201)
    (111, 12321)
    (121, 14641)
    (202, 40804)
    (212, 44944)
    (1001, 1002001)
    (1111, 1234321)
    (2002, 4008004)

可以注意到，在除了（1,4,9）之外的其他超级回文数的算数平方根都是有0,1,2组成，而且两头都是由1或者2构成。

所以可以想到BFS的解法，我们使用一个队列保存的是回文的算数平均数n，然后我们拿出队列的每个元素，像中间部分插入0,1,2作为候选的n（保证仍然是回文），然后把候选的n再次放入到队列中去，如果算数平均数n的平方大于R了，就不用拿他计算新的数字了。

最后还需要把1,2,3给放入到候选里面去，也要判断候选的回文算数平均数的平方是不是回文数，如果是的话，结果加一。

时间复杂度不会算，空间复杂度不会算.超过65%.

```python
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        que = collections.deque(["11", "22"])
        candi = set()
        while que:
            size = len(que)
            for _ in range(size):
                p = que.popleft()
                candi.add(p)
                if int(p) ** 2 > int(R):
                    continue
                for j in ["0", "1", "2"]:
                    q = (p[:len(p)//2] + j + p[len(p)//2:])
                    que.append(q)
        candi.add("1")
        candi.add("2")
        candi.add("3")
        res = 0
        for cand in candi:
            if int(L) <= int(cand) ** 2 <= int(R) and self.isPalindromes(int(cand) ** 2):
                res += 1
        return res
                
            
    def isPalindromes(self, s):
        s = str(s)
        N = len(s)
        for l in range(1, N // 2):
            if s[l] != s[N - 1 - l]:
                return False
        return True
```


## 相似题目


## 参考资料

https://leetcode.com/problems/super-palindromes/discuss/171450/Python-AC-bfs-detail-explanation

## 日期

2018 年 11 月 3 日 —— 雾霾的周六


  [1]: http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
