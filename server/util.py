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


chartData = [
    {
        "chartEntryData": {
            "currentRank": 1,
            "previousRank": 1,
            "peakRank": 1,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "115156896",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-19",
            "entryRank": 1,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Flowers",
            "trackUri": "spotify:track:0yLdNVWF3Srea0uzk55zFn",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02f429549123dbe8552764ba1d",
            "artists": [
                {
                    "name": "Miley Cyrus",
                    "spotifyUri": "spotify:artist:5YGY8feqx7naU7z4HrwZM6"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2023-01-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 2,
            "previousRank": 2,
            "peakRank": 2,
            "appearancesOnChart": 3,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "62870405",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-19",
            "entryRank": 39,
            "entryDate": "2023-01-12"
        },
        "trackMetadata": {
            "trackName": "Shakira: Bzrp Music Sessions, Vol. 53",
            "trackUri": "spotify:track:4nrPB8O7Y7wsOCJdgXkthe",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02511a66760837c2496d3375ca",
            "artists": [
                {
                    "name": "Bizarrap",
                    "spotifyUri": "spotify:artist:716NhGYqD1jl2wI1Qkgq36"
                },
                {
                    "name": "Shakira",
                    "spotifyUri": "spotify:artist:0EmeFodog0BfCgMzAIvKQp"
                }
            ],
            "labels": [
                {
                    "name": "DALE PLAY Records"
                }
            ],
            "releaseDate": "2023-01-11"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 3,
            "previousRank": 3,
            "peakRank": 1,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 7,
            "rankingMetric": {
                "value": "54778101",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-05",
            "entryRank": 3,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Kill Bill",
            "trackUri": "spotify:track:1Qrg8KqiBpW07V7PNxwwwL",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020c471c36970b9406233842a5",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-08"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 4,
            "previousRank": 4,
            "peakRank": 2,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "36446537",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-12",
            "entryRank": 3,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "Creepin' (with The Weeknd & 21 Savage)",
            "trackUri": "spotify:track:2dHHgzDwk4BJdRwy9uXhTO",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0213e54d6687e65678d60466c2",
            "artists": [
                {
                    "name": "Metro Boomin",
                    "spotifyUri": "spotify:artist:0iEtIxbK0KxaSlF7G42ZOp"
                },
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                },
                {
                    "name": "21 Savage",
                    "spotifyUri": "spotify:artist:1URnnhqYAYcrqrcwql10ft"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-12-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 5,
            "previousRank": 5,
            "peakRank": 1,
            "appearancesOnChart": 18,
            "consecutiveAppearancesOnChart": 18,
            "rankingMetric": {
                "value": "31463400",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2022-09-29",
            "entryRank": 1,
            "entryDate": "2022-09-29"
        },
        "trackMetadata": {
            "trackName": "Unholy (feat. Kim Petras)",
            "trackUri": "spotify:track:3nqQXoyQOWXiESFLlDF1hG",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a935e4689f15953311772cc4",
            "artists": [
                {
                    "name": "Sam Smith",
                    "spotifyUri": "spotify:artist:2wY79sveU1sp5g7SokKOiI"
                },
                {
                    "name": "Kim Petras",
                    "spotifyUri": "spotify:artist:3Xt3RrJMFv5SZkCfUE8C1J"
                }
            ],
            "labels": [
                {
                    "name": "EMI"
                }
            ],
            "releaseDate": "2022-09-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 6,
            "previousRank": 7,
            "peakRank": 1,
            "appearancesOnChart": 43,
            "consecutiveAppearancesOnChart": 43,
            "rankingMetric": {
                "value": "29518028",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-07",
            "entryRank": 1,
            "entryDate": "2022-04-07"
        },
        "trackMetadata": {
            "trackName": "As It Was",
            "trackUri": "spotify:track:4Dvkj6JhhA12EX05fT7y2e",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022e8ed79e177ff6011076f5f0",
            "artists": [
                {
                    "name": "Harry Styles",
                    "spotifyUri": "spotify:artist:6KImCVD70vtIoJWnq6nGn3"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2022-05-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 7,
            "previousRank": 9,
            "peakRank": 2,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 22,
            "rankingMetric": {
                "value": "26861182",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-09-29",
            "entryRank": 26,
            "entryDate": "2022-09-01"
        },
        "trackMetadata": {
            "trackName": "I'm Good (Blue)",
            "trackUri": "spotify:track:4uUG5RXrOk84mYEfFvj3cK",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02933c036cd61cd40d3f17a9c4",
            "artists": [
                {
                    "name": "David Guetta",
                    "spotifyUri": "spotify:artist:1Cs0zKBU1kc0i8ypK3B9ai"
                },
                {
                    "name": "Bebe Rexha",
                    "spotifyUri": "spotify:artist:64M6ah0SkkRsnPGtGiRAbb"
                }
            ],
            "labels": [
                {
                    "name": "Parlophone UK"
                }
            ],
            "releaseDate": "2022-08-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 8,
            "previousRank": 6,
            "peakRank": 4,
            "appearancesOnChart": 30,
            "consecutiveAppearancesOnChart": 30,
            "rankingMetric": {
                "value": "25979878",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-20",
            "entryRank": 157,
            "entryDate": "2022-07-07"
        },
        "trackMetadata": {
            "trackName": "La Bachata",
            "trackUri": "spotify:track:5ww2BF9slyYgNOk37BlC4u",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c9f744b0d62da795bc21d04a",
            "artists": [
                {
                    "name": "Manuel Turizo",
                    "spotifyUri": "spotify:artist:0tmwSHipWxN12fsoLcFU3B"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin/La Industria"
                }
            ],
            "releaseDate": "2022-05-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 9,
            "previousRank": 10,
            "peakRank": 1,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "25430315",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-27",
            "entryRank": 1,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Anti-Hero",
            "trackUri": "spotify:track:0V3wPSX9ygBnCm8psDIegu",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bb54dde68cd23e2a268ae0f5",
            "artists": [
                {
                    "name": "Taylor Swift",
                    "spotifyUri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
                }
            ],
            "labels": [
                {
                    "name": "Taylor Swift"
                }
            ],
            "releaseDate": "2022-10-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 10,
            "previousRank": 8,
            "peakRank": 8,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "24810571",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-12",
            "entryRank": 9,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "La Jumpa",
            "trackUri": "spotify:track:2mnXxnrX5vCGolNkaFvVeM",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0230326b23e30ae93d4d48165b",
            "artists": [
                {
                    "name": "Arcángel",
                    "spotifyUri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
                },
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC."
                }
            ],
            "releaseDate": "2022-12-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 11,
            "previousRank": 14,
            "peakRank": 11,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 22,
            "rankingMetric": {
                "value": "24752919",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 111,
            "entryDate": "2022-09-01"
        },
        "trackMetadata": {
            "trackName": "Calm Down (with Selena Gomez)",
            "trackUri": "spotify:track:0WtM2NBVQNNJLh6scP13H8",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a3a7f38ea2033aa501afd4cf",
            "artists": [
                {
                    "name": "Rema",
                    "spotifyUri": "spotify:artist:46pWGuE3dSwY3bMMXGBvVS"
                },
                {
                    "name": "Selena Gomez",
                    "spotifyUri": "spotify:artist:0C8ZW7ezQVs4URX5aX7Kqx"
                }
            ],
            "labels": [
                {
                    "name": "Mavin Records / Jonzing World"
                }
            ],
            "releaseDate": "2022-08-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 12,
            "previousRank": 12,
            "peakRank": 12,
            "appearancesOnChart": 9,
            "consecutiveAppearancesOnChart": 9,
            "rankingMetric": {
                "value": "24497579",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-12",
            "entryRank": 136,
            "entryDate": "2022-12-01"
        },
        "trackMetadata": {
            "trackName": "Escapism.",
            "trackUri": "spotify:track:5WxVXxCMRnvxUKFq40ELwq",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0257dd31ec4e9dbc7f4238f69a",
            "artists": [
                {
                    "name": "RAYE",
                    "spotifyUri": "spotify:artist:5KKpBU5eC2tJDzf0wmlRp2"
                },
                {
                    "name": "070 Shake",
                    "spotifyUri": "spotify:artist:12Zk1DFhCbHY6v3xep2ZjI"
                }
            ],
            "labels": [
                {
                    "name": "Human Re Sources"
                }
            ],
            "releaseDate": "2022-11-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 13,
            "previousRank": 11,
            "peakRank": 1,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "21887472",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-07-21",
            "entryRank": 3,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "Quevedo: Bzrp Music Sessions, Vol. 52",
            "trackUri": "spotify:track:2tTmW7RDtMQtBk7m2rYeSw",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021630dd349221a35ce03a0ccf",
            "artists": [
                {
                    "name": "Bizarrap",
                    "spotifyUri": "spotify:artist:716NhGYqD1jl2wI1Qkgq36"
                },
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                }
            ],
            "labels": [
                {
                    "name": "DALE PLAY Records"
                }
            ],
            "releaseDate": "2022-07-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 14,
            "previousRank": 15,
            "peakRank": 14,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 7,
            "rankingMetric": {
                "value": "21796337",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 194,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Sure Thing",
            "trackUri": "spotify:track:0JXXNGljqupsJaZsgSbMZV",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d5a8395b0d80b8c48a5d851c",
            "artists": [
                {
                    "name": "Miguel",
                    "spotifyUri": "spotify:artist:360IAlyVv4PCEVjgyMZrxK"
                }
            ],
            "labels": [
                {
                    "name": "Jive"
                }
            ],
            "releaseDate": "2010-11-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 15,
            "previousRank": 17,
            "peakRank": 15,
            "appearancesOnChart": 3,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "21542312",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 54,
            "entryDate": "2023-01-12"
        },
        "trackMetadata": {
            "trackName": "Yandel 150",
            "trackUri": "spotify:track:4FAKtPVycI4DxoOHC01YqD",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b2aec01b56eeb74610532700",
            "artists": [
                {
                    "name": "Yandel",
                    "spotifyUri": "spotify:artist:0eHQ9o50hj6ZDNBt6Ys1sD"
                },
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "La Leyenda LLC"
                }
            ],
            "releaseDate": "2023-01-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 16,
            "previousRank": 21,
            "peakRank": 16,
            "appearancesOnChart": 13,
            "consecutiveAppearancesOnChart": 13,
            "rankingMetric": {
                "value": "21137572",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 171,
            "entryDate": "2022-11-03"
        },
        "trackMetadata": {
            "trackName": "Here With Me",
            "trackUri": "spotify:track:78Sw5GDo6AlGwTwanjXbGh",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02efbe96040319db682b438f11",
            "artists": [
                {
                    "name": "d4vd",
                    "spotifyUri": "spotify:artist:5y8tKLUfMvliMe8IKamR32"
                }
            ],
            "labels": [
                {
                    "name": "Darkroom/Interscope Records"
                }
            ],
            "releaseDate": "2022-09-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 17,
            "previousRank": 44,
            "peakRank": 17,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "20784498",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 44,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Nonsense",
            "trackUri": "spotify:track:6dgUya35uo964z7GZXM07g",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02700f7bf79c9f063ad0362bdf",
            "artists": [
                {
                    "name": "Sabrina Carpenter",
                    "spotifyUri": "spotify:artist:74KM79TiuVKeVCqs8QtB0B"
                }
            ],
            "labels": [
                {
                    "name": "Island Records"
                }
            ],
            "releaseDate": "2022-07-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 18,
            "previousRank": 13,
            "peakRank": 11,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 6,
            "rankingMetric": {
                "value": "20632465",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-12",
            "entryRank": 81,
            "entryDate": "2022-12-22"
        },
        "trackMetadata": {
            "trackName": "Ditto",
            "trackUri": "spotify:track:3r8RuvgbX9s7ammBn07D3W",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02edf5b257be1d6593e81bb45f",
            "artists": [
                {
                    "name": "NewJeans",
                    "spotifyUri": "spotify:artist:6HvZYsbFfjnjFrWF950C9d"
                }
            ],
            "labels": [
                {
                    "name": "ADOR"
                }
            ],
            "releaseDate": "2022-12-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 19,
            "previousRank": 16,
            "peakRank": 14,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 22,
            "rankingMetric": {
                "value": "20504453",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-12",
            "entryRank": 85,
            "entryDate": "2022-09-01"
        },
        "trackMetadata": {
            "trackName": "golden hour",
            "trackUri": "spotify:track:5odlY52u43F5BjByhxg7wg",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c2504e80ba2f258697ab2954",
            "artists": [
                {
                    "name": "JVKE",
                    "spotifyUri": "spotify:artist:164Uj4eKjl6zTBKfJLFKKK"
                }
            ],
            "labels": [
                {
                    "name": "JVKE"
                }
            ],
            "releaseDate": "2022-09-23"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 20,
            "previousRank": 18,
            "peakRank": 14,
            "appearancesOnChart": 15,
            "consecutiveAppearancesOnChart": 15,
            "rankingMetric": {
                "value": "20384930",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-24",
            "entryRank": 119,
            "entryDate": "2022-10-20"
        },
        "trackMetadata": {
            "trackName": "Hey Mor",
            "trackUri": "spotify:track:1zsPaEkglFvxjAhrM8yhpr",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02125624f2e04f5a1ccb0dfb45",
            "artists": [
                {
                    "name": "Ozuna",
                    "spotifyUri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
                },
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "Aura Music Corp."
                }
            ],
            "releaseDate": "2022-10-07"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 21,
            "previousRank": 23,
            "peakRank": 19,
            "appearancesOnChart": 50,
            "consecutiveAppearancesOnChart": 41,
            "rankingMetric": {
                "value": "19754115",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-12",
            "entryRank": 179,
            "entryDate": "2016-12-29"
        },
        "trackMetadata": {
            "trackName": "Die For You",
            "trackUri": "spotify:track:2LBqCSwhJGcFQeTHMVGwy3",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a048415db06a5b6fa7ec4e1a",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2016-11-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 22,
            "previousRank": 19,
            "peakRank": 15,
            "appearancesOnChart": 94,
            "consecutiveAppearancesOnChart": 94,
            "rankingMetric": {
                "value": "19653525",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-13",
            "entryRank": 117,
            "entryDate": "2021-04-15"
        },
        "trackMetadata": {
            "trackName": "Another Love",
            "trackUri": "spotify:track:7jtQIBanIiJOMS6RyCx6jZ",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021917a0f3f4152622a040913f",
            "artists": [
                {
                    "name": "Tom Odell",
                    "spotifyUri": "spotify:artist:2txHhyCwHjUEpJjWrEyqyX"
                }
            ],
            "labels": [
                {
                    "name": "ITNO/Columbia"
                }
            ],
            "releaseDate": "2013-06-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 23,
            "previousRank": 22,
            "peakRank": 7,
            "appearancesOnChart": 34,
            "consecutiveAppearancesOnChart": 34,
            "rankingMetric": {
                "value": "19584423",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-09-15",
            "entryRank": 139,
            "entryDate": "2022-06-09"
        },
        "trackMetadata": {
            "trackName": "I Ain't Worried",
            "trackUri": "spotify:track:4h9wh7iOZ0GGn8QVp4RAOB",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ec96e006b8bdfc582610ec13",
            "artists": [
                {
                    "name": "OneRepublic",
                    "spotifyUri": "spotify:artist:5Pwc4xIPtQLFEnJriah9YJ"
                }
            ],
            "labels": [
                {
                    "name": "Interscope Records"
                }
            ],
            "releaseDate": "2022-05-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 24,
            "previousRank": 30,
            "peakRank": 24,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "18435450",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 95,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "OMG",
            "trackUri": "spotify:track:65FftemJ1DbbZ45DUfHJXE",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d70036292d54f29e8b68ec01",
            "artists": [
                {
                    "name": "NewJeans",
                    "spotifyUri": "spotify:artist:6HvZYsbFfjnjFrWF950C9d"
                }
            ],
            "labels": [
                {
                    "name": "ADOR"
                }
            ],
            "releaseDate": "2023-01-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 25,
            "previousRank": 24,
            "peakRank": 19,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 6,
            "rankingMetric": {
                "value": "17872222",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-22",
            "entryRank": 19,
            "entryDate": "2022-12-22"
        },
        "trackMetadata": {
            "trackName": "LET GO",
            "trackUri": "spotify:track:3zkyus0njMCL6phZmNNEeN",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028f5c20e9e14b843f1c5dddba",
            "artists": [
                {
                    "name": "Central Cee",
                    "spotifyUri": "spotify:artist:5H4yInM5zmHqpKIoMNAx4r"
                }
            ],
            "labels": [
                {
                    "name": "Central Cee"
                }
            ],
            "releaseDate": "2022-12-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 26,
            "previousRank": 27,
            "peakRank": 15,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "17736223",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-12-08",
            "entryRank": 15,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "Superhero (Heroes & Villains) [with Future & Chris Brown]",
            "trackUri": "spotify:track:0vjeOZ3Ft5jvAi9SBFJm1j",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0213e54d6687e65678d60466c2",
            "artists": [
                {
                    "name": "Metro Boomin",
                    "spotifyUri": "spotify:artist:0iEtIxbK0KxaSlF7G42ZOp"
                },
                {
                    "name": "Future",
                    "spotifyUri": "spotify:artist:1RyvyyTE3xzB2ZywiAwp0i"
                },
                {
                    "name": "Chris Brown",
                    "spotifyUri": "spotify:artist:7bXgB6jMjp9ATFy66eO08Z"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-12-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 27,
            "previousRank": 20,
            "peakRank": 20,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "17546155",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 59,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Bebe Dame",
            "trackUri": "spotify:track:0IKeDy5bT9G0bA7ZixRT4A",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025f3aef5159749e4b61686670",
            "artists": [
                {
                    "name": "Fuerza Regida",
                    "spotifyUri": "spotify:artist:0ys2OFYzWYB5hRDLCsBqxt"
                },
                {
                    "name": "Grupo Frontera",
                    "spotifyUri": "spotify:artist:6XkjpgcEsYab502Vr1bBeW"
                }
            ],
            "labels": [
                {
                    "name": "Rancho Humilde/Street Mob Records"
                }
            ],
            "releaseDate": "2022-12-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 28,
            "previousRank": 25,
            "peakRank": 2,
            "appearancesOnChart": 12,
            "consecutiveAppearancesOnChart": 12,
            "rankingMetric": {
                "value": "17442466",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-10",
            "entryRank": 2,
            "entryDate": "2022-11-10"
        },
        "trackMetadata": {
            "trackName": "Rich Flex",
            "trackUri": "spotify:track:1bDbXMyjaUIooNwFE9wn0N",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0202854a7060fccc1a66a4b5ad",
            "artists": [
                {
                    "name": "Drake",
                    "spotifyUri": "spotify:artist:3TVXtAsR1Inumwj472S9r4"
                },
                {
                    "name": "21 Savage",
                    "spotifyUri": "spotify:artist:1URnnhqYAYcrqrcwql10ft"
                }
            ],
            "labels": [
                {
                    "name": "OVO / Republic Records"
                }
            ],
            "releaseDate": "2022-11-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 29,
            "previousRank": 26,
            "peakRank": 24,
            "appearancesOnChart": 15,
            "consecutiveAppearancesOnChart": 15,
            "rankingMetric": {
                "value": "17320705",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-01",
            "entryRank": 108,
            "entryDate": "2022-10-20"
        },
        "trackMetadata": {
            "trackName": "Mockingbird",
            "trackUri": "spotify:track:561jH07mF1jHuk7KlaeF0s",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02726d48d93d02e1271774f023",
            "artists": [
                {
                    "name": "Eminem",
                    "spotifyUri": "spotify:artist:7dGJo4pcD2V6oG8kP0tJRR"
                }
            ],
            "labels": [
                {
                    "name": "Aftermath"
                }
            ],
            "releaseDate": "2004-11-12"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 30,
            "previousRank": 34,
            "peakRank": 27,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "17295155",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 189,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "I Wanna Be Yours",
            "trackUri": "spotify:track:5XeFesFbtLpXzIVDNQP22n",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024ae1c4c5c45aabe565499163",
            "artists": [
                {
                    "name": "Arctic Monkeys",
                    "spotifyUri": "spotify:artist:7Ln80lUS6He07XvHI8qqHH"
                }
            ],
            "labels": [
                {
                    "name": "Domino Recording Co"
                }
            ],
            "releaseDate": "2013-09-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 31,
            "previousRank": 37,
            "peakRank": 8,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "16986344",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-11-24",
            "entryRank": 143,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Made You Look",
            "trackUri": "spotify:track:0QHEIqNKsMoOY5urbzN48u",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021a4f1ada93881da4ca8060ff",
            "artists": [
                {
                    "name": "Meghan Trainor",
                    "spotifyUri": "spotify:artist:6JL8zeS1NmiOftqZTRgdTz"
                }
            ],
            "labels": [
                {
                    "name": "Epic"
                }
            ],
            "releaseDate": "2022-10-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 32,
            "previousRank": 35,
            "peakRank": 32,
            "appearancesOnChart": 12,
            "consecutiveAppearancesOnChart": 12,
            "rankingMetric": {
                "value": "16637957",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 169,
            "entryDate": "2022-11-10"
        },
        "trackMetadata": {
            "trackName": "PUNTO G",
            "trackUri": "spotify:track:4WiQA1AGWHFvaxBU6bHghs",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ea0efa338b8bcef4431e30a1",
            "artists": [
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                }
            ],
            "labels": [
                {
                    "name": "Quevedo"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 33,
            "previousRank": 33,
            "peakRank": 11,
            "appearancesOnChart": 16,
            "consecutiveAppearancesOnChart": 16,
            "rankingMetric": {
                "value": "16381836",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2022-10-20",
            "entryRank": 86,
            "entryDate": "2022-10-13"
        },
        "trackMetadata": {
            "trackName": "Miss You",
            "trackUri": "spotify:track:73vIOb4Q7YN6HeJTbscRx5",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025b1bff1152ef6d402c9b75a8",
            "artists": [
                {
                    "name": "Oliver Tree",
                    "spotifyUri": "spotify:artist:6TLwD7HPWuiOzvXEa3oCNe"
                },
                {
                    "name": "Robin Schulz",
                    "spotifyUri": "spotify:artist:3t5xRXzsuZmMDkQzgOX35S"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2022-08-05"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 34,
            "previousRank": 31,
            "peakRank": 2,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "15570641",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-06-02",
            "entryRank": 3,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Me Porto Bonito",
            "trackUri": "spotify:track:6Sq7ltF9Qa7SNFBsV5Cogx",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                },
                {
                    "name": "Chencho Corleone",
                    "spotifyUri": "spotify:artist:37230BxxYs9ksS7OkZw3IU"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 35,
            "previousRank": 47,
            "peakRank": 16,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "15447041",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 186,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "SNAP",
            "trackUri": "spotify:track:76OGwb5RA9h4FxQPT33ekc",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021391b1fdb63da53e5b112224",
            "artists": [
                {
                    "name": "Rosa Linn",
                    "spotifyUri": "spotify:artist:46xBNx0j6cwY6sD9LgMTm1"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2022-03-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 36,
            "previousRank": 39,
            "peakRank": 17,
            "appearancesOnChart": 21,
            "consecutiveAppearancesOnChart": 21,
            "rankingMetric": {
                "value": "15338377",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 124,
            "entryDate": "2022-09-08"
        },
        "trackMetadata": {
            "trackName": "Romantic Homicide",
            "trackUri": "spotify:track:1xK59OXxi2TAAAbmZK0kBL",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bd1a52b3d5903ee01c216da0",
            "artists": [
                {
                    "name": "d4vd",
                    "spotifyUri": "spotify:artist:5y8tKLUfMvliMe8IKamR32"
                }
            ],
            "labels": [
                {
                    "name": "Darkroom/Interscope Records"
                }
            ],
            "releaseDate": "2022-07-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 37,
            "previousRank": 46,
            "peakRank": 10,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "15023544",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-12",
            "entryRank": 86,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "Until I Found You (with Em Beihold) - Em Beihold Version",
            "trackUri": "spotify:track:1Y3LN4zO1Edc2EluIoSPJN",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022bf0876d42b90a8852ad6244",
            "artists": [
                {
                    "name": "Stephen Sanchez",
                    "spotifyUri": "spotify:artist:5XKFrudbV4IiuE5WuTPRmT"
                },
                {
                    "name": "Em Beihold",
                    "spotifyUri": "spotify:artist:7o2ZQYM7nTsaVdkXY38UAA"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-04-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 38,
            "previousRank": 50,
            "peakRank": 26,
            "appearancesOnChart": 46,
            "consecutiveAppearancesOnChart": 46,
            "rankingMetric": {
                "value": "14981176",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 66,
            "entryDate": "2022-03-17"
        },
        "trackMetadata": {
            "trackName": "Bones",
            "trackUri": "spotify:track:54ipXppHLA8U4yqpOFTUhr",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
            "artists": [
                {
                    "name": "Imagine Dragons",
                    "spotifyUri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
                }
            ],
            "labels": [
                {
                    "name": "Kid Ina Korner / Interscope"
                }
            ],
            "releaseDate": "2022-07-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 39,
            "previousRank": 28,
            "peakRank": 25,
            "appearancesOnChart": 5,
            "consecutiveAppearancesOnChart": 5,
            "rankingMetric": {
                "value": "14838481",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-05",
            "entryRank": 27,
            "entryDate": "2022-12-29"
        },
        "trackMetadata": {
            "trackName": "Gato de Noche",
            "trackUri": "spotify:track:54ELExv56KCAB4UP9cOCzC",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ed132404686f567c8f793058",
            "artists": [
                {
                    "name": "Ñengo Flow",
                    "spotifyUri": "spotify:artist:12vb80Km0Ew53ABfJOepVz"
                },
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-12-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 40,
            "previousRank": 40,
            "peakRank": 6,
            "appearancesOnChart": 27,
            "consecutiveAppearancesOnChart": 27,
            "rankingMetric": {
                "value": "14822865",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2022-10-20",
            "entryRank": 94,
            "entryDate": "2022-07-28"
        },
        "trackMetadata": {
            "trackName": "Under The Influence",
            "trackUri": "spotify:track:5IgjP7X4th6nMNDh4akUHb",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029a494f7d8909a6cc4ceb74ac",
            "artists": [
                {
                    "name": "Chris Brown",
                    "spotifyUri": "spotify:artist:7bXgB6jMjp9ATFy66eO08Z"
                }
            ],
            "labels": [
                {
                    "name": "Chris Brown Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2019-10-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 41,
            "previousRank": 38,
            "peakRank": 4,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "14692380",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-11",
            "entryRank": 5,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Tití Me Preguntó",
            "trackUri": "spotify:track:1IHWl5LamUGEuP4ozKQSXZ",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 42,
            "previousRank": 49,
            "peakRank": 19,
            "appearancesOnChart": 126,
            "consecutiveAppearancesOnChart": 126,
            "rankingMetric": {
                "value": "14635602",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 198,
            "entryDate": "2020-09-03"
        },
        "trackMetadata": {
            "trackName": "Sweater Weather",
            "trackUri": "spotify:track:2QjOHCTQ1Jl3zawyYOpxh6",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028265a736a1eb838ad5a0b921",
            "artists": [
                {
                    "name": "The Neighbourhood",
                    "spotifyUri": "spotify:artist:77SW9BnxLY8rJ0RciFqkHh"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2013-04-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 43,
            "previousRank": 36,
            "peakRank": 36,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "14603034",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 79,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Que Vuelvas",
            "trackUri": "spotify:track:6Um358vY92UBv5DloTRX9L",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025c7336d25ca101fbb0855647",
            "artists": [
                {
                    "name": "Carin Leon",
                    "spotifyUri": "spotify:artist:66ihevNkSYNzRAl44dx6jJ"
                },
                {
                    "name": "Grupo Frontera",
                    "spotifyUri": "spotify:artist:6XkjpgcEsYab502Vr1bBeW"
                }
            ],
            "labels": [
                {
                    "name": "BorderKid Records/Sony Music Latin"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 44,
            "previousRank": 43,
            "peakRank": 31,
            "appearancesOnChart": 9,
            "consecutiveAppearancesOnChart": 9,
            "rankingMetric": {
                "value": "14467752",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-08",
            "entryRank": 179,
            "entryDate": "2022-12-01"
        },
        "trackMetadata": {
            "trackName": "Bloody Mary",
            "trackUri": "spotify:track:11BKm0j4eYoCPPpCONAVwA",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a47c0e156ea3cebe37fdcab8",
            "artists": [
                {
                    "name": "Lady Gaga",
                    "spotifyUri": "spotify:artist:1HY2Jd0NmPuamShAr6KMms"
                }
            ],
            "labels": [
                {
                    "name": "Interscope"
                }
            ],
            "releaseDate": "2011-01-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 45,
            "previousRank": 45,
            "peakRank": 10,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "14385698",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2022-08-11",
            "entryRank": 58,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "Bad Habit",
            "trackUri": "spotify:track:4k6Uh1HXdhtusDW5y8Gbvy",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0268968350c2550e36d96344ee",
            "artists": [
                {
                    "name": "Steve Lacy",
                    "spotifyUri": "spotify:artist:57vWImR43h4CaDao012Ofp"
                }
            ],
            "labels": [
                {
                    "name": "L-M Records/RCA Records"
                }
            ],
            "releaseDate": "2022-07-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 46,
            "previousRank": 53,
            "peakRank": 38,
            "appearancesOnChart": 23,
            "consecutiveAppearancesOnChart": 23,
            "rankingMetric": {
                "value": "14365674",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 168,
            "entryDate": "2022-08-25"
        },
        "trackMetadata": {
            "trackName": "Feliz Cumpleaños Ferxxo",
            "trackUri": "spotify:track:2CeKVsFFXG4QzA415QygGb",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0273456ed697350847810e52b3",
            "artists": [
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "UMLE - Latino"
                }
            ],
            "releaseDate": "2022-09-14"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 47,
            "previousRank": 64,
            "peakRank": 47,
            "appearancesOnChart": 3,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "14280025",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 117,
            "entryDate": "2023-01-12"
        },
        "trackMetadata": {
            "trackName": "AMG",
            "trackUri": "spotify:track:1lRtH4FszTrwwlK5gTSbXO",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fbf10e7799f39fbcd301e55a",
            "artists": [
                {
                    "name": "Natanael Cano",
                    "spotifyUri": "spotify:artist:0elWFr7TW8piilVRYJUe4P"
                },
                {
                    "name": "Peso Pluma",
                    "spotifyUri": "spotify:artist:12GqGscKJx3aE4t07u7eVZ"
                },
                {
                    "name": "Gabito Ballesteros",
                    "spotifyUri": "spotify:artist:6Sbl0NT50roqWvy746MfVf"
                }
            ],
            "labels": [
                {
                    "name": "WEA Latina"
                }
            ],
            "releaseDate": "2022-11-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 48,
            "previousRank": 29,
            "peakRank": 21,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "14189160",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-03",
            "entryRank": 23,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Monotonía",
            "trackUri": "spotify:track:6G12ZafqofSq7YtrMqUm76",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0227b5b57343431306a7f9daec",
            "artists": [
                {
                    "name": "Shakira",
                    "spotifyUri": "spotify:artist:0EmeFodog0BfCgMzAIvKQp"
                },
                {
                    "name": "Ozuna",
                    "spotifyUri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin"
                }
            ],
            "releaseDate": "2022-10-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 49,
            "previousRank": 52,
            "peakRank": 1,
            "appearancesOnChart": 121,
            "consecutiveAppearancesOnChart": 35,
            "rankingMetric": {
                "value": "14185922",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2016-12-29",
            "entryRank": 1,
            "entryDate": "2016-12-29"
        },
        "trackMetadata": {
            "trackName": "Starboy",
            "trackUri": "spotify:track:7MXVkk9YMctZqd1Srtv4MB",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024718e2b124f79258be7bc452",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                },
                {
                    "name": "Daft Punk",
                    "spotifyUri": "spotify:artist:4tZwfgrHOc3mvqYlEYSvVi"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2016-11-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 50,
            "previousRank": 42,
            "peakRank": 5,
            "appearancesOnChart": 26,
            "consecutiveAppearancesOnChart": 26,
            "rankingMetric": {
                "value": "14172195",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-18",
            "entryRank": 6,
            "entryDate": "2022-08-04"
        },
        "trackMetadata": {
            "trackName": "DESPECHÁ",
            "trackUri": "spotify:track:53tfEupEzQRtVFOeZvk7xq",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02efc0ef9dd996312ebaf0bf52",
            "artists": [
                {
                    "name": "ROSALÍA",
                    "spotifyUri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2022-09-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 51,
            "previousRank": 58,
            "peakRank": 51,
            "appearancesOnChart": 5,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "13908861",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 57,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Snooze",
            "trackUri": "spotify:track:4iZ4pt7kvcaH6Yo8UoZ4s2",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0270dbc9f47669d120ad874ec1",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 52,
            "previousRank": 56,
            "peakRank": 13,
            "appearancesOnChart": 23,
            "consecutiveAppearancesOnChart": 20,
            "rankingMetric": {
                "value": "13867083",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-13",
            "entryRank": 30,
            "entryDate": "2022-08-04"
        },
        "trackMetadata": {
            "trackName": "CUFF IT",
            "trackUri": "spotify:track:1xzi1Jcr7mEi9K2RfzLOqS",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020e58a0f8308c1ad403d105e7",
            "artists": [
                {
                    "name": "Beyoncé",
                    "spotifyUri": "spotify:artist:6vWDO969PvNqNYHIOW5v0m"
                }
            ],
            "labels": [
                {
                    "name": "Parkwood Entertainment/Columbia"
                }
            ],
            "releaseDate": "2022-07-29"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 53,
            "previousRank": 48,
            "peakRank": 48,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "13479257",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 171,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Leão",
            "trackUri": "spotify:track:2K9kZpwD2CzTa6iiSYYOoO",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02680345244dcab673f3a1389d",
            "artists": [
                {
                    "name": "Marília Mendonça",
                    "spotifyUri": "spotify:artist:1yR65psqiazQpeM79CcGh8"
                }
            ],
            "labels": [
                {
                    "name": "Som Livre"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 54,
            "previousRank": 57,
            "peakRank": 42,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "13293935",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-12",
            "entryRank": 79,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Just Wanna Rock",
            "trackUri": "spotify:track:4FyesJzVpA39hbYvcseO2d",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020e34fd68e8ff04e4515eb72a",
            "artists": [
                {
                    "name": "Lil Uzi Vert",
                    "spotifyUri": "spotify:artist:4O15NlyKLIASxsJ0PrXPfz"
                }
            ],
            "labels": [
                {
                    "name": "Generation Now/Atlantic"
                }
            ],
            "releaseDate": "2022-10-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 55,
            "previousRank": 51,
            "peakRank": 1,
            "appearancesOnChart": 109,
            "consecutiveAppearancesOnChart": 109,
            "rankingMetric": {
                "value": "13130632",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-01-27",
            "entryRank": 168,
            "entryDate": "2020-12-31"
        },
        "trackMetadata": {
            "trackName": "Heat Waves",
            "trackUri": "spotify:track:02MWAaffLxlfxAUY7c5dvx",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029e495fb707973f3390850eea",
            "artists": [
                {
                    "name": "Glass Animals",
                    "spotifyUri": "spotify:artist:4yvcSjfu4PC0CYQyLy4wSq"
                }
            ],
            "labels": [
                {
                    "name": "Polydor Records"
                }
            ],
            "releaseDate": "2020-08-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 56,
            "previousRank": 76,
            "peakRank": 56,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "13128915",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 128,
            "entryDate": "2022-11-17"
        },
        "trackMetadata": {
            "trackName": "10:35",
            "trackUri": "spotify:track:6BePGk3eCan4FqaW2X8Qy3",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02999565cd8bea3f8f0985bb31",
            "artists": [
                {
                    "name": "Tiësto",
                    "spotifyUri": "spotify:artist:2o5jDhtHVPhrJdv3cEQ99Z"
                },
                {
                    "name": "Tate McRae",
                    "spotifyUri": "spotify:artist:45dkTj5sMRSjrmBSBeiHym"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2022-11-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 57,
            "previousRank": 41,
            "peakRank": 12,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 7,
            "rankingMetric": {
                "value": "13000147",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-15",
            "entryRank": 12,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Nobody Gets Me",
            "trackUri": "spotify:track:5Y35SjAfXjjG0sFQ3KOxmm",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0270dbc9f47669d120ad874ec1",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 58,
            "previousRank": 62,
            "peakRank": 58,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "12851329",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 180,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Escapism. - Sped Up",
            "trackUri": "spotify:track:4rPJSqrov3zqGwXlemLBMw",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0257dd31ec4e9dbc7f4238f69a",
            "artists": [
                {
                    "name": "RAYE",
                    "spotifyUri": "spotify:artist:5KKpBU5eC2tJDzf0wmlRp2"
                },
                {
                    "name": "070 Shake",
                    "spotifyUri": "spotify:artist:12Zk1DFhCbHY6v3xep2ZjI"
                }
            ],
            "labels": [
                {
                    "name": "Human Re Sources"
                }
            ],
            "releaseDate": "2022-11-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 59,
            "previousRank": 63,
            "peakRank": 40,
            "appearancesOnChart": 10,
            "consecutiveAppearancesOnChart": 10,
            "rankingMetric": {
                "value": "12747422",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-12",
            "entryRank": 97,
            "entryDate": "2022-11-24"
        },
        "trackMetadata": {
            "trackName": "Maan Meri Jaan",
            "trackUri": "spotify:track:1418IuVKQPTYqt7QNJ9RXN",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0237f65266754703fd20d29854",
            "artists": [
                {
                    "name": "King",
                    "spotifyUri": "spotify:artist:5NHm4TU5Twz7owibYxJfFU"
                }
            ],
            "labels": [
                {
                    "name": "Warner Music India"
                }
            ],
            "releaseDate": "2022-10-12"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 60,
            "previousRank": 73,
            "peakRank": 60,
            "appearancesOnChart": 5,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "12550900",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 197,
            "entryDate": "2022-12-22"
        },
        "trackMetadata": {
            "trackName": "CHORRITO PA LAS ANIMAS",
            "trackUri": "spotify:track:0CYTGMBYkwUxrj1MWDLrC5",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e027cc7b0d6a82846cd8b158f99",
            "artists": [
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "UMLE - Latino"
                }
            ],
            "releaseDate": "2022-12-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 61,
            "previousRank": 60,
            "peakRank": 1,
            "appearancesOnChart": 165,
            "consecutiveAppearancesOnChart": 165,
            "rankingMetric": {
                "value": "12545668",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2020-02-27",
            "entryRank": 7,
            "entryDate": "2019-12-05"
        },
        "trackMetadata": {
            "trackName": "Blinding Lights",
            "trackUri": "spotify:track:0VjIjW4GlUZAMYd2vXMi3b",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028863bc11d2aa12b54f5aeb36",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2020-03-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 62,
            "previousRank": 55,
            "peakRank": 6,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "12453263",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-18",
            "entryRank": 18,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Efecto",
            "trackUri": "spotify:track:5Eax0qFko2dh7Rl2lYs3bx",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 63,
            "previousRank": 59,
            "peakRank": 3,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "12328145",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-05-26",
            "entryRank": 4,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Ojitos Lindos",
            "trackUri": "spotify:track:3k3NWokhRRkEPhCzPmV8TW",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                },
                {
                    "name": "Bomba Estéreo",
                    "spotifyUri": "spotify:artist:5n9bMYfz9qss2VOW89EVs2"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 64,
            "previousRank": 54,
            "peakRank": 1,
            "appearancesOnChart": 81,
            "consecutiveAppearancesOnChart": 81,
            "rankingMetric": {
                "value": "12327712",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2021-08-05",
            "entryRank": 3,
            "entryDate": "2021-07-15"
        },
        "trackMetadata": {
            "trackName": "STAY (with Justin Bieber)",
            "trackUri": "spotify:track:567e29TDzLwZwfDuEpGTwo",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b4d59e6fa7e5e7cbc57ac33a",
            "artists": [
                {
                    "name": "The Kid LAROI",
                    "spotifyUri": "spotify:artist:2tIP7SsRs7vjIcLrU85W8J"
                },
                {
                    "name": "Justin Bieber",
                    "spotifyUri": "spotify:artist:1uNFoZAHBGtllmzznpCI3s"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2021-07-27"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 65,
            "previousRank": 65,
            "peakRank": 29,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 7,
            "rankingMetric": {
                "value": "12308053",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2022-12-15",
            "entryRank": 29,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Low",
            "trackUri": "spotify:track:2GAhgAjOhEmItWLfgisyOn",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0270dbc9f47669d120ad874ec1",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 66,
            "previousRank": 61,
            "peakRank": 1,
            "appearancesOnChart": 33,
            "consecutiveAppearancesOnChart": 33,
            "rankingMetric": {
                "value": "11749086",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-06-23",
            "entryRank": 4,
            "entryDate": "2022-06-16"
        },
        "trackMetadata": {
            "trackName": "Glimpse of Us",
            "trackUri": "spotify:track:4ewazQLXFTDC8XvCbhvtXs",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02eaac2a7955f5b8967991cacb",
            "artists": [
                {
                    "name": "Joji",
                    "spotifyUri": "spotify:artist:3MZsBdqDrRTJihTHQrO6Dq"
                }
            ],
            "labels": [
                {
                    "name": "88rising Music/Warner Records"
                }
            ],
            "releaseDate": "2022-11-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 67,
            "previousRank": 68,
            "peakRank": 67,
            "appearancesOnChart": 11,
            "consecutiveAppearancesOnChart": 11,
            "rankingMetric": {
                "value": "11730038",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 174,
            "entryDate": "2022-11-17"
        },
        "trackMetadata": {
            "trackName": "SPIT IN MY FACE!",
            "trackUri": "spotify:track:1N8TTK1Uoy7UvQNUazfUt5",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0260ddc59c8d590a37cf2348f3",
            "artists": [
                {
                    "name": "ThxSoMch",
                    "spotifyUri": "spotify:artist:4MvZhE1iuzttcoyepkpfdF"
                }
            ],
            "labels": [
                {
                    "name": "Elektra (NEK)"
                }
            ],
            "releaseDate": "2022-12-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 68,
            "previousRank": 78,
            "peakRank": 68,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "11502195",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 78,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "People",
            "trackUri": "spotify:track:26b3oVLrRUaaybJulow9kz",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fc342f95f117d48dbdde9735",
            "artists": [
                {
                    "name": "Libianca",
                    "spotifyUri": "spotify:artist:7kjSuFGKhLm8b5qXoMhRkJ"
                }
            ],
            "labels": [
                {
                    "name": "5K Records Limited"
                }
            ],
            "releaseDate": "2022-12-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 69,
            "previousRank": 67,
            "peakRank": 67,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "11281596",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 67,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Fin de Semana",
            "trackUri": "spotify:track:6TBzRwnX2oYd8aOrOuyK1p",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029b7e1ea3815a172019bc5e56",
            "artists": [
                {
                    "name": "Oscar Maydon",
                    "spotifyUri": "spotify:artist:3l9G1G9MxH6DaRhwLklaf5"
                },
                {
                    "name": "Junior H",
                    "spotifyUri": "spotify:artist:7Gi6gjaWy3DxyilpF1a8Is"
                }
            ],
            "labels": [
                {
                    "name": "Rancho Humilde"
                }
            ],
            "releaseDate": "2023-01-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 70,
            "previousRank": -1,
            "peakRank": 70,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "11010860",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 70,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "MOONLIGHT SUNRISE",
            "trackUri": "spotify:track:38DlSDrx9tgc5Gfq6y3aBa",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e026887b017d077dfc5787a3e23",
            "artists": [
                {
                    "name": "TWICE",
                    "spotifyUri": "spotify:artist:7n2Ycct7Beij7Dj7meI4X0"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records - TWICE"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 71,
            "previousRank": 96,
            "peakRank": 71,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 6,
            "rankingMetric": {
                "value": "10972453",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 145,
            "entryDate": "2022-12-22"
        },
        "trackMetadata": {
            "trackName": "PLAYA DEL INGLÉS",
            "trackUri": "spotify:track:0Sfn2TYbpQtCGMBf6C0Y6T",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ea0efa338b8bcef4431e30a1",
            "artists": [
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                },
                {
                    "name": "Myke Towers",
                    "spotifyUri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
                }
            ],
            "labels": [
                {
                    "name": "Quevedo"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 72,
            "previousRank": 75,
            "peakRank": 17,
            "appearancesOnChart": 34,
            "consecutiveAppearancesOnChart": 31,
            "rankingMetric": {
                "value": "10931244",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2018-04-05",
            "entryRank": 17,
            "entryDate": "2018-04-05"
        },
        "trackMetadata": {
            "trackName": "I Was Never There",
            "trackUri": "spotify:track:1cKHdTo9u0ZymJdPGSh6nq",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021f6a2a40bb692936879db730",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                },
                {
                    "name": "Gesaffelstein",
                    "spotifyUri": "spotify:artist:3hteYQFiMFbJY7wS0xDymP"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2018-03-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 73,
            "previousRank": 70,
            "peakRank": 70,
            "appearancesOnChart": 10,
            "consecutiveAppearancesOnChart": 10,
            "rankingMetric": {
                "value": "10909932",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 79,
            "entryDate": "2022-11-24"
        },
        "trackMetadata": {
            "trackName": "CAIRO",
            "trackUri": "spotify:track:6WbAhuwE6fCOriBu5786X1",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021068a681551526e045f4dc0d",
            "artists": [
                {
                    "name": "KAROL G",
                    "spotifyUri": "spotify:artist:790FomKkXshlbRYZFtlgla"
                },
                {
                    "name": "Ovy On The Drums",
                    "spotifyUri": "spotify:artist:3m5qlPf2OkihLz3dRYnkPA"
                }
            ],
            "labels": [
                {
                    "name": "UMLE - Latino"
                }
            ],
            "releaseDate": "2022-11-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 74,
            "previousRank": 97,
            "peakRank": 45,
            "appearancesOnChart": 20,
            "consecutiveAppearancesOnChart": 20,
            "rankingMetric": {
                "value": "10811092",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-13",
            "entryRank": 110,
            "entryDate": "2022-09-15"
        },
        "trackMetadata": {
            "trackName": "VISTA AL MAR",
            "trackUri": "spotify:track:5q86iSKkBtOoNkdgEDY5WV",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ea0efa338b8bcef4431e30a1",
            "artists": [
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                }
            ],
            "labels": [
                {
                    "name": "Quevedo"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 75,
            "previousRank": 77,
            "peakRank": 4,
            "appearancesOnChart": 76,
            "consecutiveAppearancesOnChart": 76,
            "rankingMetric": {
                "value": "10786655",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-01-06",
            "entryRank": 76,
            "entryDate": "2021-08-19"
        },
        "trackMetadata": {
            "trackName": "Cold Heart - PNAU Remix",
            "trackUri": "spotify:track:6JIC3hbC28JZKZ8AlAqX8h",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02523458c391fe8180a19a1069",
            "artists": [
                {
                    "name": "Elton John",
                    "spotifyUri": "spotify:artist:3PhoLpVuITZKcymswpck5b"
                },
                {
                    "name": "Dua Lipa",
                    "spotifyUri": "spotify:artist:6M2wZ9GZgrQXHCFfjv46we"
                },
                {
                    "name": "PNAU",
                    "spotifyUri": "spotify:artist:6n28c9qs9hNGriNa72b26u"
                }
            ],
            "labels": [
                {
                    "name": "EMI"
                }
            ],
            "releaseDate": "2021-10-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 76,
            "previousRank": 91,
            "peakRank": 76,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 17,
            "rankingMetric": {
                "value": "10781189",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 197,
            "entryDate": "2021-04-29"
        },
        "trackMetadata": {
            "trackName": "When I Was Your Man",
            "trackUri": "spotify:track:0B7wvvmu9EISAwZnOpjhNI",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02926f43e7cce571e62720fd46",
            "artists": [
                {
                    "name": "Bruno Mars",
                    "spotifyUri": "spotify:artist:0du5cEVh5yTK9QJze8zA0C"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2012-12-07"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 77,
            "previousRank": 82,
            "peakRank": 34,
            "appearancesOnChart": 76,
            "consecutiveAppearancesOnChart": 72,
            "rankingMetric": {
                "value": "10667617",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-03-31",
            "entryRank": 190,
            "entryDate": "2021-08-12"
        },
        "trackMetadata": {
            "trackName": "Dandelions",
            "trackUri": "spotify:track:2eAvDnpXP5W0cVtiI0PUxV",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0297e971f3e53475091dc8d707",
            "artists": [
                {
                    "name": "Ruth B.",
                    "spotifyUri": "spotify:artist:2WzaAvm2bBCf4pEhyuDgCY"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2017-05-05"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 78,
            "previousRank": 69,
            "peakRank": 36,
            "appearancesOnChart": 18,
            "consecutiveAppearancesOnChart": 18,
            "rankingMetric": {
                "value": "10659989",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-20",
            "entryRank": 138,
            "entryDate": "2022-09-29"
        },
        "trackMetadata": {
            "trackName": "No Se Va - En Vivo",
            "trackUri": "spotify:track:23Lyy7ZXRvzfgH4JtDkKrX",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02042b5cc9a1a0a97cfc005ee8",
            "artists": [
                {
                    "name": "Grupo Frontera",
                    "spotifyUri": "spotify:artist:6XkjpgcEsYab502Vr1bBeW"
                }
            ],
            "labels": [
                {
                    "name": "Grupo Frontera"
                }
            ],
            "releaseDate": "2022-04-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 79,
            "previousRank": 74,
            "peakRank": 20,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "10608747",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-20",
            "entryRank": 181,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Until I Found You",
            "trackUri": "spotify:track:6VhuP99TE6gYNQRJIlAWFD",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029522042f86d0bb0d4e9e3783",
            "artists": [
                {
                    "name": "Stephen Sanchez",
                    "spotifyUri": "spotify:artist:5XKFrudbV4IiuE5WuTPRmT"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-08-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 80,
            "previousRank": 72,
            "peakRank": 72,
            "appearancesOnChart": 5,
            "consecutiveAppearancesOnChart": 5,
            "rankingMetric": {
                "value": "10598916",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 180,
            "entryDate": "2022-12-29"
        },
        "trackMetadata": {
            "trackName": "Marisola - Remix",
            "trackUri": "spotify:track:0NO2zL0kw8sGGnaMvHKAZF",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0284abc8c6cf1e122113f7ab8b",
            "artists": [
                {
                    "name": "Cris Mj",
                    "spotifyUri": "spotify:artist:1Yj5Xey7kTwvZla8sqdsdE"
                },
                {
                    "name": "Duki",
                    "spotifyUri": "spotify:artist:1bAftSH8umNcGZ0uyV7LMg"
                },
                {
                    "name": "Nicki Nicole",
                    "spotifyUri": "spotify:artist:2UZIAOlrnyZmyzt1nuXr9y"
                },
                {
                    "name": "Standly",
                    "spotifyUri": "spotify:artist:0rjms710nwQTdrQheXHJfz"
                },
                {
                    "name": "Stars Music Chile",
                    "spotifyUri": "spotify:artist:2NZD6Gqfk60GEcAAnJKVsR"
                }
            ],
            "labels": [
                {
                    "name": "Virgin Music Chile"
                }
            ],
            "releaseDate": "2022-12-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 81,
            "previousRank": 81,
            "peakRank": 70,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "10433933",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2023-01-12",
            "entryRank": 106,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "The Color Violet",
            "trackUri": "spotify:track:3azJifCSqg9fRij2yKIbWz",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020c5f23cbf0b1ab7e37d0dc67",
            "artists": [
                {
                    "name": "Tory Lanez",
                    "spotifyUri": "spotify:artist:2jku7tDXc6XoB6MO2hFuqg"
                }
            ],
            "labels": [
                {
                    "name": "One Umbrella Records"
                }
            ],
            "releaseDate": "2021-12-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 82,
            "previousRank": 71,
            "peakRank": 21,
            "appearancesOnChart": 13,
            "consecutiveAppearancesOnChart": 13,
            "rankingMetric": {
                "value": "10429481",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-15",
            "entryRank": 25,
            "entryDate": "2022-11-03"
        },
        "trackMetadata": {
            "trackName": "Shirt",
            "trackUri": "spotify:track:2wSTnntOPRi7aQneobFtU4",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0270dbc9f47669d120ad874ec1",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 83,
            "previousRank": 87,
            "peakRank": 83,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "10390830",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 142,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Apna Bana Le (From \"Bhediya\")",
            "trackUri": "spotify:track:7Els4IIFYa4P4RxBkZkxdd",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0282a60b8f529feb30dfc00543",
            "artists": [
                {
                    "name": "Arijit Singh",
                    "spotifyUri": "spotify:artist:4YRxDV8wJFPHPTeXepOstw"
                },
                {
                    "name": "Sachin-Jigar",
                    "spotifyUri": "spotify:artist:1mBydYMVBECdDmMfE2sEUO"
                }
            ],
            "labels": [
                {
                    "name": "Zee Music Company"
                }
            ],
            "releaseDate": "2022-11-05"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 84,
            "previousRank": 32,
            "peakRank": 32,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "10212237",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 32,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "VIBE (feat. Jimin of BTS)",
            "trackUri": "spotify:track:61AZsmFB3VoJdmraMk5ZSn",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02f7994d33de90ec347aa477c3",
            "artists": [
                {
                    "name": "TAEYANG",
                    "spotifyUri": "spotify:artist:6udveWUgX4vu75FF0DTrXV"
                },
                {
                    "name": "Jimin",
                    "spotifyUri": "spotify:artist:1oSPZhvZMIrWW5I41kPkkY"
                }
            ],
            "labels": [
                {
                    "name": "THEBLACKLABEL/Interscope Records"
                }
            ],
            "releaseDate": "2023-01-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 85,
            "previousRank": 84,
            "peakRank": 43,
            "appearancesOnChart": 56,
            "consecutiveAppearancesOnChart": 56,
            "rankingMetric": {
                "value": "10112928",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-13",
            "entryRank": 178,
            "entryDate": "2022-01-06"
        },
        "trackMetadata": {
            "trackName": "505",
            "trackUri": "spotify:track:58ge6dfP91o9oXMzq3XkIS",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020c8ac83035e9588e8ad34b90",
            "artists": [
                {
                    "name": "Arctic Monkeys",
                    "spotifyUri": "spotify:artist:7Ln80lUS6He07XvHI8qqHH"
                }
            ],
            "labels": [
                {
                    "name": "Domino/Warner Records"
                }
            ],
            "releaseDate": "2007-04-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 86,
            "previousRank": -1,
            "peakRank": 86,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "10060027",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 86,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "AHORA QUÉ",
            "trackUri": "spotify:track:5qP24CrDI0rmY5zwRvUfzU",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ea0efa338b8bcef4431e30a1",
            "artists": [
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                }
            ],
            "labels": [
                {
                    "name": "Quevedo"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 87,
            "previousRank": 86,
            "peakRank": 38,
            "appearancesOnChart": 24,
            "consecutiveAppearancesOnChart": 24,
            "rankingMetric": {
                "value": "10031381",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-13",
            "entryRank": 95,
            "entryDate": "2022-08-18"
        },
        "trackMetadata": {
            "trackName": "LOKERA",
            "trackUri": "spotify:track:33cF8aTmGJ6TsEf23uqGIN",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029f971e4c38e5dedcb242b3ae",
            "artists": [
                {
                    "name": "Rauw Alejandro",
                    "spotifyUri": "spotify:artist:1mcTU81TzQhprhouKaTkpq"
                },
                {
                    "name": "Lyanno",
                    "spotifyUri": "spotify:artist:1Ts9of7VPZElwPQnqnDSfW"
                },
                {
                    "name": "Brray",
                    "spotifyUri": "spotify:artist:1GKIlPFdcewHtpDVCQ8zmJ"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin/Duars Entertainment"
                }
            ],
            "releaseDate": "2022-11-11"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 88,
            "previousRank": 80,
            "peakRank": 15,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "9952280",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-05-12",
            "entryRank": 15,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Neverita",
            "trackUri": "spotify:track:31i56LZnwE6uSu3exoHjtB",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 89,
            "previousRank": 88,
            "peakRank": 66,
            "appearancesOnChart": 21,
            "consecutiveAppearancesOnChart": 21,
            "rankingMetric": {
                "value": "9902445",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-17",
            "entryRank": 176,
            "entryDate": "2022-09-08"
        },
        "trackMetadata": {
            "trackName": "Shinunoga E-Wa",
            "trackUri": "spotify:track:0o9zmvc5f3EFApU52PPIyW",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0222805a1b17e41ae357bd98bc",
            "artists": [
                {
                    "name": "Fujii Kaze",
                    "spotifyUri": "spotify:artist:6bDWAcdtVR3WHz2xtiIPUi"
                }
            ],
            "labels": [
                {
                    "name": "Universal Music LLC"
                }
            ],
            "releaseDate": "2020-05-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 90,
            "previousRank": 93,
            "peakRank": 2,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "9850595",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-27",
            "entryRank": 2,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Lavender Haze",
            "trackUri": "spotify:track:5jQI2r1RdgtuT8S3iG8zFC",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bb54dde68cd23e2a268ae0f5",
            "artists": [
                {
                    "name": "Taylor Swift",
                    "spotifyUri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
                }
            ],
            "labels": [
                {
                    "name": "Taylor Swift"
                }
            ],
            "releaseDate": "2022-10-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 91,
            "previousRank": 101,
            "peakRank": 78,
            "appearancesOnChart": 17,
            "consecutiveAppearancesOnChart": 5,
            "rankingMetric": {
                "value": "9717926",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-12",
            "entryRank": 171,
            "entryDate": "2022-08-18"
        },
        "trackMetadata": {
            "trackName": "Hype Boy",
            "trackUri": "spotify:track:0a4MMyCrzT0En247IhqZbD",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029d28fd01859073a3ae6ea209",
            "artists": [
                {
                    "name": "NewJeans",
                    "spotifyUri": "spotify:artist:6HvZYsbFfjnjFrWF950C9d"
                }
            ],
            "labels": [
                {
                    "name": "ADOR"
                }
            ],
            "releaseDate": "2022-08-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 92,
            "previousRank": 66,
            "peakRank": 24,
            "appearancesOnChart": 249,
            "consecutiveAppearancesOnChart": 249,
            "rankingMetric": {
                "value": "9711356",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2018-06-14",
            "entryRank": 138,
            "entryDate": "2018-04-26"
        },
        "trackMetadata": {
            "trackName": "lovely (with Khalid)",
            "trackUri": "spotify:track:0u2P5u6lvoDfwTYjAADbn4",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028a3f0a3ca7929dea23cd274c",
            "artists": [
                {
                    "name": "Billie Eilish",
                    "spotifyUri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
                },
                {
                    "name": "Khalid",
                    "spotifyUri": "spotify:artist:6LuN9FCkKOj5PcnpouEgny"
                }
            ],
            "labels": [
                {
                    "name": "Darkroom"
                }
            ],
            "releaseDate": "2018-04-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 93,
            "previousRank": 107,
            "peakRank": 2,
            "appearancesOnChart": 36,
            "consecutiveAppearancesOnChart": 36,
            "rankingMetric": {
                "value": "9527584",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-05-26",
            "entryRank": 2,
            "entryDate": "2022-05-26"
        },
        "trackMetadata": {
            "trackName": "Late Night Talking",
            "trackUri": "spotify:track:1qEmFfgcLObUfQm0j1W2CK",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022e8ed79e177ff6011076f5f0",
            "artists": [
                {
                    "name": "Harry Styles",
                    "spotifyUri": "spotify:artist:6KImCVD70vtIoJWnq6nGn3"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2022-05-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 94,
            "previousRank": 83,
            "peakRank": 4,
            "appearancesOnChart": 211,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "9482163",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2019-10-03",
            "entryRank": 194,
            "entryDate": "2019-01-10"
        },
        "trackMetadata": {
            "trackName": "Someone You Loved",
            "trackUri": "spotify:track:7qEHsqek33rTcFNT9PFqLf",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fc2101e6889d6ce9025f85f2",
            "artists": [
                {
                    "name": "Lewis Capaldi",
                    "spotifyUri": "spotify:artist:4GNC7GD6oZMSxPGyXy4MNB"
                }
            ],
            "labels": [
                {
                    "name": "Vertigo Berlin"
                }
            ],
            "releaseDate": "2019-05-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 95,
            "previousRank": 98,
            "peakRank": 31,
            "appearancesOnChart": 70,
            "consecutiveAppearancesOnChart": 70,
            "rankingMetric": {
                "value": "9422894",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-02-24",
            "entryRank": 195,
            "entryDate": "2021-09-30"
        },
        "trackMetadata": {
            "trackName": "Without Me",
            "trackUri": "spotify:track:7lQ8MOhq6IN2w8EYcFNSUk",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e026ca5c90113b30c3c43ffb8f4",
            "artists": [
                {
                    "name": "Eminem",
                    "spotifyUri": "spotify:artist:7dGJo4pcD2V6oG8kP0tJRR"
                }
            ],
            "labels": [
                {
                    "name": "Aftermath"
                }
            ],
            "releaseDate": "2002-05-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 96,
            "previousRank": 113,
            "peakRank": 96,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 6,
            "rankingMetric": {
                "value": "9407579",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 184,
            "entryDate": "2022-12-22"
        },
        "trackMetadata": {
            "trackName": "METAMORPHOSIS",
            "trackUri": "spotify:track:2ksyzVfU0WJoBpu8otr4pz",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b852a616ae3a49a1f6b0f16e",
            "artists": [
                {
                    "name": "INTERWORLD",
                    "spotifyUri": "spotify:artist:5hKGLu4Ik88FzWcTPhWNTN"
                }
            ],
            "labels": [
                {
                    "name": "INTERWORLD"
                }
            ],
            "releaseDate": "2021-11-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 97,
            "previousRank": 100,
            "peakRank": 1,
            "appearancesOnChart": 66,
            "consecutiveAppearancesOnChart": 31,
            "rankingMetric": {
                "value": "9360737",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2018-04-05",
            "entryRank": 1,
            "entryDate": "2018-04-05"
        },
        "trackMetadata": {
            "trackName": "Call Out My Name",
            "trackUri": "spotify:track:09mEdoA6zrmBPgTEN5qXmN",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021f6a2a40bb692936879db730",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2018-03-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 98,
            "previousRank": 105,
            "peakRank": 57,
            "appearancesOnChart": 20,
            "consecutiveAppearancesOnChart": 20,
            "rankingMetric": {
                "value": "9255689",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 142,
            "entryDate": "2022-09-15"
        },
        "trackMetadata": {
            "trackName": "Something in the Orange",
            "trackUri": "spotify:track:3WMj8moIAXJhHsyLaqIIHI",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b2b6670e3aca9bcd55fbabbb",
            "artists": [
                {
                    "name": "Zach Bryan",
                    "spotifyUri": "spotify:artist:40ZNYROS4zLfyyBSs2PGe2"
                }
            ],
            "labels": [
                {
                    "name": "Warner Records"
                }
            ],
            "releaseDate": "2022-04-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 99,
            "previousRank": 104,
            "peakRank": 63,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "9254001",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-05",
            "entryRank": 96,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "ANTIFRAGILE",
            "trackUri": "spotify:track:4fsQ0K37TOXa3hEQfjEic1",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a991995542d50a691b9ae5be",
            "artists": [
                {
                    "name": "LE SSERAFIM",
                    "spotifyUri": "spotify:artist:4SpbR6yFEvexJuaBpgAU5p"
                }
            ],
            "labels": [
                {
                    "name": "SOURCE MUSIC"
                }
            ],
            "releaseDate": "2022-10-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 100,
            "previousRank": 110,
            "peakRank": 2,
            "appearancesOnChart": 112,
            "consecutiveAppearancesOnChart": 107,
            "rankingMetric": {
                "value": "9215267",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2021-02-11",
            "entryRank": 29,
            "entryDate": "2020-03-26"
        },
        "trackMetadata": {
            "trackName": "Save Your Tears",
            "trackUri": "spotify:track:5QO79kh1waicV47BqGRL3g",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028863bc11d2aa12b54f5aeb36",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2020-03-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 101,
            "previousRank": 124,
            "peakRank": 98,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 22,
            "rankingMetric": {
                "value": "9198997",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-05",
            "entryRank": 177,
            "entryDate": "2022-09-01"
        },
        "trackMetadata": {
            "trackName": "Viva La Vida",
            "trackUri": "spotify:track:1mea3bSkSGXuIRvnydlB5b",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02e21cc1db05580b6f2d2a3b6e",
            "artists": [
                {
                    "name": "Coldplay",
                    "spotifyUri": "spotify:artist:4gzpq5DPGxSnKTe4SA8HAU"
                }
            ],
            "labels": [
                {
                    "name": "Parlophone UK"
                }
            ],
            "releaseDate": "2008-05-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 102,
            "previousRank": 114,
            "peakRank": 1,
            "appearancesOnChart": 67,
            "consecutiveAppearancesOnChart": 67,
            "rankingMetric": {
                "value": "9198140",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2021-10-21",
            "entryRank": 1,
            "entryDate": "2021-10-21"
        },
        "trackMetadata": {
            "trackName": "Easy On Me",
            "trackUri": "spotify:track:46IZ0fSY2mpAiktS3KOqds",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c6b577e4c4a6d326354a89f7",
            "artists": [
                {
                    "name": "Adele",
                    "spotifyUri": "spotify:artist:4dpARuHxo51G3z768sgnrY"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2021-11-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 103,
            "previousRank": 115,
            "peakRank": 103,
            "appearancesOnChart": 50,
            "consecutiveAppearancesOnChart": 50,
            "rankingMetric": {
                "value": "9184726",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 199,
            "entryDate": "2022-02-17"
        },
        "trackMetadata": {
            "trackName": "Unstoppable",
            "trackUri": "spotify:track:2J2Z1SkXYghSajLibnQHOa",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02754b2fddebe7039fdb912837",
            "artists": [
                {
                    "name": "Sia",
                    "spotifyUri": "spotify:artist:5WUlDfRSoLAfcVSX1WnrxN"
                }
            ],
            "labels": [
                {
                    "name": "Monkey Puzzle Records/RCA Records"
                }
            ],
            "releaseDate": "2016-10-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 104,
            "previousRank": 109,
            "peakRank": 22,
            "appearancesOnChart": 18,
            "consecutiveAppearancesOnChart": 18,
            "rankingMetric": {
                "value": "9080938",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-09-29",
            "entryRank": 22,
            "entryDate": "2022-09-29"
        },
        "trackMetadata": {
            "trackName": "STAR WALKIN' (League of Legends Worlds Anthem)",
            "trackUri": "spotify:track:38T0tPVZHcPZyhtOcCP7pF",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0204cd9a1664fb4539a55643fe",
            "artists": [
                {
                    "name": "Lil Nas X",
                    "spotifyUri": "spotify:artist:7jVv8c5Fj3E9VhNjxT4snq"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2022-09-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 105,
            "previousRank": 106,
            "peakRank": 11,
            "appearancesOnChart": 13,
            "consecutiveAppearancesOnChart": 13,
            "rankingMetric": {
                "value": "9076355",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-11-03",
            "entryRank": 11,
            "entryDate": "2022-11-03"
        },
        "trackMetadata": {
            "trackName": "Lift Me Up - From Black Panther: Wakanda Forever - Music From and Inspired By",
            "trackUri": "spotify:track:6sCvvleqKbeyOkQDieBYgp",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02992a1f56ac5382848277cff2",
            "artists": [
                {
                    "name": "Rihanna",
                    "spotifyUri": "spotify:artist:5pKCCKE2ajJHZ9KAiaK11H"
                }
            ],
            "labels": [
                {
                    "name": "Roc Nation/Def Jam/Hollywood"
                }
            ],
            "releaseDate": "2022-11-11"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 106,
            "previousRank": 95,
            "peakRank": 80,
            "appearancesOnChart": 11,
            "consecutiveAppearancesOnChart": 11,
            "rankingMetric": {
                "value": "9073282",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-05",
            "entryRank": 131,
            "entryDate": "2022-11-17"
        },
        "trackMetadata": {
            "trackName": "Bombonzinho - Ao Vivo",
            "trackUri": "spotify:track:4o6v3Oooyt7HF20idztRD4",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bfd0c5fc77ce47d1623fcfd7",
            "artists": [
                {
                    "name": "Israel & Rodolffo",
                    "spotifyUri": "spotify:artist:41QLxRXlc2NwfJZkHGHKid"
                },
                {
                    "name": "Ana Castela",
                    "spotifyUri": "spotify:artist:2CKOmarVWvWqkNWUatHCex"
                }
            ],
            "labels": [
                {
                    "name": "Som Livre"
                }
            ],
            "releaseDate": "2022-11-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 107,
            "previousRank": 108,
            "peakRank": 82,
            "appearancesOnChart": 24,
            "consecutiveAppearancesOnChart": 24,
            "rankingMetric": {
                "value": "9062513",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-05",
            "entryRank": 163,
            "entryDate": "2022-08-18"
        },
        "trackMetadata": {
            "trackName": "Murder In My Mind",
            "trackUri": "spotify:track:6qyS9qBy0mEk3qYaH8mPss",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021440ffaa43c53d65719e0150",
            "artists": [
                {
                    "name": "Kordhell",
                    "spotifyUri": "spotify:artist:2W6WP4pHQTFlbr2z9S4n54"
                }
            ],
            "labels": [
                {
                    "name": "Kordhell"
                }
            ],
            "releaseDate": "2022-01-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 108,
            "previousRank": 79,
            "peakRank": 13,
            "appearancesOnChart": 37,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "9061979",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-06-23",
            "entryRank": 141,
            "entryDate": "2022-04-28"
        },
        "trackMetadata": {
            "trackName": "Te Felicito",
            "trackUri": "spotify:track:2rurDawMfoKP4uHyb2kJBt",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029a9716c90ceeb1890921e44f",
            "artists": [
                {
                    "name": "Shakira",
                    "spotifyUri": "spotify:artist:0EmeFodog0BfCgMzAIvKQp"
                },
                {
                    "name": "Rauw Alejandro",
                    "spotifyUri": "spotify:artist:1mcTU81TzQhprhouKaTkpq"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin"
                }
            ],
            "releaseDate": "2022-04-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 109,
            "previousRank": 92,
            "peakRank": 2,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "8984760",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-05-12",
            "entryRank": 2,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Moscow Mule",
            "trackUri": "spotify:track:6Xom58OOXk2SoU711L2IXO",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0249d694203245f241a1bcaa72",
            "artists": [
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-05-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 110,
            "previousRank": 130,
            "peakRank": 56,
            "appearancesOnChart": 110,
            "consecutiveAppearancesOnChart": 108,
            "rankingMetric": {
                "value": "8942050",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-09-15",
            "entryRank": 183,
            "entryDate": "2020-11-19"
        },
        "trackMetadata": {
            "trackName": "Yellow",
            "trackUri": "spotify:track:3AJwUDP919kvQ9QcozQPxg",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e023d92b2ad5af9fbc8637425f0",
            "artists": [
                {
                    "name": "Coldplay",
                    "spotifyUri": "spotify:artist:4gzpq5DPGxSnKTe4SA8HAU"
                }
            ],
            "labels": [
                {
                    "name": "Parlophone UK"
                }
            ],
            "releaseDate": "2000-07-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 111,
            "previousRank": 122,
            "peakRank": 76,
            "appearancesOnChart": 79,
            "consecutiveAppearancesOnChart": 54,
            "rankingMetric": {
                "value": "8933601",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-28",
            "entryRank": 196,
            "entryDate": "2016-12-29"
        },
        "trackMetadata": {
            "trackName": "No Role Modelz",
            "trackUri": "spotify:track:68Dni7IE4VyPkTOH9mRWHr",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c6e0948bbb0681ff29cdbae8",
            "artists": [
                {
                    "name": "J. Cole",
                    "spotifyUri": "spotify:artist:6l3HvQ5sa6mXTsMTB19rO5"
                }
            ],
            "labels": [
                {
                    "name": "Roc Nation Records LLC"
                }
            ],
            "releaseDate": "2014-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 112,
            "previousRank": 151,
            "peakRank": 112,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "8933218",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 151,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Heart To Heart",
            "trackUri": "spotify:track:7EAMXbLcL0qXmciM5SwMh2",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fa1323bb50728c7489980672",
            "artists": [
                {
                    "name": "Mac DeMarco",
                    "spotifyUri": "spotify:artist:3Sz7ZnJQBIHsXLUSo0OQtM"
                }
            ],
            "labels": [
                {
                    "name": "Mac’s Record Label"
                }
            ],
            "releaseDate": "2019-05-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 113,
            "previousRank": 121,
            "peakRank": 7,
            "appearancesOnChart": 32,
            "consecutiveAppearancesOnChart": 32,
            "rankingMetric": {
                "value": "8914599",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-06-23",
            "entryRank": 7,
            "entryDate": "2022-06-23"
        },
        "trackMetadata": {
            "trackName": "Jimmy Cooks (feat. 21 Savage)",
            "trackUri": "spotify:track:3F5CgOj3wFlRv51JsHbxhe",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028dc0d801766a5aa6a33cbe37",
            "artists": [
                {
                    "name": "Drake",
                    "spotifyUri": "spotify:artist:3TVXtAsR1Inumwj472S9r4"
                },
                {
                    "name": "21 Savage",
                    "spotifyUri": "spotify:artist:1URnnhqYAYcrqrcwql10ft"
                }
            ],
            "labels": [
                {
                    "name": "OVO"
                }
            ],
            "releaseDate": "2022-06-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 114,
            "previousRank": 94,
            "peakRank": 64,
            "appearancesOnChart": 17,
            "consecutiveAppearancesOnChart": 17,
            "rankingMetric": {
                "value": "8896945",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-17",
            "entryRank": 145,
            "entryDate": "2022-10-06"
        },
        "trackMetadata": {
            "trackName": "Besos Moja2",
            "trackUri": "spotify:track:6OzUIp8KjuwxJnCWkXp1uL",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029f05bb270f81880fd844aae8",
            "artists": [
                {
                    "name": "Wisin & Yandel",
                    "spotifyUri": "spotify:artist:1wZtkThiXbVNtj6hee6dz9"
                },
                {
                    "name": "ROSALÍA",
                    "spotifyUri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin"
                }
            ],
            "releaseDate": "2022-12-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 115,
            "previousRank": 119,
            "peakRank": 4,
            "appearancesOnChart": 306,
            "consecutiveAppearancesOnChart": 109,
            "rankingMetric": {
                "value": "8850730",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2017-11-30",
            "entryRank": 7,
            "entryDate": "2017-03-09"
        },
        "trackMetadata": {
            "trackName": "Perfect",
            "trackUri": "spotify:track:0tgVpDi06FyKpA1z0VMD4v",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ba5db46f4b838ef6027e6f96",
            "artists": [
                {
                    "name": "Ed Sheeran",
                    "spotifyUri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records UK"
                }
            ],
            "releaseDate": "2017-03-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 116,
            "previousRank": 123,
            "peakRank": 10,
            "appearancesOnChart": 34,
            "consecutiveAppearancesOnChart": 34,
            "rankingMetric": {
                "value": "8813487",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-06-09",
            "entryRank": 10,
            "entryDate": "2022-06-09"
        },
        "trackMetadata": {
            "trackName": "I Like You (A Happier Song) (with Doja Cat)",
            "trackUri": "spotify:track:0O6u0VJ46W86TxN9wgyqDj",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0234362676667a4322838ccc97",
            "artists": [
                {
                    "name": "Post Malone",
                    "spotifyUri": "spotify:artist:246dkjvS1zLTtiykXe5h60"
                },
                {
                    "name": "Doja Cat",
                    "spotifyUri": "spotify:artist:5cj0lLjcoR7YOSnhnX0Po5"
                }
            ],
            "labels": [
                {
                    "name": "Mercury Records/Republic Records"
                }
            ],
            "releaseDate": "2022-06-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 117,
            "previousRank": 116,
            "peakRank": 73,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "8789530",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-05",
            "entryRank": 191,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "Calm Down",
            "trackUri": "spotify:track:3BnDvpeuGOj21Ir2aVEtQo",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ffa52727feedfd1935d160c4",
            "artists": [
                {
                    "name": "Rema",
                    "spotifyUri": "spotify:artist:46pWGuE3dSwY3bMMXGBvVS"
                }
            ],
            "labels": [
                {
                    "name": "Mavin Records / Jonzing World"
                }
            ],
            "releaseDate": "2022-03-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 118,
            "previousRank": 85,
            "peakRank": 85,
            "appearancesOnChart": 102,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8758968",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 197,
            "entryDate": "2020-06-18"
        },
        "trackMetadata": {
            "trackName": "Riptide",
            "trackUri": "spotify:track:7yq4Qj7cqayVTp3FF9CWbm",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a9929deb093a6617d2493b03",
            "artists": [
                {
                    "name": "Vance Joy",
                    "spotifyUri": "spotify:artist:10exVja0key0uqUkk6LJRT"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2014-09-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 119,
            "previousRank": 89,
            "peakRank": 89,
            "appearancesOnChart": 10,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8745398",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 197,
            "entryDate": "2022-10-20"
        },
        "trackMetadata": {
            "trackName": "Shut up My Moms Calling",
            "trackUri": "spotify:track:3hxIUxnT27p5WcmjGUXNwx",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024e9657f8a8d50fb54f4d2c94",
            "artists": [
                {
                    "name": "Hotel Ugly",
                    "spotifyUri": "spotify:artist:35WVTyRnKAoaGExqgktVyb"
                }
            ],
            "labels": [
                {
                    "name": "Hotel Ugly, under exclusive license to Amuseio AB"
                }
            ],
            "releaseDate": "2020-02-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 120,
            "previousRank": 117,
            "peakRank": 6,
            "appearancesOnChart": 40,
            "consecutiveAppearancesOnChart": 40,
            "rankingMetric": {
                "value": "8692019",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-05-05",
            "entryRank": 28,
            "entryDate": "2022-04-28"
        },
        "trackMetadata": {
            "trackName": "PROVENZA",
            "trackUri": "spotify:track:7dSZ6zGTQx66c2GF91xCrb",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02e70c454b8989f09d1e11ea92",
            "artists": [
                {
                    "name": "KAROL G",
                    "spotifyUri": "spotify:artist:790FomKkXshlbRYZFtlgla"
                }
            ],
            "labels": [
                {
                    "name": "UMLE - Latino"
                }
            ],
            "releaseDate": "2022-04-22"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 121,
            "previousRank": 99,
            "peakRank": 1,
            "appearancesOnChart": 19,
            "consecutiveAppearancesOnChart": 19,
            "rankingMetric": {
                "value": "8682593",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-09-22",
            "entryRank": 1,
            "entryDate": "2022-09-22"
        },
        "trackMetadata": {
            "trackName": "Shut Down",
            "trackUri": "spotify:track:7gRFDGEzF9UkBV233yv2dc",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02002ef53878df1b4e91c15406",
            "artists": [
                {
                    "name": "BLACKPINK",
                    "spotifyUri": "spotify:artist:41MozSoPIsD1dJM0CLPjZF"
                }
            ],
            "labels": [
                {
                    "name": "YG Entertainment/Interscope Records"
                }
            ],
            "releaseDate": "2022-09-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 122,
            "previousRank": 131,
            "peakRank": 4,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 14,
            "rankingMetric": {
                "value": "8616754",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-27",
            "entryRank": 4,
            "entryDate": "2022-10-27"
        },
        "trackMetadata": {
            "trackName": "Midnight Rain",
            "trackUri": "spotify:track:3rWDp9tBPQR9z6U5YyRSK4",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bb54dde68cd23e2a268ae0f5",
            "artists": [
                {
                    "name": "Taylor Swift",
                    "spotifyUri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
                }
            ],
            "labels": [
                {
                    "name": "Taylor Swift"
                }
            ],
            "releaseDate": "2022-10-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 123,
            "previousRank": 118,
            "peakRank": 108,
            "appearancesOnChart": 17,
            "consecutiveAppearancesOnChart": 17,
            "rankingMetric": {
                "value": "8599387",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-12",
            "entryRank": 196,
            "entryDate": "2022-10-06"
        },
        "trackMetadata": {
            "trackName": "Superman",
            "trackUri": "spotify:track:4woTEX1wYOTGDqNXuavlRC",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e026ca5c90113b30c3c43ffb8f4",
            "artists": [
                {
                    "name": "Eminem",
                    "spotifyUri": "spotify:artist:7dGJo4pcD2V6oG8kP0tJRR"
                },
                {
                    "name": "Dina Rae",
                    "spotifyUri": "spotify:artist:5jNmxPYz8QE5rYp4GDil8t"
                }
            ],
            "labels": [
                {
                    "name": "Aftermath"
                }
            ],
            "releaseDate": "2002-05-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 124,
            "previousRank": -1,
            "peakRank": 124,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "8597700",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 124,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "Players",
            "trackUri": "spotify:track:6UN73IYd0hZxLi8wFPMQij",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021cf7cf4446b496525e423465",
            "artists": [
                {
                    "name": "Coi Leray",
                    "spotifyUri": "spotify:artist:6AMd49uBDJfhf30Ak2QR5s"
                }
            ],
            "labels": [
                {
                    "name": "Uptown / Republic Records"
                }
            ],
            "releaseDate": "2022-11-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 125,
            "previousRank": 111,
            "peakRank": 14,
            "appearancesOnChart": 10,
            "consecutiveAppearancesOnChart": 10,
            "rankingMetric": {
                "value": "8591601",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-01",
            "entryRank": 16,
            "entryDate": "2022-11-24"
        },
        "trackMetadata": {
            "trackName": "Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]",
            "trackUri": "spotify:track:1RDvyOk4WtPCtoqciJwVn8",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ef57183066d6cac0cabb85c6",
            "artists": [
                {
                    "name": "Jung Kook",
                    "spotifyUri": "spotify:artist:6HaGTQPmzraVmaVxvz6EUc"
                },
                {
                    "name": "BTS",
                    "spotifyUri": "spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX"
                },
                {
                    "name": "FIFA Sound",
                    "spotifyUri": "spotify:artist:5C01hDqpEmrmDfUhX9YWsH"
                }
            ],
            "labels": [
                {
                    "name": "Katara Studios | 2101 Records under exclusive license to UnitedMasters LLC"
                }
            ],
            "releaseDate": "2022-11-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 126,
            "previousRank": 112,
            "peakRank": 89,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 29,
            "rankingMetric": {
                "value": "8572856",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-13",
            "entryRank": 184,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "Apocalypse",
            "trackUri": "spotify:track:3AVrVz5rK8Hrqo9YGiVGN5",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e026b701428ed4c6e053902174a",
            "artists": [
                {
                    "name": "Cigarettes After Sex",
                    "spotifyUri": "spotify:artist:1QAJqy2dA3ihHBFIHRphZj"
                }
            ],
            "labels": [
                {
                    "name": "PTKF"
                }
            ],
            "releaseDate": "2017-06-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 127,
            "previousRank": 102,
            "peakRank": 7,
            "appearancesOnChart": 31,
            "consecutiveAppearancesOnChart": 31,
            "rankingMetric": {
                "value": "8494341",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-06-30",
            "entryRank": 7,
            "entryDate": "2022-06-30"
        },
        "trackMetadata": {
            "trackName": "Left and Right (Feat. Jung Kook of BTS)",
            "trackUri": "spotify:track:5Odq8ohlgIbQKMZivbWkEo",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0235d2e0ed94a934f2cc46fa49",
            "artists": [
                {
                    "name": "Charlie Puth",
                    "spotifyUri": "spotify:artist:6VuMaDnrHyPL1p4EHjYLi7"
                },
                {
                    "name": "Jung Kook",
                    "spotifyUri": "spotify:artist:6HaGTQPmzraVmaVxvz6EUc"
                },
                {
                    "name": "BTS",
                    "spotifyUri": "spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2022-10-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 128,
            "previousRank": 145,
            "peakRank": 128,
            "appearancesOnChart": 6,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8487592",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 197,
            "entryDate": "2022-11-24"
        },
        "trackMetadata": {
            "trackName": "Qué Agonía",
            "trackUri": "spotify:track:4H6o1bxKRGzmsE0vzo968m",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a2bdfe853606a681c40816c9",
            "artists": [
                {
                    "name": "Yuridia",
                    "spotifyUri": "spotify:artist:5B8ApeENp4bE4EE3LI8jK2"
                },
                {
                    "name": "Ángela Aguilar",
                    "spotifyUri": "spotify:artist:3abT87tqQ4Q5PA5nw6CYyH"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music México"
                }
            ],
            "releaseDate": "2022-10-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 129,
            "previousRank": 126,
            "peakRank": 51,
            "appearancesOnChart": 86,
            "consecutiveAppearancesOnChart": 56,
            "rankingMetric": {
                "value": "8484096",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-02-17",
            "entryRank": 189,
            "entryDate": "2021-04-22"
        },
        "trackMetadata": {
            "trackName": "The Real Slim Shady",
            "trackUri": "spotify:track:3yfqSUWxFvZELEM4PmlwIR",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02dbb3dd82da45b7d7f31b1b42",
            "artists": [
                {
                    "name": "Eminem",
                    "spotifyUri": "spotify:artist:7dGJo4pcD2V6oG8kP0tJRR"
                }
            ],
            "labels": [
                {
                    "name": "Interscope"
                }
            ],
            "releaseDate": "2000-05-23"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 130,
            "previousRank": 125,
            "peakRank": 98,
            "appearancesOnChart": 71,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8469099",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-06",
            "entryRank": 193,
            "entryDate": "2020-12-31"
        },
        "trackMetadata": {
            "trackName": "Do I Wanna Know?",
            "trackUri": "spotify:track:5FVd6KXrgO9B3JPmC8OPst",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024ae1c4c5c45aabe565499163",
            "artists": [
                {
                    "name": "Arctic Monkeys",
                    "spotifyUri": "spotify:artist:7Ln80lUS6He07XvHI8qqHH"
                }
            ],
            "labels": [
                {
                    "name": "Domino Recording Co"
                }
            ],
            "releaseDate": "2013-09-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 131,
            "previousRank": 127,
            "peakRank": 3,
            "appearancesOnChart": 65,
            "consecutiveAppearancesOnChart": 65,
            "rankingMetric": {
                "value": "8459029",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-02-24",
            "entryRank": 61,
            "entryDate": "2021-11-04"
        },
        "trackMetadata": {
            "trackName": "Enemy (with JID) - from the series Arcane League of Legends",
            "trackUri": "spotify:track:3CIyK1V4JEJkg02E4EJnDl",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
            "artists": [
                {
                    "name": "Imagine Dragons",
                    "spotifyUri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
                },
                {
                    "name": "JID",
                    "spotifyUri": "spotify:artist:6U3ybJ9UHNKEdsH7ktGBZ7"
                },
                {
                    "name": "Arcane",
                    "spotifyUri": "spotify:artist:57nPqD7z62gDdq37US9XJR"
                },
                {
                    "name": "League of Legends",
                    "spotifyUri": "spotify:artist:47mIJdHORyRerp4os813jD"
                }
            ],
            "labels": [
                {
                    "name": "Kid Ina Korner / Interscope"
                }
            ],
            "releaseDate": "2022-07-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 132,
            "previousRank": 90,
            "peakRank": 86,
            "appearancesOnChart": 16,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8418161",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-27",
            "entryRank": 182,
            "entryDate": "2022-10-06"
        },
        "trackMetadata": {
            "trackName": "How Do I Say Goodbye",
            "trackUri": "spotify:track:1aOl53hkZGHkl2Snhr7opL",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02991f6658282ef028f93b11e0",
            "artists": [
                {
                    "name": "Dean Lewis",
                    "spotifyUri": "spotify:artist:3QSQFmccmX81fWCUSPTS7y"
                }
            ],
            "labels": [
                {
                    "name": "Universal Music Australia Pty. Ltd."
                }
            ],
            "releaseDate": "2022-11-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 133,
            "previousRank": 103,
            "peakRank": 48,
            "appearancesOnChart": 16,
            "consecutiveAppearancesOnChart": 16,
            "rankingMetric": {
                "value": "8372709",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-20",
            "entryRank": 109,
            "entryDate": "2022-10-13"
        },
        "trackMetadata": {
            "trackName": "PUNTO 40",
            "trackUri": "spotify:track:58cEG7FsVoipRiRKUMgOjo",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029f971e4c38e5dedcb242b3ae",
            "artists": [
                {
                    "name": "Rauw Alejandro",
                    "spotifyUri": "spotify:artist:1mcTU81TzQhprhouKaTkpq"
                },
                {
                    "name": "Baby Rasta",
                    "spotifyUri": "spotify:artist:0GgyFUpOyzWDRDqx8FCTDN"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music Latin/Duars Entertainment"
                }
            ],
            "releaseDate": "2022-11-11"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 134,
            "previousRank": 129,
            "peakRank": 4,
            "appearancesOnChart": 167,
            "consecutiveAppearancesOnChart": 167,
            "rankingMetric": {
                "value": "8367121",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2020-07-23",
            "entryRank": 21,
            "entryDate": "2019-11-21"
        },
        "trackMetadata": {
            "trackName": "Watermelon Sugar",
            "trackUri": "spotify:track:6UelLqGlWMcVH1E5c4H7lY",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0277fdcfda6535601aff081b6a",
            "artists": [
                {
                    "name": "Harry Styles",
                    "spotifyUri": "spotify:artist:6KImCVD70vtIoJWnq6nGn3"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2019-12-13"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 135,
            "previousRank": 133,
            "peakRank": 16,
            "appearancesOnChart": 312,
            "consecutiveAppearancesOnChart": 312,
            "rankingMetric": {
                "value": "8292009",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2017-06-29",
            "entryRank": 73,
            "entryDate": "2017-02-09"
        },
        "trackMetadata": {
            "trackName": "Believer",
            "trackUri": "spotify:track:0pqnGHJpmpxLKifKRmU6WP",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025675e83f707f1d7271e5cf8a",
            "artists": [
                {
                    "name": "Imagine Dragons",
                    "spotifyUri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
                }
            ],
            "labels": [
                {
                    "name": "Kid Ina Korner / Interscope"
                }
            ],
            "releaseDate": "2017-06-23"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 136,
            "previousRank": 132,
            "peakRank": 132,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "8280292",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 132,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Party In The U.S.A.",
            "trackUri": "spotify:track:3E7dfMvvCLUddWissuqMwr",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d6c3ad6a2a27471e1d5e8103",
            "artists": [
                {
                    "name": "Miley Cyrus",
                    "spotifyUri": "spotify:artist:5YGY8feqx7naU7z4HrwZM6"
                }
            ],
            "labels": [
                {
                    "name": "Hollywood Records"
                }
            ],
            "releaseDate": "2009-01-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 137,
            "previousRank": 153,
            "peakRank": 21,
            "appearancesOnChart": 68,
            "consecutiveAppearancesOnChart": 68,
            "rankingMetric": {
                "value": "8273161",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-01-27",
            "entryRank": 193,
            "entryDate": "2021-10-14"
        },
        "trackMetadata": {
            "trackName": "I Love You So",
            "trackUri": "spotify:track:4SqWKzw0CbA05TGszDgMlc",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029214ff0109a0e062f8a6cf0f",
            "artists": [
                {
                    "name": "The Walters",
                    "spotifyUri": "spotify:artist:027TpXKGwdXP7iwbjUSpV8"
                }
            ],
            "labels": [
                {
                    "name": "Warner Records"
                }
            ],
            "releaseDate": "2014-11-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 138,
            "previousRank": 141,
            "peakRank": 58,
            "appearancesOnChart": 24,
            "consecutiveAppearancesOnChart": 24,
            "rankingMetric": {
                "value": "8270977",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-13",
            "entryRank": 175,
            "entryDate": "2022-08-18"
        },
        "trackMetadata": {
            "trackName": "Sex, Drugs, Etc.",
            "trackUri": "spotify:track:7DbdUf8aHSYoliSjO6LZv6",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d965622035c698fefc8c8a4a",
            "artists": [
                {
                    "name": "Beach Weather",
                    "spotifyUri": "spotify:artist:7I3bkknknQkIiatWiupQgD"
                }
            ],
            "labels": [
                {
                    "name": "8123 / Arista Records"
                }
            ],
            "releaseDate": "2016-11-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 139,
            "previousRank": 148,
            "peakRank": 11,
            "appearancesOnChart": 71,
            "consecutiveAppearancesOnChart": 68,
            "rankingMetric": {
                "value": "8241937",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-03-17",
            "entryRank": 50,
            "entryDate": "2021-03-25"
        },
        "trackMetadata": {
            "trackName": "Ghost",
            "trackUri": "spotify:track:6I3mqTwhRpn34SLVafSH7G",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02e6f407c7f3a0ec98845e4431",
            "artists": [
                {
                    "name": "Justin Bieber",
                    "spotifyUri": "spotify:artist:1uNFoZAHBGtllmzznpCI3s"
                }
            ],
            "labels": [
                {
                    "name": "RBMG/Def Jam"
                }
            ],
            "releaseDate": "2021-03-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 140,
            "previousRank": 193,
            "peakRank": 131,
            "appearancesOnChart": 26,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8172757",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-20",
            "entryRank": 200,
            "entryDate": "2022-07-21"
        },
        "trackMetadata": {
            "trackName": "Stargirl Interlude",
            "trackUri": "spotify:track:5gDWsRxpJ2lZAffh5p7K0w",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a048415db06a5b6fa7ec4e1a",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                },
                {
                    "name": "Lana Del Rey",
                    "spotifyUri": "spotify:artist:00FQb4jTyendYWaN8pK0wa"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2016-11-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 141,
            "previousRank": 170,
            "peakRank": 57,
            "appearancesOnChart": 25,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "8170763",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-07-14",
            "entryRank": 57,
            "entryDate": "2022-07-14"
        },
        "trackMetadata": {
            "trackName": "Normal",
            "trackUri": "spotify:track:0T2pB7P1VdXPhLdQZ488uH",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0273456ed697350847810e52b3",
            "artists": [
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "UMLE - Latino"
                }
            ],
            "releaseDate": "2022-09-14"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 142,
            "previousRank": 138,
            "peakRank": 52,
            "appearancesOnChart": 73,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8138261",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2021-02-11",
            "entryRank": 180,
            "entryDate": "2016-12-29"
        },
        "trackMetadata": {
            "trackName": "The Hills",
            "trackUri": "spotify:track:7fBv7CLKzipRk6EC6TWHOB",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e027fcead687e99583072cc217b",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                }
            ],
            "labels": [
                {
                    "name": "Universal Republic Records"
                }
            ],
            "releaseDate": "2015-08-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 143,
            "previousRank": 135,
            "peakRank": 27,
            "appearancesOnChart": 14,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8137992",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-07-28",
            "entryRank": 27,
            "entryDate": "2022-07-28"
        },
        "trackMetadata": {
            "trackName": "TV",
            "trackUri": "spotify:track:3GYlZ7tbxLOxe6ewMNVTkw",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e027a4781629469bb83356cd318",
            "artists": [
                {
                    "name": "Billie Eilish",
                    "spotifyUri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
                }
            ],
            "labels": [
                {
                    "name": "Darkroom/Interscope Records"
                }
            ],
            "releaseDate": "2022-07-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 144,
            "previousRank": 172,
            "peakRank": 63,
            "appearancesOnChart": 47,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8112162",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2017-08-31",
            "entryRank": 63,
            "entryDate": "2017-08-31"
        },
        "trackMetadata": {
            "trackName": "Revenge",
            "trackUri": "spotify:track:5TXDeTFVRVY7Cvt0Dw4vWW",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02203c89bd4391468eea4cc3f5",
            "artists": [
                {
                    "name": "XXXTENTACION",
                    "spotifyUri": "spotify:artist:15UsOTVnJzReFVN1VCnxy4"
                }
            ],
            "labels": [
                {
                    "name": "Bad Vibes Forever / EMPIRE"
                }
            ],
            "releaseDate": "2017-08-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 145,
            "previousRank": 154,
            "peakRank": 74,
            "appearancesOnChart": 27,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8106536",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-09-08",
            "entryRank": 194,
            "entryDate": "2022-07-07"
        },
        "trackMetadata": {
            "trackName": "LA INOCENTE",
            "trackUri": "spotify:track:5jt25aFjW2kNoBqaEVaz5W",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02851222dc5c5681bd4c3119d3",
            "artists": [
                {
                    "name": "Mora",
                    "spotifyUri": "spotify:artist:0Q8NcsJwoCbZOHHW63su5S"
                },
                {
                    "name": "Feid",
                    "spotifyUri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
                }
            ],
            "labels": [
                {
                    "name": "Rimas Entertainment LLC"
                }
            ],
            "releaseDate": "2022-04-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 146,
            "previousRank": 146,
            "peakRank": 4,
            "appearancesOnChart": 72,
            "consecutiveAppearancesOnChart": 72,
            "rankingMetric": {
                "value": "8086581",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2021-11-04",
            "entryRank": 11,
            "entryDate": "2021-09-16"
        },
        "trackMetadata": {
            "trackName": "Shivers",
            "trackUri": "spotify:track:3xWGA8pa0IKFI7IMPri4P0",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ef24c3fdbf856340d55cfeb2",
            "artists": [
                {
                    "name": "Ed Sheeran",
                    "spotifyUri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records UK"
                }
            ],
            "releaseDate": "2021-10-29"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 147,
            "previousRank": 142,
            "peakRank": 142,
            "appearancesOnChart": 4,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8079898",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 151,
            "entryDate": "2023-01-05"
        },
        "trackMetadata": {
            "trackName": "Those Eyes",
            "trackUri": "spotify:track:50x1Ic8CaXkYNvjmxe3WXy",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e021bb5dc21200bfc56d8f7ef41",
            "artists": [
                {
                    "name": "New West",
                    "spotifyUri": "spotify:artist:69bG9tC62d8oTFC9aTTosn"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2019-05-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 148,
            "previousRank": 162,
            "peakRank": 66,
            "appearancesOnChart": 77,
            "consecutiveAppearancesOnChart": 77,
            "rankingMetric": {
                "value": "8060755",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2021-09-16",
            "entryRank": 165,
            "entryDate": "2021-08-12"
        },
        "trackMetadata": {
            "trackName": "Dark Red",
            "trackUri": "spotify:track:3EaJDYHA0KnX88JvDhL9oa",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e023d2dfa42f771cd458b194979",
            "artists": [
                {
                    "name": "Steve Lacy",
                    "spotifyUri": "spotify:artist:57vWImR43h4CaDao012Ofp"
                }
            ],
            "labels": [
                {
                    "name": "Three Quarter"
                }
            ],
            "releaseDate": "2017-02-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 149,
            "previousRank": 137,
            "peakRank": 119,
            "appearancesOnChart": 17,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "8040598",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-12",
            "entryRank": 192,
            "entryDate": "2022-01-20"
        },
        "trackMetadata": {
            "trackName": "Space Song",
            "trackUri": "spotify:track:7H0ya83CMmgFcOhw0UB6ow",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029b7190e673e46271b2754aab",
            "artists": [
                {
                    "name": "Beach House",
                    "spotifyUri": "spotify:artist:56ZTgzPBDge0OvCGgMO3OY"
                }
            ],
            "labels": [
                {
                    "name": "Sub Pop Records"
                }
            ],
            "releaseDate": "2015-08-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 150,
            "previousRank": 152,
            "peakRank": 9,
            "appearancesOnChart": 37,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7967045",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-06-02",
            "entryRank": 31,
            "entryDate": "2022-05-05"
        },
        "trackMetadata": {
            "trackName": "About Damn Time",
            "trackUri": "spotify:track:6HMtHNpW6YPi1hrw9tgF8P",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02fe3b1b9cb7183a94e1aafd43",
            "artists": [
                {
                    "name": "Lizzo",
                    "spotifyUri": "spotify:artist:56oDRnqbIiwx4mymNEv7dS"
                }
            ],
            "labels": [
                {
                    "name": "Nice Life/Atlantic"
                }
            ],
            "releaseDate": "2022-07-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 151,
            "previousRank": 197,
            "peakRank": 5,
            "appearancesOnChart": 89,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7908293",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2021-04-29",
            "entryRank": 5,
            "entryDate": "2021-04-29"
        },
        "trackMetadata": {
            "trackName": "Save Your Tears (Remix) (with Ariana Grande) - Bonus Track",
            "trackUri": "spotify:track:1oFAF1hdPOickyHgbuRjyX",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b5097b81179824803664aaaf",
            "artists": [
                {
                    "name": "The Weeknd",
                    "spotifyUri": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
                },
                {
                    "name": "Ariana Grande",
                    "spotifyUri": "spotify:artist:66CXWjxzNUsdJxJ2JdwvnR"
                }
            ],
            "labels": [
                {
                    "name": "XO / Republic Records"
                }
            ],
            "releaseDate": "2020-03-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 152,
            "previousRank": 177,
            "peakRank": 108,
            "appearancesOnChart": 34,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7870446",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-08-18",
            "entryRank": 177,
            "entryDate": "2022-06-02"
        },
        "trackMetadata": {
            "trackName": "Night Changes",
            "trackUri": "spotify:track:5O2P9iiztwhomNh8xkR9lJ",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d304ba2d71de306812eebaf4",
            "artists": [
                {
                    "name": "One Direction",
                    "spotifyUri": "spotify:artist:4AK6F7OLvEQ5QYCBNiQWHq"
                }
            ],
            "labels": [
                {
                    "name": "Syco Music"
                }
            ],
            "releaseDate": "2014-11-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 153,
            "previousRank": 156,
            "peakRank": 94,
            "appearancesOnChart": 24,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7858855",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-09-22",
            "entryRank": 180,
            "entryDate": "2022-07-28"
        },
        "trackMetadata": {
            "trackName": "Summertime Sadness",
            "trackUri": "spotify:track:1FEiijYPJtyswChfcpv3p0",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02f894be72a77b1488292672c7",
            "artists": [
                {
                    "name": "Lana Del Rey",
                    "spotifyUri": "spotify:artist:00FQb4jTyendYWaN8pK0wa"
                }
            ],
            "labels": [
                {
                    "name": "Urban"
                }
            ],
            "releaseDate": "2012-01-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 154,
            "previousRank": 144,
            "peakRank": 28,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 38,
            "rankingMetric": {
                "value": "7846844",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-07-21",
            "entryRank": 170,
            "entryDate": "2022-05-12"
        },
        "trackMetadata": {
            "trackName": "Sunroof",
            "trackUri": "spotify:track:4h4QlmocP3IuwYEj2j14p8",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e020ed2184bf3fb4466d623a874",
            "artists": [
                {
                    "name": "Nicky Youre",
                    "spotifyUri": "spotify:artist:7qmpXeNz2ojlMl2EEfkeLs"
                },
                {
                    "name": "dazy",
                    "spotifyUri": "spotify:artist:38PzLQE4GW8o7A18oGhi0x"
                }
            ],
            "labels": [
                {
                    "name": "Thirty Knots/Columbia"
                }
            ],
            "releaseDate": "2021-12-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 155,
            "previousRank": 149,
            "peakRank": 12,
            "appearancesOnChart": 131,
            "consecutiveAppearancesOnChart": 131,
            "rankingMetric": {
                "value": "7842671",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2020-09-10",
            "entryRank": 140,
            "entryDate": "2020-07-30"
        },
        "trackMetadata": {
            "trackName": "Heather",
            "trackUri": "spotify:track:4xqrdfXkTW4T0RauPLv3WA",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0288e3cda6d29b2552d4d6bc43",
            "artists": [
                {
                    "name": "Conan Gray",
                    "spotifyUri": "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2020-03-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 156,
            "previousRank": -1,
            "peakRank": 156,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7797383",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 156,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "Puta Mexicana",
            "trackUri": "spotify:track:4mD9hjoTckjeL1CrJCx0MT",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022479aa0668d6cc22b664a9e5",
            "artists": [
                {
                    "name": "DJ Jeeh FDC",
                    "spotifyUri": "spotify:artist:5lal0BjsooQ7ON4t7B73bp"
                },
                {
                    "name": "MC Menor MT",
                    "spotifyUri": "spotify:artist:4EMRE0wdcc2xjv1PCmTqUU"
                },
                {
                    "name": "Yuri Redicopa",
                    "spotifyUri": "spotify:artist:0pVJXCGsBydS7rq0R4w4hm"
                },
                {
                    "name": "Mc Pelé",
                    "spotifyUri": "spotify:artist:5kfgervAs5bJUOC0vbYB12"
                }
            ],
            "labels": [
                {
                    "name": "PMI Records Oficial"
                }
            ],
            "releaseDate": "2022-12-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 157,
            "previousRank": 171,
            "peakRank": 104,
            "appearancesOnChart": 62,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7747235",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2021-02-11",
            "entryRank": 184,
            "entryDate": "2020-12-31"
        },
        "trackMetadata": {
            "trackName": "Why'd You Only Call Me When You're High?",
            "trackUri": "spotify:track:086myS9r57YsLbJpU0TgK9",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024ae1c4c5c45aabe565499163",
            "artists": [
                {
                    "name": "Arctic Monkeys",
                    "spotifyUri": "spotify:artist:7Ln80lUS6He07XvHI8qqHH"
                }
            ],
            "labels": [
                {
                    "name": "Domino Recording Co"
                }
            ],
            "releaseDate": "2013-09-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 158,
            "previousRank": 143,
            "peakRank": 21,
            "appearancesOnChart": 12,
            "consecutiveAppearancesOnChart": 12,
            "rankingMetric": {
                "value": "7734219",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-11-10",
            "entryRank": 21,
            "entryDate": "2022-11-10"
        },
        "trackMetadata": {
            "trackName": "Die For You",
            "trackUri": "spotify:track:26hOm7dTtBi0TdpDGl141t",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02eaac2a7955f5b8967991cacb",
            "artists": [
                {
                    "name": "Joji",
                    "spotifyUri": "spotify:artist:3MZsBdqDrRTJihTHQrO6Dq"
                }
            ],
            "labels": [
                {
                    "name": "88rising Music/Warner Records"
                }
            ],
            "releaseDate": "2022-11-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 159,
            "previousRank": 157,
            "peakRank": 112,
            "appearancesOnChart": 38,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7696640",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-11",
            "entryRank": 178,
            "entryDate": "2022-04-21"
        },
        "trackMetadata": {
            "trackName": "After Dark",
            "trackUri": "spotify:track:5FkJHVudUByVjanCqFXRql",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b492477206075438e0751176",
            "artists": [
                {
                    "name": "Mr.Kitty",
                    "spotifyUri": "spotify:artist:0pWwt5vGNzezEhfAcc420Y"
                }
            ],
            "labels": [
                {
                    "name": "Negative Gain Productions"
                }
            ],
            "releaseDate": "2014-10-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 160,
            "previousRank": -1,
            "peakRank": 107,
            "appearancesOnChart": 51,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7688180",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2023-01-05",
            "entryRank": 190,
            "entryDate": "2017-01-05"
        },
        "trackMetadata": {
            "trackName": "Can't Hold Us (feat. Ray Dalton)",
            "trackUri": "spotify:track:22skzmqfdWrjJylampe0kt",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022a6b364528b128a4a17d100d",
            "artists": [
                {
                    "name": "Macklemore & Ryan Lewis",
                    "spotifyUri": "spotify:artist:5BcAKTbp20cv7tC5VqPFoC"
                },
                {
                    "name": "Macklemore",
                    "spotifyUri": "spotify:artist:3JhNCzhSMTxs9WLGJJxWOY"
                },
                {
                    "name": "Ryan Lewis",
                    "spotifyUri": "spotify:artist:4myTppRgh0rojLxx8RycOp"
                },
                {
                    "name": "Ray Dalton",
                    "spotifyUri": "spotify:artist:4e0nWw2r4BoQSKPQ2zpU13"
                }
            ],
            "labels": [
                {
                    "name": "Macklemore"
                }
            ],
            "releaseDate": "2012-10-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 161,
            "previousRank": 169,
            "peakRank": 113,
            "appearancesOnChart": 59,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7673113",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-28",
            "entryRank": 147,
            "entryDate": "2017-06-15"
        },
        "trackMetadata": {
            "trackName": "Blank Space",
            "trackUri": "spotify:track:1u8c2t2Cy7UBoG4ArRcF5g",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029abdf14e6058bd3903686148",
            "artists": [
                {
                    "name": "Taylor Swift",
                    "spotifyUri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
                }
            ],
            "labels": [
                {
                    "name": "Big Machine Records, LLC"
                }
            ],
            "releaseDate": "2014-10-27"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 162,
            "previousRank": 168,
            "peakRank": 101,
            "appearancesOnChart": 93,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7647945",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-28",
            "entryRank": 189,
            "entryDate": "2021-02-18"
        },
        "trackMetadata": {
            "trackName": "Counting Stars",
            "trackUri": "spotify:track:2tpWsVSb9UEmDRxAl1zhX1",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02e80e7dbce3996a1ae5967751",
            "artists": [
                {
                    "name": "OneRepublic",
                    "spotifyUri": "spotify:artist:5Pwc4xIPtQLFEnJriah9YJ"
                }
            ],
            "labels": [
                {
                    "name": "Mosley / Interscope"
                }
            ],
            "releaseDate": "2014-01-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 163,
            "previousRank": 194,
            "peakRank": 63,
            "appearancesOnChart": 24,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7622666",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-13",
            "entryRank": 186,
            "entryDate": "2022-07-28"
        },
        "trackMetadata": {
            "trackName": "Atlantis",
            "trackUri": "spotify:track:1Fid2jjqsHViMX6xNH70hE",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028c33272a7c77042f5eb39d75",
            "artists": [
                {
                    "name": "Seafret",
                    "spotifyUri": "spotify:artist:4Ly0KABsxlx4fNj63zJTrF"
                }
            ],
            "labels": [
                {
                    "name": "Sweet Jane Recordings"
                }
            ],
            "releaseDate": "2016-01-29"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 164,
            "previousRank": -1,
            "peakRank": 164,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7610829",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 164,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "KNIGHT CRAWLER (feat. Juice WRLD)",
            "trackUri": "spotify:track:3fNMgjG8yXaSam46swhz7w",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02bbdaebbe96beb77e38781def",
            "artists": [
                {
                    "name": "Trippie Redd",
                    "spotifyUri": "spotify:artist:6Xgp2XMz1fhVYe7i6yNAax"
                },
                {
                    "name": "Juice WRLD",
                    "spotifyUri": "spotify:artist:4MCBfE4596Uoi2O4DtmEMz"
                }
            ],
            "labels": [
                {
                    "name": "TenThousand Projects"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 165,
            "previousRank": 199,
            "peakRank": 165,
            "appearancesOnChart": 3,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "7604145",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2023-01-26",
            "entryRank": 196,
            "entryDate": "2023-01-12"
        },
        "trackMetadata": {
            "trackName": "Boy's a liar",
            "trackUri": "spotify:track:3NanY0K4okhIQzL33U5Ad8",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025911dc1602a9d100ebe955fc",
            "artists": [
                {
                    "name": "PinkPantheress",
                    "spotifyUri": "spotify:artist:78rUTD7y6Cy67W1RVzYs7t"
                }
            ],
            "labels": [
                {
                    "name": "Warner Records"
                }
            ],
            "releaseDate": "2022-11-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 166,
            "previousRank": 160,
            "peakRank": 2,
            "appearancesOnChart": 106,
            "consecutiveAppearancesOnChart": 6,
            "rankingMetric": {
                "value": "7603975",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2018-05-24",
            "entryRank": 13,
            "entryDate": "2018-04-12"
        },
        "trackMetadata": {
            "trackName": "One Kiss (with Dua Lipa)",
            "trackUri": "spotify:track:7ef4DlsgrMEH11cDZd32M6",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02d09f96d82310d4d77c14c108",
            "artists": [
                {
                    "name": "Calvin Harris",
                    "spotifyUri": "spotify:artist:7CajNmpbOovFoOoasH2HaY"
                },
                {
                    "name": "Dua Lipa",
                    "spotifyUri": "spotify:artist:6M2wZ9GZgrQXHCFfjv46we"
                }
            ],
            "labels": [
                {
                    "name": "Sony Music UK"
                }
            ],
            "releaseDate": "2018-04-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 167,
            "previousRank": 165,
            "peakRank": 17,
            "appearancesOnChart": 101,
            "consecutiveAppearancesOnChart": 30,
            "rankingMetric": {
                "value": "7577859",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2019-08-08",
            "entryRank": 20,
            "entryDate": "2019-07-04"
        },
        "trackMetadata": {
            "trackName": "LA CANCIÓN",
            "trackUri": "spotify:track:0fea68AdmYNygeTGI4RC18",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024891d9b25d8919448388f3bb",
            "artists": [
                {
                    "name": "J Balvin",
                    "spotifyUri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
                },
                {
                    "name": "Bad Bunny",
                    "spotifyUri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
                }
            ],
            "labels": [
                {
                    "name": "Universal Music Latino / Rimas"
                }
            ],
            "releaseDate": "2019-06-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 168,
            "previousRank": -1,
            "peakRank": 61,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7565721",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2021-10-21",
            "entryRank": 183,
            "entryDate": "2021-10-14"
        },
        "trackMetadata": {
            "trackName": "Set Fire to the Rain",
            "trackUri": "spotify:track:7j4OmvkjRz0PrjFADlHfQx",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e022118bf9b198b05a95ded6300",
            "artists": [
                {
                    "name": "Adele",
                    "spotifyUri": "spotify:artist:4dpARuHxo51G3z768sgnrY"
                }
            ],
            "labels": [
                {
                    "name": "XL Recordings"
                }
            ],
            "releaseDate": "2011-01-24"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 169,
            "previousRank": 198,
            "peakRank": 105,
            "appearancesOnChart": 26,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7520362",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-08-11",
            "entryRank": 158,
            "entryDate": "2022-06-09"
        },
        "trackMetadata": {
            "trackName": "Everybody Wants To Rule The World",
            "trackUri": "spotify:track:4RvWPyQ5RL0ao9LPZeSouE",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0222463d6939fec9e17b2a6235",
            "artists": [
                {
                    "name": "Tears For Fears",
                    "spotifyUri": "spotify:artist:4bthk9UfsYUYdcFyqxmSUU"
                }
            ],
            "labels": [
                {
                    "name": "UMC (Universal Music Catalogue)"
                }
            ],
            "releaseDate": "1985-02-25"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 170,
            "previousRank": 155,
            "peakRank": 33,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "7505812",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-08",
            "entryRank": 33,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "Too Many Nights (feat. Don Toliver & with Future)",
            "trackUri": "spotify:track:2Hh3ETdQKrmSI3QS0hme7g",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0213e54d6687e65678d60466c2",
            "artists": [
                {
                    "name": "Metro Boomin",
                    "spotifyUri": "spotify:artist:0iEtIxbK0KxaSlF7G42ZOp"
                },
                {
                    "name": "Future",
                    "spotifyUri": "spotify:artist:1RyvyyTE3xzB2ZywiAwp0i"
                },
                {
                    "name": "Don Toliver",
                    "spotifyUri": "spotify:artist:4Gso3d4CscCijv0lmajZWs"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-12-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 171,
            "previousRank": 136,
            "peakRank": 136,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7504478",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 188,
            "entryDate": "2022-11-10"
        },
        "trackMetadata": {
            "trackName": "WORTH NOTHING - Fast & Furious: Drift Tape/Phonk Vol 1",
            "trackUri": "spotify:track:5Zlb01Jcn0Ld49zazzZJSB",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02a6fb54b3fe850150c61e5980",
            "artists": [
                {
                    "name": "TWISTED",
                    "spotifyUri": "spotify:artist:1rPf3UFQ9PzH7MafzfHTnG"
                },
                {
                    "name": "Oliver Tree",
                    "spotifyUri": "spotify:artist:6TLwD7HPWuiOzvXEa3oCNe"
                }
            ],
            "labels": [
                {
                    "name": "APG Inc – FF10"
                }
            ],
            "releaseDate": "2022-09-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 172,
            "previousRank": 186,
            "peakRank": 106,
            "appearancesOnChart": 48,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7493389",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-28",
            "entryRank": 111,
            "entryDate": "2022-01-06"
        },
        "trackMetadata": {
            "trackName": "Locked out of Heaven",
            "trackUri": "spotify:track:5g7sDjBhZ4I3gcFIpkrLuI",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02926f43e7cce571e62720fd46",
            "artists": [
                {
                    "name": "Bruno Mars",
                    "spotifyUri": "spotify:artist:0du5cEVh5yTK9QJze8zA0C"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records"
                }
            ],
            "releaseDate": "2012-12-07"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 173,
            "previousRank": -1,
            "peakRank": 50,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7489020",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2022-10-20",
            "entryRank": 71,
            "entryDate": "2022-10-13"
        },
        "trackMetadata": {
            "trackName": "THE LONELIEST",
            "trackUri": "spotify:track:7exHT4swWOKL5addPeqkLP",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c1b211b5fcdef31be5f806df",
            "artists": [
                {
                    "name": "Måneskin",
                    "spotifyUri": "spotify:artist:0lAWpj5szCSwM4rUMHYmrr"
                }
            ],
            "labels": [
                {
                    "name": "Epic"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 174,
            "previousRank": -1,
            "peakRank": 174,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7479524",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 174,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "Komet",
            "trackUri": "spotify:track:7oQepKHmXDaPC3rgeLRvQu",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028945d66b89a2fefd8e6b2181",
            "artists": [
                {
                    "name": "Udo Lindenberg",
                    "spotifyUri": "spotify:artist:7iWcRnQMinCoV2u5ICgsW0"
                },
                {
                    "name": "Apache 207",
                    "spotifyUri": "spotify:artist:1qQLhymHXFPtP5U8KNKsm6"
                }
            ],
            "labels": [
                {
                    "name": "WM Germany"
                }
            ],
            "releaseDate": "2023-01-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 175,
            "previousRank": -1,
            "peakRank": 175,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7460023",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 175,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "WANDA",
            "trackUri": "spotify:track:0Iozrbed8spxoBnmtBMshO",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ea0efa338b8bcef4431e30a1",
            "artists": [
                {
                    "name": "Quevedo",
                    "spotifyUri": "spotify:artist:52iwsT98xCoGgiGntTiR7K"
                }
            ],
            "labels": [
                {
                    "name": "Quevedo"
                }
            ],
            "releaseDate": "2023-01-20"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 176,
            "previousRank": 147,
            "peakRank": 147,
            "appearancesOnChart": 13,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "7441733",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 194,
            "entryDate": "2022-03-17"
        },
        "trackMetadata": {
            "trackName": "Demons",
            "trackUri": "spotify:track:5qaEfEh1AtSdrdrByCP7qR",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b2b2747c89d2157b0b29fb6a",
            "artists": [
                {
                    "name": "Imagine Dragons",
                    "spotifyUri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
                }
            ],
            "labels": [
                {
                    "name": "Kid Ina Korner / Interscope"
                }
            ],
            "releaseDate": "2012-09-04"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 177,
            "previousRank": 179,
            "peakRank": 11,
            "appearancesOnChart": 57,
            "consecutiveAppearancesOnChart": 57,
            "rankingMetric": {
                "value": "7432440",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-04-28",
            "entryRank": 197,
            "entryDate": "2021-12-30"
        },
        "trackMetadata": {
            "trackName": "MIDDLE OF THE NIGHT",
            "trackUri": "spotify:track:58HvfVOeJY7lUuCqF0m3ly",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0253a2e11c1bde700722fecd2e",
            "artists": [
                {
                    "name": "Elley Duhé",
                    "spotifyUri": "spotify:artist:67MNhiAICFY6Pwc2YxCO0K"
                }
            ],
            "labels": [
                {
                    "name": "Not Fit For Society/RCA Records"
                }
            ],
            "releaseDate": "2020-01-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 178,
            "previousRank": 159,
            "peakRank": 158,
            "appearancesOnChart": 10,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7383915",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-01",
            "entryRank": 194,
            "entryDate": "2022-11-17"
        },
        "trackMetadata": {
            "trackName": "Limbo",
            "trackUri": "spotify:track:37F7E7BKEw2E4O2L7u0IEp",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0269b381d574b329409bd806e6",
            "artists": [
                {
                    "name": "Freddie Dredd",
                    "spotifyUri": "spotify:artist:0dlDsD7y6ccmDm8tuWCU6F"
                }
            ],
            "labels": [
                {
                    "name": "Doomshop Records/RCA Records"
                }
            ],
            "releaseDate": "2022-08-11"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 179,
            "previousRank": 185,
            "peakRank": 40,
            "appearancesOnChart": 61,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7375962",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_UP",
            "peakDate": "2022-10-06",
            "entryRank": 191,
            "entryDate": "2021-09-02"
        },
        "trackMetadata": {
            "trackName": "Gangsta's Paradise",
            "trackUri": "spotify:track:1DIXPcTDzTj8ZMHt3PDt8p",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02c31d3c870a3dbaf7b53186cc",
            "artists": [
                {
                    "name": "Coolio",
                    "spotifyUri": "spotify:artist:3y24n3XhZ96wgwRXjvS17T"
                },
                {
                    "name": "L.V.",
                    "spotifyUri": "spotify:artist:2LhsePRtgCo4THVKULQBL7"
                }
            ],
            "labels": [
                {
                    "name": "Tommy Boy Music, LLC"
                }
            ],
            "releaseDate": "1995-11-07"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 180,
            "previousRank": 161,
            "peakRank": 2,
            "appearancesOnChart": 23,
            "consecutiveAppearancesOnChart": 23,
            "rankingMetric": {
                "value": "7323392",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-25",
            "entryRank": 2,
            "entryDate": "2022-08-25"
        },
        "trackMetadata": {
            "trackName": "Pink Venom",
            "trackUri": "spotify:track:5zwwW9Oq7ubSxoCGyW1nbY",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02002ef53878df1b4e91c15406",
            "artists": [
                {
                    "name": "BLACKPINK",
                    "spotifyUri": "spotify:artist:41MozSoPIsD1dJM0CLPjZF"
                }
            ],
            "labels": [
                {
                    "name": "YG Entertainment/Interscope Records"
                }
            ],
            "releaseDate": "2022-09-15"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 181,
            "previousRank": 164,
            "peakRank": 44,
            "appearancesOnChart": 107,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7313912",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-02-24",
            "entryRank": 171,
            "entryDate": "2017-01-05"
        },
        "trackMetadata": {
            "trackName": "Lose Yourself - From \"8 Mile\" Soundtrack",
            "trackUri": "spotify:track:1v7L65Lzy0j0vdpRjJewt1",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02eab40fc794b88b9d1e012578",
            "artists": [
                {
                    "name": "Eminem",
                    "spotifyUri": "spotify:artist:7dGJo4pcD2V6oG8kP0tJRR"
                }
            ],
            "labels": [
                {
                    "name": "Aftermath"
                }
            ],
            "releaseDate": "2005-12-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 182,
            "previousRank": -1,
            "peakRank": 72,
            "appearancesOnChart": 29,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7313262",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2022-07-14",
            "entryRank": 175,
            "entryDate": "2017-12-07"
        },
        "trackMetadata": {
            "trackName": "Don’t Blame Me",
            "trackUri": "spotify:track:1R0a2iXumgCiFb7HEZ7gUE",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02da5d5aeeabacacc1263c0f4b",
            "artists": [
                {
                    "name": "Taylor Swift",
                    "spotifyUri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
                }
            ],
            "labels": [
                {
                    "name": "Big Machine Records, LLC"
                }
            ],
            "releaseDate": "2017-11-10"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 183,
            "previousRank": -1,
            "peakRank": 120,
            "appearancesOnChart": 15,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7303494",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2022-10-20",
            "entryRank": 184,
            "entryDate": "2022-09-15"
        },
        "trackMetadata": {
            "trackName": "Somewhere Only We Know",
            "trackUri": "spotify:track:0ll8uFnc0nANY35E0Lfxvg",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02045d0a38105fbe7bde43c490",
            "artists": [
                {
                    "name": "Keane",
                    "spotifyUri": "spotify:artist:53A0W3U0s8diEn9RhXQhVz"
                }
            ],
            "labels": [
                {
                    "name": "Interscope"
                }
            ],
            "releaseDate": "2004-01-01"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 184,
            "previousRank": 163,
            "peakRank": 2,
            "appearancesOnChart": 79,
            "consecutiveAppearancesOnChart": 79,
            "rankingMetric": {
                "value": "7298057",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2021-08-19",
            "entryRank": 5,
            "entryDate": "2021-07-29"
        },
        "trackMetadata": {
            "trackName": "INDUSTRY BABY (feat. Jack Harlow)",
            "trackUri": "spotify:track:5Z9KJZvQzH6PFmb8SNkxuk",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02be82673b5f79d9658ec0a9fd",
            "artists": [
                {
                    "name": "Lil Nas X",
                    "spotifyUri": "spotify:artist:7jVv8c5Fj3E9VhNjxT4snq"
                },
                {
                    "name": "Jack Harlow",
                    "spotifyUri": "spotify:artist:2LIk90788K0zvyj2JJVwkJ"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2021-09-17"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 185,
            "previousRank": 120,
            "peakRank": 24,
            "appearancesOnChart": 7,
            "consecutiveAppearancesOnChart": 7,
            "rankingMetric": {
                "value": "7259794",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-15",
            "entryRank": 24,
            "entryDate": "2022-12-15"
        },
        "trackMetadata": {
            "trackName": "Blind",
            "trackUri": "spotify:track:2CSRrnOEELmhpq8iaAi9cd",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0270dbc9f47669d120ad874ec1",
            "artists": [
                {
                    "name": "SZA",
                    "spotifyUri": "spotify:artist:7tYKF4w9nC0nq9CsPZTHyP"
                }
            ],
            "labels": [
                {
                    "name": "Top Dawg Entertainment/RCA Records"
                }
            ],
            "releaseDate": "2022-12-09"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 186,
            "previousRank": 134,
            "peakRank": 94,
            "appearancesOnChart": 9,
            "consecutiveAppearancesOnChart": 9,
            "rankingMetric": {
                "value": "7259319",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-22",
            "entryRank": 145,
            "entryDate": "2022-12-01"
        },
        "trackMetadata": {
            "trackName": "Gatita",
            "trackUri": "spotify:track:4ilZV1WNjL7IxwE81OnaRY",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02070c919f062e9fbfc03ca16b",
            "artists": [
                {
                    "name": "Bellakath",
                    "spotifyUri": "spotify:artist:4yjm4SvYqC5FFuLbB6TyHr"
                }
            ],
            "labels": [
                {
                    "name": "La Mafia del Perreo"
                }
            ],
            "releaseDate": "2022-10-05"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 187,
            "previousRank": 140,
            "peakRank": 7,
            "appearancesOnChart": 271,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "7235417",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2017-01-12",
            "entryRank": 10,
            "entryDate": "2016-12-29"
        },
        "trackMetadata": {
            "trackName": "Say You Won't Let Go",
            "trackUri": "spotify:track:5uCax9HTNlzGybIStD3vDh",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0220beb61f61fcbeb33b10a9ab",
            "artists": [
                {
                    "name": "James Arthur",
                    "spotifyUri": "spotify:artist:4IWBUUAFIplrNtaOHcJPRM"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2016-10-28"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 188,
            "previousRank": 139,
            "peakRank": 139,
            "appearancesOnChart": 2,
            "consecutiveAppearancesOnChart": 2,
            "rankingMetric": {
                "value": "7216106",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-19",
            "entryRank": 139,
            "entryDate": "2023-01-19"
        },
        "trackMetadata": {
            "trackName": "Sie weiß (feat. Mero)",
            "trackUri": "spotify:track:7DyDjhZMEIK5Ied4juTCyc",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02e9a48bf583d23ef54caa967c",
            "artists": [
                {
                    "name": "AYLIVA",
                    "spotifyUri": "spotify:artist:2rEVnwCPBeGkWMv425KoG1"
                },
                {
                    "name": "MERO",
                    "spotifyUri": "spotify:artist:5wyWp867LWGjFmYZXVSFnZ"
                }
            ],
            "labels": [
                {
                    "name": "Whiteheart Records/WM Germany"
                }
            ],
            "releaseDate": "2023-01-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 189,
            "previousRank": 189,
            "peakRank": 1,
            "appearancesOnChart": 301,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7188533",
                "type": "STREAMS"
            },
            "entryStatus": "NO_CHANGE",
            "peakDate": "2017-01-12",
            "entryRank": 1,
            "entryDate": "2017-01-12"
        },
        "trackMetadata": {
            "trackName": "Shape of You",
            "trackUri": "spotify:track:7qiZfU4dY1lWllzX7mPBI3",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02ba5db46f4b838ef6027e6f96",
            "artists": [
                {
                    "name": "Ed Sheeran",
                    "spotifyUri": "spotify:artist:6eUKZXaKkcviH0Ku9w2n3V"
                }
            ],
            "labels": [
                {
                    "name": "Atlantic Records UK"
                }
            ],
            "releaseDate": "2017-03-03"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 190,
            "previousRank": 188,
            "peakRank": 82,
            "appearancesOnChart": 22,
            "consecutiveAppearancesOnChart": 3,
            "rankingMetric": {
                "value": "7149750",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-10-13",
            "entryRank": 188,
            "entryDate": "2017-09-14"
        },
        "trackMetadata": {
            "trackName": "I'm Not The Only One",
            "trackUri": "spotify:track:5QM0SsyzmBM0pbFY52Xj1X",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02b11bdc91cb9ac6b14f5c1dae",
            "artists": [
                {
                    "name": "Sam Smith",
                    "spotifyUri": "spotify:artist:2wY79sveU1sp5g7SokKOiI"
                }
            ],
            "labels": [
                {
                    "name": "Capitol"
                }
            ],
            "releaseDate": "2014-05-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 191,
            "previousRank": 180,
            "peakRank": 18,
            "appearancesOnChart": 70,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7098332",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-03-24",
            "entryRank": 150,
            "entryDate": "2021-09-09"
        },
        "trackMetadata": {
            "trackName": "Where Are You Now",
            "trackUri": "spotify:track:3uUuGVFu1V7jTQL60S1r8z",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e028d7a7f1855b04104ba59c18b",
            "artists": [
                {
                    "name": "Lost Frequencies",
                    "spotifyUri": "spotify:artist:7f5Zgnp2spUuuzKplmRkt7"
                },
                {
                    "name": "Calum Scott",
                    "spotifyUri": "spotify:artist:6ydoSd3N2mwgwBHtF6K7eX"
                }
            ],
            "labels": [
                {
                    "name": "Epic Amsterdam"
                }
            ],
            "releaseDate": "2021-07-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 192,
            "previousRank": 166,
            "peakRank": 99,
            "appearancesOnChart": 16,
            "consecutiveAppearancesOnChart": 16,
            "rankingMetric": {
                "value": "7098121",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2023-01-05",
            "entryRank": 145,
            "entryDate": "2022-10-13"
        },
        "trackMetadata": {
            "trackName": "Eu Gosto Assim - Ao Vivo",
            "trackUri": "spotify:track:4ASA1PZyWGbuc4d9N8OAcF",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0219bb2fb697a42c1084d71f6c",
            "artists": [
                {
                    "name": "Gustavo Mioto",
                    "spotifyUri": "spotify:artist:1X6ORK7IekgmyjV6IFPszP"
                },
                {
                    "name": "Mari Fernandez",
                    "spotifyUri": "spotify:artist:0BHm7qbh3ENxvXzkQAG7MP"
                }
            ],
            "labels": [
                {
                    "name": "Universal Music Ltda."
                }
            ],
            "releaseDate": "2022-09-16"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 193,
            "previousRank": -1,
            "peakRank": 108,
            "appearancesOnChart": 95,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7086722",
                "type": "STREAMS"
            },
            "entryStatus": "RE_ENTRY",
            "peakDate": "2021-03-18",
            "entryRank": 199,
            "entryDate": "2017-01-26"
        },
        "trackMetadata": {
            "trackName": "Take Me to Church",
            "trackUri": "spotify:track:3dYD57lRAUcMHufyqn9GcI",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e024ca68d59a4a29c856a4a39c2",
            "artists": [
                {
                    "name": "Hozier",
                    "spotifyUri": "spotify:artist:2FXC3k01G6Gw61bmprjgqS"
                }
            ],
            "labels": [
                {
                    "name": "Columbia"
                }
            ],
            "releaseDate": "2014-09-19"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 194,
            "previousRank": -1,
            "peakRank": 194,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7083105",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 194,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "Ch y la Pizza",
            "trackUri": "spotify:track:0UbesRsX2TtiCeamOIVEkp",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02cdbbe3160616f7c85e2eb2c8",
            "artists": [
                {
                    "name": "Fuerza Regida",
                    "spotifyUri": "spotify:artist:0ys2OFYzWYB5hRDLCsBqxt"
                },
                {
                    "name": "Natanael Cano",
                    "spotifyUri": "spotify:artist:0elWFr7TW8piilVRYJUe4P"
                }
            ],
            "labels": [
                {
                    "name": "Rancho Humilde/Street Mob Records"
                }
            ],
            "releaseDate": "2022-12-30"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 195,
            "previousRank": -1,
            "peakRank": 195,
            "appearancesOnChart": 1,
            "consecutiveAppearancesOnChart": 1,
            "rankingMetric": {
                "value": "7062018",
                "type": "STREAMS"
            },
            "entryStatus": "NEW_ENTRY",
            "peakDate": "2023-01-26",
            "entryRank": 195,
            "entryDate": "2023-01-26"
        },
        "trackMetadata": {
            "trackName": "Muñecas",
            "trackUri": "spotify:track:1PAvhqefivTNdxZ4u8RT1d",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0271e643229b72d00c82c7799a",
            "artists": [
                {
                    "name": "TINI",
                    "spotifyUri": "spotify:artist:7vXDAI8JwjW531ouMGbfcp"
                },
                {
                    "name": "La Joaqui",
                    "spotifyUri": "spotify:artist:60XHOAhvEBiV6BGBOv8ClM"
                },
                {
                    "name": "Steve Aoki",
                    "spotifyUri": "spotify:artist:77AiFEVeAVj2ORpC85QVJs"
                }
            ],
            "labels": [
                {
                    "name": "5020 Records"
                }
            ],
            "releaseDate": "2023-01-12"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 196,
            "previousRank": 167,
            "peakRank": 24,
            "appearancesOnChart": 8,
            "consecutiveAppearancesOnChart": 8,
            "rankingMetric": {
                "value": "7055949",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-12-08",
            "entryRank": 24,
            "entryDate": "2022-12-08"
        },
        "trackMetadata": {
            "trackName": "Niagara Falls (Foot or 2) [with Travis Scott & 21 Savage]",
            "trackUri": "spotify:track:4WuOWVnAqvEQxgSRrspBgt",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e0213e54d6687e65678d60466c2",
            "artists": [
                {
                    "name": "Metro Boomin",
                    "spotifyUri": "spotify:artist:0iEtIxbK0KxaSlF7G42ZOp"
                },
                {
                    "name": "Travis Scott",
                    "spotifyUri": "spotify:artist:0Y5tJX1MQlPlqiwlOH1tJY"
                },
                {
                    "name": "21 Savage",
                    "spotifyUri": "spotify:artist:1URnnhqYAYcrqrcwql10ft"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-12-02"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 197,
            "previousRank": 183,
            "peakRank": 14,
            "appearancesOnChart": 23,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "7052483",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-09-15",
            "entryRank": 16,
            "entryDate": "2022-08-18"
        },
        "trackMetadata": {
            "trackName": "Super Freaky Girl",
            "trackUri": "spotify:track:2yjlYDiNiQkdxVqTlaSrlX",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e02facb808b493713699283feca",
            "artists": [
                {
                    "name": "Nicki Minaj",
                    "spotifyUri": "spotify:artist:0hCNtLu0JehylgoiP8L4Gh"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2022-08-26"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 198,
            "previousRank": 195,
            "peakRank": 1,
            "appearancesOnChart": 218,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "6967133",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2019-01-10",
            "entryRank": 5,
            "entryDate": "2018-10-25"
        },
        "trackMetadata": {
            "trackName": "Sunflower - Spider-Man: Into the Spider-Verse",
            "trackUri": "spotify:track:0RiRZpuVRbi7oqRdSMwhQY",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e029478c87599550dd73bfa7e02",
            "artists": [
                {
                    "name": "Post Malone",
                    "spotifyUri": "spotify:artist:246dkjvS1zLTtiykXe5h60"
                },
                {
                    "name": "Swae Lee",
                    "spotifyUri": "spotify:artist:1zNqQNIdeOUZHb8zbZRFMX"
                }
            ],
            "labels": [
                {
                    "name": "Republic Records"
                }
            ],
            "releaseDate": "2019-09-06"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 199,
            "previousRank": 191,
            "peakRank": 15,
            "appearancesOnChart": 27,
            "consecutiveAppearancesOnChart": 27,
            "rankingMetric": {
                "value": "6962547",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-08-04",
            "entryRank": 16,
            "entryDate": "2022-07-28"
        },
        "trackMetadata": {
            "trackName": "Doja",
            "trackUri": "spotify:track:3LtpKP5abr2qqjunvjlX5i",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e023c7d945b6baf935e8a0ebdaa",
            "artists": [
                {
                    "name": "Central Cee",
                    "spotifyUri": "spotify:artist:5H4yInM5zmHqpKIoMNAx4r"
                }
            ],
            "labels": [
                {
                    "name": "Central Cee"
                }
            ],
            "releaseDate": "2022-07-21"
        }
    },
    {
        "chartEntryData": {
            "currentRank": 200,
            "previousRank": 173,
            "peakRank": 1,
            "appearancesOnChart": 34,
            "consecutiveAppearancesOnChart": 4,
            "rankingMetric": {
                "value": "6938508",
                "type": "STREAMS"
            },
            "entryStatus": "MOVED_DOWN",
            "peakDate": "2022-06-09",
            "entryRank": 4,
            "entryDate": "2022-06-02"
        },
        "trackMetadata": {
            "trackName": "Running Up That Hill (A Deal With God) - 2018 Remaster",
            "trackUri": "spotify:track:75FEaRjZTKLhTrFGsfMUXR",
            "displayImageUri": "https://i.scdn.co/image/ab67616d00001e025c390e413e27798edd4d18b4",
            "artists": [
                {
                    "name": "Kate Bush",
                    "spotifyUri": "spotify:artist:1aSxMhuvixZ8h9dK9jIDwL"
                }
            ],
            "labels": [
                {
                    "name": "Rhino"
                }
            ],
            "releaseDate": "1985-09-16"
        }
    }
]

result = json_filter(chartData)
save_to_json(result, "chart_data.json")