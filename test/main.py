import matplotlib.pyplot as plt

data = [24, 17, 53, 21, 35]
labels = ['Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar']

fig, ax = plt.subplots()
ax.pie(data, labels=labels)

plt.show()
