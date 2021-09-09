import requests
import json
import urllib
import pandas as pd

# Use the filters as it is only possible to extract 1000 companies at a time.

# Decide whether you want the export as a json or csv file
export_type = "csv"

# enter the path for the export file
file_path = "current_dir"


# insert the following filters as a string as they are published at ycombinator.com.
# Seperate them by a comma. ["S21", "S20"]

# if all you want all batches insert nothing. If you want specific batches,
# S21, W21, S20, W20, S19, W19, S18, W18, S17, W17, IK12, S16, W16, S15, W15, S14, W14,
# S13, W13,S12, W12, S11, W11, S10, W10, S09, W09, S08, W08, S07, W07, S06, W06, S05
batch = []


# if all you want all industries insert nothing for certain industries choose between B2B Software,
# Services, Education, Consumer, Healthcare, Real Estate, Construction, Financial Technology, Industrials or Government.
industries = []

# Filter after different status with the following Active, Public, Acquired & Inactive Status.
# if all you want all companies regardless the status let the filter empty
status = []


# if all you want all (anywhere) insert nothing. If you want specific choose between,
# North America, Asia, Europe, Africa, Central America, South America, Oceania
regions = []


def create_facet_filters(batch, industries, status, regions):
    facet_filters = []

    filters = {
        "batch": batch,
        "industries": industries,
        "status": status,
        "regions": regions,
    }

    for key, value in filters.items():
        # skiping a filter if filter is emtpy
        if len(value) == 0:
            continue

        value = list(map(lambda x: f"{key}:" + x, value))
        facet_filters.append(value)

    return json.dumps(facet_filters)


def create_params_string():

    facets = [
        "top_company",
        "isHiring",
        "nonprofit",
        "batch",
        "industries",
        "subindustry",
        "status",
        "regions",
    ]
    facetFilters = create_facet_filters(batch, industries, status, regions)
    params = {
        "hitsPerPage": "1000",
        "query": "",
        "page": "0",
        "facets": json.dumps(facets),
        "tagFilters": "",
        "facetFilters": facetFilters,
    }

    return urllib.parse.urlencode(params)


def request_data_companies():
    params = create_params_string()
    url = "https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries"

    querystring = {
        "x-algolia-agent": "Algolia for JavaScript (3.35.1); Browser; JS Helper (3.4.4)",
        "x-algolia-application-id": "45BWZJ1SGC",
        "x-algolia-api-key": "Zjk5ZmFjMzg2NmQxNTA0NGM5OGNiNWY4MzQ0NDUyNTg0MDZjMzdmMWY1NTU2YzZkZGVmYjg1ZGZjMGJlYjhkN3Jlc3RyaWN0SW5kaWNlcz1ZQ0NvbXBhbnlfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTVEJmFuYWx5dGljc1RhZ3M9JTVCJTIyeWNkYyUyMiU1RA==",
    }

    payload = {
        "requests": [
            {
                "indexName": "YCCompany_production",
                # "params": "hitsPerPage=3000&query=&page=0&facets=%5B%22top_company%22%2C%22isHiring%22%2C%22nonprofit%22%2C%22batch%22%2C%22industries%22%2C%22subindustry%22%2C%22status%22%2C%22regions%22%5D&tagFilters=&facetFilters=%5B%5B%22batch%3AS21%22%2C%22batch%3AW21%22%2C%22batch%3AS20%22%5D%2C%5B%22industries%3AHealthcare%22%5D%5D",
                "params": params,
            },
            {
                "indexName": "YCCompany_production",
                "params": "hitsPerPage=1&query=&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D§&tagFilters=&analytics=false&clickAnalytics=false&facets=batch",
            },
        ]
    }

    headers = {
        "Connection": "keep-alive",
        "accept": "application/json",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "content-type": "application/json",
        "Origin": "https://www.ycombinator.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.ycombinator.com/",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7",
    }

    response = requests.request(
        "POST", url, json=payload, headers=headers, params=querystring
    )

    return json.loads(response.text)


def export_df_to_csv(df, file_path=file_path, export_type=export_type):
    df.to_csv(
        path_or_buf=f"{file_path}.{export_type}",
        encoding="utf-8",
        sep="\t",
        index=False,
    )


def export_df_to_json(df, file_path=file_path, export_type=export_type):
    df.to_json(path_or_buf=f"{file_path}.{export_type}")


def clean_and_export_data():
    # Clean data process - export to json and pandas?
    response = request_data_companies()
    response = response["results"][0]["hits"]
    # convert response to pandas dataframe and clean data
    data = pd.json_normalize(response)
    data = data.iloc[:, :-4]

    if export_type == "csv":
        export_df_to_csv(data)
    else:
        export_df_to_json(data)


clean_and_export_data()
# EOF
