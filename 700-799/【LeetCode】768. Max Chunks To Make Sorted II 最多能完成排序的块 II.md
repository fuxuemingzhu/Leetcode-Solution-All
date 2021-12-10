作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/

## 题目描述：

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are ``not necessarily distinct``, the input array could be up to length ``2000``, and the elements could be up to ``10**8``.

-------

Given an array arr of integers (``not necessarily distinct``), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

    Input: arr = [5,4,3,2,1]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Example 2:

    Input: arr = [2,1,3,4,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [2, 1], [3, 4, 4].
    However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

Note:

1. arr will have length in range [1, 2000].
1. arr[i] will be an integer in range [0, 10**8].


## 题目大意

把可能含有重复数字的数组分为尽可能多的块，使得每个块分别进行排序后拼接在一起，能得到整体有序的数值。

## 解题方法

这个题是[769. Max Chunks To Make Sorted][1]的变形，769题的数字范围是0~N-1不重复的数字。可是这个题改成了可能包含有重复的数字。

Grandyang大神的[可排序的最大块数之二][2]一文已经总结的非常好了，先给他赞一个。

### 方法一：

第一种方法就是观察分块的结果和原始数组排序的结果，发现每个块中的``元素和``与对应的排序切片的元素和是相等，所以根据这个可以解决。

     2  1    4  3    4
    
    (1  2)  (3  4)  (4)
    
     1  2    3  4    4

可能会想到为什么和相等就能判断一定是在同一个块中？比如上面的4,3和是7，会不会出现5,2和也是7导致判断错误呢？看一个例子就知道了，数字不同会排序到不同的位置的，所以不用多虑。

     2  1     5   2   4
    
    (1  2)   (2   4   5)
    
     1  2     2   4   5

代码中，我把划分出每个块之后的sum1,sum2复原成0，对于Python没有必要，但是对于c++和java要注意是否会超过int范围。

时间复杂度是O(N*log(N))，空间复杂度是O(1)。其中N是所有数组的长度。

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        asort = sorted(arr)
        res = 0
        sum1 = 0
        sum2 = 0
        for i, a in enumerate(arr):
            sum1 += a
            sum2 += asort[i]
            if sum1 == sum2:
                res += 1
                sum1 = 0
                sum2 = 0
        return res
```

### 方法二：

考虑一下是什么导致分块的位置呢？应该是小的数字跑到了后面，这样就不得不把它和前面的数字划分到一个组，这样排序之后才会在前面。所以使用两个数组，f数组保存每个位置之前出现的最大值，b数组保存每个数字之后出现的最小值，然后对每个位置进行一个判断：如果这个数字之前的最大值 <= 这个数字之后的最小值，那么这个数字可以成为一个新的分块。这个意思是我们后面的数字都比较大，你前面就放心分块吧！

举个栗子：

    nums    2   1   3   4   4
    f       2   2   3   4   4
    b       1   1   3   4   4
    结果    (1, 2) (3) (4) (4)

代码如下：

时间复杂度是O(N)，空间复杂度是O(1)。其中N是所有数组的长度。

```Python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = 1
        f, b = [0] * n, [0] * n
        f[0] = arr[0]
        b[-1] = arr[-1]
        for i in range(1, n):
            f[i] = max(arr[i], f[i - 1])
        for i in range(n - 2, -1, -1):
            b[i] = min(arr[i], b[i + 1])
        for i in range(n - 1):
            if f[i] <= b[i + 1]:
                res += 1
        return res
```

### 方法三：

使用单调栈Monotonous Stack。单调栈我之前看到过设计题，但是这是第一次使用。

单调栈从底至顶是单调递增的，其保存的是到目前为止的遇到的最大值。当一个新元素到达的时候，如果比栈顶大，直接进栈；如果比栈顶小，那么保存一下栈顶curMax，再对栈进行出栈操作直至栈顶元素小于当前元素，最后再把curMax入栈。这样遍历一遍所有的数字之后，得到的栈中的元素个数就是我们要求的块的个数。

这个道理和方法二基本一样的，导致块数变少的原因是来自后面出现了一个较小的元素。这个较小元素的存在，导致了我们必须把它划分到前面去，所以就一路打通到前面一个比它小的元素，这些被打通的元素属于同一个块。最后把curMax进栈，curMax的含义是我们前面一个块的最大值，也就是每个块排序后的最后一个元素。所以最后栈里多少个元素就是我们有多少个块，栈里的每个元素是每个块的结尾元素。用Grandyang的栗子如下：

> 比如数组为 [1 0 3 3 2]，我们先把第一个数字1压入栈，此时栈为：
> 
> stack：1
> 
> 然后遍历到第二个数字0，发现小于栈顶元素，将栈顶元素1取出存入curMax，此时栈为空了，不做任何操作，将curMax压回栈，此时栈为：
> 
> stack：1
> 
> 然后遍历到第三个数字3，大于栈顶元素，压入栈，此时栈为：
> 
> stack：1，3
> 
> 然后遍历到第四个数字3，等于栈顶元素，压入栈，此时栈为：
> 
> stack：1，3，3
> 
> 然后遍历到第五个数字2，小于栈顶元素，将栈顶元素3取出存入curMax，此时新的栈顶元素3，大于当前数字2，移除此栈顶元素3，然后新的栈顶元素1，小于当前数字2，循环结束，将curMax压回栈，此时栈为：
> 
> stack：1，3
> 
> 所以最终能拆为两个块儿，即stack中数字的个数。

时间复杂度是O(N)，空间复杂度是O(1)。其中N是所有数组的长度。


```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        stack = list()
        stack.append(arr[0])
        curMax = arr[0]
        for i in range(1, n):
            if arr[i] >= stack[-1]:
                stack.append(arr[i])
            else:
                curMax = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(curMax)
        return len(stack)
```

参考资料：

http://www.cnblogs.com/grandyang/p/8850299.html

## 日期

2018 年 10 月 3 日 —— 玩游戏导致没睡好，脑子是浆糊。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80482014
  [2]: http://www.cnblogs.com/grandyang/p/8850299.html
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82931106
