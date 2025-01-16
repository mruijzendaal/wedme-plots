import numpy as np
import wedme.apply.a0
import matplotlib.pyplot as plt

wedme.figure.thesis()
plt.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)))
plt.show()

wedme.subplots.poster(1, 2)
plt.show()
