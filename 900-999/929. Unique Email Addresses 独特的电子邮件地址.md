作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/unique-email-addresses/description/

## 题目描述

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in ``alice@leetcode.com``, ``alice`` is the local name, and ``leetcode.com`` is the domain name.

Besides lowercase letters, these emails may contain ``'.'``s or ``'+'``s.

If you add periods (``'.'``) between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, ``"alice.z@leetcode.com"`` and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus (``'+'``) in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example ``m.y+name@email.com`` will be forwarded to ``my@email.com``.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of ``emails``, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

    Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
     

Note:

1. 1 <= emails[i].length <= 100
1. 1 <= emails.length <= 100
1. Each emails[i] contains exactly one '@' character.


## 题目大意

判断有多少个不重复的email.

邮箱的规则是这样的：域名部分不用管，只管用户名部分，用户名中如果包含有``'.'``，那么把这个``'.'``给去掉；如果用户名中有``'+'``，那么把加号以及后面的用户名部分全部去掉。

## 解题方法

### set + 字符串操作

Python处理这种字符串题目简直不要太简单，这个题是周赛第一题，用了6分钟读完题目，然后提交通过了。

首先把``'.'``给替换掉，然后查找是不是包含``'+'``，如果有的话，只保留其前面的部分就好了。

因为要去重，所以要使用一个set保存所有不重复的结果。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        eset = set()
        for email in emails:
            simper = self.simpifyEmail(email)
            eset.add(simper)
        return len(eset)
    
    def simpifyEmail(self, email):
        local, domain = email.split("@")
        local = local.replace('.', '')
        plus_i = local.find('+')
        if plus_i != -1:
            local = local[:plus_i]
        return local + "@" + domain
```

代码可以优化变短，使用replace代替find函数。

```python
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0].replace(".", "")
            res.add(name + "@" + domain)
        return len(res)
```

## 参考资料


## 日期

2018 年 10 月 28 日 —— 啊，悲伤的周赛

