import json

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

# chartData = array of objects from the original spotify api;

# result = json_filter(chartData)
# save_to_json(result, "chart_data.json")