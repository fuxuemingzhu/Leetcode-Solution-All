
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
个人公众号：负雪明烛
本文关键词：两数相加，链表，求加法，题解，leetcode, 力扣，python, c++, java

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/add-two-numbers/description/


# 题目描述

You are given two ``non-empty`` linked lists representing two non-negative integers. The digits are stored in ``reverse order`` and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

# 题目大意

有两个链表，分别是逆序了的十进制数字。现在要求两个十位数字的和，要求返回的结果也是链表。

# 解题方法
## 十进制加法
我们先回顾一下十进制加法的计算过程：

![加法.001.jpeg](https://img-blog.csdnimg.cn/img_convert/40e5641e8d1c2011a7db9fbb5424ef0d.png)


**使用「竖式」计算十进制的加法的方式：**

1. 两个「**加数**」的右端对齐；
1. 从最右侧开始，依次计算对应的两位数字的和。如果和大于等于 10，则把和的个位数字计入结果，并向前面进位。
1. 依次向左计算对应位置两位数字的和，如果有进位需要加上进位。如果和大于等于 10，仍然把和的个位数字计入结果，并向前面进位。
1. 当两个「**加数**」的每个位置都计算完成，如果最后仍有进位，需要把进位数字保留到计算结果中。




## 链表相加
本题中的两个链表表示的数字是个位在前，高位在后。
​

所以，我们可以从两个链表的开头开始同时向后遍历，模拟上面加法的过程。[图源](https://leetcode.com/problems/add-two-numbers/solution/)。
​

![image.png](https://img-blog.csdnimg.cn/img_convert/2f86beba9dfa163212ec030dabf1be9c.png)


---
可以用两种做法：**循环 + 递归**。
​

## 在实现中需要注意的有：

1. 不可以把链表先转化成 int 型数字再求和，因为**可能溢出**；
1. 两个「**加数**」的字符串长度可能不同；
1. 在最后，如果进位 `carry` 不为 0，那么**最后需要计算进位**；

​

## 方法一：循环
循环的思想比较朴素，就是两个指针同时遍历两个链表每个节点并相加的过程。
### 代码中的巧妙之处：

1. `while (i >= 0 || j >= 0 || carry != 0)`含义：
   1. 链表 `a` 和 `b` 只要有一个没遍历完，那么就继续遍历；
   1. 如果链表 `a` 和 `b` 都遍历完了，但是最后留下的进位 `carry != 0`，那么需要把进位也保留到结果中。
2. 取 `a` 和 `b` 当前位置数字 的时候，如果链表 `a` 或 `b` 已经遍历完了（即 $i <= 0$ 或者 $j <= 0$），则认为 `a` 和 `b` 的对应位置是 $0$ 。


Java 代码如下：

```Java 
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int i1 = l1 != null ? l1.val : 0;
            int i2 = l2 != null ? l2.val : 0;
            int add = i1 + i2 + carry;
            carry = add >= 10 ? 1 : 0;
            add = add >= 10 ? add - 10 : add;
            cur.next = new ListNode(add);
            cur = cur.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return dummy.next;
    }
}
```

C++ 代码如下：

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            int i1 = l1 ? l1->val : 0;
            int i2 = l2 ? l2->val : 0;
            int add = i1 + i2 + carry;
            carry = add >= 10 ? 1 : 0;
            add = add >= 10 ? add - 10 : add;
            cur->next = new ListNode(add);
            cur = cur->next;
            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
        }
        return dummy->next;
    }
};
```

Python 代码如下：

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            i1 = l1.val if l1 else 0
            i2 = l2.val if l2 else 0
            add = i1 + i2 + carry
            carry = 1 if add >= 10 else 0
            add = add - 10 if add >= 10 else add
            cur.next = ListNode(add)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

复杂度分析：

- 时间复杂度：$O(max(M, N))$，$M$ 和 $N$ 分别是链表 `a` 和 `b` 的长度；
- 空间复杂度：$O(1)$，只使用了常数的空间。

​

## 方法二：递归


递归解法非常巧妙。
​

> 做递归题目一定要牢记「递归函数的定义」。

​

**递归函数定义**：`addTwoNumbers` 表示将两个链表 `l1` 和 `l2` 相加得到的新链表；
**递归终止条件**：如果 `l1` 和 `l2` 有一个为空，则返回另外一个。
**递归函数内容**：

- 把两个链表节点的值相加（结果记为 `add` ）。把 `add` 模 $10$ 作为当前的链表节点的值。
- 把两个链表的 `next` 节点相加。（注意：如果当前相加的结果 $add >= 10$，需要把 $next$ 节点相加得到的结果 `+ 1`。）

​
递归解法妙在天然地处理好了两个链表不一样长、最终相加结果有进位的情况。


Java 代码如下：

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        int add = l1.val + l2.val;
        ListNode res = new ListNode(add % 10);
        res.next = addTwoNumbers(l1.next, l2.next);
        if (add >= 10)
            res.next = addTwoNumbers(res.next, new ListNode(1));
        return res;
    }
}
```

C++ 代码如下：

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        int target = l1->val + l2->val;
        ListNode* res = new ListNode(target % 10);
        res->next = addTwoNumbers(l1->next, l2->next);
        if (target >= 10)
            res->next = addTwoNumbers(res->next, new ListNode(1));
        delete l1, l2;
        return res;
    }
};
```

Python 代码如下：

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        add = l1.val + l2.val
        res = ListNode(add % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)
        if add >= 10:
            res.next = self.addTwoNumbers(res.next, ListNode(1))
        return res
```

# 类似题目
看完本题解本题，你可以解决以下题目：

- [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/)
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
- [66. 加一](https://leetcode-cn.com/problems/plus-one/)
- [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)

​

# 总结

1. 「**加法**」系列题目都不难，其实就是 **「列竖式」模拟法**。
1. 需要注意的是 `while`循环结束条件，注意遍历两个「加数」不要越界，以及进位。


**博主有算法题解的微信公众号啦，欢迎关注「负雪明烛」，持续更新算法题的解题思路：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/5a8961b2e3e741f4871cbe498e2b878f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6LSf6Zuq5piO54Ob,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center#pic_center#pic_center)


# 日期

2018 年 2 月 26 日 
2019 年 1 月 11 日 —— 小光棍节？
2021 年 10 月 31 日


  [1]: https://leetcode.com/problems/add-two-numbers/Figures/2_add_two_numbers.svg
