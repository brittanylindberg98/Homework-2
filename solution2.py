Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("number\tsquare\tcube")
number	square	cube
>>> for i in range(6):
	print(i,"\t",pow(i,2),"\t",pow(i,3))

	
0 	 0 	 0
1 	 1 	 1
2 	 4 	 8
3 	 9 	 27
4 	 16 	 64
5 	 25 	 125
>>> 
>>> celsius = float(input('Enter temperature in Celsius: '))
Enter temperature in Celsius: -40
>>> fahrenheit = (celsius * 9/5) +32
>>> print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
-40.0 Celsius is equal to -40.0 degree Fahrenheit
>>> Celsius = float(input('Enter temperature in Celsius: '))
Enter temperature in Celsius: 0
>>> fahrenheit = (celsius * 9/5) +32
>>> print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
-40.0 Celsius is equal to -40.0 degree Fahrenheit
>>> celsius = float(input('Enter temperature in Celsius: '))
Enter temperature in Celsius: 0
>>> fahrenheit = (celsius * 9/5) + 32
>>> print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
0.0 Celsius is equal to 32.0 degree Fahrenheit
>>> celsius = float(input('Enter temperature in Celsius: '))
Enter temperature in Celsius: 40
>>> fahrenheit = (celsius * 9/5) + 32
>>> print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
40.0 Celsius is equal to 104.0 degree Fahrenheit
>>> celsius = float(input('Enter temperature in Celsius: '))
Enter temperature in Celsius: 100
>>> fahrenheit = (celsius * 9/5) + 32
>>> print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
100.0 Celsius is equal to 212.0 degree Fahrenheit
>>> 
==================== RESTART: C:/Users/Owner/Desktop/sum.py ====================
Enter the value of a:1000
Enter the value of b:2000
Enter the value of c:4000
Sum is =  7000
>>> 
================== RESTART: C:/Users/Owner/Desktop/average.py ==================
Enter the value of a:1000
Enter the value of b:2000
Enter the value of c:4000
Average is =  2333.3333333333335
>>> 