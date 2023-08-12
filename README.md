## Introduction

This research is created with the purpose of fast querying all locations within given radius from current user location.

## Generate pseudo locations

generate_spatial_location.py support generating any number of random locations.

**Usage**

```
python generate_spatial_location.py --num-samples=<number of samples>
```

**Options**

* `--num-samples` or `-ns` : Number of samples you want to create. Default is 100

## Proposed Approach

`Distance function (Haversine distance)`

For all proposed approach we will use the same distance function. The distance function will be used is the Haversine function.

<i>Haversine function determines the circle distance between two points on the sphere given their latitudes and longitudes.</i>

**Formula**

$$
d = 2r.arcsin(\sqrt{hav(\phi_1 - \phi_2) + cos(\phi_1)cos(\phi_2)hav(\lambda_1 - \lambda_2)})\\
= 2r.arcsin(\sqrt{sin^2(\frac{\phi_2 - \phi_1}{2}) + cos(\phi_1)cos(\phi_2)sin^2(\frac{\lambda_2-\lambda_1}{2})})
$$

in which $\phi$ is latitude, $\lambda$ is longitude and $r$ is radius

* By substituting user locations with $\phi$ and $\lambda$ and the radius $r$ will be equal to radius to radius of the Earth (6371 Km)

`Approach 1: Using spatial function of MySQL`

* In this approach, we will use the <b>ST_Distance_Sphere</b> spatial data function of MySQL to calculate the distance between two points and find all locations in a given radius.

* To increase the query performance, we also utilize the spatial index of MySQL (For more information : [Creating Spatial Indexes](https://dev.mysql.com/doc/refman/8.0/en/creating-spatial-indexes.html#:~:text=SPATIAL%20INDEX%20creates%20an%20R,but%20not%20for%20range%20scans.)).

* For the query, please refer to [Find nearby location query](/sql_query/find_neaby_location.sql).

`Approach 2: Using machine learning model (BallTree)`

* We will use KNN (K-Nearest Neighbor) Algorithm for this problem.
* There are 3 algorithm that can be used for this problem: Brute KNN, KD Tree and Ball Tree. After doing research, we see that Brute KNN isn't a good choice for data that have high dimensional space and the query time of Ball Tree is faster than KD Tree so we will use Ball Tree for this problem.

**Processing data step**

* The data have to be 2 dimensional in which the first dimension represent latitude and the second dimension represent longitude.

* We assume that the data stored in database is in degree unit. In order to use the Haversine distance function, <b>we have to convert degree to radian</b>.

`Approach 3: Storing data in Parquet file`

* Incoming ....

## Benchmark

We compare the query times of each approach for 10 different random locations. The following is the table that show the result through the test cases :

* Location information is written in the following format : (latitude, longitude).

* The query time is measured in seconds(s).

| Location | Aprroach 1 (seconds) | Approach 2 (seconds) |
| :---: | :-----: | :-------:|
| (-45.615177,  128.918880)|     11.322522      |    0.012155       |
| (3.2693677,   174.406829)|    11.241704       |    0.005028       |
| (-3.1414800,  41.6408665)|    10.285750       |    0.004771     |
| (-39.021237,  128.357045)|    9.529558        |    0.005636       |
| (-60.770185,  -155.182407)|    11.471666     |    0.005001       |
| (-2.4184236,  107.923392)|      11.073095     |    0.005003       |
| (-22.458415,  151.211147)|       9.845515     |    0.005572     |
| (29.385264,   -6.23489428)|      10.316774    |    0.004627     |
| (-10.713211,  41.9828035)|      8.280211     |    0.004598     |
| (16.273357,   -130.421662)|      12.247621 |    0.005170       |
