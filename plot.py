from bokeh.plotting import figure
from bokeh.io import output_file,show

x=[8,-5,2,8]
y=[6,1,-5,6]

output_file('output.html')
fig=figure()

fig.line(x,y)
show(fig)