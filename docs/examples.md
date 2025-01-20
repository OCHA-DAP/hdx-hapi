# Code Examples

---

In each of these code examples you will need to insert your generated app
identifier in place of `{ your app identifier }` text. To generate an app
identifier follow the getting started guide.

## 1. Query a sub-category end point and loop through pages

Themes are the core data of the API.  The results are paginated and so
multiple calls are needed to get the whole dataset.  Below we query the 3W
sub-category for Afghanistan and return all results into a single object.
To query a different sub-category or country change the constant variable
of `THEME` to another sub-category or `LOCATION` to a different
ISO3 country code.

=== "Python"

    ```python
    import json
    from urllib import request


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

            with request.urlopen(url) as response:
                print(f"Getting results {offset} to {offset+limit-1}")
                json_response = json.loads(response.read())

                results.extend(json_response['data'])

                # If the returned results are less than the limit,
                # it's the last page
                if len(json_response['data']) < limit:
                    break

            idx += 1

        return results


    APP_IDENTIFIER = { your app identifier }
    THEME = "coordination-context/operational-presence"
    LOCATION = "AFG"
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/{THEME}?"
        f"output_format=json"
        f"&location_code={LOCATION}"
        f"&app_identifier={APP_IDENTIFIER}"
    )
    LIMIT = 1000

    results = fetch_data(BASE_URL, LIMIT)
    print(results)
    ```

=== "JavaScript"

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

            results = results.concat(jsonResponse['data']);

            // If the returned results are less than the limit, it's the last page
            if (jsonResponse['data'].length < limit) {
                break;
            }

            idx++;
        }

        return results;
    }

    const APP_IDENTIFIER = { your app identifer }
    const THEME = "coordination-context/operational-presence"
    const LOCATION = "AFG"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    const LIMIT = 1000;
    window.onload = async function() {
        const results = await fetchData(BASE_URL, LIMIT);
        console.log(results);
    };
    ```

=== "Node.js"

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

            results = results.concat(jsonResponse['data']);

            // If the returned results are less than the limit, it's the last page
            if (jsonResponse['data'].length < limit) {
                break;
            }

            idx++;
        }

        return results;
    }

    const APP_IDENTIFIER = { your app identifer }
    const THEME = "coordination-context/operational-presence"
    const LOCATION = "AFG"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    const LIMIT = 1000;

    fetchData(BASE_URL, LIMIT).then(results => {
        console.log(results);
    });
    ```

=== "R"

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

        results <- append(results, list(json_response$data))

        # If the returned results are less than the limit, it's the last page
        if(length(json_response$data) < limit) {
          break
        }

        idx <- idx + 1
      }

      return(results)
    }

    APP_IDENTIFIER <- { your app identifier }
    THEME <- "coordination-context/operational-presence"
    LOCATION <- "AFG"
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/", THEME, "?",
        "output_format=json",
        "&location_code=", LOCATION,
        "&app_identifier=", APP_IDENTIFIER
    )
    LIMIT <- 1000

    results <- fetch_data(BASE_URL, LIMIT)
    print(results)
    ```

## 2. Filtering results

It is possible to add extra filters to the call to get a subset of results.
To see the full set of filters that can be used for each sub-category,
please check
[the API endpoint documentation](https://hapi.humdata.org/docs).

### Filter by Sector

Change the code to include a new parameter in the URL.

=== "Python"

    ```python
    from urllib import parse

    SECTOR = parse.quote("Emergency Shelter and NFI")
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/{THEME}?"
        f"output_format=json"
        f"&location_code={LOCATION}"
        f"&sector_name={SECTOR}"
        f"&app_identifier={APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const SECTOR = "Emergency Shelter and NFI"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&sector_name=${SECTOR}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const SECTOR = "Emergency Shelter and NFI"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&sector_name=${SECTOR}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    SECTOR <- "Emergency Shelter and NFI"
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/", THEME, "?",
        "output_format=json",
        "&location_code=", LOCATION,
        "&sector_name=", SECTOR,
        '&app_identifier=", APP_IDENTIFIER
    )
    ```

### Filter by Admin 1 P-code

=== "Python"

    ```python
    ADMIN1= "AF01"
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/{THEME}?"
        f"output_format=json"
        f"&location_code={LOCATION}"
        f"&admin1_code={ADMIN1}"
        f"&app_identifier={APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const ADMIN1 = "AF01"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&admin1_code=${ADMIN1}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const ADMIN1 = "AF01"
    const BASE_URL = `https://hapi.humdata.org/api/v1/${THEME}?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&admin1_code=${ADMIN1}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    ADMIN1 <- "AF01"
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/", THEME, "?",
        "output_format=json",
        "&location_code=", LOCATION,
        "&admin1_code=", ADMIN1,
        "&app_identifier=", APP_IDENTIFIER
    )
    ```

