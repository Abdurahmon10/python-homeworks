import matplotlib.pyplot as plt
import numpy as np
import math

# #1

# x=np.arange(-10,10,0.001)
# y=(x**2-4*x+4)

# fx=plt.subplot()

# fx.plot(x,y)

# fx.spines["right"].set_position("zero")
# fx.spines["top"].set_position("zero")

# fx.spines["left"].set_color("none")
# fx.spines["bottom"].set_color("none")

# fx.set_xlabel("X-axis",size=12,labelpad=-20,x=1.0,rotation=1)
# fx.set_xlabel("Y-axis",size=12,labelpad=-20,x=1.0,rotation=0)

# fx.xaxis.set_label_coords(1.05,0.5)
# fx.xaxis.set_label_coords(0.5,1.05)



# # Optional: Add grid
# fx.grid(True)


# plt.show()


# #2
# pi=(math.pi).__round__(4)

# x=np.arange(0,2*pi,0.0001)
# fx=np.cos(x)
# gx=np.sin(x)

# trig_plot=plt.subplot()

# trig_plot.plot(fx,"b",label="cos(x)")

# trig_plot.plot(gx,"r",label="sin(x)")

# trig_plot.spines["left"].set_position("zero")
# trig_plot.spines["top"].set_position("zero")

# trig_plot.spines["right"].set_color("none")
# trig_plot.spines["bottom"].set_color("none")

# trig_plot.set_xlabel("X-axis",size=12,labelpad=-20,x=0.,rotation=1)
# trig_plot.set_xlabel("Y-axis",size=12,labelpad=-20,x=0,rotation=0)

# trig_plot.legend()

# trig_plot.xaxis.set_label_coords(1.05,0.5)
# trig_plot.xaxis.set_label_coords(0.5,1.05)

# plt.show()

# #3

# sbp1=plt.subplot(2,2,1)
# sbp2=plt.subplot(2,2,2)
# sbp3=plt.subplot(2,2,3)
# sbp4=plt.subplot(2,2,4)

# sbp1.set_title("x^3")
# sbp2.set_title("sin(x)")
# sbp3.set_title("e^x")
# sbp4.set_title("log(x+1)")

# x1=np.arange(-4,4,0.1)
# pi=(math.pi).__round__(4)
# x2=np.arange(-pi,pi,0.0001)
# x3=np.arange(-4,4,0.1)
# x4=np.arange(0,8,0.1)

# fx1=x1**3
# fx2=np.sin(x2)
# e=(math.e).__round__(4)
# fx3=e**x3
# fx4=np.log(x4+1)

# sbp1.plot(x1,fx1,"k")
# sbp2.plot(x2,fx2,'r--')
# sbp3.plot(x3,fx3,'g')
# sbp4.plot(x4,fx4,"b.")

# sbp1.spines["left"].set_position("zero")
# sbp1.spines["top"].set_position("zero")

# sbp1.spines["right"].set_color("none")
# sbp1.spines["bottom"].set_color("none")

# sbp1.set_xlabel("X-axis",size=12,labelpad=-20,x=0.,rotation=1)
# sbp1.set_xlabel("Y-axis",size=12,labelpad=-20,x=0,rotation=0)


# sbp2.spines["left"].set_position("zero")
# sbp2.spines["top"].set_position("zero")

# sbp2.spines["right"].set_color("none")
# sbp2.spines["bottom"].set_color("none")

# sbp2.set_xlabel("X-axis",size=12,labelpad=-20,x=0.,rotation=1)
# sbp2.set_xlabel("Y-axis",size=12,labelpad=-20,x=0,rotation=0)


# sbp3.spines["left"].set_position("zero")
# sbp3.spines["top"].set_position("zero")

# sbp3.spines["right"].set_color("none")
# sbp3.spines["bottom"].set_color("none")

# sbp3.set_xlabel("X-axis",size=12,labelpad=-20,x=0.,rotation=1)
# sbp3.set_xlabel("Y-axis",size=12,labelpad=-20,x=0,rotation=0)


# sbp4.spines["left"].set_position("zero")
# sbp4.spines["top"].set_position("zero")

# sbp4.spines["right"].set_color("none")
# sbp4.spines["bottom"].set_color("none")

# sbp4.set_xlabel("X-axis",size=12,labelpad=-20,x=0.,rotation=1)
# sbp4.set_xlabel("Y-axis",size=12,labelpad=-20,x=0,rotation=0)

# sbp1.grid(True)
# sbp2.grid(True)
# sbp3.grid(True)
# sbp4.grid(True)


# plt.show()



# #4
# x=np.arange(0,10,0.1)
# y=np.random.randint(0,10,100)

# sizes=np.abs(np.random.randn(100))*100

# plt.scatter(x,y,s=sizes,c=y,cmap="spring")

# plt.colorbar()

# plt.show()


# #5

# data=np.random.normal(0,1,1000)

# plt.hist(data,bins=30,alpha=0.1,label="Data",color="cyan",edgecolor="green")
# plt.title("Histogram of normalised dataset")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.show()


# #6

# x=np.arange(-5,5,0.01)
# y=np.arange(-5,5,0.01)

# xx,yy=np.meshgrid(x,y)


# z=np.sin(xx**2+yy**2)

# fg=plt.figure()
# ax=plt.axes(projection="3d")

# surf=ax.plot_surface(xx,yy,z,cmap="spring")
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")
# ax.set_zlabel("Z-axis")

# # Adjust layout to prevent overlap
# plt.tight_layout()
# cbar = plt.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="sin(x² + y²)", pad=0.1)

# plt.show()

# #7

# categories=['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# values=[200, 150, 250, 175, 225]
# colors = ['red', 'blue', 'green', 'purple',"yellow"]
# x=[i for i in range(5)]

# plt.bar(categories,values,color=colors)
# plt.title("Products")
# plt.xlabel("categories")
# plt.ylabel("values")

# plt.show()

#8
categories=['Category A', 'Category B', 'Category C']
colors1="r"
colors2="b"
colors3="g"
colors4="y"

values1=np.random.randint(1,10,3)
values2=np.random.randint(1,10,3)
values4=np.random.randint(1,10,3)
values3=np.random.randint(1,10,3)

plt.bar(categories,values1,color=colors1,label="T1")
plt.bar(categories,values2,bottom=values1,color=colors2,label="T2")
plt.bar(categories,values3,bottom=values2+values1,color=colors3,label="T3")
plt.bar(categories,values4,bottom=values3+values2+values3,color=colors4,label="T4")

plt.grid(True, axis='y')

plt.title("Categories over 4 periods")

plt.xlabel("Categories")
plt.ylabel("Values")

plt.legend()

plt.show()