
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/teemo-attacking/description/

## 题目描述

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:

    Input: [1,4], 2
    Output: 4
    Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
    This poisoned status will last 2 seconds until the end of time point 2. 
    And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
    So you finally need to output 4.
    
Example 2:

    Input: [1,2], 2
    Output: 3
    Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
    This poisoned status will last 2 seconds until the end of time point 2. 
    However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
    Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
    So you finally need to output 3.

Note:
1. You may assume the length of given time series array won't exceed 10000.
1. You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.

## 题目大意

给了一个递增的时间点序列，表示提莫放毒的时间点，给出了每次放毒持续的时间长度。求总的中毒时间。

## 解题方法


正向思维是遍历数组，然后在每次放毒的时候去判断是否还在中毒状态，等等。稍微麻烦。

逆向思维很好用：如果两次中毒时间不存在交叉，那么总的中毒时间易求出。再用总的中毒时间-两次中毒之间重叠的时间，就是答案。

代码：

```python
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            if timeSeries[i] < timeSeries[i - 1] + duration:
                total -= timeSeries[i - 1] + duration - timeSeries[i]
        return total
```

二刷，使用start和end来表示这次中毒的开始和结束时间。需要判断新一次中毒的时候，是否还在上一次的中毒周期内。

```cpp
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (timeSeries.size() == 0) return 0;
        int start = timeSeries[0], end = start + duration;
        int res = 0;
        for (int i = 1; i < timeSeries.size(); i++) {
            int time = timeSeries[i];
            if (end > time)
                res += time - start;
            else
                res += duration;
            end = time + duration;
            start = time;
        }
        res += duration;
        return res;
    }
};
```


## 日期

2018 年 3 月 4 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始
