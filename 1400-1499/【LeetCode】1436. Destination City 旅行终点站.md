- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/destination-city/

# 题目描述
给你一份旅游线路图，该线路图中的旅行线路用数组 `paths` 表示，其中 `paths[i] = [cityAi, cityBi]` 表示该线路将会从 `cityAi` 直接前往 `cityBi` 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。
 

示例 1：

    输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    输出："Sao Paulo" 
    解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。

示例 2：

    输入：paths = [["B","C"],["D","B"],["C","A"]]
    输出："A"
    解释：所有可能的线路是：
    "D" -> "B" -> "C" -> "A". 
    "B" -> "C" -> "A". 
    "C" -> "A". 
    "A". 
    显然，旅行终点站是 "A" 。

示例 3：

    输入：paths = [["A","Z"]]
    输出："Z"
 

提示：

1. `1 <= paths.length <= 100`
1. `paths[i].length == 2`
1. `1 <= cityAi.length, cityBi.length <= 10`
1. `cityAi != cityBi`
1. 所有字符串均由大小写英文字母和空格字符组成。


# 题目大意
给出的是一个有向无环图，找出旅行的终点站。

# 解题方法

## set

第一个感觉是 拓扑排序，但这个是周赛的 Easy 题，应该很简单。

注意题目给出的条件：**只会有一个旅行终点站。**

所以，我们找出 哪个站 没有**出度**就行了。说人话：只有一个站不会出现在出发点上。

所以，对所有的站进行统计，如果一个站没有出现在出发点上，那这个站就是最终的旅行终点站。

Python 代码如下：

```python
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        starts = set()
        ends = set()
        for path in paths:
            starts.add(path[0])
            ends.add(path[1])
        for end in ends:
            if end not in starts:
                return end
        return ""
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 3 日 —— 天气好热，瞬间入夏


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
