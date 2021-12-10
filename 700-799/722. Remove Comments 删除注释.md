# 【LeetCode】722. Remove Comments 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/remove-comments/description/

## 题目描述：

Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.
    
    Example 1:
    Input: 
    source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    
    The line by line code is visualized as below:
    /*Test program */
    int main()
    { 
      // variable declaration 
    int a, b, c;
    /* This is a test
       multiline  
       comment for 
       testing */
    a = b + c;
    }
    
    Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    
    The line by line code is visualized as below:
    int main()
    { 
      
    int a, b, c;
    a = b + c;
    }
    
    Explanation: 
    The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
    
    Example 2:
    Input: 
    source = ["a/*comment", "line", "more_comment*/b"]
    Output: ["ab"]
    Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].

Note:

1. The length of source is in the range [1, 100].
1. The length of source[i] is in the range [0, 80].
1. Every open block comment is eventually closed.
1. There are no single-quote, double-quote, or control characters in the source code.


## 题目大意

去除c++语言中的注释。包括//、/**/等。

另外请注意，如果//不是从行首开始的时候，其之前的字符都要进行保存。同理/**/也是。总之不要删除注释范围以内的东西。

## 解题方法

看似挺简单的字符串的题，也需要使用遍历去做。这个遍历的方式是加入multi变量是不是一个多行的注释。根据这个变量进行针对性的操作。如果不是多行注释，遇到``//``直接跳过，遇到``/*``要把multi改成多行标记并把i+1来跳过``*``号，如果不是上述两种注释则为正常的代码，加入字符串变量。如果是多行注释时，遇到``*/``修改multi结束多行字符串并把i+1来跳过``/``号。

需要注意的是line重新变成空字符串的位置应该在append之后呀，因为我们认为这部分字符串已经结束了。只要这样的操作才能满足题目中Example 2返回ab的结果。

```python
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        multi = False
        line = ''
        for s in source:
            i = 0
            while i < len(s):
                if not multi:
                    if s[i] == '/' and i < len(s) - 1 and s[i + 1] == '/':
                        break
                    elif s[i] == '/' and i < len(s) - 1 and s[i + 1] == '*':
                        multi = True
                        i += 1
                    else:
                        line += s[i]
                else:
                    if s[i] == '*' and i < len(s) - 1 and s[i + 1] == '/':
                        multi = False
                        i += 1
                i += 1
            if not multi and line:
                res.append(line)
                line = '' # 注意line重新设置成空字符串的位置
        return res

```

## 日期

2018 年 3 月 13 日 