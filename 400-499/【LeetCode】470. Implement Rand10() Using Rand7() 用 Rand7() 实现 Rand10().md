
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/implement-rand10-using-rand7/description/

## 题目描述

Given a function ``rand7`` which generates a uniform random integer in the range 1 to 7, write a function ``rand10`` which generates a uniform random integer in the range 1 to 10.

Do NOT use system's ``Math.random()``.

 

Example 1:

    Input: 1
    Output: [7]

Example 2:

    Input: 2
    Output: [8,4]

Example 3:

    Input: 3
    Output: [8,1,10]
 
Note:

1. rand7 is predefined.
1. Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

1. What is the expected value for the number of calls to rand7() function?
1. Could you minimize the number of calls to rand7()?


## 题目大意

利用一个范围在1~7的随机数产生器，构造一个范围在1～10的随机数产生器。

## 解题方法

范围在1～7的随机数产生器，即1~7各个数字出现的概率皆为1/7.
范围在1～10的随机数产生器，即1~10各个数字出现的概率皆为1/10.

这个题的构造思路是先构造一个randN，这个N必须是10的整数倍，然后randN % 10就可以得到了rand10.

所以可以从rand7先构造出rand49，再把rand49中大于等于40的都过滤掉，这样就得到了rand40，在对10取余即可。

具体一点就是：

1. rand7()等概率地产生1,2,3,4,5,6,7.
2. rand7() - 1等概率地产生[0,6].
3. (rand7() - 1) *7等概率地产生0, 7, 14, 21, 28, 35, 42
4. (rand7() - 1) * 7 + (rand7() - 1)等概率地产生[0, 48]这49个数字
5. 如果步骤4的结果大于等于40，那么就重复步骤4，直到产生的数小于40
6. 把步骤5的结果mod 10 再加1， 就会等概率的随机生成[1, 10]

所以过程是：

rand7 --> rand49 --> rand40 --> rand10.

其中，构造rand49的方式是：

    7 * (rand7() - 1) + rand7() - 1

那么，如何理解呢？上面的做法到底如果理解才能记住呢？看下面这个表格：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190123094429137.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)
看上面的表格，可以这么理解：我们先产生[1,49]之间的随机正整数，构建的方式是扔两次rand7()两次的结果分别作为表格的行和列，因此，``7 * (rand7() - 1) + rand7()``的取值范围是[1, 49]，代表上面表格的任意位置。注意，我们需要把上图黄色部分的给过滤掉，因为这9个数字超出了40的范围，即如果两次扔rand7()产生的数字在上面黄色的部分需要重新扔。得到了[1,49]之后，然后减去1 再 mod 10 再加1即可。


这个方法我觉得最好要记住。

```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return self.rand40() % 10 + 1
        
    def rand49(self):
        """
        random integer in 0 ~ 48
        """
        return 7 * (rand7() - 1) + rand7() - 1
        
    def rand40(self):
        """
        random integer in 0 ~ 40
        """
        num = self.rand49()
        while num >= 40:
            num = self.rand49()
        return num
```

C++代码如下：

```cpp
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        return rand40() % 10 + 1;
    }
    
    int rand49() {
        return (rand7() - 1) * 7 + (rand7() - 1);
    }
    
    int rand40() {
        int r = rand49();
        while (r >= 40) {
            r = rand49();
        }
        return r;
    }
};
```

## 日期

2018 年 8 月 18 日 —— 天在下雨
2019 年 1 月 23 日 —— 又一连过去了几天
