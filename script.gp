# cd "C:/Users/matej/OneDrive/Desktop/viewchaos/Pcode"
# load "script.gp"

load 'inferno.pal'
set palette negative
#set terminal png size 3072,1920

# set terminal pngcairo size 8000,5000
set terminal pngcairo size 1000,1000
# set terminal pngcairo size 500,400
#set xrange [-2:0.5];
#set yrange [-1:1];
set xrange [-1.5:1.5];
set yrange [-1.5:1.5];
set colorbox

set output 'multibrot15.png'


# The graphic title
set title 'Mandelbrot'

#plot the graphic
plot 'output.txt' using 1:2:3 with points palette



#2.5 / x = 3072
#2 / y = 1920

#Best for mandelbrot - inferno, magma
#Negative - rdgy, magma, inferno, bupu