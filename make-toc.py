from collections import defaultdict
import os

leetcodePath = "./"

solutions = os.listdir(leetcodePath)

indexes = defaultdict(list)
reversed_indexes = defaultdict()

for solu in solutions:
    if os.path.isdir(leetcodePath + solu) and not solu.startswith("."):
        for doc in os.listdir(leetcodePath + solu):
            problemId = doc.split(".")[0]
            fromPath =  leetcodePath + solu + "/" + doc.replace(" ", "\ ")
            indexes[solu].append([problemId, doc])
            reversed_indexes[doc] = solu


cates = list(indexes.keys())
print(cates)
cates.sort(key=lambda x : int(x.split("-")[0]))
for cate in cates:
    with open(leetcodePath + "toc.md", "a") as f:
        f.write("\n## " + cate + "\n")
    problems = indexes[cate]
    problems.sort(key=lambda x : int(x[0]))
    for probem in problems:
        with open(leetcodePath + "toc.md", "a") as f:
            f.write("- [" + probem[1].replace(".md", "") + "](" + reversed_indexes[probem[1]] + "/" + probem[1].replace(" ", "%20") + ")\n")

