

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/anagrams/#/description][1]


## 题目描述


Given an array of strings, group anagrams together.

Example:

	Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
	
	Output:
	[
	  ["ate","eat","tea"],
	  ["nat","tan"],
	  ["bat"]
	]

Note:

1. All inputs will be in lowercase.
1. The order of your output does not matter.

## 题目大意

把相同字符的字符串组成相同的group，然后返回。

## 解题方法

### 排序+hash

这个题目方法很容易想到，只要判断两个字符串是不是相同字符组成的就好了。一种简单的方法是使用hash保存对每个字符串按字母表重新排序的结果。这样的好处在字符串的长度都很短，排序花销很小，这样就可以加快运行速度。

时间复杂度在O(n*m*log(m))。其中m是字符串的长度。

```java
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
		if (strs == null || strs.length == 0) {
			List<List<String>> ans = new ArrayList<List<String>>();
			return ans;
		}
		HashMap<String, List<String>> hash = new HashMap<String, List<String>>();
		for (String s : strs) {
			char ca[] = s.toCharArray();
			Arrays.sort(ca);
			String temp = String.valueOf(ca);
			if (!hash.containsKey(temp)) {
				List<String> vals = new ArrayList<String>();
				vals.add(s);
				hash.put(temp, vals);
			} else {
				hash.get(temp).add(s);
			}
		}
		List<List<String>> ans = new ArrayList<List<String>>();
		ans.addAll(hash.values());
		return ans;
    }
}
```

---
二刷  python

对字符串进行排序，同样的字符串聚集在一起，用列表保存在一起就好了。

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()
```

---

三刷，C++

在C++里面注意sort是在原地操作的，所以要把字符串复制一份，否则会修改原来的字符串。

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m_;
        for (string str: strs) {
            string sort_str = str;
            sort(sort_str.begin(), sort_str.end());
            m_[sort_str].push_back(str);
        }
        vector<vector<string>> res;
        for (auto m : m_) {
            res.push_back(m.second);
        }
        return res;
    }
};
```

## 日期

2017 年 4 月 9 日 
2018 年 3 月 21 日
2019 年 1 月 2 日 —— 2019年开刷


  [1]: https://leetcode.com/problems/anagrams/#/description
