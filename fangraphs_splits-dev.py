import requests

cookies = {
    '_omappvp': 'IyFZ4xI9SGl3zsBh8B0STWK7ERpJuQ4wENBagQE6jPZg4kdkrsWPaut4yRTpoGhF6NrBMCsGdg05EVAHNkGQqH40QU9gfLTA',
    '_jsuid': '3879880429',
    '_cb': 'DeMY-VDu7wIYDpHI9v',
    'ezosuibasgeneris-1': 'baa41b10-5910-4a5a-66a0-f4ad3031b754',
    '_sharedid': '54ded4c5-1fea-4717-b7a8-84c97b72b5fa',
    'ezux_lpl_126045': '1676593160663|d9cabb61-50f7-4536-4f7b-244470e33fb5|false',
    '__qca': 'P0-1640035325-1676593319604',
    'cto_bundle': 'G1Ne1l9KQUxaWGNvWXNRNHQ0ekZyMjRKdnByM3NwTVhtbmxpcEFPd1RNaFRoVHVDWGo0RUpZVnF5SSUyQjZRZ2R0V2IydG91THM4Y3loJTJCc0tkYVk5JTJGbHhqbE1SU1ppMGR0bWh4WGFRcUFmeG5HTlFVOEElMkJGOEMlMkY5NWtqdXBZMVJFVUFjdU50U0NvWVJSOXpKODlmc3lvSUE3MHAyTHRtbDFXa0l4T1BrUXRnWkdHJTJCdWhQQVFuU2JqOFFVZGRMMGE0RCUyQmtoaA',
    'cto_bidid': '3j3dx19hZndoU2olMkJrSXZCWmlTVyUyRjVxQmdSQndKOXdBaTI3OUpER2sySUhTeElOTXBKOUlHUTBaTk5OSWtoUkJ0dEkzUTJxZkp3UGFCeE5yMndoa081JTJCcDBuVmlPYk5yQVhCSktZN3lJSmJCT2pYJTJGY09ydzJHYUtFUyUyQklEciUyRjV5U3RjUHJHM3Rrd0Zvb0ExZ2dQOSUyRlZ5YVFYUSUzRCUzRA',
    '_cc_id': 'fe3e75f2f0b06a6ad5ee8126f0eea30b',
    'wordpress_logged_in_0cae6f5cb929d209043cb97f8c2eee44': 'nvb5140%7C1708150356%7C3DGR61jsbsL8Q2MDVAyW31DAcL65VNJa4PzIWchszIw%7C93be2ceaebbbb96e955a7f5c243fec810fb37483f3b06f92d361bf8bb5a33717',
    '_ga': 'GA1.1.564289413.1676593150',
    '_chartbeat2': '.1637245781625.1681443141694.1001100000000001.Ba4tlZBajMcDD3DqllGrVMgCF45qs.1',
    '_cb_svref': 'null',
    '_chartbeat5': '665|194|%2F|https%3A%2F%2Fwww.fangraphs.com%2Fleaders%2Fsplits-leaderboards|5TpZsDtz051DZeVU8DdGw4S62Oug||c|BGTuU8E8kDUCwAivODZU1JGCO53us|fangraphs.com|',
    '_chartbeat4': 't=C_M4x6DYdejugGbPkDEd3GaC7pOBR&E=18&x=53&c=0.31&y=7958&w=576',
    '_ga_757YGY2LKP': 'GS1.1.1681439898.51.1.1681443162.0.0.0',
}

