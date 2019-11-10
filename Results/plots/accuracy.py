import matplotlib.pyplot as plt 

# x axis values 
x = [1,3,5,7,9,15] 
# corresponding y axis values 
y = [75.11,83.01,87.55,88.27,90.19,90.66] 

# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 

# naming the x axis 
plt.xlabel('x - axis (K-Value)') 
# naming the y axis 
plt.ylabel('y - axis (Accuracy in Percentage)') 

# giving a title to my graph 
plt.title('Accuracy vs K-Value') 

# function to show the plot 
plt.show() 
