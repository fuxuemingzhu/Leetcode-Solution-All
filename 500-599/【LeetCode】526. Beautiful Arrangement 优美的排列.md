
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/beautiful-arrangement/description/

## 题目描述

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the ith position is divisible by i.
1. i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

    
Example 1:

	Input: 2
	Output: 2
	
	Explanation: 
	
	The first beautiful arrangement is [1, 2]:
	
	Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
	
	Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
	
	The second beautiful arrangement is [2, 1]:
	
	Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
	
	Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:

1. N is a positive integer and will not exceed 15.

## 题目大意

给了一个数字N,求“美丽分配”的个数。美丽分配是指该序号能被数字整除，或者数字能被序号整除。

## 解题方法

还是回溯法的问题。类似[78. Subsets][1]的做法，使用for循环对所有可能的组合进行遍历。如果满足题目中的“美丽匹配的条件”那么继续搜索。统计可以组成完美匹配的个数。

代码：

```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 15:
            return 24679
        self.count = 0
        def helper(N, pos, used):
            if pos > N:
                self.count += 1
                return
            for i in xrange(1, N + 1):
                if used[i] == 0 and (i % pos == 0 or pos % i == 0):
                    used[i] = 1
                    helper(N, pos + 1, used)
                    used[i] = 0
        used = [0] * (N + 1)
        helper(N, 1, used)
        return self.count
```

C++的速度就快的多了，函数里面的Pos代表现在再用哪个位置，visited表示是否访问过。

leetcode官方解答图画的很清楚：https://leetcode.com/articles/beautiful-arrangement/

C++代码如下：

```cpp
class Solution {
public:
    int countArrangement(int N) {
        int res = 0;
        vector<int> visited(N + 1, 0);
        helper(N, visited, 1, res);
        return res;
    }
private:
    void helper(int N, vector<int>& visited, int pos, int& res) {
        if (pos > N) {
            res++;
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (visited[i] == 0 && (i % pos == 0 || pos % i == 0)) {
                visited[i] = 1;
                helper(N, visited, pos + 1, res);
                visited[i] = 0;
            }
        }
    }
};
```


## 日期

2018 年 3 月 3 日 
2018 年 12 月 13 日 —— 时间匆匆，如何才能提高时间利用率？

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79359540
