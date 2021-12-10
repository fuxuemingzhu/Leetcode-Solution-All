
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/relative-ranks/#/description][1]


## 题目描述

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example：

    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
    For the left two athletes, you just need to output their relative ranks according to their scores.
    
    Output:
    7

Note:

 1. N is a positive integer and won't exceed 10,000.
 2. All the scores of athletes are guaranteed to be unique.

## 题目大意

把一个数组中最大的三个位置设置成金银铜奖，其他位置是当前数字的排名。

## 解题方法

### 排序

java也可以通过sort的方法，把类似键值对的数组按照第一维排序，第二维也会跟着排序：

    Example:
    
    nums[i]    : [10, 3, 8, 9, 4]
    pair[i][0] : [10, 3, 8, 9, 4]
    pair[i][1] : [ 0, 1, 2, 3, 4]
    
    After sort:
    pair[i][0] : [10, 9, 8, 4, 3]
    pair[i][2] : [ 0, 3, 2, 4, 1]

这样就可以找出前几个较大值对应的序号，从而标出名词。

参考这个详细解答：[https://discuss.leetcode.com/topic/77876/easy-java-solution-sorting][2]

```java
public class Solution {
    public String[] findRelativeRanks(int[] nums) {
		int pair[][] = new int[nums.length][2];
		for (int i = 0; i < nums.length; i++) {
			pair[i][0] = nums[i];
			pair[i][4] = i;
		}
		Arrays.sort(pair, (a, b) -> (b[0] - a[0]));
		String[] ans = new String[nums.length];
		for (int i = 0; i < nums.length; i++) {
			if (i == 0) {
				ans[pair[i][5]] = "Gold Medal";
			} else if (i == 1) {
				ans[pair[i][6]] = "Silver Medal";
			} else if (i == 2) {
				ans[pair[i][7]] = "Bronze Medal";
			} else {
				ans[pair[i][8]] = "" + (i + 1);
			}
		}
		return ans;
    }
}
```

### argsort


这个题，因为我用python做kNN的时候也要找出前几个大值所在的序号，就用了numPy的argsort()函数。LeetCode也可以用Numpy的！！看我的解法！！

```python
import numpy as np
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = np.argsort(np.array(nums))[::-1]
        N = len(nums)
        res = list(map(str, ranks))
        for r in range(N):
            if r == 0:
                res[ranks[0]] = "Gold Medal"
            elif r == 1:
                res[ranks[1]] = "Silver Medal"
            elif r == 2:
                res[ranks[2]] = "Bronze Medal"
            else:
                res[ranks[r]] = str(r + 1)
        return res
```

### 堆

```python
import numpy as np
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        N = len(nums)
        res = [""] * N
        count = 1
        while heap:
            num, i = heapq.heappop(heap)
            if count == 1:
                res[i] = "Gold Medal"
            elif count == 2:
                res[i] = "Silver Medal"
            elif count == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(count)
            count += 1
        return res
```


## 日期

2017 年 4 月 14 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/relative-ranks/#/description
  [2]: https://discuss.leetcode.com/topic/77876/easy-java-solution-sorting
