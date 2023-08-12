-- Find nearby location within 10 kilometers.

set @userLocation = st_geomfromtext('point(-83.110089 99.7269053)', 4326);

SELECT name,
       ST_Distance_Sphere(`position`, @userLocation) AS `distance_m`, 
       st_longitude(position) as `Longitude`,
       st_latitude(position) as `Latitude`
FROM GeoLocation
HAVING distance_m <= 1000000; 