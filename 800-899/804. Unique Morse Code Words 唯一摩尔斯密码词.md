
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/unique-morse-code-words/description/

## 题目描述：

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:

    Input: words = ["gin", "zen", "gig", "msg"]
    Output: 2
    Explanation: 
    The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    
    There are 2 different transformations, "--...-." and "--...--.".


Note:

- The length of words will be at most 100.
- Each words[i] will have length in range [1, 12].
- words[i] will only consist of lowercase letters.
    
## 题目大意

找出一组字符串进行莫尔斯电码的编码有多少种不同情况。

## 解题方法

### set + map

找出多少种不同的情况，完全可以用len(set())的方式进行处理。所以，先得到每个字符的莫尔斯电码，然后把字符串所有进行拼接。很简单了哈。

时间复杂度是O(n)，空间复杂度是O(1)。

代码：

```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        moorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = lambda x: moorse[ord(x) - ord('a')]
        map_word = lambda word: ''.join([trans(x) for x in word])
        res = map(map_word, words)
        return len(set(res))
```

### set + 字典

上面的做法需要ord函数，其实如果用字典速度会更快的。另外有个加速的经验就是，对字符串word+="dfs"操作是很慢的，改成word = word + "dfs"会变快很多。

时间复杂度是O(n)，空间复杂度是O(26)。


```python
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        edict = dict(zip(english, morse))
        res = set()
        for word in words:
            mword = ""
            for w in word:
                mword = mword + edict[w]
            res.add(mword)
        return len(res)
```

## 日期

2018 年 3 月 31 日 ———— 晚上睡不好，一天没精神啊
2018 年 11 月 2 日 —— 浑浑噩噩的一天
