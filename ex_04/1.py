smallest_so_far = None
print("Before",smallest_so_far)
for the_num in[9,41,12,3,74,15]:
   if the_num is None or smallest_so_far < the_num :
       smallest_so_far = the_num
   print(smallest_so_far,the_num)
print("After",smallest_so_far)
