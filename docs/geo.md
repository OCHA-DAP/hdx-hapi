# Geo Data for HAPI

Most subcategories in HAPI contain fields called pcodes (place codes).  These pcodes are unique identifiers given to adminstrative geographical boundaries. These pcodes can be joined to the corresponding geo data to then create maps and carry out geographical based analysis. This geo data is part of the Common Operational Datasets (CODs)

A complementary API provided by ITOS (Information Technology Outreach Services of the University of Georgia) provide a [geo data api](https://codgis.itos.uga.edu/arcgis/rest/services/COD_External). A wide range of geo formats is available and additional geo based queries are possible. Check the [documentation](https://apps.itos.uga.edu/CODV2API/Help) for the full capabilities.

Check the [COD dashboard](https://cod.unocha.org/) for current status and coverage

## API calls for commonly used formats

### API call for shapefiles
```
https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/{ iso3 code }/versions/current/SHP/{ admlevel } 
```

replacing { iso3 code } and { admlevel } with appropriate values

### API call for geojsons
```
https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/{ iso3 code }/versions/current/GEOJSON/{ admlevel } 
```

replacing { iso3 code } and { admlevel } with appropriate values

## Code Examples

Please check the code examples section for how to combine data from HAPI with the ITOS api