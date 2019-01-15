#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- Imports --- {{{1
import warnings
import pandas as pd
from plotnine import *
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n,
    sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction) 
ggplot = DelayFunction(ggplot)

# --- Fonts --- {{{1

import matplotlib.font_manager as fm
fpath = '/System/Library/Fonts/Avenir.ttc'
font = fm.FontProperties(fname=fpath)


# --- Helper Functions --- {{{1

# --- Load Data --- {{{1

df = pd.DataFrame({'x': [i for i in range(100)], 'y': [i ** 2 for i in range(100)]})
df['z'] = ['one' if x % 2 == 0 else 'two' for x in df['x']]
df['facet_group'] = ['Group 1' if x % 5 == 0 else 'Group 2' for x in df['x']]

# --- Manipulate Data --- {{{1


# --- Plotting --- {{{1

df = DplyFrame(df)

plot = ( 
df >>
ggplot(X._, aes('x','y')) +
geom_point(aes(color = 'z')) +
facet_grid('~facet_group') +
theme(
    text = element_text(fontproperties = font),
    strip_text = element_text(ha = 'center', va = 'center')    
  ) +
scale_color_brewer(palette = 'Dark2', type = 'qual')
)

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    plot.save('example.png', dpi = 300)
