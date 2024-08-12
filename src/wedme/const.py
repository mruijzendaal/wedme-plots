## Size definitions
_MM_TO_INCH = 0.0393700787
_PT_TO_MM = 0.3515
_PT_TO_INCH = _PT_TO_MM * _MM_TO_INCH
GOLDEN_RATIO = 1.61803398875

SIZE_SM = 30 * _MM_TO_INCH
SIZE_10 = 90 * _MM_TO_INCH
SIZE_15 = 140 * _MM_TO_INCH
SIZE_20 = 190 * _MM_TO_INCH

# Papers (Science, Nature, Elsevier) # TODO: split
# Width
PAPER_SCW = 121.095 * _MM_TO_INCH
PAPER_HSCW = PAPER_SCW / 2
PAPER_CW = 90 * _MM_TO_INCH
PAPER_FW = 190 * _MM_TO_INCH
# Height
PAPER_DH = PAPER_CW / GOLDEN_RATIO
PAPER_GH = PAPER_CW / GOLDEN_RATIO
PAPER_PH = 550 * _PT_TO_INCH
PAPER_PW = 345 * _PT_TO_INCH

# Thesis
THESIS_PW = 6.9  # page width
THESIS_PH = 9.8  # page height
THESIS_DW = 90 * _MM_TO_INCH  # approximately half the page
THESIS_DH = THESIS_DW / GOLDEN_RATIO
# Landscape
THESIS_LFW = THESIS_PH  # TODO: subtract margins
THESIS_LFH = THESIS_PW

# 16:9 slides
# Width
SLIDE_FW = 10
SLIDE_TTW = SLIDE_FW * 2 / 3
SLIDE_HW = SLIDE_FW / 2
SLIDE_FTW = SLIDE_FW * 5 / 12
SLIDE_TW = SLIDE_FW / 3
SLIDE_QW = SLIDE_FW / 4
SLIDE_RW = SLIDE_FW / 5
SLIDE_SW = SLIDE_FW / 6
# Height
SLIDE_FH = SLIDE_FW * 9 / 16
SLIDE_HH = SLIDE_FH / 2
SLIDE_TTH = SLIDE_FH * 2 / 3
SLIDE_FTH = SLIDE_FH * 5 / 12
SLIDE_TH = SLIDE_FH / 3
SLIDE_QH = SLIDE_FH / 4
SLIDE_RH = SLIDE_FH / 5
SLIDE_SH = SLIDE_FH / 6


# A0 poster
# Height
A0_FH = 46.8
A0_HH = A0_FH / 2
A0_TH = A0_FH / 3
A0_QH = A0_FH / 4
A0_RH = A0_FH / 5
A0_SH = A0_FH / 6
# Width
A0_FW = 33.1
A0_HW = A0_FW / 2
A0_TW = A0_FW / 3
A0_QW = A0_FW / 4
A0_RW = A0_FW / 5
A0_SW = A0_FW / 6
