from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class PointSet(object):
	
	def __init__(self,filename,delimeter):
		self.X = []; self.Y = []; self.Z = []
		
		f = open(filename).readlines()
		
		for l in f:
			l = l.split(delimeter)
			self.X.append(float(l[0]))
			self.Y.append(float(l[1]))
			self.Z.append(float(l[2]))

			
	def clear_location(self):
		minX = min(self.X)
		minY = min(self.Y)
		minZ = min(self.Z)
		for i in range(len(self.X)):
			X[i] -= minX
			Y[i] -= minY
			Z[i] -= minZ
		

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

p = PointSet('foo.asc',',')

#sample points
#X = [1,2,3,4,5,6,7,8,9]
#Y = [4,5,6,7,7,8,5,3,5]
#Z = [3,6,7,8,6,5,3,2,1]

ax.scatter(p.X,p.Y,p.Z, c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


