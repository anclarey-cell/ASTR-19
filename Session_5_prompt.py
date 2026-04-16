# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:11:29 2026

@author: arian
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 2*np.pi, 1000)
    print(x)

    fig, axs = plt.subplots(nrows=1, ncols=1)

    sinx = np.sin(x)

    axs.plot(x, sinx, label='sin x')
    axs.set_xlabel("x")
    axs.set_ylabel("y")
    
    
if __name__ == "__main__":
    main()