import matplotlib.pyplot as plt 

# x axis values 
x = [1,3,5,7,9,15] 
# corresponding y axis values 
y = [64.28,75.15,80.86,82.38,84.90,86.45] 

# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

# naming the x axis 
plt.xlabel('x - axis (K-Value)') 
# naming the y axis 
plt.ylabel('y - axis (Precision in Percentage)') 

# giving a title to my graph 
plt.title('Precision vs K-Value') 

# function to show the plot 
plt.show() 
