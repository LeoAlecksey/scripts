
f = open(r'./object.txt', 'r')
st = f.read()
st = st = st.split('\n')

st1 = str(st[0])
st2 = str(st[1])

st1 = st1.split('=')
st2 = st2.split('=')

ob1 = str(st1[0])
adress1 = str(st1[1])

ob2 = str(st2[0])
adress2 = str(st2[1])


f.close()