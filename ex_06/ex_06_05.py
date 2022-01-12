data = 'X-DSPAM-Confidence: 0.8475'
cpos = data.find(':')
#print(cpos)
piece = data[cpos+2:]
#print(piece)
value = float(piece)
print(value)
