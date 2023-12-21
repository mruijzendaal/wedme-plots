"""We Don't Make Embarrassing Plots

Import the `wedme` module to apply styles:

    >>> import wedme
    >>> wedme.paper()

"""

# Standard library imports
from importlib import resources as _resources
import matplotlib.pyplot as _plt

## Size definitions
_MM_TO_INCH = 0.0393700787

SIZE_SM = 30 * _MM_TO_INCH
SIZE_10 = 90 * _MM_TO_INCH
SIZE_15 = 140 * _MM_TO_INCH
SIZE_20 = 190 * _MM_TO_INCH

PAPER_FW = 190 * _MM_TO_INCH
PAPER_CW = 90 * _MM_TO_INCH
PAPER_GH = PAPER_CW / 1.618

SLIDE_FH = 7.5
SLIDE_HH = SLIDE_FH / 2
SLIDE_TH = SLIDE_FH / 3
SLIDE_FW = SLIDE_FH * 16 / 9
SLIDE_HW = SLIDE_FW / 2
SLIDE_TW = SLIDE_FW / 3


## Functions for applying the wedme styles
def _apply_style(stylename):
    with _resources.files("wedme") / f"{stylename}.mplstyle" as file_path:
        _plt.style.use(file_path)


def _common():
    _apply_style("common")


def slides():
    _common()
    _apply_style("slides")


def paper():
    _common()
    _apply_style("elspaper")


def poster():
    # _common()
    raise NotImplementedError("Poster style is not yet implemented")


## Some more utility functions
class _metafigure(type):
    def __getattr__(cls, name: str):
        nameparts = name.upper().split("_")
        if len(nameparts) != 3:
            figsize = None
            tname = nameparts[0]
        else:
            tname, wname, hname = name.upper().split("_")
            wname = "_".join([tname, wname])
            hname = "_".join([tname, hname])

            h = globals()[hname]
            w = globals()[wname]
            figsize = (w, h)

        def myfig(*args, **kwargs):
            kws = {}
            kws.update(kwargs)
            kws.update(figsize=figsize)
            if tname == "PAPER":
                paper()
            elif tname == "SLIDE" or tname == "SLIDES":
                slides()
            elif tname == "POSTER":
                poster()
            else:
                raise ValueError(f"Unknown figure type {tname}")
            _plt.figure(*args, **kws)

        return myfig


class figure(metaclass=_metafigure):
    pass
