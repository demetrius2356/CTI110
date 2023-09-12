import matplotlib.pyplot as plt

print("enter pokeman data:")
print("day 1:", end="")
day1= int(input())

print("day 2:", end="")
day2= int(input())

print("day 3:", end="")
day3= int(input())

data=[day1,day2,day3]


fig, ax = plt.subplots()
ax.plot([1, 2, 3],data)
plt.xlabel('day #')
plt.title('pokeman data')
plt.ylabel('pokemans collected')
plt.show()