## 3. Filter for admin level

Some sub-categories have data at multiple admin levels. If you don't filter
for a particular level, you could receive data from multiple levels
in one call. To filter
for only admin 1 data, add this parameter to the URL:

```shell
&admin_level=1
```

## 4. Get data from supporting tables

Each supporting table such as `orgs`, `orgs_type`, `sector` and more have a
unique URL to call to get the range of possible values. Below we show the
base URL for getting of the sector names and codes.

=== "Python"

    ```python
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/metadata/sector?"
        f"output_format=json"
        f"&app_identifier=${APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/sector?` +
                     `output_format=json` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/sector?` +
                     `output_format=json` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/metadata/sector?"
        "output_format=json"
        "&app_identifier=", APP_IDENTIFIER
    )
    ```

## 5. Getting dataset metadata for a resource

Each row returned from a sub-category endpoint contains the field
`resource_hdx_id`, which can be used to obtain the dataset metadata,
including information about the contributing organization,
from the `resource` endpoint

=== "Python"

    ```python
    RESOURCE_HDX_ID = "562e7757-0683-4d61-87bd-a7c94af2ee38"
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/metadata/resource?"
        f"output_format=json"
        f"&resource_hdx_id={RESOURCE_HDX_ID}"
        f"&app_identifier={APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const RESOURCE_HDX_ID = "562e7757-0683-4d61-87bd-a7c94af2ee38"
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/resource?` +
                     `output_format=json` +
                     `&resource_hdx_id=${RESOURCE_HDX_ID}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const RESOURCE_HDX_ID = "562e7757-0683-4d61-87bd-a7c94af2ee38"
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/resource?` +
                     `output_format=json` +
                     `&resource_hdx_id=${RESOURCE_HDX_ID}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    RESOURCE_HDX_ID <- "562e7757-0683-4d61-87bd-a7c94af2ee38"
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/metadata/resource?"
        "output_format=json"
        "&resource_hdx_id", RESOURCE_HDX_ID,
        "&app_identifier=", APP_IDENTIFIER
    )
    ```

## 6. Get admin level data for a country

The admin 1 and admin 2 API endpoints provide data about subnational
administrative boundary names and p-codes (place codes). Below is an
example that will retrieve the admin 1 level information for Afghanistan:

