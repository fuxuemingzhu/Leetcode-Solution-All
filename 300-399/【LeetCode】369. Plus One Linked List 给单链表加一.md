- 作者： 负雪明烛
- id：	fuxuemingzhu
- 个人博客：	http://fuxuemingzhu.cn/
- 公众号：负雪明烛
- 本文关键词：Leetcode, 力扣，链表相加，两数相加，两数之和，求加法，代码模板，Python, C++, Java

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/plus-one-linked-list/


# 题目描述

用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。

你可以假设这个整数除了 0 本身，没有任何前导的 0。

这个整数的各个数位按照 **高位在链表头部、低位在链表尾部** 的顺序排列。

示例:

	输入: [1,2,3]
	输出: [1,2,4]

# 题目大意

把一个用链表表示的整数加一，仍然用链表形式返回。

# 解题方法
大家好，我是 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/)。欢迎关注。

## 前言

**加法**是我们上小学的时候开始学习的第一种数学运算。

在算法题中，「求加法」问题大多考察「**列竖式**」求和。

题目中，「两数之和」通常与其他形式表示的数字结合起来：

- **两个字符串形式的数字相加（第 415 题）**
- **两个链表形式的数字相加（第 2 、445、369 题）**
- **数组形式的数字相加（第 66 、989题）**
- **两个二进制形式的数字相加（第 67 题）**

做法都是非常类似的，本质是在考察各种数据表示形式：**字符串，链表，数组，二进制**。

我们只要掌握了用「列竖式」求「两数之和」的方法，这类题目全都可以秒杀。

## 十进制加法

我们先回顾一下十进制加法的计算过程：

