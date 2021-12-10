
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/queue-reconstruction-by-height/#/description][1]


## 题目描述

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example：

    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    
    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    
## 题目大意

给出了一个数组，数组的每个元素表示一个人的身高以及在一个队伍前面不比他矮的人的个数。现在要重新排列，使得数组是满足条件的。

## 解题方法

这个题怎么想出来的呢？是因为我们考虑如果先把个子高的排好序，那么在任何位置插入数据都不会对已经排好序的数组造成影响。而，与此同时，我们已经知道了个子高的排序，那么当新的数据到的时候，我们要确定它的位置也很简单，因为现在的所有数据都比他高，所以只要根据他的第二个数字确定他的位置即可。

先对已有的数组进行排序。按照高度降序排列，如果高度一样，按照k的值升序排列。这样比如一开始[7，0]   [7，1]   [7，2]就会排好，然后比如说后面有一个[6，1]， 说明只有一个大于或等于它，又因为比6大的已经全部取出。所以把它放在位置1，这样就变成[7，0]  [6，1]  [7，1]  [7，2].然后比如又有一个[5，0].就放在位置0，以此类推。

即对于案列。首先排序成：

    [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

然后对于第二个数字进行插入对应位置：

    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


Python代码如下：

```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x : (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
```

C++代码如下，需要注意自定义sort()函数的比较方法。

```cpp
class Solution {
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(), people.end(), [](const pair<int, int> a, const pair<int, int> b) {
            return (a.first > b.first) || (a.first == b.first && a.second < b.second);
        });
        vector<pair<int, int>> res;
        for (auto p : people) {
            res.insert(res.begin() + p.second, p);
        }
        return res;
    }
};
```

Java代码如下，之前写的，有点冗长了。

```java
public class Solution {
    public int[][] reconstructQueue(int[][] people) {
		if (people == null || people.length == 0) {
			return people;
		}
		Arrays.sort(people, new Comparator<int[]>() {
			@Override
			public int compare(int[] p1, int[] p2) {
				return p1[0] == p2[0] ? p1[1] - p2[1] : p2[0] - p1[0];
			}
		});
		List<int[]> temp = new ArrayList<int[]>();
		for (int[] aPeople : people) {
			if (people.length == aPeople[1]) {
				temp.add(aPeople);
			} else {
				temp.add(aPeople[1], aPeople);
			}
		}
		int ans[][] = new int[people.length][2];
		for (int i = 0; i < temp.size(); i++) {
			ans[i] = temp.get(i);
		}
		return ans;
    }
}
```

## 日期

2017 年 3 月 30 日 
2018 年 12 月 6 日 —— 周四啦！

  [1]: https://leetcode.com/problems/queue-reconstruction-by-height/#/description
