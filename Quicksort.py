#coding: utf-8;

import random, time

class Quicksort:

    def sort(self, list, p ,q, key=-1):
        if p < q :
            #print 'result of sort:'
            #print list
            if key > 0:
                r = self.single_partition(list, p, q)
            else:
                r = self.double_partition(list, p, q)
            self.sort(list, p, r-1)
            self.sort(list, r+1, q)
            

    def single_partition(self, list, p, q):
        self.proceed(list, p, q)
        pivot = list[q]
        i = p
        for j in range(p, q):
            if list[j] < pivot:
                if i != j:
                    list[i], list[j] = list[j], list[i]
                i += 1
        list[i], list[q] = list[q], list[i]
        return i

    def double_partition(self, list, p, q):
        self.proceed(list, p, q)
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

    def proceed(self, list, p, q):
        rand = random.randint(p, q)
        list[rand], list[q] = list[q], list[rand]

if __name__=="__main__":
    
    content = open('data.txt')
    list = []
    try:
        for line in content.readlines():
            list.append(int(line))
    finally:
        content.close()

    print 'raw list:', len(list)

    
    quick = Quicksort()
    t1 = time.time()
    quick.sort(list, 0, len(list)-1)#双向
    t2 = time.time()
    #quick.sort(list, 0, len(list)-1, 1)
    #t3 = time.time()
    print '用时：', t2 - t1
    #print '用时2：', t3 - t2
    #print 'the final list:', list[1:20]
