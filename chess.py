import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class chess():
    def __init__(self):
        self.rotate_flag=0
        self.reverse_flag=0

    def reverse(self):
        self.chess=self.chess.T
        self.reverse_flag=(self.reverse_flag+1)%2
        self.rotate_flag=self.rotate_flag%4

    def rotate(self):
        ori_shape=self.chess.shape
        temp_chess=np.zeros([ori_shape[1],ori_shape[0]])
        for i in range(ori_shape[1]):
            for j in range(ori_shape[0]):
                temp_chess[i,j]=self.chess[ori_shape[0]-j-1,i]
        self.chess=temp_chess
        self.rotate_flag=(self.rotate_flag+1)%4

    def plot_chess(self):
        fig, ax = plt.subplots()
        shape=self.chess.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                place=np.array([j,shape[0]-i-1])
                if self.chess[i,j]:
                    color="r"
                else:
                    color="w"
                rec=patches.Rectangle(xy=place,width=1,height=1,color=color)
                ax.add_patch(rec)
        plt.axis('equal')
        plt.grid()
        plt.show()

class chess0(chess):
    # chess 0
    #   .
    def __init__(self):
        self.chess=np.ones([1,1] ,dtype=bool)
        self.count=1
        super(chess0,self).__init__()

class chess1(chess):
    # chess 1
    #   ..
    def __init__(self):
        self.chess=np.ones([1,2] ,dtype=bool)
        self.count=2
        super(chess1,self).__init__()

class chess2(chess):
    # chess 2
    #   ...
    def __init__(self):
        self.chess = np.ones([1, 3] ,dtype=bool)
        self.count=3
        super(chess2, self).__init__()
        
class chess3(chess):
    # chess 3
    #    .
    #   ..
    def __init__(self):
        self.chess = np.ones([2, 2] ,dtype=bool)
        self.chess[0,0]=0
        self.count=3
        super(chess3, self).__init__()
        
class chess4(chess):
    # chess 4
    #   ....
    def __init__(self):
        self.chess = np.ones([1, 4] ,dtype=bool)
        self.count=4
        super(chess4, self).__init__()
        
class chess5(chess):
    # chess 5
    #    .
    #    .
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 2] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.count = 4
        super(chess5, self).__init__()
        
class chess6(chess):
    # chess 6
    #    .
    #   ...
    def __init__(self):
        self.chess = np.ones([2, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[0,2]=0
        self.count = 4
        super(chess6, self).__init__()
        
class chess7(chess):
    # chess 7
    #   ..
    #   ..
    def __init__(self):
        self.chess = np.ones([2, 2] ,dtype=bool)
        self.count = 4
        super(chess7, self).__init__()
        
class chess8(chess):
    # chess 8
    #    ..
    #   ..
    def __init__(self):
        self.chess = np.ones([2, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,2]=0
        self.count = 4
        super(chess8, self).__init__()
        
class chess9(chess):
    # chess 9
    #   .....
    def __init__(self):
        self.chess = np.ones([1, 5] ,dtype=bool)
        self.count=5
        super(chess9, self).__init__()
        
class chess10(chess):
    # chess 10
    #    .
    #    .
    #    .
    #   ..
    def __init__(self):
        self.chess = np.ones([4, 2] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.chess[2,0]=0
        self.count = 5
        super(chess10, self).__init__()
        
class chess11(chess):
    # chess 11
    #    .
    #    .
    #   ..
    #   .
    def __init__(self):
        self.chess = np.ones([4, 2] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.chess[3,1]=0
        self.count = 5
        super(chess11, self).__init__()
        
class chess12(chess):
    # chess 12
    #    .
    #   ..
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 2] ,dtype=bool)
        self.chess[0,0]=0
        self.count = 5
        super(chess12, self).__init__()
        
class chess13(chess):
    # chess 13
    #   ..
    #    .
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 2] ,dtype=bool)
        self.chess[1,0]=0
        self.count = 5
        super(chess13, self).__init__()
        
class chess14(chess):
    # chess 14
    #    .
    #   ....
    def __init__(self):
        self.chess = np.ones([2, 4] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[0,2]=0
        self.chess[0,3]=0
        self.count = 5
        super(chess14, self).__init__()
        
class chess15(chess):
    # chess 15
    #    .
    #    .
    #   ...
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.chess[0,2]=0
        self.chess[1,2]=0
        self.count = 5
        super(chess15, self).__init__()
        
class chess16(chess):
    # chess 16
    #     .
    #     .
    #   ...
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[0,1]=0
        self.chess[1,0]=0
        self.chess[1,1]=0
        self.count = 5
        super(chess16, self).__init__()
        
class chess17(chess):
    # chess 17
    #     .
    #    ..
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[0,1]=0
        self.chess[1,0]=0
        self.chess[2,2]=0
        self.count = 5
        super(chess17, self).__init__()
        
class chess18(chess):
    # chess 18
    #    ..
    #    .
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.chess[1,2]=0
        self.chess[2,2]=0
        self.count = 5
        super(chess18, self).__init__()
        
class chess19(chess):
    # chess 19
    #    .
    #    ..
    #   ..
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[1,0]=0
        self.chess[0,2]=0
        self.chess[2,2]=0
        self.count = 5
        super(chess19, self).__init__()
        
class chess20(chess):
    # chess 20
    #    .
    #   ...
    #    .
    def __init__(self):
        self.chess = np.ones([3, 3] ,dtype=bool)
        self.chess[0,0]=0
        self.chess[0,2]=0
        self.chess[2,0]=0
        self.chess[2,2]=0
        self.count = 5
        super(chess20, self).__init__()


if __name__=="__main__":
    chesses=[
        chess0(),chess1(),chess2(),chess3(),chess4(),chess5(),chess6(),
        chess7(),chess8(),chess9(),chess10(),chess11(),chess12(),chess13(),
        chess14(),chess15(),chess16(),chess17(),chess18(),chess19(),chess20()
    ]
    for i,eachchess in enumerate(chesses):
        print(i)
        eachchess.plot_chess()