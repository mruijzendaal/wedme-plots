# 👗 wedme-plots: We Don't Make Embarrassing Plots

Matplotlib styles for papers, posters and presentations. Tailored for academic use.

## Too long; didn't read
```python
import wedme

# Open a figure in `paper` style, with size (PAPER_CW, PAPER_DH)
# which equals (journal column width, default height)
wedme.figure.paper_cw_dh()

# Open a figure with the style `slide` and size (SLIDE_TW, SLIDE_HH) 
# which equals (1/3 slide width, 1/2 slide height)
wedme.figure.slide_tw_hh()
```

## Styling
We applied a clean style. The style and sizes of `paper` style are compatible with most journals (Nature, Science, Elsevier). The `slide` style is compatible with a Microsoft Powerpoint presentation. `poster`  is compatible with A0 posters.

## Usage
Import the `wedme` module and apply the desired style. Then proceed with `matplotlib` plotting as you're used to.

Example:
```python
import wedme

# These commands apply a style to subsequent Matplotlib figures.

# For Elsevier-compatible paper styles
wedme.paper()

# For a 16:9 Powerpoint slide
wedme.slide()

# For A0 posters (not implemented yet)
wedme.poster()

# Proceed with plotting as usual
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 1000)

plt.figure()
plt.plot(x, np.sin(x), label="Sine")
plt.plot(x, np.cos(x), label="Cosine")
plt.show()
```

## Sizing
For custom figure sizes, we include reference points for every style:

- Paper. Default size: `(wedme.PAPER_CW, wedme.paper_GH)`
  - `wedme.PAPER_FW` is the full textwidth of an Elsevier journal, 190mm.
  - `wedme.PAPER_CW` is the full columnwidth of an Elsevier journal in two-column layout, 90mm.
  - `wedme.PAPER_GH` is the height that has a golden ratio (1:1.618) to `wedme.PAPER_CW`.
- Slide. Default size: `(wedme.SLIDE_TW, wedme.slide_HH)`
  - `wedme.SLIDE_FW`, `wedme.SLIDE_HW` and `wedme.SLIDE_TW` represent 100%, 50% and 33% of the width of a Powerpoint 16:9 Widescreen slide.
  - `wedme.SLIDE_FH`, `wedme.SLIDE_HH` and `wedme.SLIDE_TH` represent 100%, 50% and 33% of the height of a Powerpoint 16:9 Widescreen slide.

These can be used as follows:
```python
import wedme
wedme.slide()
# Create a new figure that occupies 33% of the width of a ppt slide and 50% its height.
plt.figure(figsize=(wedme.SLIDE_TW, wedme.SLIDE_HH))
```

Alternatively, we provide functions to compress the above code:
```python
wedme.figure.slide_tw_hh()
```
Such a function exists for every combination of heights and widths for a given style.

To open a figure with one of `wedme`'s styles without applying any sizing, use e.g.
```python
wedme.figure.slide()
```

## Powerpoint
Powerpoint automatically resizes artwork to a size that is different from the export size. To undo this:
- Insert the figure in Powerpoint.
- Picture Format > Reset Picture > Reset Picture & Size.

## Fonts
Sans-serif fonts are the standards for figures because they remain readable even when small or pixelated. Helvetica or Arial fonts are preferred by Nature, Science and Elsevier. 

We try to find Helvetica, Arial, Verdana, Inter, Nimbus Sans on your system, in that order. The first font found will be applied to the figures.

## Exporting
`wedme` sets the `pdf.fonttype` parameter to `42` as recommended by Nature. This ensures that the text is editable even after exporting a pdf. `wedme` also changes the parameters `figure.autolayout` and `savefig.bbox` such that the specified sizes are respected.

For saving figures, consider using [pypdfplot](https://github.com/dcmvdbekerom/pypdfplot) to maintain the ability to later change how data is displayed. Of course, we don't make embarassing plots to begin with.

## Examples
<img src="https://github.com/mruijzendaal/wedme-plots/blob/main/img/calibration_curve_rot.png?raw=true" width="512">


