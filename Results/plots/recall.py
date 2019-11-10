import matplotlib.pyplot as plt 

# x axis values 
x = [1,3,5,7,9,15] 
# corresponding y axis values 
y = [71.05,79.60,86.18,87.23,88.81,89.01] 

# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

# naming the x axis 
plt.xlabel('x - axis (K-Value)') 
# naming the y axis 
plt.ylabel('y - axis (Recall in Percentage)') 

# giving a title to my graph 
plt.title('Recall vs K-Value') 

# function to show the plot 
plt.show() 
