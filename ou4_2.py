#!/usr/bin/env python3
import matplotlib.pyplot as plt
from heltal import Heltal
from time import perf_counter as pc
def main():
	f = Heltal(5)
	print(f.get())
	f.set(7)
	print(f.get())
	py_times = []
	c_times = []
	for i in range(30,31):
		start = pc()
		fib_py(i)
		end = pc()
		py_times.append(round(end - start, 2))
		start = pc()
		f.fib(i)
		end = pc()
		c_times.append(round(end - start, 2))
	fig, ax = plt.subplots()

	ax.scatter(range(30,31), py_times, color='g', marker='s')
	ax.scatter(range(30,31), c_times, color='r', marker='s')
	fig.savefig("Python vs C")
	#print(f.fib(47)) #


def fib_py(n):
	if n <= 1:
		return n
	else:
 		return(fib_py(n-1) + fib_py(n-2))

if __name__ == '__main__':
	main()