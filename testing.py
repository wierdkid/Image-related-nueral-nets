import numpy as np
import matplotlib.pyplot as plt

width, height = 1024, 1024

random_noise = np.random.randint(0, 256, (height, width))

plt.imshow(random_noise, cmap='gray')
plt.axis('off')
plt.show()
