作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/fruit-into-baskets/description/

## 题目描述：

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
1. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

    Input: [1,2,1]
    Output: 3
    Explanation: We can collect [1,2,1].

Example 2:

    Input: [0,1,2,2]
    Output: 3
    Explanation: We can collect [1,2,2].
    If we started at the first tree, we would only collect [0, 1].

Example 3:

    Input: [1,2,3,2,2]
    Output: 4
    Explanation: We can collect [2,3,2,2].
    If we started at the first tree, we would only collect [1, 2].

Example 4:
    
    Input: [3,3,3,1,2,1,1,2,3,3,4]
    Output: 5
    Explanation: We can collect [1,2,1,1,2].
    If we started at the first tree or the eighth tree, we would only collect 4 fruits.
     

Note:

1. 1 <= tree.length <= 40000
1. 0 <= tree[i] < tree.length


## 题目大意

输入是一排树，每棵树上结的有果子，这个数字代表果子的种类（注意，不是数目）。让你从某个位置开始向右连续的去摘果子，只有两个篮子，每个篮子只能放同一类果子。如果向右遍历的过程中没有果子可以摘了，或者果篮里没法放当前树的果子，那么就停止，问总的能摘多少果子。

## 解题方法

现在LeetCode就喜欢出一个情景题，让人花了很长时间理解题意，并且抽象出来。这个题如果抽象成模型的话就是，求一个数组的最长连续子数组，要求这个子数组中最多只存在两个不同的元素。

如果做了上面的抽象，那么我们就很容易想到使用双指针，计算双指针区间内的所有元素的个数，这个个数就是我们要求的能摘取的果子个数。同时在移动的过程中要保证，双指针区间内的元素种类最多为2.之前做题的时候有使用Counter直接数一个区间内所有的个数，这样会超时的。所以使用了字典进行存储，每次只更新最右边和最左边的元素的个数即可。

时间复杂度是O(N)，空间复杂度是O(N).

```python
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left, right = 0, 0
        res = 0
        cnt = collections.defaultdict(int)
        while right < len(tree):
            cnt[tree[right]] += 1
            while len(cnt) > 2:
                cnt[tree[left]] -= 1
                if cnt[tree[left]] == 0:
                    del cnt[tree[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
```

参考资料：

https://blog.csdn.net/XX_123_1_RJ/article/details/82828570

## 日期

2018 年 9 月 30 日 —— 9月最后一天啦！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82903681
