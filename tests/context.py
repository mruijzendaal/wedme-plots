import matplotlib.pyplot as plt

# The default parameters in Matplotlib
with plt.style.context("ggplot"):
    plt.figure()

plt.plot([1, 2, 3, 4])

# Similar to ggplot from R
# with plt.style.context("ggplot"):
#     plt.plot([1, 2, 3, 4][::-1])

plt.show()
