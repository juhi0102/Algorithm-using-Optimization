using PyCall
@pyimport numpy as np
@pyimport matplotlib.pyplot as plt

# Generate r and theta arrays
rad_arr = np.radians(np.linspace(0, 360, 20))
r_arr = np.arange(0, 1, 0.1)

# Define the function using Julia syntax
function func(r, theta)
    return r .* sin.(theta)
end

# Create a meshgrid for r and theta
r, theta = np.meshgrid(r_arr, rad_arr)

# Get the values of response variables
values = func(r, theta)

# Plot the polar coordinates
fig, ax = plt.subplots(subplot_kw=Dict("projection" => "polar"))
ax.contourf(theta, r, values, cmap="Spectral_r")
plt.show()
