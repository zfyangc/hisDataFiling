# coding:utf-8



class A:
    wwww= "dfsfsdf"

    def __init__(self, qq):
        self.qq=qq

print(getattr(A, "wwww"))
print(getattr(A('aaa'), "qq"))
print(A('aaaa').qq)