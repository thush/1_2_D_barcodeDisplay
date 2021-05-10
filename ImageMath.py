print(__doc__)


import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import make_biclusters
from sklearn.cluster import SpectralCoclustering
from sklearn.metrics import consensus_score

data, rows, columns = make_biclusters(
    shape=(300, 300), n_clusters=5, noise=5,
    shuffle=False, random_state=0)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")

# shuffle clusters
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")

model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
score = consensus_score(model.biclusters_,
                        (rows[:, row_idx], columns[:, col_idx]))

print("consensu_score".format(score))


plt.show()


# import  numpy as np
# import  matplotlib.pyplot as plt
# from skimage.color import rgb2gray
# from skimage import data
# from skimage.filters import gaussian
# from skimage.segmentation import active_contour
#
# img = data.astronaut()
#
# s = np.linspace(0, 2*np.pi, 400)
# x = 220 + 100*np.cos(s)
# y = 100 + 100*np.sin(s)
# init = np.array([x, y]).T
#
# # formation of the active contour
# cntr = active_contour(gaussian(img ,2),init, alpha=0.015, beta=10, gamma=0.001)
# fig, ax = plt.subplots(1, 2, figsize=(7, 7))
# ax[0].imshow(img, cmap=plt.cm.gray)
# ax[0].set_title("Original Image")
#
# ax[1].imshow(img, cmap=plt.cm.gray)
# # circular boundary
# ax[1].plot(init[:, 0], init[:, 1], '--r', lw=3)
# ax[1].plot(cntr[:, 0], cntr[:, 1], '-b', lw=3)
# ax[1].set_title("Active Contour Image")