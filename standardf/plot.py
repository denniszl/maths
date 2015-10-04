import numpy as np
import matplotlib.pyplot as plt
import standard

t = np.arange(1., 15., 1)

c = []
lin = []
log = []
q = []
for i in xrange(1, 15):
    c.append(standard.constant_time(i))
    lin.append(standard.linear_time(i))
    log.append(standard.logarithmic_time(i))
    q.append(standard.quadratic_time(i))
# red dashes, blue squares and green triangles
plt.plot(t, np.array(c), 'r--', t, np.array(log), 'bs',
         t, np.array(lin), 'g^', t, np.array(q), 'ro')
plt.show()
