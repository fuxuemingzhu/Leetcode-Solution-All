
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/task-scheduler/description/

## 题目描述

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:

1. The number of tasks is in the range [1, 10000].
1. The integer n is in the range [0, 100].



## 题目大意

对很多task进行CPU调度的计算。同样的两个task之间的时间间距不能少于n,否则会用idle填充。问这批task需要多少时间片才能完成。

## 解题方法

### 公式法

这个是一个关于CPU调度的问题，刚开始说实话我是很怵这个的，毕竟当年考研机试最后的题目就是CPU调度，我没有做出来。

但是真正做这个题目的时候，发现单个CPU做调度其实很简单。只要知道出现最多的那个（或几个）task就行了，其他的任务往缝隙里面塞。

比如：

1. 如给定：AAABBCD，n=2。那么我们满足个数最多的任务所需的数量，即可以满足任务间隔要求，即：AXXAXXA；（其中，X表示需要填充任务或者idle的间隔）
1. 如果有两种或两种以上的任务具有相同的最多的任务数，如：AAAABBBBCCDE，n=3。那么我们将具有相同个数的任务A和B视为一个任务对，最终满足要求的分配为：ABXXABXXABXXAB，剩余的任务在不违背要求间隔的情况下穿插进间隔位置即可，空缺位置补idle。
1. 由上面的分析我们可以得到最终需要最少的任务时间：**（最多任务数-1）*（n + 1） + （相同最多任务的任务个数）**。

有上面的例子来说就是：(num(A)-1) * (3+1) + (2)。

其中，（最多任务数-1）*（n + 1）代表的是ABXXABXXABXX，（相同最多任务的任务个数）代表的是最后的AB.

最后，别忘了要对任务数求最大值，毕竟每个任务都是要调度一遍的。

代码如下：

```python3
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = collections.Counter(tasks)
        most = count.most_common()[0][1]
        num_most = len([i for i, v in count.items() if v == most])
        time = (most - 1) * (n + 1) + num_most
        return max(time, len(tasks))
```

二刷的时候选择的是C++语言，这个公式我很快推导出来了，但是有一点没注意到，就是要返回这个公式求得的时间和任务个数的最大值。

比如对于测试用例``["A","A","A","B","B","B"]，0``，公式求得是(3-1)*(0+1)+2=4，而事实上，任务最少都要被调度一遍的，所以必须对任务个数求个最大值。

为什么会出现这种情况呢？很简单的解释就是当n很小的时候，这个时候n要求两个相同任务调度之间的间隔可以很小，但是事实上，相同任务间隔不可能完全按照n来确定，因为其他的任务也要插在中间。综上，必须要对任务总个数求个最大值。

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        map<char, int> counter;
        for (char task : tasks)
            ++counter[task];
        int most_common = 0;
        for (auto t : counter)
            most_common = max(most_common, t.second);
        int count_most = 0;
        for (auto t : counter)
            if (t.second == most_common)
                count_most ++;
        int res = (n + 1) * (most_common - 1) + count_most;
        return max(res, int(tasks.size()));
    }
};
```

参考资料：https://blog.csdn.net/Koala_Tree/article/details/78498586

## 日期

2018 年 8 月 22 日 —— 时不我待
2019 年 1 月 2 日 —— 2019年开刷