headers = {
    'authority': 'www.fangraphs.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_omappvp=IyFZ4xI9SGl3zsBh8B0STWK7ERpJuQ4wENBagQE6jPZg4kdkrsWPaut4yRTpoGhF6NrBMCsGdg05EVAHNkGQqH40QU9gfLTA; _jsuid=3879880429; _cb=DeMY-VDu7wIYDpHI9v; ezosuibasgeneris-1=baa41b10-5910-4a5a-66a0-f4ad3031b754; _sharedid=54ded4c5-1fea-4717-b7a8-84c97b72b5fa; ezux_lpl_126045=1676593160663|d9cabb61-50f7-4536-4f7b-244470e33fb5|false; __qca=P0-1640035325-1676593319604; cto_bundle=G1Ne1l9KQUxaWGNvWXNRNHQ0ekZyMjRKdnByM3NwTVhtbmxpcEFPd1RNaFRoVHVDWGo0RUpZVnF5SSUyQjZRZ2R0V2IydG91THM4Y3loJTJCc0tkYVk5JTJGbHhqbE1SU1ppMGR0bWh4WGFRcUFmeG5HTlFVOEElMkJGOEMlMkY5NWtqdXBZMVJFVUFjdU50U0NvWVJSOXpKODlmc3lvSUE3MHAyTHRtbDFXa0l4T1BrUXRnWkdHJTJCdWhQQVFuU2JqOFFVZGRMMGE0RCUyQmtoaA; cto_bidid=3j3dx19hZndoU2olMkJrSXZCWmlTVyUyRjVxQmdSQndKOXdBaTI3OUpER2sySUhTeElOTXBKOUlHUTBaTk5OSWtoUkJ0dEkzUTJxZkp3UGFCeE5yMndoa081JTJCcDBuVmlPYk5yQVhCSktZN3lJSmJCT2pYJTJGY09ydzJHYUtFUyUyQklEciUyRjV5U3RjUHJHM3Rrd0Zvb0ExZ2dQOSUyRlZ5YVFYUSUzRCUzRA; _cc_id=fe3e75f2f0b06a6ad5ee8126f0eea30b; wordpress_logged_in_0cae6f5cb929d209043cb97f8c2eee44=nvb5140%7C1708150356%7C3DGR61jsbsL8Q2MDVAyW31DAcL65VNJa4PzIWchszIw%7C93be2ceaebbbb96e955a7f5c243fec810fb37483f3b06f92d361bf8bb5a33717; _ga=GA1.1.564289413.1676593150; _chartbeat2=.1637245781625.1681443141694.1001100000000001.Ba4tlZBajMcDD3DqllGrVMgCF45qs.1; _cb_svref=null; _chartbeat5=665|194|%2F|https%3A%2F%2Fwww.fangraphs.com%2Fleaders%2Fsplits-leaderboards|5TpZsDtz051DZeVU8DdGw4S62Oug||c|BGTuU8E8kDUCwAivODZU1JGCO53us|fangraphs.com|; _chartbeat4=t=C_M4x6DYdejugGbPkDEd3GaC7pOBR&E=18&x=53&c=0.31&y=7958&w=576; _ga_757YGY2LKP=GS1.1.1681439898.51.1.1681443162.0.0.0',
    'origin': 'https://www.fangraphs.com',
    'referer': 'https://www.fangraphs.com/leaders/splits-leaderboards', #'https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=1&startDate=2022-04-01&endDate=2022-04-30&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&sort=22,1',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

json_data = {
    'strPlayerId': 'all',
    'strSplitArr': [],
    'strGroup': 'season',
    'strPosition': 'B',
    'strType': 2, # 1 : standard, 2 : advanced, 3 : batted_balls
    'strStartDate': '2022-04-01',
    'strEndDate': '2022-04-30',
    'strSplitTeams': False,
    'dctFilters': [],
    'strStatType': 'player',
    'strAutoPt': 'false',  # 'true' 'false'
    'arrPlayerId': [],
    'strSplitArrPitch': [],
    'arrWxTemperature': None,
    'arrWxPressure': None,
    'arrWxAirDensity': None,
    'arrWxElevation': None,
    'arrWxWindSpeed': None,
}

response = requests.post(
    'https://www.fangraphs.com/api/leaders/splits/splits-leaders',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"strPlayerId":"all","strSplitArr":[],"strGroup":"season","strPosition":"B","strType":1,"strStartDate":"2022-04-01","strEndDate":"2022-04-30","strSplitTeams":false,"dctFilters":[],"strStatType":"player","strAutoPt":"true","arrPlayerId":[],"strSplitArrPitch":[],"arrWxTemperature":null,"arrWxPressure":null,"arrWxAirDensity":null,"arrWxElevation":null,"arrWxWindSpeed":null}'
# response = requests.post(
#     'https://www.fangraphs.com/api/leaders/splits/splits-leaders',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )



res = response.json()
