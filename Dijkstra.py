#coding: utf-8;

import sys

class Dijkstra(object):

    def sort(self, v, n, graph, dist, flag, prev, maxint=sys.maxint):
        u = v
        flag[u] = True
        dist[u] = 0
        prev[u] = -1
        for i in range(1, n):
            #更新dist和prev
            for j in range(1, n):
                if not flag[j] and graph[u][j]<maxint:
                    ndist = dist[u] + graph[u][j]
                    if ndist < dist[j]:
                        dist[j] = ndist
                        prev[j] = u
            
            #找到最短路径并更新flag
            temp = maxint
            for j in range(1, n):
                if not flag[j] and graph[u][j]<temp:
                    temp = graph[u][j]
                    value = j
            u = value
            flag[u] = True

    def searchPath(self, prev, v, d):
        path = []
        u = d
        path.append(u)
        while prev[u] != v:
            u = prev[u]
            if u < 0:
                print "起始地%d与目标地%d之间不存在通路"%(v, d)
                return
            path.append(u)
        path.append(v)
        return path

    def init(self, n, filePath):
        
        #初始化flag
        flag = [False for i in range(0, n)]

        #初始化dist
        dist = [sys.maxint for i in range(0, n)]

        #初始化prev
        prev = [-1 for i in range(0, n)]

        #初始化data
        content = open(filePath)
        graph = [[sys.maxint for i in range(0, n)] for i in range(0, n)]
        for line in content.readlines():
            line = map(eval, line.split(" "))
            graph[line[0]][line[1]] = line[2]
            graph[line[1]][line[0]] = line[2]

        return dist, flag, prev, graph
    

if __name__=="__main__":
    
    sort = Dijkstra()
    filePath = "data4Dijkstra.txt"
    n = 5
    v = 1
    d = 3
    n += 1
    dist, flag, prev, graph = sort.init(n,filePath)
    sort.sort(v, n, graph, dist, flag, prev)
    path = sort.searchPath(prev, v, d)[::-1]
    print "prev:", prev[1:n]
    print "dist:", dist[1:n]
    
    print reduce(lambda x,y: str(x)+'->'+str(y), path)



            
