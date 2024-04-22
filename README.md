### Soil geochemistry take-home exercise

The objective of this exercise is to infer and plot a continuous spatial distribution of trace metal
concentrations for an entire area from a set of soil samples taken in the field.

**Background**
Geochemical soil surveys are commonly used in mineral exploration. Workers walk or drive
around a (potentially large) area and collect soil samples at specified locations. These samples
are analyzed to determine the concentration of certain trace metals. The metal content in soils
depends both on the composition of the bedrock directly beneath the soils and by surficial
processes like fluid flows.

The data provided in this repo are typical of a geochemical soil survery. There are several sparse locations
with coordinates and a measured concentration of copper (Cu) and/or cobalt (Co) given in units of parts-per-million (ppm).
The locations are pseudo locations (i.e. not in reference to a geographic coordinate system). 

**Method**
In order to infer and plot a continuous spatial distribution from the sparse, uneven sample locations, we will use two different
interpolation strategies. Ideally, we could quantify how the variability of the metal concentrations changes with 
distance and direction. We can do so using a model, or variogram, that captures the variation in the concentration
with distance from each sample location. By assessing the fit of a range of theoretical models (e.g. spherical, exponential, or
gaussian, etc.) we selected the 'matern' model for the Copper dataset, and from this applied an ordinary kriging estimator to calculate
estimations for unobserved locations. Both the fitting of the variogram and kriging estimator are determined using tools within
the SciKit GStat library (https://scikit-gstat.readthedocs.io/en/latest/index.html). 

Alternatively, we can estimate the concentrations at unobserved locations using the concentrations at the nearest observed locations. For
this, we just need to find the euclidean distance between each point on a regular grid, and the sample locations within a search window. This
approach is implemented using the NearestNDInterpolator method within the scipy.interpolate sub-package
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.NearestNDInterpolator.html). The simpler approach is
used to estimate the concentrations of Cobalt, since none of the variogram models were able to describe the variability in 
sample concentration with distance and direction. 

**Results**
Continuous maps of Copper and Cobalt created using Krigging and Nearest Neighboor interpolation respectively aare stored within the
data folder, and the notebook within the notebook folder. The Copper map also includes an estimate of the kriggin error across the field.
We are not able to provide a similar measure of error using the nearest neighboor interpolation--however, by splitting the Cobalt dataset
into training and testing sets, we can asses the estimation visually. Both approaches are able to capture hotspots of higher metal
concentrations, however both the greater number of sample locations and the interpolation method used for estimating Copper produce a more accurate
map.


**References**

Mirko Mälicke, Egil Möller, Helge David Schneider, & Sebastian Müller. (2021, May 28).
mmaelicke/scikit-gstat: A scipy flavoured geostatistical variogram analysis toolbox (Version v0.6.0). Zenodo. http://doi.org/10.5281/zenodo.4835779