'''
SF1512/SF1514 Projekt HT26.

Fil för att animera robotens väg.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation


def animate(x, y, theta=None, interval=50, repeat=False):
    '''
    Animera robotens väg.

    Indata:
    x -- vektor med x-koordinater
    y -- vektor med y-koordinater
    theta -- vektor med orienteringsvinklar (valfri)
    interval -- antal millisekunder mellan videoramarna
                (styr hur snabb animeringen är) (valfri,
                standardvärde: 50)
    repeat -- om animeringen ska starta om när den är klar
              (valfri, standardvärde: False)
    '''
    n = np.size(x)
    xlims = [np.min(x), np.max(x)]
    ylims = [np.min(y), np.max(y)]

    def animfun(j):
        plt.clf()
        plt.plot(xlims, ylims, '.', alpha=0)
        plt.plot(x[:j+1], y[:j+1], color='tab:blue')
        plt.plot(x[j], y[j], 'o', color='tab:red')
        if theta is not None:
            L = 0.2
            xn = x[j] + L*np.cos(theta[j])
            yn = y[j] + L*np.sin(theta[j])
            plt.plot([x[j], xn], [y[j], yn], linewidth=2, color='tab:red',
                     alpha=0.5)
        plt.axis('equal')
        return

    global __anim1
    __anim1 = matplotlib.animation.FuncAnimation(
        plt.gcf(), animfun, n, interval=interval, repeat=repeat,
    )
    return
