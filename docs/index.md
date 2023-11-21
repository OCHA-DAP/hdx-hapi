# Summary

For full documentation visit [the reference documentation](https://placeholder.url). Please note, in late 2023 and early 2024, HAPI is undergoing continual development. **Both the capabilities of the API and the data within it may change frequently.**

HAPI is a service of the [Humanitarian Data Exchange (HDX)](https://data.humdata.org), part of UNOCHA's [Centre for Humanitarian Data](https://centre.humdata.org). The purpose of HAPI is to improve access to key humanitarian datasets taken from the HDX catalog data to better support automated visualisation and analysis. HAPI is primarily intended for application developers and data scientists working within the humanitarian community.

HAPI provides a consistent, standardised and machine-readable interface to query and retrieve data from a set of high-value humanitarian indicators drawn from the HDX catalogue. With HAPI, the HDX team aims to provide a single point of access to critical humanitarian data in a standardised and structured way. 

As of November 2023, HAPI is in active development and early release. The number of indcators in HAPI is limited, and work is ongoing to continually add more data. The initial scope of HAPI will be the data included in the [HDX Data Grids](https://data.humdata.org/dashboards/overview-of-data-grids).

# Terms Of Use

[The HDX Terms of Service] (https://data.humdata.org/faqs/terms)

# The Structure of HAPI
## Indicator Endpoints
HAPI is organized around a set of key humanitarian indicators like **Baseline Population** and **3W - Operational Presence**. Each of these indicators can be queried via its endpoint.

### Current list of indicator endpoints in HAPI
- [population](https://placeholder.url/docs#/population): Get data about baseline populations of a location
- [3w](https://placeholder.url/docs#/3W): Get data about operational presence. You can learn more about 3w data [here](https://3w.unocha.org/)

## Supporting Tables
Additional supporting endpoints provide information about locations, codelists, and metadata.
### Current list of supporting endpoints in HAPI
- [admin-level](https://placeholder.url/docs#/admin-level): Get the lists of locations (countries and similar), and administrative subdivisions used as location references in HAPI. These are taken from the [Common Operational Datasets](https://data.humdata.org/dashboards/cod)
- [humanitarian-response](https://placeholder.url/docs#/humanitarian-response): Get the lists of organizations, organization types, and humanitarian sectors used in the data available in HAPI.
- [demographic](https://placeholder.url/docs#/demographic): Get the lists of gender categories and age groupings used in the data available in HAPI.
- [hdx-metadata](https://placeholder.url/docs#/hdx-metadata): Retrieve metadata about the source of any data available in HAPI.
## Dates
As of version 1 (released in late 2023), the data in HAPI is static and intended only for testing purposes. However you can filter your HAPI queries based on the date the source data was updated in HDX. Future versions will offer more robust date-related features.

# Getting Started with the API

In addtion to this getting started section we suggest exploring the [query interface](https://placeholder.url/docs) which details all available filtering options for each endpoint, providing a hands-on way to familiarize yourself with the API's structure.

Below, you will find example URLs to help you learn how to construct your API queries. These URLs can be entered directly into your web browser for immediate results.

## Accessing 3W Data

Retrieve the latest 3W (Who's doing What, Where) data for a specific country using the `location_name` filter. The following example demonstrates how to get data for Mali:

Copy this link into your browser to see the results

```plaintext
https://placeholder.url/api/themes/3w?location_name=Mali&output_format=json&offset=0&limit=10000
```

A single row of the result looks like this:

```JSON
[
  {
    "sector_code":"NUT",
    "dataset_hdx_stub":"mali-operational-presence",
    "resource_hdx_id":"a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
    "org_acronym":"ACF-E",
    "org_name":"Action Contre la Faim-Espagne",
    "sector_name":"Nutrition",
    "location_code":"MLI",
    "location_name":"Mali",
    "admin1_code":"ML07",
    "admin1_name":"Gao",
    "admin2_code":"ML0702",
    "admin2_name":"Bourem"
  }
]
```

The above result was in JSON. It is also possible to get a CSV by changing the output format as follows ```output_format=csv```.

The maximum number of rows returned in a single response is 10,000. To access more data beyond this limit, you can paginate through results by increasing the ```offset``` parameter as shown here:

```plaintext
https://placeholder.url/api/themes/3w?location_name=Mali&output_format=json&offset=10000&limit=10000
```

Check the code example section to see code for querying multiple pages and loading into a single result.

With the 3w theme endpoint there are a variety of filters to target your results include ```sector_name```, ```admin2_code``` and ```org_name```

This query gets all of the WASH activities happening in Yobe, Nigeria using the ```sector_name``` and ```admin1_name``` filter

```plaintext
https://placeholder.url/api/themes/3w?sector_name=Water%20Sanitation%20Hygiene&location_name=Nigeria&admin1_name=Yobe&output_format=json&offset=0&limit=1000
```

Remember to check the [technical documentation](https://placeholder.url/docs) for the full list of filters available

## Exploring Population Data

The Population endpoint delivers detailed demographic breakdowns by age range and gender.  The example query below uses ```location_code``` rather than ```location_name``` to use the iso3 code for Afghanistan ```AFG```. In addition it also uses the ```admin_level=1``` filter to get only admin level 1 results.

```
https://placeholder.url/api/themes/population?location_code=AFG&output_format=json&offset=0&limit=10000&admin_level=1
```

To refine this query to retrieve population statistics specifically for males under the age of 5, append the age_range_code and gender_code filters to your request:

```
https://placeholder.url/api/themes/population?location_code=AFG&output_format=json&offset=0&limit=10000&admin_level=1&age_range_code=0-4&gender_code=m
```

By tailoring these filters, you can obtain a variety of demographic insights from the API

## Understanding Supporting Tables

Each theme within our API is bolstered by associated supporting tables. These tables are essential for understanding the range of possible values you can work with in the theme-specific tables. For example, if you're filtering by age range—as we did with `age_range_code=0-4`—you'll want to know what age range codes are available.

You can retrieve a list of possible age ranges by querying the `age_range` support table like so:

```plaintext
https://placeholder.url/api/age_range?output_format=json&offset=0&limit=1000
```

This functionality is not limited to age ranges. There are similar support tables for a variety of filters such as organizations, genders, sectors, and more. Querying these support tables provides you with the necessary information to apply precise filters and extract the data that's most relevant to your needs.

## Getting Metadata through API Queries

When you inspect the JSON output from an initial API query, you'll encounter a variety of detailed fields. Take a look at this sample output:

```json
[
  {
    "sector_code": "NUT",
    "dataset_hdx_stub": "mali-operational-presence",
    "resource_hdx_id": "a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
    "org_acronym": "ACF-E",
    "org_name": "Action Contre la Faim-Espagne",
    "sector_name": "Nutrition",
    "location_code": "MLI",
    "location_name": "Mali",
    "admin1_code": "ML07",
    "admin1_name": "Gao",
    "admin2_code": "ML0702",
    "admin2_name": "Bourem"
  }
]
```

Among these fields, ```dataset_hdx_stub``` and ```resource_hdx_id``` are keys to unlocking metadata about the dataset. This metadata includes the last update date, the organization responsible for the data, and links to download the original dataset.

To dive deeper into the data's origin, use the resource_hdx_id in the resource endpoint URL:

```
https://placeholder.url/api/resource?hdx_id=a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1&update_date_min=2020-01-01&update_date_max=2024-12-31&output_format=json&offset=0&limit=1000
```

Executing this query provides a response like the following:

```JSON
[
  {
    "hdx_id": "a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
    "name": "MALI_3W_June_2023",
    "format": "XLSX",
    "update_date": "2023-09-28T10:45:27",
    "is_hxl": false,
    "download_url": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1/download/mali-3w_maj-2.xlsx",
    "dataset_hdx_id": "d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3",
    "dataset_hdx_stub": "mali-operational-presence",
    "dataset_title": "Mali: Operational Presence",
    "dataset_hdx_provider_stub": "ocha-mali",
    "dataset_hdx_provider_name": "OCHA Mali",
    "hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1/",
    "hdx_api_link": "https://data.humdata.org/api/action/resource_show?id=a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
    "dataset_hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/",
    "dataset_hdx_api_link": "https://data.humdata.org/api/action/package_show?id=d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3"
  }
]
```

This output gives you a comprehensive view of the dataset's metadata, including the update date, the contributing organization, and direct links to more information via the CKAN API and the original data file download.

As a starting point to effectively use our API, we encourage you to experiment with different queries using the technical documentation's query interface and review the provided code examples for guidance.

# Code Examples

## 1. Query a theme end point and loop through pages

Themes are the core data of the API.  The results are paginated and so multiple calls are needed to get the whole dataset.  Below we query the 3W theme for Afghanistan and return all results into a single object.  To query a different theme or country change the constant variable of ```THEME``` to another theme or ```LOCATION``` to a different ISO3 country code.

The current themes supported ```population```, ```3w```.

The current countries supported ```AFG```, ```MLI```, ```NGA```

### Python

```python
import urllib.request
import json

def fetch_data(base_url, limit=1000):
    """
    Fetch data from the provided base_url with pagination support.
    
    Args:
    - base_url (str): The base URL endpoint to fetch data from.
    - limit (int): The number of records to fetch per request.
    
    Returns:
    - list: A list of fetched results.
    """
    
    idx = 0
    results = []
    
    while True:
        offset = idx * limit
        url = f"{base_url}&offset={offset}&limit={limit}"
        
        with urllib.request.urlopen(url) as response:
            print(f"Getting results {offset} to {offset+limit-1}")
            json_response = json.loads(response.read())
            
            results.extend(json_response)
            
            # If the returned results are less than the limit, it's the last page
            if len(json_response) < limit:
                break
        
        idx += 1
        
    return results

THEME = "3w"
LOCATION = "AFG"
BASE_URL = f"https://placeholder.url/api/themes/{THEME}?output_format=json&location_code={LOCATION}"
LIMIT = 1000


results = fetch_data(BASE_URL, LIMIT)
print(results)
```

### Plain Javascript

```javascript
async function fetchData(baseUrl, limit = 1000) {
    let idx = 0;
    let results = [];

    while (true) {
        const offset = idx * limit;
        const url = `${baseUrl}&offset=${offset}&limit=${limit}`;

        console.log(`Getting results ${offset} to ${offset + limit - 1}`);
        
        const response = await fetch(url);
        const jsonResponse = await response.json();

        results = results.concat(jsonResponse);

        // If the returned results are less than the limit, it's the last page
        if (jsonResponse.length < limit) {
            break;
        }

        idx++;
    }

    return results;
}

const THEME = "3W"
const LOCATION = "AFG"
const BASE_URL = `https://placeholder.url/api/themes/${THEME}?output_format=json&location_code=${LOCATION}`;
const LIMIT = 1000;

window.onload = async function() {
    const results = await fetchData(BASE_URL, LIMIT);
    console.log(results);
};
```

### Node

```javascript
import fetch from 'node-fetch'

async function fetchData(baseUrl, limit = 1000) {
    let idx = 0;
    let results = [];

    while (true) {
        const offset = idx * limit;
        const url = `${baseUrl}&offset=${offset}&limit=${limit}`;

        console.log(`Getting results ${offset} to ${offset + limit - 1}`);
        
        const response = await fetch(url);
        const jsonResponse = await response.json();

        results = results.concat(jsonResponse);

        // If the returned results are less than the limit, it's the last page
        if (jsonResponse.length < limit) {
            break;
        }

        idx++;
    }

    return results;
}

const THEME = "3W"
const LOCATION = "AFG"
const BASE_URL = `https://placeholder.url/api/themes/${THEME}?output_format=json&location_code=${LOCATION}`;
const LIMIT = 1000;

fetchData(BASE_URL, LIMIT).then(results => {
    console.log(results);
});
```

### R

```R
library(jsonlite)
library(httr)

fetch_data <- function(base_url, limit = 1000) {
  idx <- 0
  results <- list()
  
  while(TRUE) {
    offset <- idx * limit
    url <- paste0(base_url, "&offset=", offset, "&limit=", limit)
    
    response <- GET(url)
    
    cat("Getting results", offset, "to", offset + limit - 1, "\n")
    
    json_response <- fromJSON(content(response, "text"))
    
    results <- append(results, list(json_response))
    
    # If the returned results are less than the limit, it's the last page
    if(nrow(json_response) < limit) {
      break
    }
    
    idx <- idx + 1
  }
  
  return(do.call(rbind, results))
}

THEME <- "3w"
LOCATION <- "AFG"
BASE_URL <- paste0("https://placeholder.url/api/themes/", THEME, "?output_format=json&location_code=", LOCATION)
LIMIT <- 1000

results <- fetch_data(BASE_URL, LIMIT)
print(results)
```

## 2. Filtering results

It is possible to add extra filters to the call to get a subset of results. To see the full set of filters that can be used for each theme, please check this documentation:

https://placeholder.url/docs#/humanitarian-response/

### Python

#### Filter by Sector

Change the code to include a new parameter in the URL.

```python
SECTOR= urllib.parse.quote("Emergency Shelter and NFI")
BASE_URL = f"https://placeholder.url/api/themes/{THEME}?output_format=json&location_code={LOCATION}&sector_name={SECTOR}"
```

#### Filter by Admin1

```python
ADMIN1= "AF01"
BASE_URL = f"https://placeholder.url/api/themes/{THEME}?output_format=json&location_code={LOCATION}&admin1_code={ADMIN1}"
```

### Plain Javascript and Node

Change the code to include a new parameter in the URL.

#### Filter by Sector

```javascript
const SECTOR = "Emergency Shelter and NFI"
const BASE_URL = `https://placeholder.url/api/themes/${THEME}?output_format=json&location_code=${LOCATION}&sector_name=${SECTOR}`;
```

#### Filter by Admin1

```javascript
const ADMIN1 = "AF01"
const BASE_URL = `https://placeholder.url/api/themes/${THEME}?output_format=json&location_code=${LOCATION}&admin1_code=${ADMIN1}`;
```

### R

Change the code to include a new parameter in the URL.

#### Filter by Sector

```R
SECTOR <- "Emergency Shelter and NFI"
BASE_URL <- paste0("https://placeholder.url/api/themes/", THEME, "?output_format=json&location_code=", LOCATION, "&sector_name=",SECTOR)
```

#### Filter by Admin1

```R
ADMIN1 <- "AF01"
BASE_URL <- paste0("https://placeholder.url/api/themes/", THEME, "?output_format=json&location_code=", LOCATION, "&admin1_code=",ADMIN1)
```

## 3. Filter for admin level

Some themes have data at multiple admin levels. If you don't filter for a particular levels you will recieve data from both in one call. To filter for just admin1 data add these parameters to URL
```
admin_level=1
```

## 4. Get data from supporting tables

Each supporting table such as ```orgs```, ```orgs_type```, ```sector``` and more have a unique URL to call to get the range of possible values.  Below we show the URL for getting of the sector names and codes.  Change the code at the top to have a new ```BASEURL``` and remove the URL parameters above it. Full code examples can be seen in the example repo.

### Python

```python
BASE_URL "https://placeholder.url/api/sector?output_format=json&offset=0&limit=1000"
```

### Javascript

```javascript
CONST BASE_URL "https://placeholder.url/api/sector?output_format=json&offset=0&limit=1000"
```

## 5. Get admin level data for a country

The admin1 and admin2 api end points provide data about subnational adminstration boundary names and p-codes (place codes). The geometry associated with each admin boundary is not yet available via the API, but it can be downloaded from HDX or obtained from the ITOS API service.

```
https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/{pCode}/versions/current/{format}/{level}
```

Here is an example of how to get the admin1 geojson for Afghanistan

```
https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1
```

[Full documentation](https://apps.itos.uga.edu/CODV2API/Help)
## 6. Download as CSV

The code examples so far have been using JSON output and then processing this data. To query this data as csv, change the ```output_format``` to ```csv``` as per the examples below. Visiting this URL through the browser will download the CSV to then be used on your computer.

```python
BASE_URL = "https://placeholder.url/api/admin1?location_code=MLI&output_format=csv&offset=0&limit=1000"
```

### Javascript

```javascript
CONST BASE_URL = "https://placeholder.url/api/admin1?location_code=MLI&output_format=csv&offset=0&limit=1000"
```

## 7. Query Population and join to GeoJson from ITOS service

### Python

```python
import urllib.request
import json

def fetch_data(base_url, limit=1000):
    """
    Fetch data from the provided base_url with pagination support.
    
    Args:
    - base_url (str): The base URL endpoint to fetch data from.
    - limit (int): The number of records to fetch per request.
    
    Returns:
    - list: A list of fetched results.
    """
    
    idx = 0
    results = []
    
    while True:
        offset = idx * limit
        url = f"{base_url}&offset={offset}&limit={limit}"
        
        with urllib.request.urlopen(url) as response:
            print(f"Getting results {offset} to {offset+limit-1}")
            json_response = json.loads(response.read())
            
            results.extend(json_response)
            
            # If the returned results are less than the limit, it's the last page
            if len(json_response) < limit:
                break
        
        idx += 1
        
    return results

def download_geojson(geojson_url):
    """
    Download GeoJSON data from the provided URL.
    
    Args:
    - geojson_url (str): The URL to download the GeoJSON data from.
    
    Returns:
    - dict: The GeoJSON data as a dictionary.
    """
    with urllib.request.urlopen(geojson_url) as response:
        print("Downloading GeoJSON data...")
        return json.loads(response.read())

def append_population_to_geojson(geojson, population_data):
    """
    Append population data to the GeoJSON properties.
    
    Args:
    - geojson (dict): The GeoJSON data.
    - population_data (list): The population data to append.
    
    Returns:
    - dict: The updated GeoJSON data.
    """
    for feature in geojson['features']:
        feature_id = feature['properties']['ADM1_PCODE']
        corresponding_data = next((item for item in population_data if item['admin1_code'] == feature_id), None)
        if corresponding_data:
             feature['properties']['population_f_80+'] = corresponding_data['population']
        pass

    return geojson

def save_geojson(geojson, filename):
    """
    Save the GeoJSON data to a file.
    
    Args:
    - geojson (dict): The GeoJSON data.
    - filename (str): The filename to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(geojson, file)
        print(f"GeoJSON saved to {filename}")

THEME = "population"
LOCATION = "AFG"
AGE_RANGE_CODE = "80%2B"
GENDER = "f"
BASE_URL = f"https://placeholder.url/api/themes/{THEME}?output_format=json&location_code={LOCATION}&age_range_code={AGE_RANGE_CODE}&gender={GENDER}&admin1_is_unspecified=false&admin2_is_unspecified=true"
LIMIT = 1000
results = fetch_data(BASE_URL, LIMIT)

geojson_url = "https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1"
geojson_data = download_geojson(geojson_url)
updated_geojson = append_population_to_geojson(geojson_data, results)
save_geojson(updated_geojson, 'updated_data.geojson')
```

### R

```R
library(httr)
library(jsonlite)

fetch_data <- function(base_url, limit=1000) {
  results <- list()
  idx <- 0
  
  repeat {
    offset <- idx * limit
    url <- sprintf("%s&offset=%d&limit=%d", base_url, offset, limit)
    print(sprintf("Getting results %d to %d", offset, offset+limit-1))
    
    response <- GET(url)
    stop_for_status(response)
    json_response <- content(response, "parsed", type = "application/json")
    
    results <- c(results, json_response)
    
    if (length(json_response) < limit) {
      break
    }
    idx <- idx + 1
  }
  
  return(results)
}

download_geojson <- function(geojson_url) {
  print("Downloading GeoJSON data...")
  response <- GET(geojson_url)
  stop_for_status(response)
  geojson_data <- content(response, "parsed", type = "application/json")
  return(geojson_data)
}

append_population_to_geojson <- function(geojson, population_data) {
  geojson$features <- lapply(geojson$features, function(feature) {
    feature_id <- feature$properties$ADM1_PCODE
    corresponding_data <- Filter(function(item) item$admin1_code == feature_id, population_data)
    if (length(corresponding_data) > 0) {
      feature$properties$population_f_80plus <- corresponding_data[[1]]$population
    }
    return(feature)
  })
  return(geojson)
}

save_geojson <- function(geojson, filename) {
  write_json(geojson, filename)
  print(paste("GeoJSON saved to", filename))
}

# Use the functions
THEME <- "population"
LOCATION <- "AFG"
AGE_RANGE_CODE <- "80%2B"
GENDER <- "f"
BASE_URL <- sprintf("https://placeholder.url/api/themes/%s?output_format=json&location_code=%s&age_range_code=%s&gender=%s&admin1_is_unspecified=false&admin2_is_unspecified=true",
                    THEME, LOCATION, AGE_RANGE_CODE, GENDER)
LIMIT <- 1000
results <- fetch_data(BASE_URL, LIMIT)

geojson_url <- "https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1"
geojson_data <- download_geojson(geojson_url)
updated_geojson <- append_population_to_geojson(geojson_data, results)
save_geojson(updated_geojson, 'updated_data.geojson')
```


## 8. Load data intoa google spreadsheet using app script and periodically update

### App script

#### 1. Create a New Google Spreadsheet:

Create a new Google Spreadsheet where you want to load the data.

#### 2. Open the Script Editor:

Click on Extensions -> Apps Script in the top menu to open the Google Apps Script editor.

#### 3. Use this code

A simple script that will fetch the API data and place it in the spreadsheet

```javascript
function loadApiData() {
  var baseUrl = "https://placeholder.url/api/themes/3w?output_format=json";
  var limit = 10000;
  var offset = 0;
  
  var allData = [];

  while (true) {
    // Fetch data from the current page
    var url = baseUrl + "&offset=" + offset + "&limit=" + limit;
    var response = UrlFetchApp.fetch(url);
    var jsonData = JSON.parse(response.getContentText());
    
    // If there's no data or less data than the limit, break out of the loop
    if (!jsonData.length || jsonData.length < limit) {
      allData = allData.concat(jsonData);
      break;
    }

    // Otherwise, store the data and increment the offset for the next page
    allData = allData.concat(jsonData);
    offset += limit;
  }

  // Convert the JSON data to a 2D array for the spreadsheet
  var dataArray = [];
  
  // If there's data, add headers from the first item's keys
  if (allData.length > 0) {
    dataArray.push(Object.keys(allData[0]));
  }

  allData.forEach(function(item) {
    var row = [];
    for (var key in item) {
      row.push(item[key]);
    }
    dataArray.push(row);
  });

  // Get the active sheet and clear existing data
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clear();

  // Write the headers and data to the spreadsheet
  if (dataArray.length > 0) {
    sheet.getRange(1, 1, dataArray.length, dataArray[0].length).setValues(dataArray);
  }
}

```

#### 4. Set up a Daily Trigger:

- Click on the clock icon on the left sidebar to view the project's triggers.
- Click on the + Add Trigger button at the bottom right.
- Set the function to loadApiData, the deployment to Head, the event source to Time-driven, and then select Day timer to choose a specific time of day.
- Click Save.

#### 5. Authorize the Script:

When you run the script for the first time or set up a trigger, it will ask for permissions. Make sure to grant them so the script can access the external API and modify your Google Spreadsheet.

Now, the script will run daily at the time you specified and load the API data into your Google Spreadsheet.