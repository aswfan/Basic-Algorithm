#coding: utf-8;

import math
from random import randint
from collections import defaultdict

'''
    This algorithm has brought some thoughts from stuntgoat
    (https://github.com/stuntgoat/kmeans).

'''

class KMeansClustering(object):
    def distance(self, a, b):
        dimensions = min(len(a), len(b))
        val = 0
        for i in xrange(dimensions):
            val += (a[i]-b[i])**2
        return math.sqrt(val)

    def avg_center(self, data, center):
        if len(data)<1:
            return center
        centers = []
        dimensions = len(data[0])
        for i in xrange(dimensions):
            val = 0
            for point in data:
                val += point[i]
            centers.append(val/float(len(data)))
        return centers

    def update_center(self, data, category, centers):
        group = defaultdict(list)
        mCenters = []
        for i, point in zip(category, data):
            group[i].append(point)
        i = 0
        for points in group.itervalues():
            mCenters.append(self.avg_center(points, centers[i]))
            i += 1
        return mCenters
    
    def assign_points(self, data, centers):
        category = []
        for point in data:
            shortest = () #positive infinity
            shortest_index = 0
            for i in xrange(len(centers)):
                val = self.distance(point, centers[i])
                if val < shortest:
                    shortest = val
                    shortest_index = i
            category.append(shortest_index)
        return category

    def init_center(self, data, k):
        
        """
        one feasible but kind of complex method:
        
        mdict = defaultdict(double)
        dimensions = len(data[0])
        centers = []
        for i in xrange(dimensions):
            mMax = "max%d"%i
            mMin = "min%d"%i
            mdict[mMax] = 0
            mdict[mMin] = 0
            index = 0
            for point in data:
                mdict[mMax] = point[i] if point[i]>mdict[mMax] else mdict[mMax]
                mdict[mMin] = point[i] if point[i]<mdict[mMin] else mdict[mMin]
            for i in xrange(k):
                ...
        """
        
        centers = []
        length = len(data)
        for i in xrange(k):
            centers.append(data[randint(0, length-1)])
        return centers   

       
    

if __name__=="__main__":
    
    points = [
                [1, 2],
                [2, 1],
                [3, 1],
                [5, 4],
                [5, 5],
                [6, 5],
                [10, 8],
                [7, 9],
                [11, 5],
                [14, 9],
                [14, 14],
            ]
    k = 3

    cluster = KMeansClustering()
    centers = cluster.init_center(points, k)
    category = cluster.assign_points(points, centers)
    temp = []
    while category != temp:
        temp = category
        centers = cluster.update_center(points, category, centers)
        category = cluster.assign_points(points, centers)        
        
    print zip(category, points)



            
