import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

if __name__ == '__main__':
    x1 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y1 = np.tan(x1)
    x2 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y2 = np.arctan(x2)

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(x1 / np.pi, y1, linestyle='dashed', label='y = tgx')
    axs[1].plot(x2 / np.pi, y2, linestyle='dashdot', label='y = arctgx')

    axs[0].set(ylim=(-2, 2), yticks=np.linspace(-2, 2, 8),
               xlabel='x', ylabel='y', title='y = tgx')
    axs[1].set(ylim=(-2, 2), yticks=np.linspace(-2, 2, 8),
               xlabel='x', ylabel='y', title='y = arctgx')

    axs[0].grid()
    axs[1].grid()

    axs[0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))
    axs[0].xaxis.set_major_locator(ticker.MultipleLocator(base=0.5))

    axs[1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))
    axs[1].xaxis.set_major_locator(ticker.MultipleLocator(base=0.5))

    fig.tight_layout()
    plt.show()
