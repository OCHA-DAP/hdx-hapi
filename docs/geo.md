# Geo Data

---

Much of the data in HAPI references a geographical area.  The complimentary geodata to this is provided by ITOS via ARCGIS service accessible here: [https://apps.itos.uga.edu/CODV2API/api/v1/](https://apps.itos.uga.edu/CODV2API/api/v1/)


This service contains the common operational datasets administration boundaries and it can be accessed in a number formats. Enhanced datasets have been standardised and contain the data formatting. Check the [CODs Dashboard](https://cod.unocha.org/) to see the status of different countries.


Below are examples of how to access the shapefile and geojson for the supported countries


## Geojson


URL (replace iso3 and admlevel with appropriate values)
```
https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/{ iso3 }/versions/current/geoJSON/{ admlevel }
```

E.g. to get the boundaries for Afghanistan admin level 1 in geojson use the URL:


[https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1](https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1)


## SHP file


URL (replace iso3 and admlevel with appropriate values)
```
https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/{ iso3 }/versions/current/SHP/{ admlevel }
```

E.g. to get the boundaries for Afghanistan admin level 1 in SHP file use the URL:

[https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/AFG/versions/current/SHP/1](https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/AFG/versions/current/SHP/1)
