class Fib(object):
    def __init__(self, age):
        self.age= age


    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        if self.age>0:
            self.age = self.age-1
            return self.age  # 返回下一个值
        raise StopIteration();
    def __getitem__(self, item):
        a=self.age
        for x in range(item):
            a = a -1
        return a
f=Fib(10)
'''
for n in Fib(10):
    print(n)
'''
print(f[6])