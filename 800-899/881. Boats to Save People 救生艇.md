# 【LeetCode】881. Boats to Save People 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/boats-to-save-people/description/

## 题目描述：

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)

Example 2:

    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

Note:

1. 1 <= people.length <= 50000
1. 1 <= people[i] <= limit <= 30000


## 题目大意

一条船最多坐两个人，同时船有个载重，问最少需要多少条船才能装下所有人。

## 解题方法

如果感觉题目不好做的时候，建议再仔细读读题，题目说了最多坐两个人。。

方法比较简单，先排序，然后使用双指针。一个指向重的人，一个指向轻的人。题目说了一个人的重量不会超过载重。。

1. 如果两个人能坐在同一条船上，那么把两个指针向中间移动
2. 如果两个人的重量大于船的载重，那么让胖的人坐！因为瘦的人可以和别人挤挤，但是胖子不行啊，这个船必须都是他的了。（汽车的副驾驶2333）
3. 重复上述操作

也就是说指向胖子的指针一定会移动，指向瘦子的指针只有在能坐下两个人的时候才能移动。

同时注意一下，循环的过程中，循环的条件中，允许hi == lo，因为这种情况下说明剩了一个人还没挤上船。

采用双指针，把每个人都遍历了一遍，所以时间复杂度是O(n)，空间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res = 0
        hi, lo = len(people) - 1, 0
        while hi >= lo:
            if people[hi] + people[lo] <= limit:
                lo += 1
            hi -= 1
            res += 1
        return res
```

参考资料：

https://leetcode.com/problems/boats-to-save-people/discuss/156855/6-lines-Java-O(nlogn)-code-sorting-+-greedy-with-greedy-algorithm-proof.

## 日期

2018 年 9 月 21 日 —— 转眼这个月又快过去了
