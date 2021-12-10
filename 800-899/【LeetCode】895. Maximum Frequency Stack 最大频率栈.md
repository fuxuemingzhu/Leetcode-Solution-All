# 【LeetCode】895. Maximum Frequency Stack 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/maximum-frequency-stack/description/

## 题目描述：

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

    Input: 
    ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
    [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
    Output: [null,null,null,null,null,null,null,5,7,5,4]
    Explanation:
    After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
    
    pop() -> returns 5, as 5 is the most frequent.
    The stack becomes [5,7,5,7,4].
    
    pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
    The stack becomes [5,7,5,4].
    
    pop() -> returns 5.
    The stack becomes [5,7,4].
    
    pop() -> returns 4.
    The stack becomes [5,7].
 

Note:

1. Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
1. It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
1. The total number of FreqStack.push calls will not exceed 10000 in a single test case.
1. The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
1. The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

## 题目大意

构造一个能弹出最大频率值的栈，如果有多个值出现的都是最大频率且相等，那么返回最靠近栈顶的那一个。

## 解题方法

同时优化两个目标：出现的频率和出现的索引。所以天然想到用优先级队列。python的优先级队列是个最小堆，而我们要优化的目标是求最大，因此，使用负号即可。

使用m保存出现的次数，使用index保存索引，使用q表示堆。

把出现的次数和出现的索引取反进堆，这样每次弹出堆的时候都是把这两个目标优化了的。pop的时候要更新频率。

我考虑了以下问题：

    我觉得是否有个问题？因为pop的过程中并没有更正已经进堆的那些数字的频率，也就是堆里面仍然是以前的频率。这里是否有问题？

其实，事实上这么想是错的，我们堆里面保留的并不是每个数字真实的频率，而是它入堆的时候的频率。当每次Pop的时候会把各个字符出现的频率恢复到它入堆前的样子（题目给出了如果同样的频率时，弹出最后push进去的数字）。当这个数字是最大频率数字，并且多次出现的时候，尽可能弹出靠最后的进入数字保证了提前进入堆的那些数字的频率是正确的。

这是个巧妙的解法，而且第一眼看上去好像是错的。非常有意思。

堆的平均时间复杂度是O(1)，空间复杂度是O(N)。

代码如下：

```python
class FreqStack(object):

    def __init__(self):
        self.m = collections.defaultdict(int)
        self.q = []
        self.index = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.m[x] += 1
        heapq.heappush(self.q, (-self.m[x], -self.index, x))
        self.index += 1

    def pop(self):
        """
        :rtype: int
        """
        val = heapq.heappop(self.q)[2]
        self.m[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
```

参考资料：

https://leetcode.com/problems/maximum-frequency-stack/discuss/163416/Java-Priority-Queue-easy-understand

## 日期

2018 年 9 月 18 日 —— 铭记这一天
