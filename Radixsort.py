#coding: utf-8;

import math


class Radixsort(object):

    def sort(self, list, radix=10):#形参radix若有传入值则为该值，若无则为默认值10
        heap = int(math.ceil(math.log(max(list), radix)))
        bucket = [[] for i in range(0, radix)]#创建指定大小的数组
        print len(bucket)
        for i in range(0, heap):
            for item in list:
                bucket[item/(10**i)%10].append(item)
            del list[:]#删除数组
            for item in bucket:
                list += item
                del item[:]
    

if __name__=="__main__":
    
    sort = Radixsort()

    content = open("data.txt")
    list = []
    for line in content.readlines():
        list.append(int(line))

    print "raw list: ", list
    sort.sort(list)
    print "result: ", list



            
