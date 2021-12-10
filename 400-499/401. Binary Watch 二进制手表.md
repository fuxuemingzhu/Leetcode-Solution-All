作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/binary-watch/][1]

 - Difficulty: Easy

## 题目描述


A binary watch has 4 LEDs on the top which represent the hours ``(0-11)``, and the 6 LEDs on the bottom represent the minutes ``(0-59)``.

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

![在这里插入图片描述](https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg)

Example:

	Input: n = 1
	Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

- The order of output does not matter.
- The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
- The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

## 题目大意

有个二进制手表，求亮n个灯的时候，能显示多少种时间？


## 解题方法

### java解法

尝试暴力解决。看12小时内的哪个一分钟的二进制表示值等于题目给的num，效率不太高。

```java
public class Solution {
    public List<String> readBinaryWatch(int num) {
        ArrayList<String> times = new ArrayList<String>();
        for(int h =0; h<12; h++){
            for(int m=0; m<60; m++){
                if(Integer.bitCount(h*64 + m) == num){
                    times.add(String.format("%d:%02d", h, m));
                }
            }
        }
        return times;
    }
}
```

AC: 34 ms 超过14.87%

----更新----

### Python解法

还是使用回溯法。这个题的回溯法其实就是枚举小时亮灯数和分钟亮灯数。

知道小时的灯的亮的个数需要使用python的combinations进行一次组合运算，才能遍历所有的小时情况。

另外就是要注意，小时和分钟这两个循环是嵌套的。

题目中给的时间的范围是0-11小时和0-59分钟，越界判断也要注意。

```python
from itertools import combinations
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, 0, res)
        return res
        
    def dfs(self, num, hours, res):
        if hours > num : return
        for hour in combinations([1, 2, 4, 8], hours):
            hs = sum(hour)
            if hs >= 12 : continue
            for minu in combinations([1, 2, 4, 8, 16, 32], num - hours):
                mins = sum(minu)
                if mins >= 60 : continue
                res.append("%d:%02d" % (hs, mins))
        self.dfs(num, hours + 1, res)
```

## 日期

2017 年 1 月 11 日 
2018 年 2 月 24 日
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/binary-watch/
  [2]: https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg
