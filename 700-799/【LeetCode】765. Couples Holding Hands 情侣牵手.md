作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/couples-holding-hands/description/

## 题目描述：

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

    Input: row = [0, 2, 1, 3]
    Output: 1
    Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

    Input: row = [3, 2, 0, 1]
    Output: 0
    Explanation: All couples are already seated side by side.

Note:

1. len(row) is even and in the range of [4, 60].
1. row is guaranteed to be a permutation of 0...len(row)-1.

## 题目大意

有0~N-1这些数字的排列组成的一个数组，0和1，2和3，...，N-2和N-1分别是情侣，现在要让情侣坐在一起，每次能交换两个人的座位，求最少需要换多少次座位。

## 解题方法

这个题不愧是Hard题，虽然题目简单，但是没有任何思路。

看了Grandyang大神的做法，使用贪心策略。直接找出第偶数个位置是否和他的另一半在一起，是的话不用交换，否则找出另一半在哪里，然后直接把现在和自己坐在一起的人与自己的另一半的位置交换即可。（不会证明）

原文是：

> 当我们暂时对如何用代码来解决问题没啥头绪的时候，一个很好的办法是，先手动解决问题，意思是，假设这道题不要求你写代码，就让你按照要求排好序怎么做。我们随便举个例子来说吧，比如：
> 
> [3   1   4   0   2   5]
> 
> 我们如何将其重新排序呢？首先明确，我们交换数字位置的动机是要凑对儿，如果我们交换的两个数字无法组成新对儿，那么这个交换就毫无意义。来手动交换吧，我们两个两个的来看数字，前两个数是3和1，我们知道其不成对儿，数字3的老相好是2，不是1，那么怎么办呢？我们就把1和2交换位置呗。好，那么现在3和2牵手成功，度假去了，再来看后面的：
> 
> [3   2   4   0   1   5]
> 
> 我们再取两数字，4和0，互不认识！4跟5有一腿儿，不是0，那么就把0和5，交换一下吧，得到：
> 
> [3   2   4   5   1   0]
> 
> 好了，再取最后两个数字，1和0，两口子，不用动！前面都成对的话，最后两个数字一定成对。而且这种方法所用的交换次数一定是最少的。

使用了一个很高效的求另一半的方式，使用1异或。如果是偶数的话，最后位是0，‘异或’上1等于加了1，变成了可以的成对奇数。如果是奇数的话，最后位是1，‘异或’上1后变为了0，变成了可以的成对偶数。

最坏情况下的时间复杂度是O(N^2)，空间复杂度是O(1)。

```python
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        res = 0
        n = len(row)
        for i in range(0, n - 1, 2):
            if row[i + 1] == (row[i] ^ 1):
                continue
            for j in range(i + 1, n):
                if row[j] == (row[i] ^ 1):
                    row[j], row[i + 1] = row[i + 1], row[j]
            res += 1
        return res
```

另外一个解法，是使用并查集。但是这个解法我没有看懂，所以只贴上代码，不讲解了。

```Python
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        cnt = n / 2
        self.par = range(n)
        for i in range(0, n, 2):
            x = self.find(row[i] / 2)
            y = self.find(row[i + 1] / 2)
            if x != y:
                self.par[x] = y
                cnt -= 1
        return n / 2 - cnt
        
    def find(self, x):
        return x if self.par[x] == x else self.find(self.par[x])
```


参考资料：

http://www.cnblogs.com/grandyang/p/8716597.html

## 日期

2018 年 10 月 1 日 —— 欢度国庆！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
