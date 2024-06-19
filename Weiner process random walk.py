import matplotlib.pyplot as plt
import random
import math

def binaryStepSelection():
    if (random.random()<0.5):
        binaryStep=-1
    else:
        binaryStep=1

    return binaryStep

def RandomWalk():
    steps=int(input("Enter the number of steps"))
    stepSize=1/math.sqrt(steps)
    step=[0 for i in range(steps)]
    
    walk=[0 for i in range(steps)]
    
    walk[1]=binaryStepSelection()*stepSize
    for i in range(2,steps):
        walk[i]=walk[i-1]+binaryStepSelection()*stepSize
        i+=1

    for j in range(1,steps):
        step[j]=j
        j+=1
    
    plt.plot(step,walk)

    return plt.show()

RandomWalk()

