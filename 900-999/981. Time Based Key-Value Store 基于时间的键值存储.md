作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/time-based-key-value-store/


## 题目描述

Create a timebased key-value store class ``TimeMap``, that supports two operations.

1. ``set(string key, string value, int timestamp)``

- Stores the ``key`` and ``value``, along with the given timestamp.

2. ``get(string key, int timestamp)``

- Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
- If there are multiple such values, it returns the one with the largest timestamp_prev.
- If there are no values, it returns the empty string (``""``).
 

Example 1:

    Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    Output: [null,null,"bar","bar",null,"bar2","bar2"]
    Explanation:   
    TimeMap kv;   
    kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
    kv.get("foo", 1);  // output "bar"   
    kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
    kv.set("foo", "bar2", 4);   
    kv.get("foo", 4); // output "bar2"   
    kv.get("foo", 5); //output "bar2"   

Example 2:
    
    Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    Output: [null,null,null,"","high","high","low","low"]
 

Note:

1. All key/value strings are lowercase.
1. All key/value strings have length in the range [1, 100]
1. The timestamps for all TimeMap.set operations are strictly increasing.
1. 1 <= timestamp <= 10^7
1. TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.


## 题目大意

构建一个带有时间版本的KV存储器。即每次保存的时候会保存当前的时间，查询的时候给出一个时间，要求找到先于该时间的最新的key对应的value。

## 解题方法

### 字典

没想到LC还会出这么新颖的题目，这个应用场景在数据库设计中确实会用到。

首先分析一下，我们应该怎么办。首先，如果给出了任意的时间，我们都要找出先于这个时间的key对应的value，说明我们必须把每次的插入结果与对应的时间都保存，而不能使用覆盖的方式。

很显然我们会使用字典这种数据结构来存储kv对，为了保存每个key插入的时间，而且要保证最快的查询时间，我分开保存每次插入的key的time和value。为什么这么做有效呢？因为如果我如果使用``key : [(time1, value1), (time2, value2)...]``这种存储方式，对快速查找是不利的。而使用``key : [time1, time2...]``，``key : [value1, value2...]``这种存储方式能保证time和value是一一对应的。所以这种方式先根据key和time快速查找到小于该时间的timex，然后就能根据索引快速找到此索引对应的valuex.

在有序列表中快速查找小于一个time的time_x，当然使用二分了，所以使用了bisect_right来快速查找到了一个不大于该time的时间对应的索引，然后拿这个索引找到对应的value即可。

万万没想到的是，竟然没通过！我已经优化了存储和查找啊！看了下没通过的测试用例，发现是一个键值对反复的插入查找，每次查找的时间都是最新的时间。好吧，那么我使用了一个这个max_字典，用来保存当前的key更新的时间。这样的好处是，当我们查找一个不小于当前时间的值的时候，一定是最后一次插入的那个时间。

最后，说句题外话，这个题没有考到的是我们的删除操作怎么办？其实业界做法是使用延迟删除的方式，即插入一个标志位代表删除，而不进行真正的删除操作。比如我们在最后的时刻设置key为""，这样我们查找的时候发现这个key的数值是""就意味着被删除。


```python
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t_ = collections.defaultdict(list)
        self.v_ = collections.defaultdict(list)
        self.max_ = collections.defaultdict(int)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.t_[key].append(timestamp)
        self.v_[key].append(value)
        self.max_[key] = max(self.max_[key], timestamp)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.t_:
            return ""
        if timestamp >= self.max_[key]:
            return self.v_[key][-1]
        v = bisect.bisect_right(self.t_[key], timestamp)
        if v:
            return self.v_[key][v - 1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```


## 日期

2019 年 1 月 27 日 —— 这个周赛不太爽
