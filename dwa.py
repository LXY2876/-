
import  numpy as np
from math import *
class DWAplanner:
    def __init__(self,plan_x,plan_g,plan_ob):
        self.vx=plan_x[2]
        self.vw=plan_x[3]
        self.goal=plan_g
        self.ax=1
        self.aw=1
        self.t=1
        self.threshold=1.5
        self.feasible=np.array([])
        self.ob=plan_ob
        self.r=0.25
        self.v_min=max(-0.2,vx-self.ax*self.t)
        self.v_max=min(0.2,vx+self.ax*self.t)
        self.V=np.arange(v_min, v_max, 0.1)
        self.w_min=max(-0.5,vw-self.aw*self.t)
        self.w_max=min(0.5,vw+self.aw*self.t)
        self.W=np.arange(w_min,w_max,0.1)
    def plan(self):



        self.feasible=np.zeros()
        for i in range(len(self.V)):
            for j in range(len(self.W)):
                
                self.feasible[i][j]=value(self.V[i],self.W[j])
        i,j=np.where(self.feasible==self.feasible.max())
        i=int(i)
        j=int(j)
        v=V[i]
        w=W[j]
        return [v,w]

    def value(self,v,w):
        alpha=w*self.t        
        r=v*self.t/alpha
        dx=r*sin(alpha)
        dy=r-r*cos(alpha)
        flag=False
        value=-10
        for i in range(len(self.ob)):
            flag,dist=check(dx,dy)
            if flag==True:
                heading=(self.goal[0]*dx+self.goal[1]*dy)/(sqrt(pow(dx,2)+pow(dy,2))*sqrt(pow(self.goal[0],2)+pow(self.goal[1],2)))
                
                value=self.a*heading+self.b*dist/self.threshold+self.c*v/self.v_max
        return value

    def check(self,dx,dy)：
        flag=True    
        d=self.threshold
        for i in range(self.ob):
            x=self.ob[i][0]
            y=self.ob[i][1]
            
            d=min[d,sqrt(pow(x-dx,2)+pow(y-dy,2))]
            
            if d<self.r；
                flag=False
                break   
        return [flag,d]



    
 