作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/majority-element/](https://leetcode.com/problems/majority-element/)

Total Accepted: 110538 Total Submissions: 268289 Difficulty: Easy


## 题目描述

> Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
> 
> You may assume that the array is non-empty and the majority element always exist in the array.
> 
## 题目大意

找出数组中出现次数超过一半的数字。

## 解题方法

### 思路

第一想法，用HashMap。嗯。之前也这么做过，但是一想就不对，肯定效率太差。

然后也没想到太好的方法。但是官方给了几个思路：


> 1. 时间复杂度: O(n2) — 蛮力法: 依次检查每一个元素是否为众数
> 
> 1. 时间复杂度: O(n), 空间复杂度: O(n) — 哈希表: 维护一个每一个元素出现次数的哈希表, 然后找到出现次数最多的元素
> 
> 1. 时间复杂度: O(n log n) — 排序: 在排序后找出连续重复出现次数最多的元素
> 
> 1. 平均时间复杂度: O(n), 最坏复杂度: 无穷大 — 随机算法: 随机选取一个元素计算其是否为众数. 如果不是，就重复上一步骤直到找到为止。 由于选出众数的概率 1 / 2, 因此期望的尝试次数 < 2
> 
>1.  时间复杂度: O(n log n) — 分治法: 将数组拆成2半, 然后找出前一半的众数A和后一半的众数B。则全局众数要么是A要么是B。如果 A == B, 则它自然而然就是全局众数。 如果不是, 则A和B都是候选众数, 则至多只需要检查这两个元素的出现次数即可。
>1.  时间复杂度, T(n) = T(n/2) + 2n = O(n log n).
> 
> 1. 时间复杂度: O(n) — Moore投票算法: 我们维护一个当前的候选众数和一个初始为0的计数器。遍历数组时，我们看当前的元素x：
 	- 如果计数器是0, 我们将候选众数置为 x 并将计数器置为 1 如果计数器非0, 我们根据x与当前的候选众数是否相等对计数器+1或者-1；
 	- 一趟之后, 当前的候选众数就是所求众数. 
> 1. 时间复杂度 = O(n). 时间复杂度: O(n) — 位操作法: 我们需要32次迭代,
	- 每一次计算所有n个数的第i位的1的个数。由于众数一定存在，那么或者1的个数 0的个数多 或者反过来(但绝不会相同)。
	- 众数的第i位一定是计数较多数字。

### hashmap统计次数

加入不考虑空间复杂度，直接使用字典统计次数，然后找出出现次数最大的那个数字，就能通过。

python代码如下：

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return count.most_common(1)[0][0]
```

C++代码如下：

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        const int N = nums.size();
        unordered_map<int, int> count;
        for (int n : nums)
            ++count[n];
        for (auto& c : count) {
            if (c.second > N / 2) {
                return c.first;
            }
        }
        return -1;
    }
};
```

### 摩尔投票法 Moore Voting

这个投票方法挺好玩。就是多数派问题。

这个思路是这样的：

1. 对于v[i](1<=i<=n)，如果c此时为未知状态，则c=v[i]，t=1，递增i。
2. 如果c==v[i]，++t，递增i。
3. 如果c!=v[i]，--t，如果t==0，将c置为未知状态，递增i。 
4. 所有投票处理完毕后，如果c为未知状态，则说明不存在任何候选人的得票数过半，否则重新遍历数组v，统计候选人c的实际得票总数，如果c的得票数确实过半，则c就是最终结果。

这个做法的原理就是既然有出现次数超过一半的数字，那么我们把没出现一半的数字的次数进行抵消，出现一半以上的数字仍然不会被完全消除掉。

比如对于数据[1,2,1,1,3,1,4,4]

	i		1	2	3	4	5	6	7	8
	v[i]	1	2	1	1	3	1	4	4
	c		1	?	1	1	1	1	1	?
	t		1	0	1	2	1	2	1	0

程序运行的最终结果，c处于未知状态，说明对于投票数组v，不存在任何候选人的得票数过半。

如果v[1...9]={1,2,1,1,3,1,4,4,1}，此时c的最后状态为1，重新遍历数组v，查看候选人1的得票数是否确实过半，统计结果1出现了5次，大于9/2，所以候选人1的票数过半。

因为题目中已经保证了存在数据出现过半。所以结尾的c那个元素一定不是不确定状态，直接返回就好。



C++代码如下：

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int c = -1;
        int t = 0;
        for (int n : nums) {
            if (t == 0) {
                c = n;
                t = 1;
            } else {
                if (n == c) {
                    ++t;
                } else {
                    --t;
                }
            }
        }
        return c;
    }
};
```

python版本代码如下：

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = cm = 0
        for num in nums:
            if m == num:
                cm += 1
            elif cm == 0:
                m = num
                cm = 1
            else:
                cm -= 1
        return m
```


Java代码：

```java
public class Solution {
    public int majorityElement(int[] nums) {
        int candidate=nums[0];
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(count==0){
                candidate=nums[i];
                count++;
                continue;
            }
            if(candidate==nums[i]){
                count++;
            }else{
                count--;
                if(count==0){
                    candidate=-1;
                }
            }
        }
        return candidate;
        
    }
}
```

### 位运算统计位数

位操作法: 我们需要32次迭代, 每一次计算所有n个数的第i位的1的个数。

由于众数一定存在，那么或者1的个数0的个数多，或者反过来(但绝不会相同)。

众数的第i位一定是计数较多数字（1或0）。

这个题需要注意的是如何设置一个int的指定位是1：或上一个该指定为是1其余位是0的数字即可。

时间复杂度 = O(n).

一、指定的某一位数置1

	宏 #define setbit(x,y)  x|=(1<<y)

二、指定的某一位数置0

	宏  #define clrbit(x,y)  x&=~(1<<y)

三、指定的某一位数取反

	宏  #define reversebit(x,y)  x^=(1<<y)

三、获取的某一位的值

	宏 #define getbit(x,y)   ((x) >> (y)&1)

C++代码如下：

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        const int N = nums.size();
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            int mask = 1 << i;
            int onecount = 0;
            for (int n : nums) {
                if (n & mask) {
                    ++onecount;
                }
            }
            if (onecount > N / 2)
                res |= mask;
        }
        return res;
    }
};
```



## 相似题目

[229. Majority Element II](https://blog.csdn.net/fuxuemingzhu/article/details/83501323)

## 参考资料

[多数派问题](http://blog.csdn.net/joylnwang/article/details/7081575)
https://blog.csdn.net/qq_37858386/article/details/78419911 

## 日期

2016/5/1 0:00:49 
2018 年 10 月 29 日 —— 美好的一周又开始了
2018 年 11 月 11 日 —— 剁手节快乐
