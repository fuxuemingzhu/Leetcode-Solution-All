作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/random-flip-matrix/description/


## 题目描述：

You are given the number of rows ``n_rows`` and number of columns ``n_cols`` of a 2D binary matrix where all values are initially 0. Write a function ``flip`` which chooses a 0 value uniformly at random, changes it to 1, and then returns the position ``[row.id, col.id]`` of that value. Also, write a function ``reset`` which sets all values back to 0. **Try to minimize the number of calls to system's Math.random()** and optimize the time and space complexity.

Note:

1. ``1 <= n_rows, n_cols <= 10000``
1. ``0 <= row.id < n_rows`` and ``0 <= col.id < n_cols``
1. ``flip`` will not be called when the matrix has no 0 values left.
1. the total number of calls to ``flip`` and ``reset`` will not exceed 1000.

Example 1:

    Input: 
    ["Solution","flip","flip","flip","flip"]
    [[2,3],[],[],[],[]]
    Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:

    Input: 
    ["Solution","flip","flip","reset","flip"]
    [[1,2],[],[],[],[]]
    Output: [null,[0,0],[0,1],null,[0,0]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.



## 题目大意

题目是用n_rows, n_cols给出了一个空白的二维数组，二维数组每个数字都是0.现在要使用flip函数随机选择0的位置翻转成1.同时还有一个函数reset是把整个二维数组重置成0.实现这个要求，并尽可能的优化时间和空间，并且减少random()函数的调用。

## 解题方法

### 方法一：循环生成随机数

这个题的心路历程：时间消耗比较多的肯定是random()的调用次数，首先分析这个函数能调用多少次。很激动的是flip函数竟然最多只调用1000次！而行和列的大小竟然到达了10000！所以很明显这个题需要我们用时间换空间嘛。肯定不能开个很大的二维数组然后记录这个过程。

所以我想了类似位图的方法，只需要一个随机数字，然后把这个数字转成二维空间的行数和列数就行。所以使用set来保存已经使用过的数字，然后选随机数，如果这个随机数已经出现过，那么继续循环找到一个没有出现过的数字。然后计算这个数字在二维列表中的位置就好了。

求一个数字应该排列在二维数组中的位置方式是``[pos / self.N, pos % self.N]``。要记住。

效率怎么样呢？很容易想象，当这个二维数组比较小的时候，那么冲突肯定很多，所以循环的调用次数很多。但是，当二维数组足够大，比如题目中有10000*10000的空位时候，flip最多才1000次，那么随机数碰撞的次数肯定很少了，效率就比较高了。

时间复杂度是O(N)，空间复杂度是O(N).N是调用次数。超过了52%的提交。

```python
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.M = n_rows
        self.N = n_cols
        self.total = self.M * self.N
        self.fliped = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        pos = random.randint(0, self.total - 1)
        while pos in self.fliped:
            pos = random.randint(0, self.total - 1)
        self.fliped.add(pos)
        return [pos / self.N, pos % self.N]

    def reset(self):
        """
        :rtype: void
        """
        self.fliped.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
```

### 方法二：Fisher–Yates shuffle 洗牌算法

看到题目说了尽可能的优化随机数的调用，就知道还有更高效的算法，果然有啊！著名的Fisher–Yates shuffle 洗牌算法！但是需要改进一下。关于这个算法可以看[这个视频][1]，还是挺容易弄懂的。这个算法对N个数字进行随机洗牌，只需要调用N - 1次随机函数。

这个洗牌算法的思想就是，使用一个指针从后向前遍历，它标记的是洗牌的末尾。即这个指针之后的数字已经全部洗牌了，不用再考虑；前面的数字还没有洗牌，需要处理；随机生成一个范围在前面数组长度的随机数，表示选中了哪个，然后和指针标记的位置进行交换，指针前移，重复这个过程。

我用一句更明白的话：每次在前面未洗牌部分随机选择一个数字，然后放到已经洗牌了数字里头。

至于为什么需要指针以及交换数字，那是为了在原地in-place操作使用的。

同样地，在这个题中不能直接使用那么大的数组进行这个过程的模拟，内存不够。所以，使用一个字典保存已经被随机数选择过的位置，把这个位置和末尾的total交换的实现方式是使用字典保存这个位置交换成了末尾的那个数字。每次随机到一个数字，然后在字典中查，如果这个数字不在字典中，表示这个数字还没被选中过，那么就直接返回这个数字，把这个数字和末尾数字交换；如果随机数已经在字典中出现过，那么说明这个位置已经被选中过，使用字典里保存的交换后的数字返回。

举个例子吧：

输入：

    ["Solution", "flip", "flip", "flip", "flip", "flip", "flip"]
    [[2, 3], [], [], [], [], [], []]

代码第21行打印出来的r, x, self.total, self.d如下

    (0, 0, 5, {0: 5})
    (0, 5, 4, {0: 4})
    (3, 3, 3, {0: 4, 3: 3})
    (2, 2, 2, {0: 4, 2: 2, 3: 3})
    (1, 1, 1, {0: 4, 1: 1, 2: 2, 3: 3})
    (0, 4, 0, {0: 4, 1: 1, 2: 2, 3: 3})

希望这个例子能帮助理解吧！

时间复杂度是O(N)，空间复杂度是O(N).N是调用次数。超过了31%的提交。


```python
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.M = n_rows
        self.N = n_cols
        self.total = self.M * self.N
        self.d = dict()

    def flip(self):
        """
        :rtype: List[int]
        """
        r = random.randint(0, self.total - 1)
        self.total -= 1
        x = self.d.get(r, r)
        self.d[r] = self.d.get(self.total, self.total)
        # print(r, x, self.total, self.d)
        return [x / self.N, x % self.N]
        

    def reset(self):
        """
        :rtype: void
        """
        self.d.clear()
        self.total = self.M * self.N


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
```


## 日期

2018 年 10 月 19 日 —— 自古逢秋悲寂寥，我言秋日胜春朝


  [1]: https://www.youtube.com/watch?v=tLxBwSL3lPQ
