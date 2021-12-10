
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/daily-temperatures/description/

## 题目描述

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

    For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## 解题方法

### 倒序遍历

这个题难在找到下一个比当前气温高的位置和当前位置的差。注意到题目中温度变化范围只有60，而天数的变化范围有30000，所以对温度遍历是可以接受的，对天数遍历不可接受。

所以我们倒序遍历温度，保留每个温度的最新的天数位置，保存在字典中。对当前的温度，我们从字典中找所有比他大的温度的位置，保留最小值。如果没有比他大的，就写入0.

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        save = {}
        answer = []
        for day in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[day]
            save[temp] = day
            larger = []
            for i in range(temp + 1, 102):
                if i in save:
                    larger.append(save[i] - day)
            if larger:
                answer.append(min(larger))
            else:
                answer.append(0)
        return answer[::-1]
```

### 栈

如果正序遍历的话需要一个栈，栈的操作是这样的：

如果栈是空或者栈顶的元素小于当前元素，那么说明前面的这天的温度小于今天的，所以直接弹出前面这天，并且把他这天的结果设置为和今天的位置差。

需要注意的是，无论当天的温度是高是低，它的结果的确定需要根据后面确定，所以要入栈。

```python
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        N = len(T)
        stack = []
        res = [0] * N
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                oi = stack.pop()[1]
                res[oi] = i - oi
            stack.append((t, i))
        return res
```

C++版本的代码如下：

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        const int N = T.size();
        stack<pair<int, int>> s;
        vector<int> res(N);
        for (int i = 0; i < N; i++) {
            while (!s.empty() && s.top().first < T[i]) {
                int io = s.top().second; s.pop();
                res[io] = i - io;
            }
            s.push({T[i], i});
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 7 日 
2018 年 12 月 7 日 —— 恩，12月又过去一周了
