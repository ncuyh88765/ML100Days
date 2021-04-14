#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import widgets
from bokeh.io import output_notebook

# 讓網頁直接輸出在NOTEBOOK
output_notebook()

output_file("out.html")
p = figure()
p.line([1,2,3,4,5],[5,4,3,2,1])
show(p)


# In[2]:


from bokeh.plotting import figure, output_file, show
# 讓網頁直接輸出在NOTEBOOK
output_notebook()

# create a Figure object
p = figure(plot_width=300, plot_height=300, tools="pan,reset,save")

# 添加圓點的分佈圖
# p.circle (x/y 座標, size, color, and 透明度)
p.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], size=20, color="navy", alpha=0.5)

# specify how to output the plot(s)
output_file("foo.html")

# 秀圖
show(p)


# In[3]:


from bokeh.plotting import figure, output_file, show

output_file("toolbar.html")

# 新增工具欄, 位置在繪製圖區域下方
p = figure(plot_width=400, plot_height=400,
           title=None, toolbar_location="below",
           toolbar_sticky=False)
# 工具欄位置與軸發生衝突，在這種情況下，將toolbar_sticky選項設置為False將工具欄移動到繪製軸的區域之外。

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)


# In[4]:


import bokeh.sampledata
bokeh.sampledata.download()


# In[6]:


import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

# 準備資料
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

#設定視窗
window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# 輸出靜態 HTML file
output_file("fruitdata.html", title="fruit.py exercise")

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=350, x_axis_type="fruits")

# add renderers
p.bar(fruits, size=4, color='darkgrey', alpha=0.2, legend_label='close')


# NEW: customize by setting attributes
p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'fruits'
p.yaxis.axis_label = 'counts'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)


# In[ ]:


import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

# 準備資料
aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

#設定視窗
window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# 輸出靜態 HTML file
output_file("stocks.html", title="stocks.py example")

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=350, x_axis_type="datetime")

# add renderers
p.circle(aapl_dates, aapl, size=4, color='darkgrey', alpha=0.2, legend_label='close')
p.line(aapl_dates, aapl_avg, color='navy', legend_label='avg')

# NEW: customize by setting attributes
p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)

