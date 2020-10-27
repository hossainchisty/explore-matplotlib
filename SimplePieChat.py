import matplotlib.pyplot as plt

values = [91.4, 5.8, 2.9]
gender = ["Men","Wemen","Other"]

plt.pie(values, labels=gender, autopct='%.1f%%',shadow=True)
plt.title('Programmer According To Genders Survey By Github')
plt.show()