#!/usr/bin/env python3

import requests
import re
import json
from bs4 import BeautifulSoup


def retrieve_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from {url}")
        return None


def get_html_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None


def nepali_to_english(text):
    nepali_to_english = {
        '०': '0',
        '१': '1',
        '२': '2',
        '३': '3',
        '४': '4',
        '५': '5',
        '६': '6',
        '७': '7',
        '८': '8',
        '९': '9'
    }
    return ''.join([nepali_to_english.get(char, char) for char in text])


provinceDataBaseUrl = "https://sthaniya.gov.np/gis/data/Province{number}.json"
districtDataBaseUrl = "https://sthaniya.gov.np/gis/data/Dist_GaPa/{targetCode}.json"
municipalityDataBaseUrl = "https://sthaniya.gov.np/gis/gapanapa.php?p={did}-{gnid}-00"

provinceUrls = [provinceDataBaseUrl.replace("{number}", str(x)) for x in range(1,8)]

provinceData = []
for url in provinceUrls:
    print(f"Retrieving Data From {url}")
    province_data = retrieve_data(url)
    if province_data:
        print("--> Success!")
        provinceData.append(province_data)
    else:
        print("--> Failure!")

print("Extracting districts from province data.")
_districts = []
for provinceInfo in provinceData:
    _districts.append(provinceInfo["features"])
districts = [dist for distList in _districts for dist in distList]

print("Creating district urls.")
districeUrls = [districtDataBaseUrl.replace("{targetCode}", x["properties"]["TARGET"].title()) for x in districts]

districtData = []
for url in districeUrls:
    print(f"Retrieving Data From {url}")
    district_data = retrieve_data(url)
    if district_data:
        print("--> Success!")
        districtData.append(district_data)
    else:
        print("--> Failure!")

print("Extracting municipalities from district data.")
_municipalities = []
for districtInfo in districtData:
    _municipalities.append(districtInfo["features"])
municipalities = [mun for municipalityList in _municipalities for mun in municipalityList]

print("Creating municipality urls.")
municipalityUrls = []
for municipalitiy in municipalities:
    props = municipalitiy["properties"]
    name = props["FIRST_GaPa"] or ""
    district = props["FIRST_DIST"] or ""
    gnid = str(props["gnid"] or 0)
    did = str(props["did"] or 0)
    if did != "0" and gnid != "0" and district != "":
        municipalityUrls.append((name, district.title(), municipalityDataBaseUrl.replace("{gnid}", gnid).replace("{did}", did), did, gnid))

municipalityData = []
for url in municipalityUrls:
    print(f"Retrieving Data From {url[2]}")
    municipality_data = get_html_text(url[2])
    if municipality_data:
        pattern = r'जम्मा वडा संख्या\n(.+)'
        match = re.search(pattern, municipality_data, re.MULTILINE)
        if match:
            print("--> Success!")
            municipalityData.append((url[0], url[1], nepali_to_english(match.group(1)), url[3], url[4]))
        else:
            print("--> Failure!")
    else:
        print("--> Failure!")
        
finalData = []
for municipality in municipalityData:
    finalData.append({
        "name": municipality[0],
        "district": municipality[1],
        "ward": municipality[2],
        "did": municipality[3],
        "gnid": municipality[4]
    });
    

fileJson = json.dumps(finalData)
jsonFile = open("data.json", "w")
jsonFile.write(fileJson)
jsonFile.close()
