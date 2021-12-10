作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/number-of-boomerangs/][1]

 - Difficulty: Easy

## 题目描述


Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points ``(i, j, k)`` such that the distance between ``i`` and ``j`` equals the distance between ``i`` and ``k`` (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most ``500`` and coordinates of points are all in the range ``[-10000, 10000]`` (inclusive).

Example:

	Input:
	[[0,0],[1,0],[2,0]]
	
	Output:
	2
	
	Explanation:
	The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

## 题目大意

如果一个三元组，第一个元素和第二个元素的距离 等于 第一个元素和第三个元素的距离，那么是一个回旋镖。问题目给出的n个长度的点中，有多少个回旋镖。

## 解题方法

题目的意思是找出距离到其他的点都相等的点，并且判断相等的路径的排列有多少条。

尝试暴力解决。

双重循环是没有问题的，因为题目要求出一个点到其余各个点的距离，因此，必须有双重循环。在存储距离的时候，要使用HashMap，这里有个技巧，可以节省代码：hashmap.put(distance, hashmap.getOrDefault(distance, 0) + 1);，如果没有这个距离的话，就放入1，有的话就把之前的值加1。

在这个大的循环里边，遍历完到其余个点的距离后，再把HashMap中的距离相等的值给拿出来，如果某个点到其他的点的距离都不相等，那么这个值是1，所以结果为0；否则是N*(N-1).

```java
public class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int res = 0;
        HashMap<Integer, Integer> hashmap=new HashMap<>();
        for(int i =0; i< points.length; i++){
            for(int j=0; j< points.length; j++){
                if(i == j){
                    continue;
                }
                int distance = getDistance(points[i], points[j]);
                hashmap.put(distance, hashmap.getOrDefault(distance, 0) + 1);
                
            }
            for(int val : hashmap.values()) {
                res += val * (val-1);
            }            
            hashmap.clear();
        }
        return res;
    }
    public int getDistance(int[] point1, int[] point2){
        int dx= point2[0] - point1[0];
        int dy=point2[1] - point1[1];
        return dx*dx + dy*dy;
    }
}
```

AC: 188 ms 超过61%

python写法：

```python
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p0 in points:
            d = collections.defaultdict(int)
            for p1 in points:
                d[(p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2] += 1
            for d, v in d.items():
                res += v * (v - 1)
        return res
```

## 日期

2017 年 1 月 12 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/problems/number-of-boomerangs/
