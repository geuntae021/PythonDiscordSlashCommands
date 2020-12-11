import discord
import aiohttp

client = discord.Client()


@client.event
async def on_ready():
    print("Ready!\n=======")


@client.event
async def on_socket_response(msg):
    if not msg["t"] == "INTERACTION_CREATE":
        return
    print(msg)
    data = msg['d']
    requested = f"https://discord.com/api/v8/interactions/{data['id']}/{data['token']}/callback"

    if data["data"]["name"] == "test":
        response = {
            "type": 5,
            "data": {
                "content": "Test"
            }
        }
    else:
        return
    async with aiohttp.ClientSession() as session:
        async with session.post(requested, json=response) as resp:
            print(resp.status)
            print(await resp.text())


client.run('') # 토큰을 넣어주세요.