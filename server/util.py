import json

#last updated on 3/5/2023

# url used to fetch the data
# https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-global-weekly/latest

def json_filter(list):
    new_data_array = []
    for data in list:
        new_data = {
            "currentRank": data["chartEntryData"]["currentRank"],
            "trackName": data["trackMetadata"]["trackName"],
            "name": data["trackMetadata"]["artists"][0]["name"],
            "displayImageUri": data["trackMetadata"]["displayImageUri"],
            "value": data["chartEntryData"]["rankingMetric"]["value"]
        }
        new_data_array.append(new_data)
    return new_data_array

def save_to_json(data, filename):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


#chartData = []
		
# chartData = array of objects from the original spotify api;

# result = json_filter(chartData)
# save_to_json(result, "chart_data.json")