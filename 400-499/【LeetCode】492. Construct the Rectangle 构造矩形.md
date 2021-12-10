
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/construct-the-rectangle/#/description][1]


## 题目描述

For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

    1. The area of the rectangular web page you designed must equal to the given target area.
    
    2. The width W should not be larger than the length L, which means L >= W.
    
    3. The difference between length L and width W should be as small as possible.

You need to output the length L and the width W of the web page you designed in sequence.

Example :

    Input: 4
    Output: [2, 2]
    Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
    But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

## 题目大意

现在要设计一个矩形网页，要求其面积是area，并且要求这个矩形的L >= W，返回L和W尽可能接近的矩形。

## 解题方法

### Java解法

这个题目的意思其实就是找出指定数的约数，并且约数尽量靠近平方根，第一个约数的值大于第二个约数。

给定的数字可以很大，千万量级，那么只能用O(n)量级的算法了。我的想法就是首先找出平方根，因为约数肯定尽量靠近了平方根。用到了数学运算sqrt，这个平方根是个double型的，转换成int型会舍去末尾小数。这样，如果强转之后的int的平方等于area，说明area能是个完全平方数，直接把平方根返回就好。否则，说明area不是平方数，只能进行遍历了。遍历的方法是从平方根强转后的int开始越来越小的遍历，这样，保证了尽量靠近了平方根。因为强转是丢失小数的，所以只能往小了遍历，才不会出现错误。然后如果能整除area，计算响应的长宽即可。注意此时的i是小的，那么应该对应宽。

循环的过程中一定不要忘记break，否则会在遍历完到1才停止。

```java
public class Solution {
    public int[] constructRectangle(int area) {
        double sqrt = Math.sqrt(area);
        int int_sqrt = (int) sqrt;
        int []answer = new int[2];
        if(int_sqrt * int_sqrt == area){
            answer[0] = int_sqrt;
            answer[1] = int_sqrt;
        }else{
            for(int i= int_sqrt; i >= 1; i--){
                if(area % i == 0){
                    answer[0] = area / i;
                    answer[1] = i;
                    break;//不要忘记
                }
            }
        }
        return answer;
    }
}
```

我的上面的想法是可行的，但是有点麻烦。可以这么简化，不用判断强转之后是否是平方根，直接循环判断。

```java
public class Solution {
    public int[] constructRectangle(int area) {
        int w = (int) Math.sqrt(area);
        while(area % w != 0){
            w--;
        }
        return new int[]{area / w, w};
    }
}
```

### python解法

```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(math.sqrt(area))
        for w in range(sqrt, 0, -1):
            if area % w == 0:
                return [area / w, w]
        return [area, 1]
```

## 日期

2017 年 4 月 3 日 
2018 年 11 月 15 日 —— 时间太快，不忍直视


  [1]: https://leetcode.com/problems/construct-the-rectangle/#/description