![加法.001.jpeg](https://img-blog.csdnimg.cn/img_convert/40e5641e8d1c2011a7db9fbb5424ef0d.png)

**使用「竖式」计算十进制的加法的方式：**

1. 两个「**加数**」的右端对齐；
1. 从最右侧开始，从右向左依次计算对应的两位数字的和，如果有进位需要加上进位。如果和大于等于 10，则把和的个位数字计入结果，并向前面进位；
1. 重复步骤 2；
1. 当两个「**加数**」的每个位置都计算完成，如果最后仍有进位，需要把进位数字保留到计算结果中。

### 在实现中需要注意的有：

1. 不可以把链表/字符串表示的「加数」先转化成 `int` 型数字再求和，因为**可能溢出**；
1. 两个「**加数**」的字符串长度可能不同；
1. 在最后，如果进位 carry 不为 0，那么**最后需要计算进位**。
1. 注意 结果数字 是否为低位结果在前，根据题目要求判断最后**是否要反转结果**。

## 思路

本题与 [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/solution/fu-xue-ming-zhu-xiang-jie-qiu-jia-fa-xue-ofb5/) 非常类似。只需要略微修改即可。


本题中给出的链表表示的数字是个位在后，高位在前。


因为加法需要从个位数开始相加，而链表的遍历是从头部（十进制的高位）开始的，因此我们需要把链表翻转过来。
​

那么就有了两种思路：
​

**思路一：反转链表。**
**思路二：使用栈保存链表中的数字。**（栈是先进后出的，所以起到了翻转功能）
​

我是用的方法是：**不修改输入的链表**，用思路二「栈」来解决。




## 方法：栈 + 循环


#### 步骤：



1. 先把题目给出的链表遍历放到栈中；
2. 从栈中弹出栈顶数字 `digit`，计算 `adder` 之和（`adder` 在初始化的时候是 1，之后都是 0；表示链表与 1 相加），再加上进位 `carry`，得到当前位置的和 `sum`。
   1. 如果 `sum >= 10` ，那么进位 `carry = 1` ，当前位设置为 `sum - 10`。
   1. 如果 `sum < 10`，那么进位 `carry = 0`，当前位设置为 `sum`。
3. 设置新链表节点，其值为 `sum`，**逆序拼接成链表即可。**


### 代码中的巧妙之处：


1. `while (!st.empty() || adder != 0  || carry > 0) `含义： 
   1. 栈中的元素没遍历完，或者 `adder` 不为 0，那么就继续遍历；
   1. 如果栈遍历完了，但是最后留下的进位 `carry != 0`，那么需要把进位也保留到结果中。
2. 取栈顶元素的时候，如果栈已经遍历完了（即 $st.empty()$ ），则认为当前的加数是 $0$ 。
3. **逆序拼接链表的方法**：先定义了一个哑结点`dummy` ，然后每次把新构建的链表结点放到 `dummy` 和 `dummy->next` 之间，最后返回结果是 `dummy->next` 。



Java 语言的代码如下：

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode plusOne(ListNode head) {
        Stack<Integer> st = new Stack();
        while (head != null) {
            st.push(head.val);
            head = head.next;
        }
        int carry = 0;
        ListNode dummy = new ListNode(0);
        int adder = 1;
        while (!st.empty() || adder != 0 || carry > 0) {
            int digit = st.empty() ? 0 : st.pop();
            int sum = digit + adder + carry;
            carry = sum >= 10 ? 1 : 0;
            sum = sum >= 10 ? sum - 10 : sum;
            ListNode cur = new ListNode(sum);
            cur.next = dummy.next;
            dummy.next = cur;
            adder = 0;
        }
        return dummy.next;
    }
}
```

C++ 原因的代码如下：

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        stack<int> st;
        while (head) {
            st.push(head->val);
            head = head->next;
        }
        int carry = 0;
        ListNode* dummy = new ListNode(0);
        int adder = 1;
        while (!st.empty() || adder != 0 || carry > 0) {
            int digit = 0;
            if (!st.empty()) {
                digit = st.top();
                st.pop();
            }
            int sum = digit + adder + carry;
            carry = sum >= 10 ? 1 : 0;
            sum = sum >= 10 ? sum - 10 : sum;
            ListNode* cur = new ListNode(sum);
            cur->next = dummy->next;
            dummy->next = cur;
            adder = 0;
        }
        return dummy->next;
    }
};
```
Python 代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        st = []
        while head:
            st.append(head.val)
            head = head.next
        carry = 0
        dummy = ListNode(0)
        adder = 1
        while st or adder != 0 or carry > 0:
            digit = st.pop() if st else 0
            sum = digit + adder + carry
            carry = 1 if sum >= 10 else 0
            sum = sum - 10 if sum >= 10 else sum
            cur = ListNode(sum)
            cur.next = dummy.next
            dummy.next = cur
            adder = 0
        return dummy.next
```


**复杂度分析：**


- 时间复杂度：$O(max(N))$，$N$ 是链表的长度；
- 空间复杂度：$O(1)$，只使用了常数的空间。

# 类似题目

看完本文，你可以解决以下题目：

- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
- [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/)
- [369. 给单链表加一](https://leetcode-cn.com/problems/plus-one-linked-list/)
- [66. 加一](https://leetcode-cn.com/problems/plus-one/)
- [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)

# 总结

1. 「**求加法**」系列题目都不难，其实就是 **「列竖式」** 计算。
1. 需要注意的是：
   1. while循环结束条件；
   1. 遍历「加数」不要越界；
   1. 进位；
   1. 链表在插入的时候如何进行反转。

---

我是 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/) ，刷算法题 1000 多道，写了 1000 多篇算法题解，收获阅读量 300 万。**关注我**，你将不会错过我的精彩动画题解、面试题分享、组队刷题活动，进入主页 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/) 右侧有刷题组织，从此刷题不再孤单。

- 在刷题的时候，如果你不知道该怎么刷题，可以看 [LeetCode 应该怎么刷？](https://mp.weixin.qq.com/s/viDYrSlF5INEhVWiJhM2EQ)
- 如果你觉得题目太多，想在短时间内快速提高，可以看 [LeetCode 最经典的 100 道题](https://mp.weixin.qq.com/s/e51CEkEP6Wz850JYbgz8dw)。


# 日期

2017 年 1 月 12 日 
2018 年 11 月 19 日 —— 周一又开始了
2021 年 11 月 3 日 —— 求加法的题目全都更新完了
