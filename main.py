import requests


token = "" # 봇의 토큰을 넣어주세요.
id = 000 #앱의 ID를 넣어주세요


url = f"https://discord.com/api/v8/applications/{id}/commands"

json = {
    "name": "test",
    "description": "Just Test"
}


headers = {
    "Authorization": f"Bot {token}"
}

r = requests.post(url, headers=headers, json=json)
print(r.content)
