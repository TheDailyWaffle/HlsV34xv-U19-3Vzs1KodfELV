import requests
response = requests.get('https://youkosoapi.rin.one/getPaste?id=Xdw6AWE0')
print(response.text)
file = open("output.txt", "w")
file.write(response.text)
file.close()
