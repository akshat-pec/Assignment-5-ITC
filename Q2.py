lower_num = int(input("Enter lower range limit : "))
upper_num = int(input("Enter upper range limit : "))
div_num = int(input("Enter the number that should be divided by : "))
for i in range(lower_num,upper_num+1):
   if( i%div_num==0 ):
      print(i)
else:
       print("Oops")
