作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/number-of-atoms/description/

## 题目描述：

Given a chemical ``formula`` (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:

    Input: 
    formula = "H2O"
    Output: "H2O"
    Explanation: 
    The count of elements are {'H': 2, 'O': 1}.

Example 2:

    Input: 
    formula = "Mg(OH)2"
    Output: "H2MgO2"
    Explanation: 
    The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:

    Input: 
    formula = "K4(ON(SO3)2)2"
    Output: "K4N2O14S4"
    Explanation: 
    The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Note:

- All atom names consist of lowercase letters, except for the first character which is uppercase.
- The length of ``formula`` will be in the range [1, 1000].
- ``formula`` will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.


## 题目大意

给出了一个化学分式，计算里面的原子个数是多少，并且按照原子字母的递增有序输出。

## 解题方法

### 方法一：DFS

这个题第一眼就看到了括号，立马想到了括号匹配问题。括号匹配问题使用一个记数指针，遇到左括号加一，遇到右括号减一，如果该记数指针等于０了，说明找到了匹配的括号。在这个题中就相当于找到了一个分子团，该分子团后面会有个数字，代表这个分子团出现的次数。所以，做法就是如果不是分子团，那么统计元素的个数；如果是分子团，那么把这个分子团当做分子，计算里面元素的个数再乘以外边的分子团的个数。所以就是个DFS问题。

比较难办的就是寻找每个元素，需要根据大小写和数字等判断；寻找个数，需要把字符串转成１０进制。最后把分子式内的元素个数×分子式的个数的时候，按照元素迭代的方式做，不要使用对分子式个数的for循环去累加。

最坏的时间复杂度是O(N！)，最优时间复杂度是O(N)，空间复杂度是O(Ｎ)。其中N是分子的长度。

```python
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        count = self.dfs(formula)
        res = ""
        for atom, num in sorted(count.items()):
            if num == 1:
                res += atom
            else:
                res += atom + str(num)
        return res
        
    def dfs(self, formula):
        count = collections.Counter()
        if not formula: return count
        i = 0
        while i < len(formula):
            if formula[i].isalpha(): # 首字母是英文字符
                atom = formula[i]
                atomNum = 0
                # 找到这个元素所有字符
                i += 1
                while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    atom += formula[i]
                    i += 1
                while i < len(formula) and formula[i].isdigit(): # 后面是否有数字
                    atomNum = 10 * atomNum + int(formula[i])
                    i += 1
                count[atom] += 1 if atomNum == 0 else atomNum　＃　使用加号
            elif formula[i] == "(": # 括号匹配
                left = i # 左括号位置
                parent = 1 #　统计括号个数
                while i < len(formula) and parent != 0:
                    i += 1
                    if formula[i] == "(":
                        parent += 1
                    elif formula[i] == ")":
                        parent -= 1
                right = i
                atomNum = 0
                i += 1
                while i < len(formula) and formula[i].isdigit(): # 后面是否有数字
                    atomNum = 10 * atomNum + int(formula[i])
                    i += 1
                innerCount = self.dfs(formula[left + 1 : right])
                for c, n in innerCount.items():
                    count[c] += n * atomNum
        count += self.dfs(formula[i + 1 :])
        return count
```

### 方法二：栈

看到括号匹配，也会让人立马想到栈，其实DFS本身就是栈实现的，所以也完全可以用栈来解决。

方法是，左括号进栈，然后把字母依次进栈，当遇到右括号的时候，需要对栈进行退栈操作，这个时候要统计每个元素的次数，当退栈的时候遇到左括号，说明内部的分子团已经结束，那么把遇到的第一个左括号退栈，把内部的分子团的各个元素和其个数进栈。然后遍历就好了！这个方法的好处是，当最后遍历结束的时候，栈里面保存的只剩下了已经统计好了的各个元素和其个数的对应，每个元素只会出现一次，相当于已经做了元素的求和操作，最后只需要排序即可。

为了方便，我把分子式用括号包了起来，方便栈操作的判断。

这个题做了很久，主要是查一个bug，查了一个小时，感觉很诡异。其实仔细对比一下和上面DFS的解法，大同小异。区别是我用字母n保存了分子式的长度，然后下面退栈的for循环中又使用了n这个变量名称！！由于python不用声明变量，所以直接把外边的n覆盖掉了！！做法很简单，把内部for循环里的变量名改一下就好了！生气！！

最坏的时间复杂度是O(N！)，最优时间复杂度是O(N)，空间复杂度是O(Ｎ)。其中N是分子的长度。

代码如下：

```Python
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = list()
        formula = "(" +  formula + ")1"
        i = 0
        n = len(formula)
        
        while i < n:
            if i >= n: continue
            if formula[i] == "(":
                stack.append("(")
                i += 1
            elif formula[i] == ")":
                parentNum = 0
                i += 1
                while i < n and formula[i].isdigit():
                    parentNum = 10 * parentNum + int(formula[i])
                    i += 1
                count = collections.Counter()
                while stack[-1] != "(":
                    atom, atomNum = stack.pop()
                    count[atom] += atomNum * parentNum
                if stack[-1] == "(":
                    stack.pop()
                for c, t in count.items(): # 刚开始把变量t写成了n!!错了很多次
                    stack.append((c, t))
            elif formula[i].isalpha():
                atom = formula[i]
                atomNum = 0
                i += 1
                while i < n and formula[i].isalpha() and formula[i].islower():
                    atom += formula[i]
                    i += 1
                while i < n and formula[i].isdigit():
                    atomNum = 10 * atomNum + int(formula[i])
                    i += 1
                atomNum = 1 if atomNum == 0 else atomNum
                stack.append((atom, atomNum))
            
                    
        res = ""
        for atoms in sorted(stack):
            if atoms == "(":
                continue
            c, n = atoms
            if n == 1:
                res += c
            else:
                res += c + str(n)
        return res
```

参考资料：


## 日期

2018 年 10 月 ４ 日 —— 一个很不容易察觉的小错误，需要总结一下坑了！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80482014
  [2]: http://www.cnblogs.com/grandyang/p/8850299.html
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82931106
