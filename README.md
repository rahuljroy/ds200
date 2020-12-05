# Project Repository of Research Methods course DS200

## Code  

The code is available in the zip file Code_and_plots.zip, and is named plotting.py.  
Its a python can script and can be run by the following command:  

<code>python plotting.py</code>

## Dataset  

We will be dealing with the dataset from this [link](https://data.gov.in/catalog/gdp-india-and-major-sectors-economy-share-each-sector-gdp-and-growth-rate-gdp-and-other?filters%5Bfield_catalog_reference%5D=88141&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc).  
It has the details about the GDP of major sectors of the Indian Economy during the timeline 1951 to 2013.  

We will be using Pandas to read the file into a dataframe. The dataset is of a .xml format.  
So we would be using the <code>read_excel</code> function from Pandas.  

<code>df = pd.read_excel('GDP_and_Major_Industrial_Sectors_of_Economy_Dataset.xls')</code>

We would also drop the rows with NaN values, and this can be achieved by the function <code>dropna()</code>

<code>df.dropna(inplace=True)</code>

## Scatter Plot  

We will be plotting the percentage growth rate of the GDP against time.  
Also we would be plotting the growth rate of sectors - Mining and Quarrying, and the Services sector against it, such that we can see the correlation between the performance of the services and the growth in the country's GDP.  

The scatter plot can be drawn by the <code>plt.scatter()</code> fucntion, which takes in the x and the y values to be plotted.

You can see the plot below:

![alt text](https://github.com/rjroy196/ds200/blob/main/Scatter_Plot.jpg)  

From the plot, we can see that the services industry is closely correlated with the GDP growth, both showing similar trend.  
The mining sector on the other hand, exhibits large variation, and this does not reflect in the GDP's variation.

## Box Plot  

We will be plotting the box and whiskers plot of Agriculture, Industry, Mining, Manufacturing and the Services growth over the years.  

You can see the plot below:

![alt text](https://github.com/rjroy196/ds200/blob/main/Box_Plot.jpg)

## Line Plot  


We would be plotting line plots of Agriculture, Industry and the Manufacting sectors.

You can see the plot below:

![alt text](https://github.com/rjroy196/ds200/blob/main/Line_Plot.jpg)
# Project Repository of Research Methods course DS200

## Code  

The code is available in the zip file Code_and_plots.zip, and is named plotting.py.  
Its a python can script and can be run by the following command:  

<code>python plotting.py</code>

## Dataset  

We will be dealing with the dataset from this [link](https://data.gov.in/catalog/gdp-india-and-major-sectors-economy-share-each-sector-gdp-and-growth-rate-gdp-and-other?filters%5Bfield_catalog_reference%5D=88141&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc).  
It has the details about the GDP of major sectors of the Indian Economy during the timeline 1951 to 2013.  

<<<<<<< HEAD
=======
We will be using Pandas to read the file into a dataframe. The dataset is of a .xml format.  
So we would be using the <code>read_excel</code> function from Pandas.  

<code>df = pd.read_excel('GDP_and_Major_Industrial_Sectors_of_Economy_Dataset.xls')</code>

We would also drop the rows with NaN values, and this can be achieved by the function <code>dropna()</code>

<code>df.dropna(inplace=True)</code>

>>>>>>> be9d07ca7c7e3f3c81d7f41a240a42ed78f15bb6
## Scatter Plot  

We will be plotting the percentage growth rate of the GDP against time.  
Also we would be plotting the growth rate of sectors - Mining and Quarrying, and the Services sector against it, such that we can see the correlation between the performance of the services and the growth in the country's GDP.  

The scatter plot can be drawn by the <code>plt.scatter()</code> fucntion, which takes in the x and the y values to be plotted.

You can see the plot below:

<<<<<<< HEAD
![alt text](https://github.com/rjroy196/ds200/blob/main/Scatter_Plot.jpg)
=======
![alt text](https://github.com/rjroy196/ds200/blob/main/Scatter_Plot.jpg)  

From the plot, we can see that the services industry is closely correlated with the GDP growth, both showing similar trend.  
The mining sector on the other hand, exhibits large variation, and this does not reflect in the GDP's variation.
>>>>>>> be9d07ca7c7e3f3c81d7f41a240a42ed78f15bb6

## Box Plot  

We will be plotting the box and whiskers plot of Agriculture, Industry, Mining, Manufacturing and the Services growth over the years.  

You can see the plot below:

![alt text](https://github.com/rjroy196/ds200/blob/main/Box_Plot.jpg)

## Line Plot  


We would be plotting line plots of Agriculture, Industry and the Manufacting sectors.

You can see the plot below:

<<<<<<< HEAD
![alt text](https://github.com/rjroy196/ds200/blob/main/Line_Plot.jpg)
=======
![alt text](https://github.com/rjroy196/ds200/blob/main/Line_Plot.jpg)
>>>>>>> be9d07ca7c7e3f3c81d7f41a240a42ed78f15bb6
