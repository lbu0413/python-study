# 만약 sizes의 길이가 홀 수라면 마지막 조각은 건들지 않는다.

# 1)
s = "descognail"
sizes = [3, 2, 3, 1, 1]
["des", "co", "gna", "i", "l"]
answer = "codesignal"

# ex2)
s = "secondfirst"
sizes = [6, 5]
["second", "first"]
answer = "firstsecond"


# 2
"""
Input
3 3
1 2 3
4 5 6
7 8 9

Output
7 4 1
4 5 6
9 6 3
"""


# 3
"""
string = (ab(d){3}){2}

step1#
(ab(d){3}){2} --> (abddd){2}

step2#
(abddd){2} --> abdddabddd


ex)
Input: (ab){3}(cd){2}
Output: abababcdcd

ex2)
Input: (ab(c){3}d){2}
Output: abcccdabcccd
"""
