
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/subdomain-visit-count/description/

## 题目描述

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
    
    Input: 
    ["9001 discuss.leetcode.com"]
    
    Output: 
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    
    Explanation: 
    We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
    
Example 2:
    
    Input: 
    ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    Output: 
    ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    
    Explanation: 
    We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

1. The length of cpdomains will not exceed 100. 
1. The length of each domain name will not exceed 100.
1. Each address will have either 1 or 2 "." characters.
1. The input count in any count-paired domain will not exceed 10000.
    
## 题目大意

互联网在访问某个域名的时候也会访问其上层域名，现在告诉你访问该域名的次数，统计所有域名被访问的次数。

## 解题方法

### 字典统计次数

这个题逻辑并不复杂，就是使用字典来保存每个域名被访问的次数。有点难点的地方是要得到每个域名及其所有上级域名，我使用的while循环和字符串切片来完成这个操作。

代码：

```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            times, domains = cpdomain.split()
            times = int(times)
            domain_counts[domains] += times
            while '.' in domains:
                domains = domains[domains.index('.') + 1:]
                domain_counts[domains] += times
        return [str(v) + ' ' + d for d, v in domain_counts.items()]
```

二刷的时候基本同样的方法，但是并没有每次都去更改子域名，而是使用了遍历的方式。

```python
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ")
            times = int(times)
            count[domain] += times
            for i, c in enumerate(domain):
                if c == '.':
                    count[domain[i + 1 : ]] += times
        return [str(times) + " " + domain for domain, times in count.items()]
```

## 日期

2018 年 4 月 2 日 —— 要开始准备ACM了
2018 年 11 月 6 日 —— 腰酸背痛要废了

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79787425
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79787660
