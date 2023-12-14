"""We Don't Make Embarrassing Plots

Import the `wedme` module to apply styles:

    >>> import wedme
    >>> wedme.paper()

"""

# Standard library imports
from importlib import resources as _resources
import matplotlib.pyplot as _plt

_MM_TO_INCH = 0.0393700787

SIZE_SM = 30 * _MM_TO_INCH
SIZE_10 = 90 * _MM_TO_INCH
SIZE_15 = 140 * _MM_TO_INCH
SIZE_20 = 190 * _MM_TO_INCH


def _apply_style(stylename):
    with _resources.path("wedme", f"{stylename}.mplstyle") as file_path:
        _plt.style.use(file_path)


def slides():
    _apply_style("umppt")


def paper():
    _apply_style("elspaper")


def poster():
    raise NotImplementedError("Poster style is not yet implemented")


# Version of wedme-plots package
__version__ = "1.0"
