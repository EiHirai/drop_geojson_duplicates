import json

with open("./sample.json") as f:
    geojson = json.load(f)

def drop_geojson_duplicates(geojson):
    input = geojson['features']
    unique_geojson = list(map(json.loads, set(map(json.dumps, input))))
    output = {
        "features": unique_geojson,
        "type": "FeatureCollection"
    }
    print(output)
    return output

if __name__ == '__main__':
    drop_geojson_duplicates(geojson)
