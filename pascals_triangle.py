"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Pascal's Triangle is like
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
"""


def generate(numRows: int):
    ans = []
    for i in range(numRows):
        if i < 2:
            ans.append([1 for _ in range(i + 1)])
        else:
            temp = [
                ans[i - 1][j] + ans[i - 1][j + 1] for j in range(len(ans[i - 1]) - 1)
            ]
            temp.insert(0, 1)
            temp.append(1)
            ans.append(temp)
    return ans


print(generate(6))
