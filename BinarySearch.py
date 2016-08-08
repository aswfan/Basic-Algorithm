#coding: utf-8;

from Quicksort import Quicksort

class BinarySearch(object):

    def bSearch(self, list, left, right, target):
        while left < right:
            mid = (left + right)>>1
            if target > list[mid]:
                left = mid + 1
            elif target <list[mid]:
                right = mid -1
            else:
                return mid
        return -1

if __name__=="__main__":

    target = 21
    
    sort = Quicksort()
    search = BinarySearch()

    content = open("data.txt")
    list = []
    for line in content.readlines():
        list.append(int(line))

    if list == None or len(list)<0:
        print "查找失败数列的长度小于0！"
    else:
        sort.sort(list, 0, len(list)-1)
        print list
        result = search.bSearch(list, 0, len(list)-1, target)
        if result>=0:
            print "找到目标值，位于数列的第%d个位置！"%(result+1)
        else:
            print "未找到目标值！"



            
