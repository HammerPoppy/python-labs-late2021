import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

if __name__ == '__main__':
    x1 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y1 = np.tan(x1)
    x2 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y2 = np.arctan(x2)

    fig, ax = plt.subplots()

    ax.plot(x1 / np.pi, y1, linestyle='dashed', label='y = tgx')
    ax.plot(x2 / np.pi, y2, linestyle='dashdot', label='y = arctgx')

    ax.legend(loc='lower left')

    ax.set(ylim=(-2, 2), yticks=np.linspace(-2, 2, 8),
           xlabel='x', ylabel='y')

    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=0.5))

    plt.show()
