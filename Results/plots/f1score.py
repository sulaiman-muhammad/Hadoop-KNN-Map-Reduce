import matplotlib.pyplot as plt 

# x axis values 
x = [1,3,5,7,9,15] 
# corresponding y axis values 
y = [67.49,77.31,83.44,84.24,86.81,87.30] 

# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

# naming the x axis 
plt.xlabel('x - axis (K-Value)') 
# naming the y axis 
plt.ylabel('y - axis (F1-Score in Percentage)') 

# giving a title to my graph 
plt.title('F1-Score vs K-Value') 

# function to show the plot 
plt.show() 
