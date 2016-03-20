import base64
import commands

data = raw_input()

for i in range(16) :
    data = base64.b64decode(data)

print data
