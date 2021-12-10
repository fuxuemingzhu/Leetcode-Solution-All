
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/last-stone-weight/

## 题目描述

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights ``x`` and ``y`` with ``x <= y``.  The result of this smash is:

    - If x == y, both stones are totally destroyed;
    - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

    Input: [2,7,4,1,8,1]
    Output: 1
    Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1. 1 <= stones.length <= 30
1. 1 <= stones[i] <= 1000 

## 题目大意

每次拿出两个最大的石头进行抵消。如果两个石头的重量一样，那么都粉碎；否则把大的石头粉碎掉和小的石头同样的重量，然后继续放到石头堆里。最后最多只会剩下一个石头，返回这个石头的重量或者0.


## 解题方法

### 大根堆

这个题还是挺经典的，不久前微软面试的时候问过类似的题目。

这个题就是我们在数据结构与算法中都学过的哈弗曼树的改变。哈弗曼树是指每次选择最小的两个元素合并成一个更大的元素，然后和剩下的一些元素继续重复这个操作。而这个题反其道而行之，每次选择最大的两个元素合并成一个较小的元素，然后和剩下的元素重复这个操作。

实现哈弗曼树最简单的方式就是使用堆。显然这个题使用大根堆。在python中的堆默认是小根堆，为了实现大根堆，一个方式是把所有的数字进行取反操作，最后的结果再取反即可。C++的堆默认是大根堆，那么我们就直接使用。

我觉得技术上的难点只有要进行多次的判断。一定要注意在进行pop的时候是否还有元素，特别是这个题要进行两次连续的pop。另外一个注意的点是如果两个石头抵消了，那么结果0就不一样放入原来的数组中了。最后一个注意的点事最后可能全部都抵消了，所以如果结果为空则返回0。

时间复杂度是O(NlogN)。

Python代码如下：

```python
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = map(lambda x : -x, stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, -abs(x - y))
        return 0 if not stones else -stones[0]
```

C++代码如下：


```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;
        for (int s : stones)
            q.push(s);
        while (q.size() >= 2) {
            int a = q.top(); q.pop();
            if (!q.empty()) {
                int b = q.top(); q.pop();
                if (a != b) {
                    q.push(abs(a - b));
                }
            }
        }
        return q.empty() ? 0 : q.top();
    }
};
```

## 日期

2019 年 6 月 8 日 —— 刷题尽量不要停
