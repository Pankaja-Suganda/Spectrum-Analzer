"""
Created on Sat Mar 12 07:17:30 2022
@author: Pankaja Suganda
"""
# application title
# you can change aplication title 
APPLICATION_TITLE   = "Spectrum Analyzer"

# text style for
FONT_GENERAL        = 'Bebas Kai'

# font sizes
LABEL_FONT          = (FONT_GENERAL, 8, 'bold')

# here you can change Background and button Colors
BACKGROUND_COLOR    = 'Gray10'
BUTTON_COLOR        = 'Gray99'
TEXT_COLOR          = 'Gray80'
GRAPH_COLOR         = (0.1,0.1,0.1)
GRAPH_AXIS_COLOR    = (0.8,0.8,0.8)

# graph animation interval
INTERVAL            = 100

# label texts for top bar
REF_LABEL   = "Ref Lev  : {ref:.2f} dBm"
ATT_LABEL   = "Att\t: {att:.2f} dB"
RVB_LABEL   = "RBV\t: {rvb:.2f} MHz"
VBW_LABEL   = "VBW\t: {vbw:.2f} MHz"
SWT_LABEL   = "SWT : {swt:.2f} ms"
MODE_LABEL  = "Mode : {mode:} "

# label texts for bottom bar
CENTER_FREQ_LABEL   = "Center : {center_freq:.2f} MHz"
SPAN_LABEL          = "Span   : {span:.2f} MHz"
FREQUENCY_DIV       = "Freq Div : {FreqDiv:} MHz/"

# graph parameters
PLOTTING_COLOR = 'y'

#serial communication parameters
BANDRATE_TIME   = 115200
START_FLAG      = 'S'
END_FLAG        = 'P'