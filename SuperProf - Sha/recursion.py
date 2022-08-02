from visualiser.visualiser import Visualiser as vs


maps_data = {
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",

  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },

    ]
  }],
  "status": "OK"
}


"""Recursively fetch values from nested JSON."""

@vs()
def extract(obj, list, key):
    """Recursively search for values of key in JSON tree."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extract(v, arr, key)
            elif k == key:
                arr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extract(item, arr, key)
    return arr


arr = []
print(extract(maps_data, arr, 'text'))


