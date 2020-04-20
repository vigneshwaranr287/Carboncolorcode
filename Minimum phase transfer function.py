#### This program is to get the polar plot of a stable and linear system and frequency
#### parameters of the same system using the given pole and zero positions. Additionally,
#### it can find the value of "k".(Constant value)(i.e,)for how much the system must be scaled 
#### to get the desired GM/PM/BOTH.
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

################//FUNCTION TO FIND THE CLOSEST WITH THE SAME SIGN//###############

def closestsamesign(list1,k): 
  list2=[]
  for i in list1:
    if(i>k):
        list2=list2+[abs(k-i)]
    elif(i<k):
        list2=list2+[abs(k-i)]
    else:
        list2=list2+[0]
  return(list1[list2.index(min(list2))])

##########// FUNCTION TO FIND THE CLOSEST IRRESPECTIVE OF THE SIGN//############

def closest(list1,k): 
  list2=[]
  for i in list1:
    if(i>k):
        if(i>0 and k<0):
            list2=list2+[abs(-i-k)]
        elif(i<0 and k<0):
            list2=list2+[abs(k-i)]
        elif(i>0 and k>0):
            list2=list2+[i-k]
        else:
            list2=list2+[abs(k)]

    elif(i<k):
        if(i>0 and k>0):
              list2=list2+[k-i]
        elif(i<0 and k>0):
              list2=list2+[k+i]
        elif(i<0 and k<0):
              list2=list2+[abs(i-k)]
        else:
              list2=list2+[abs(k)]
    else:
        list2=list2+[0]
  return(list1[list2.index(min(list2))])

########################//TO GET POLE AND ZERO POSITION//#######################
print("Message : We recommend the user to give no of poles<5 and >0")
p=int(input("Enter the number of poles"))
while(p>4 or p<1):
   print("Error : Oops! The number of poles must be <5 and >0")
   p=int(input("Enter the number of poles again"))
print("Message : We recommend the user to give no of zeros<3 and >=0")
z=int(input("Enter the number of zeros"))
while (z>2 or z<0):
   print("Error : Oops! The number of zeros must be <3 and >0")
   z=int(input("Enter the number of zeros again"))
isk=input("Is there any constant in the numerator other than 1")
print("Message : Poles and zeors must be at the left side of jw line,poles can be at 0 but zeros should not be at 0 for a stable linear system")
x=[]  #list to contain pole positions
xz=[]  #list to contain zero values
d=[]  #list to contain pole sample values wrt w
e=[]  #list to contain zero sample values wrt w
typ=0   #variable to calculate type of the system
str1=""  
str2=""

#######################// TO SAMPLE THE VALUES OF W//###########################

x1=np.arange(0.1,50,0.05).tolist()
w=[]
for i in x1:
   w=w+[round(i,3)]
y=len(w)

for i in range(0,y):
           d=d+[1]
           e=e+[1]

#######################// TO FIND POLE SAMPLES WRT VALUES OF W//################

for j in range(0,p):
    p1=eval(input("Enter pole position"))
    while(p1>0):
       print("Unstable systems can not be analysed using polar plots")
       p1=eval(input("Enter a valid pole position:"))
    if(p1==0):
        for i in range(0,y):
           d[i]=d[i]*(complex(0,w[i]))
    else:
        for i in range(0,y):
           d[i]=d[i]*(complex(1,(1/abs(p1))*w[i]))
    x=x+[-p1]

                      
############################// TO PRINT THE POLES //############################
for i in range(0,p):
    if(x[i]>0):
        str1=str1+"(s+"+str(x[i])+")"
    else:
        typ+=1
        str1=str1+"s"

#######################// TO FIND ZERO SAMPLES WRT VALUES OF W//################

for j in range(0,z):
    z1=eval(input("Enter the zero position"))
    while(z1>=0):
       print("Unstable systems can not be analysed using polar plots")
       z1=eval(input("Enter a valid zero position:"))
    for i in range(0,y):
           e[i]=e[i]*(complex(1,(1/abs(z1))*w[i]))
    xz=xz+[abs(z1)]

