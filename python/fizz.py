def fizzbuzz():
 for i in range(1,100):
    print("fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)
   
print(fizzbuzz())
   