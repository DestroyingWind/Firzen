class a:
    def test1(self,test2):
        print(test2(1))

class b:
    @staticmethod
    def test2(z):
        return z+1

x=a()
y=b()
x.test1(b.test2)