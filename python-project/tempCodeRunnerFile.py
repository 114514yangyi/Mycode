response=opener.open(request)

content=response.read().decode('utf-8')

print(content)
