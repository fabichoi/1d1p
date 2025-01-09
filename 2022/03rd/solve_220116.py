# BOJ 1076
color_value = {
    'black': ['0', ''],
    'brown': ['1', '0'],
    'red': ['2', '00'],
    'orange': ['3', '000'],
    'yellow': ['4', '0000'],
    'green': ['5', '00000'],
    'blue': ['6', '000000'],
    'violet': ['7', '0000000'],
    'grey': ['8', '00000000'],
    'white': ['9', '000000000']
}

r1, r2, r3 = [color_value.get(input()) for _ in range(3)]
res = r1[0] + r2[0] + r3[1]
res = res if res[0] != '0' else res[1:]
print(res if res.count('0') != len(res) else '0')