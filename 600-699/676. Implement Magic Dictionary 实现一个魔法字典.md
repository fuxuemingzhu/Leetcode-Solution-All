
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/implement-magic-dictionary/description/

## 题目描述

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False

Note:

1. You may assume that all the inputs are consist of lowercase letters a-z.
1. For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
1. Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.



## 题目大意

判断只修改一个字符的情况下，能不能把search()输入的字符串变成buildDict()中已有的字符。

## 解题方法

### 字典

这个题可以直接使用dict完成。我们在进行buildDict()操作的时候就统计出如果修改一个字符能变成的字符串的个数。在search的过程中，我们要同样的看该word在修改一个字符的情况下能变成哪些字符串。

注意题目中说search时不能和已有的字符串完全一样，但是如果修改该词的某个字符构成的字符串能在buildDict()中出现的次数>1，那么说明可被与其不等的其他的字符串修改一个字符串构成。

顺便学习了一下python运算符的优先级：

    优先级关系：or<and<not，同一优先级默认从左往右计算。

用案例进行说明：

``Your input``
    
    ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    [[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    [[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    
``Your stdout``
    
    set([u'hello', u'leetcode'])
    Counter({u'leetc*de': 1, u'*ello': 1, u'lee*code': 1, u'le*tcode': 1, u'leetco*e': 1, u'h*llo': 1, u'hel*o': 1, u'l*etcode': 1, u'leetcod*': 1, u'*eetcode': 1, u'hell*': 1, u'he*lo': 1, u'leet*ode': 1})
    set([u'hallo', u'hello', u'leetcode'])
    Counter({u'h*llo': 2, u'leetc*de': 1, u'*ello': 1, u'hall*': 1, u'ha*lo': 1, u'le*tcode': 1, u'hal*o': 1, u'hel*o': 1, u'l*etcode': 1, u'leetco*e': 1, u'leetcod*': 1, u'lee*code': 1, u'*allo': 1, u'hell*': 1, u'he*lo': 1, u'*eetcode': 1, u'leet*ode': 1})
    
``Your answer``
    
    [null,null,false,true,false,false]
    [null,null,true,true,false,false]

代码：

```python
class MagicDictionary(object):
    
    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.words = set(words)
        print self.words
        self.near = collections.Counter([word for word in words for word in self._candidate(word)])
        print self.near

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return any(self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidate(word))


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
```

### 汉明间距

题目的意思其实就是找汉明间距为1的字符串。

二刷的时候，使用更简单的方法。首先判断字符串长度是否相等，在相等的情况下，判断字符串之间不同的字符是不是只有一位，如果是的话，那就返回true；如果遍历结束都没找到最后的结果，就返回false;

```cpp
class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        d = dict;
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        for (string wd : d) {
            const int N = wd.size();
            if (N == word.size()) {
                int diff = 0;
                for (int i = 0; i < N; ++i) {
                    if (wd[i] != word[i])
                        diff ++;
                }
                if (diff == 1) 
                    return true;
            }
        }
        return false;
    }
private:
    vector<string> d;
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */
```

## 日期

2018 年 3 月 5 日 
2018 年 12 月 18 日 —— 改革开放40周年