if(isk=="yes"):
    k=eval(input("Enter the value of k:"))
    str2=str2+str(k)
else:
    if(z==0):
        k=1
        str2=str2+str(k)
    else:
        k=1
        str2=str2
        


#######################// TO PRINT THE ZEROS //#################################

for i in range(0,z):
      if(xz[i]>0):
          str2=str2+"(s+"+str(xz[i])+")"
      else:
          str2=str2+"s"
poles=[]
zeros=[]
for i in x:
  poles=poles+[-i]
for i in xz:
  zeros=zeros+[-i]
print("\n")
print("Poles of your system:",poles)
print("Zeros of your system:",zeros)
print("Transfer function of the system is:"+str2+"/"+str1)
if(p<=4):
  print("\n")
  print("System you want to analyse is of order",p," and type",typ,sep="")
  Dictord={1:"270 degree",2:"180 degree",3:"90 degree",4:"0 degree"}
  Dicttyp={0:"0 degree",1:"270 degree",2:"180 degree",3:"90 degree"}
  print("Polar plot starts at",Dicttyp[typ],"ends at",Dictord[p])

#######################//TO CALCULATE MAGNITUDE & PHASE OF SAMPLES//##############

f=[]
m=[]
ph=[]
for i in range(0,y):
   f=f+[k*(e[i]/d[i])]
   pair=cmath.polar(f[i])
   m=m+[round(pair[0],3)]
   ph=ph+[round(pair[1],3)]
data_theta=[]
for i in range(0,len(ph)):
    data_theta=data_theta+[ph[i]*180/3.14]
    data_theta[i]=math.trunc(data_theta[i])


g=closest(data_theta,180)
print("\n") 
print("The closest value to 180 is",g)

if(((g<170 or g>190) and g>0) or ((g>-170 or g<-190 )and g<0)):
   print("Gain Margin in linearscale is",0)
   print("Gain Margin in db scale is",1)
else: 
   u=m[data_theta.index(g)]
   print("The phase crossover frequency in (rad/s):",w[data_theta.index(g)])
   print("Gain Margin in linearscale:",1/u)
   print("Gain Margin in db:",20*math.log10(1/u))
h=closest(m,1)
print("\n")
print("The closest magnitude to 1 is",h)
print("The gain crossover frequency in (rad/s):",w[m.index(h)])
print("Phase Margin in degrees:",180+data_theta[m.index(h)])


############// TO FIND THE VALUE OF CONSTANT(K) FOR THE DESIRED PM/GM //#####


q=input("\nDo you want to find the value of K(constant) so as to get desired Phase/Gain Marginwithout changing the pole/zero position?")
if(q=="yes"):
      print("\n")
      print("Enter 1 if you want to design for desired PM")
      if(((g>170 and g<190) and g>0) or ((g<-170 and g>-190 )and g<0)):
            print("Enter -1 if you want to design for desired GM")
            print("Enter 0 if you want to design for desired PM and GM seperately")
      r=eval(input())
      if(r>=0):
            pm=eval(input("Enter the desired Phase Margin:"))
            phi=pm-180
            ga=m[data_theta.index(closestsamesign(data_theta,phi))]
            print("K value for given PM",pm,"is",1/ga)
      if(r<=0):
            gm=eval(input("Enter the desired Gain Margin(in dB):"))
            ga=1/(10**(gm/20))
            gb=u
            print("K value for the given GM",gm,"(in dB) is",ga/gb)
print("Values of w(angular frequency) as samples",w)
print("Values of magnitude:",m)
print("Values of theta:",data_theta)

#########################//TO PLOT POLAR CHART//################################

data_theta2=[]
for i in data_theta:
    data_theta2.append(i*np.pi/180)
ax = plt.subplot(111, projection='polar')
ax.plot(data_theta2, m)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  
ax.set_rlabel_position(-22.5)  
ax.grid(True)

ax.set_title("A polar plot of the linear system", va='bottom')
plt.show()

################################ THE END ########################################
