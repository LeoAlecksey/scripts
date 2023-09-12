
f = open(r'./secure.txt', 'r')
st = f.read()
st = st = st.split('=')

login = str(st[0])
password = str(st[1])


f.close()