#coding: utf-8;

import random, time

class BFPRT:

    def topK(self, list, k, p ,q):
        if list == None or len(list)<0 :
            print "sort failed! list is None."
            return
        
        flag = self.partition(list, p, q)
        #print p, flag, q
        if flag > k:
            self.topK(list, k, p, flag-1)
        elif flag < k:
            self.topK(list, k, flag+1, q)
        else:
            print "sort success"

    def partition(self, list, p, q):
        self.random_proceed(list, p, q)
        pivot = list[q]
        i = p
        j = q
        while i<j:
            while list[i]<=pivot and i<j:
                i += 1
            list[j] = list[i]
            while list[j]>=pivot and i<j:
                j -= 1
            list[i] = list[j]
        list[i] = pivot
        return i

    #用随机数防quick_sort退化
    def random_proceed(self, list, p, q):
        rand = random.randint(p, q)
        #print rand
        list[rand], list[p] = list[p], list[rand]

    #用中位数防退化
    def mid_proceed(self, list, p, q, step=5):
        if p == q - 1:
            return
        i = 0
        while i < q-p-step:
            self.Insertsort(list, p+i, i+step)
            list[p+i/step], list[p+i+2] =  list[p+i+2], list[p+i/step]
            i +=step
        num = q - 1- p - i
        if num > 0:
            self.Insertsort(list, p+i, q)
            list[p+i/step], list[p+i+num>>1] =  list[p+i+num>>1], list[p+i/step]
            i += 5
        if i/step == 1:
            return

        self.mid_proceed(list, p, p+i/step)

    def Insertsort(self, list, p, q):
        for i in range(p+1, q):
            value = list[i]
            j = i - 1
            while list[j]>value and j>=p:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = value
        

if __name__=="__main__":

    k = 80
    
    content = open('data.txt')
    list = []
    try:
        for line in content.readlines():
            list.append(int(line))
    finally:
        content.close()

    print 'raw list:', list[0:100]

    t1 = time.time()
    sort = BFPRT()
    sort.topK(list, k, 0, len(list)-1)

    t2 = time.time()

    print "用时：", t2 - t1
    print 'the final list:', list[0:k]
