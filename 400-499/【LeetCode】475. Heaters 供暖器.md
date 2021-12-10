
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/heaters/


## 题目描述

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
1. Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
1. Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
1. As long as a house is in the heaters' warm radius range, it can be warmed.
1. All the heaters follow your radius standard and the warm radius will the same.

Example 1:

    Input: [1,2,3],[2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

    Input: [1,2,3,4],[1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

## 题目大意

这道题就是有一个加热器的地址列表，还有一个屋子列表，现在需要让你制定一个加热器的加热半径，使得所有的屋子都能被加热（加热器的位置就是加热器地址列表里的了）。

## 解题方法

### 遍历

最朴素的思想。

题目给的不是有序的，一定要先排序，排序了之后，对houses进行遍历，找出大于house的最小的heater，然后求出house据左右的heater的最小距离。然后求出整个的最大距离，即为所求。

这个题的思路是从把heater对house进行覆盖的思路转化成house距离左右heater的最小距离。结果是所有最小距离的最大距离。

```python
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        ans = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house)
            ans = max(ans, r)
        return ans
```

下面这个做法是，如果后面的heater距离当前的房子距离比当前heater更小，那么就一直使用这个最小的距离。C++版本如下:

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int res = 0;
        int pos = 0;
        int N = heaters.size();
        sort(heaters.begin(), heaters.end());
        sort(houses.begin(), houses.end());
        for (int i = 0; i < houses.size(); ++i) {
            int cur = houses[i];
            while (pos < N - 1 && abs(heaters[pos + 1] - cur) <= abs(heaters[pos] - cur)) {
                ++pos;
            }
            res = max(res, abs(heaters[pos] - cur));
        }
        return res;
    }
};
```

参考资料：http://www.cnblogs.com/grandyang/p/6181626.html

## 日期

2018 年 2 月 4 日 
2018 年 11 月 26 日 —— 11月最后一周！
