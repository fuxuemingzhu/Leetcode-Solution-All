作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/reorganize-string/description/

## 题目描述：

Given a string ``S``, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

    Input: S = "aab"
    Output: "aba"

Example 2:

    Input: S = "aaab"
    Output: ""

Note:

1. S will consist of lowercase letters and have length in range [1, 500].

## 题目大意

输入是一个字符串，如果这个字符串重新排列之后能组成一个新字符串使得这个字符串相邻的字符都不相同，那么返回这个新字符串；如果做不到，就返回空字符串。

## 解题方法

这个题我知道要用Counter，而且也知道要做多次操作，可是我想的是递归，没做出来。。看了[书影博客][1]，才做出来的。

方法是：

统计这个字符串每个字符的出现频率，在组成新字符串时，在满足和上一个字符不相同的情况下，优先使用最流行的字符串。每用一个字符都对counter进行更新，直至循环结束。注意如果次数为0要删除，否则counter不会为空。

```python
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        ans = "#"
        while counter:
            stop = True
            for item, times in counter.most_common():
                if ans[-1] != item:
                    ans += item
                    counter[item] -= 1
                    if not counter[item]:
                        del counter[item]
                    stop = False
                    break
            if stop: break
        return ans[1:] if len(ans) == len(S) + 1 else ""
```
其实这个题和[358. Rearrange String k Distance Apart](https://blog.csdn.net/fuxuemingzhu/article/details/83039098)题目一模一样的，都是使用小根堆+优先使用出现次数多的字符方法进行模拟。

需要留意的地方是出现的次数是正的，python的堆是小根堆，所以进堆的时候把次数取了符号，这样的话，中间对次数-1的步骤实际上使用的是+1。另外，已经使用过了的字符这轮就不会再取了，所以使用temp临时保存一下。

代码也基本相同，如下：

```python
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        _len = len(S)
        count = collections.Counter(S)
        que = [(-v, c) for c, v in count.items()]
        heapq.heapify(que)
        res = ""
        while _len:
            cnt = min(_len, 2)
            temp = list()
            for i in range(cnt):
                if not que:
                    return ""
                v, c = heapq.heappop(que)
                res += c
                if v + 1 != 0:
                    temp.append((v + 1, c))
                _len -= 1
            for x in temp:
                heapq.heappush(que, x)
        return res
```

## 日期

2018 年 6 月 13 日 ———— 腾讯赛圆满结束！两个月修得正果哈哈～～
2018 年 10 月 14 日 —— 周赛做出来3个题，开心

  [1]: http://bookshadow.com/weblog/2018/01/21/leetcode-reorganize-string/
