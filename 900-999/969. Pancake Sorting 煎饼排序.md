
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/pancake-sorting/


## 题目描述

Given an array ``A``, we can perform a pancake flip: We choose some positive integer ``k <= A.length``, then reverse the order of the first ``k`` elements of ``A``.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array ``A``.

Return the k-values corresponding to a sequence of pancake flips that sort ``A``.  Any valid answer that sorts the array within ``10 * A.length`` flips will be judged as correct.

Example 1:

    Input: [3,2,4,1]
    Output: [4,2,4,3]
    Explanation: 
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 

Example 2:

    Input: [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.
 
Note:

1. 1 <= A.length <= 100
1. A[i] is a permutation of [1, 2, ..., A.length]


## 题目大意

煎饼排序。这个排序方式很有意思，每次可以把前k个数字进行翻转，问翻转多少次之后可以达到有序状态。

就像一摞煎饼一样，每次能把铲子插入煎饼中的某个位置，然后把铲子之上的煎饼都翻转一下，问一系列位置能使结果是排序的。


## 解题方法

### 模拟法

这次周赛没有考常规的数据结构。搜了下资料，还真有这个煎饼排序，比如[算法系列：煎饼排序][1]。

其实这个题还是挺好想出来的，我们想：我们把后面的数字先排好，这样再翻转前面的时候就不会影响到后面。所以，先把最大的数字放到最后，然后再把次大的位置放在倒数第二个位置……如何把最大的数字放到最后呢？一个很简单的想法就是先把它翻转到第一个位置上去！

所以，思路很清晰了：每次找到还没排序的数字之中最大的数字的位置，把这个位置之前的数字翻转，这一步使得最大数字去了最前面。第二步，再次翻转，把最大位置翻到准确的位置上去。

这个题目一个比较好的地方是，给的数字是1~N的全排列，所以我们每次要找哪个数字很容易确定，不需要O(N)的遍历去判断最大的数字是谁。

这个题目不好的地方是，给的第一个例子不是按照常规的煎饼排序的思想列出来的，否则大家肯定很容易想出来解法。


C++代码如下：

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& A) {
        vector<int> res;
        const int N = A.size();
        int pos, i;
        for (pos = N; pos > 0; pos--) {
            for (i = 0; A[i] != pos; i ++);
            reverse(A.begin(), A.begin() + i + 1);
            if (i != 0)
                res.push_back(i + 1);
            reverse(A.begin(), A.begin() + pos);
            res.push_back(pos);
        }
        return res;
    }
};
```

python代码简洁一点，可以直接使用Index函数找到x，然后再翻转，但是这个翻转操作还不如C++的reverse函数来的简单。

```python
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = []
        for x in range(N, 0, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res
```

如果写一个reverse函数，发现python代码的运行时间从56ms 变成了 536ms。。代码如下：

```python
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = []
        for x in range(N, 0, -1):
            i = A.index(x)
            if i != 0:
                res.append(i + 1)
            res.append(x)
            self.reverse(A, 0, i + 1);
            self.reverse(A, 0, x);
            print(A)
        return res
    
    #[start, end)
    def reverse(self, A, start, end):
        A[start:end] = A[start:end][::-1]
```


## 日期

2019 年 1 月 6 日 —— 打球打的腰酸背痛


  [1]: http://blog.jobbole.com/74263/
