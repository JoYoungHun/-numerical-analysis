import matplotlib as mpl


import matplotlib.font_manager

matplotlib.font_manager._rebuild()
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist if f.name.startswith("Nanum")])

# 폰트 설정
mpl.rc('font', family='NanumGothic')
# 유니코드에서  음수 부호설정
mpl.rc('axes', unicode_minus=False)

font1 = {'family': 'NanumMyeongjo', 'size': 24,
         'color':  'black'}
font2 = {'family': 'NanumBarunpen', 'size': 18, 'weight': 'bold',
         'color':  'darkred'}
font3 = {'family': 'NanumBarunGothic', 'size': 12, 'weight': 'light',
         'color':  'blue'}

import numpy as np


import matplotlib.pylab as plt

#plt.axis('equal')

from sklearn.datasets import load_digits
# digits = load_digits()
# X = digits.images[0]
# print(X)
#
# plt.title("mnist digits; 0")
# plt.imshow(X, interpolation='nearest', cmap=plt.cm.bone_r)
# plt.xticks([])
# plt.yticks([])
# plt.grid(False)
# plt.subplots_adjust(left=0.35, right=0.65, bottom=0.35, top=0.65)
# plt.show()
#
# dir(plt.cm)[:10]
# print(dir(plt.cm)[:10])
#
import matplotlib.tri as mtri

x = np.asarray([0, 1, 2, 3, 4, 2])
y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
triang = mtri.Triangulation(x, y, triangles)
# plt.title("여러개의 삼각형 그리기")
# plt.triplot(triang, 'ko-')
# plt.xlim(-0.1, 4.1)
# plt.ylim(-0.1, 3.7)
# plt.show()

refiner = mtri.UniformTriRefiner(triang)
# triang2 = refiner.refine_triangulation(subdiv=2)
# plt.title("그리드 세분화")
# plt.triplot(triang2, 'ko-')
# plt.xlim(-0.1, 4.1)
# plt.ylim(-0.1, 3.7)
# plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

triang3 = refiner.refine_triangulation(subdiv=3)
z3 = np.cos(1.5 * triang3.x) * np.cos(1.5 * triang3.y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title("삼각 그리드에서의 3D Surface Plot")
ax.plot_trisurf(triang3.x, triang3.y, z3, cmap=cm.jet, linewidth=0.2)
ax.tricontourf(triang3, z3, zdir='z', offset=-1.2, cmap=cm.coolwarm)
ax.set_zlim(-1, 1)
ax.view_init(40, -40)
plt.show()