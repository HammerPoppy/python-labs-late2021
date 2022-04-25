import matplotlib.pyplot as plt

data = [24, 15, 55, 21, 35]
names = ['Yamaha', 'CASIO', 'Fender', 'AudioTechnika', 'B&B']

fig, axs = plt.subplots(1, 2)

axs[0].pie(data, labels=names)
axs[1].bar(names, data)

plt.show()
