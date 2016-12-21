#coding: utf-8;

import pickle  

bb = [0 for i in range(10)]
f = open('d:\\p.txt','r')  
bb = pickle.load(f)  
f.close()  
print bb 
            