=== "Python"

    ```python
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/metadata/admin1?"
        f"output_format=json"
        f"&location_code={LOCATION}"
        f"&app_identifier=${APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/admin1?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/admin1?` +
                     `output_format=json` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/metadata/admin1?"
        "output_format=json"
        "&location_code=", LOCATION,
        "&app_identifier=", APP_IDENTIFIER
    )
    ```

The geometry
associated with each admin boundary is not yet available via the API,
but it can be downloaded from HDX or obtained from the ITOS API service:

```shell
https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/{p-code}/versions/current/{format}/{level}
```

Here is an example of how to get the admin 1 geojson for Afghanistan:

```shell
https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1
```

Please see the [full documentation](https://apps.itos.uga.edu/CODV2API/Help)
for more details.

## 7. Download as CSV

The code examples so far have been using JSON output and then processing this
data. To query this data as csv, change the `output_format` to `csv` as per
the examples below. Visiting this URL through the browser will download the
CSV to then be used on your computer.

=== "Python"

    ```python
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/metadata/admin1?"
        f"output_format=csv"
        f"&location_code={LOCATION}"
        f"&app_identifier={APP_IDENTIFIER}"
    )
    ```

=== "JavaScript"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/admin1?` +
                     `output_format=csv` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = `https://hapi.humdata.org/api/v1/metadata/admin1?` +
                     `output_format=csv` +
                     `&location_code=${LOCATION}` +
                     `&app_identifier=${APP_IDENTIFIER}`;
    ```

=== "R"

    ```R
    SECTOR <- "Emergency Shelter and NFI"
    BASE_URL <- paste0(
        "https://hapi.humdata.org/api/v1/metadata/admin1",
        "output_format=csv",
        "&location_code=", LOCATION,
        "&sector_name=", SECTOR,
        '&app_identifier=", APP_IDENTIFIER
    )
    ```

## 8. Query Population and join to GeoJson from ITOS service

=== "Python"

    ```python
    import json
    from urllib import request


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
            print(url)
            with request.urlopen(url) as response:
                print(f"Getting results {offset} to {offset+limit-1}")
                json_response = json.loads(response.read())

                results.extend(json_response['data'])

                # If the returned results are less than the limit,
                # it's the last page
                if len(json_response['data']) < limit:
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
        with request.urlopen(geojson_url) as response:
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
            corresponding_data = next(
                (
                    item
                    for item in population_data
                    if item['admin1_code'] == feature_id
                ),
                None,
            )
            if corresponding_data:
                feature['properties']['population_f_80+'] = corresponding_data[
                    'population'
                ]
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


    APP_IDENTIFIER = { your app identifier }
    THEME = "population-social/population"
    LOCATION = "AFG"
    AGE_RANGE = "0-4"
    GENDER = "f"
    BASE_URL = (
        f"https://hapi.humdata.org/api/v1/{THEME}?"
        f"output_format=json"
        f"&location_code={LOCATION}"
        f"&age_range={AGE_RANGE_CODE}"
        f"&gender={GENDER}"
        f"&admin_level=1"
        f"&app_identifier=APP_IDENTIFIER"
    )
    LIMIT = 1000
    results = fetch_data(BASE_URL, LIMIT)

    geojson_url = ("https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/"
                   "locations/AFG/versions/current/geoJSON/1")
    geojson_data = download_geojson(geojson_url)
    updated_geojson = append_population_to_geojson(geojson_data, results)
    save_geojson(updated_geojson, 'updated_data.geojson')

    ```

=== "R"

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

        results <- c(results, json_response$data)

        if (length(json_response$data) < limit) {
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
        corresponding_data <- Filter(function(item) {
          item$admin1_code == feature_id
        }, population_data)
        if (length(corresponding_data) > 0) {
          feature$properties$population_f_80plus <-
            corresponding_data[[1]]$population
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
    APP_IDENTIFIER <- { your app identifier }
    THEME <- "population-social/population"
    LOCATION <- "AFG"
    AGE_RANGE <- "0-4"
    GENDER <- "f"
    BASE_URL <- paste0(
            "https://hapi.humdata.org/api/v1/", THEME, "?",
            "output_format=json",
            "&location_code=", LOCATION,
            "&age_range", AGE_RANGE,
            "&gender", GENDER,
            "&app_identifier=", APP_IDENTIFIER
        )
    LIMIT <- 1000
    results <- fetch_data(BASE_URL, LIMIT)

    geojson_url <- paste0(
      "https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/",
      "locations/AFG/versions/current/geoJSON/1"
    )
    geojson_data <- download_geojson(geojson_url)
    updated_geojson <- append_population_to_geojson(geojson_data, results)
    save_geojson(updated_geojson, 'updated_data.geojson')
    ```

## 9. Load data into Google Sheets using an app script and periodically update

### 1. Create a New Google Spreadsheet:

Create a new Google Spreadsheet where you want to load the data.

### 2. Open the Script Editor:

Click on Extensions -> Apps Script in the top menu to open the Google Apps
Script editor.

### 3. Use this code:

A simple script that will fetch the API data and place it in the spreadsheet

=== "JavaScript"
    ```javascript
    function loadApiData() {
      var baseUrl = "https://hapi.humdata.org/api/v1/coordination-context/" +
                  "operational-presence?output_format=json&" +
                  "location_code=AFG&app_identifier={ your app identifier }";
      var limit = 10000;
      var offset = 0;

      var allData = [];

      while (true) {
        // Fetch data from the current page
        var url = baseUrl + "&offset=" + offset + "&limit=" + limit;
        var response = UrlFetchApp.fetch(url);
        var jsonData = JSON.parse(response.getContentText());

        // If there's no data or less data than the limit, break out of the loop
        if (!jsonData.data.length || jsonData.data.length < limit) {
          allData = allData.concat(jsonData.data);
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
        sheet.getRange(1, 1, dataArray.length,
                       dataArray[0].length).setValues(dataArray);
      }
    }

    ```

### 4. Set up a Daily Trigger:

- Click on the clock icon on the left sidebar to view the project's triggers.
- Click on the + Add Trigger button at the bottom right.
- Set the function to loadApiData, the deployment to Head, the event source to
  Time-driven, and then select Day timer to choose a specific time of day.
- Click Save.

### 5. Authorize the Script:

When you run the script for the first time or set up a trigger, it will ask
for permissions. Make sure to grant them so the script can access the external
API and modify your Google Spreadsheet.

Now, the script will run daily at the time you specified and load the API
data into your Google Spreadsheet.
