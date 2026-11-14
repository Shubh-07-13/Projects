import matplotlib.pyplot as plt
#names = ["John", "Joe", "Jim", "Jimmy", "King John Johnicus Jimmicus Optimus the Third"]
#scores = [94, 94, 86, 97, 67]
#plt.plot(names, scores, color="purple", marker="o", ms="10", mec="black", linewidth = "2.5")
#plt.xlabel("names")
#plt.ylabel("scores")
#plt.title("Student Test Score Analysis")
#plt.show()

countries = ["United States", "China", "India", "Germany", "Russia"]
people = [350, 1400, 1500, 80, 140]
plt.barh(countries, people, color="green", edgecolor="red", linewidth="3")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.title("Population (in the millions)")
plt.show()