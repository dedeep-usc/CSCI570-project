def f(a, n=100):
	import time
	time.sleep(2)
	b = [a] * n
	time.sleep(1)
	return b

from memory_profiler import memory_usage

if __name__ ==  '__main__':
	memory_usage((f, (1,), {'n' : int(1e6)}))

