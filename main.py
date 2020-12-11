import requests


token = "" # 봇의 토큰을 넣어주세요.
id = 000 #앱의 ID를 넣어주세요


url = f"https://discord.com/api/v8/applications/{id}/commands"

json = {
    "name": "test",
    "description": "Just Test"
}

# For authorization, you can use either your bot token 
headers = {
    "Authorization": f"Bot {token}"
}

# or a client credentials token for your app
# headers = {
#     "Authorization": "Bearer 5mQHn5wDne1-NRY3CcCi2oMBw5MvwAPz"
# }

r = requests.post(url, headers=headers, json=json)
print(r.content)
