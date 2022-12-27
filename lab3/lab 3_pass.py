from pyDatalog import pyDatalog
import random
pyDatalog.create_terms('a, b, c, x, SM, DIV, AVER, SUMRAND')
(x[a] == sum_(c, for_each=c)) <= ((c._in(range_(a+1))))
print(x[888888] == SM)
(DIV[a, c] == b) <= (a // c == b)
print(DIV[x[888888], 888888] == AVER)
l = sorted([random.choice(range(888888)) for i in range(100)])
(x['sum_rand'] == sum_(b, for_each=b)) <= b.in_(l)
print(x['sum_rand'] == SUMRAND)
print("Median: ", (l[49] + l[50]) / 2)