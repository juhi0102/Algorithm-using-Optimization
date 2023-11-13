using PyCall
using PyPlot

@pyimport numpy as np

function func(x, y)
    return np.sin.(x).^2 + np.cos.(y).^2
end

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)

x, y = np.meshgrid(x, y)
z = func(x, y)

# Draw rectangular contour plot
contour(x, y, z, cmap="gist_rainbow_r")
show()
