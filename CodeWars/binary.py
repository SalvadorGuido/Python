# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))
#
# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range[17]))
#
# with open('binary', 'br') as bin_file1:
#     for b in bin_file1:
#         print(b)


a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
d = 2998302 # 00 2D C0 1E

with open('binary2', 'bw') as bf:
    bf.write(a.to_bytes(2, 'big'))
    bf.write(b.to_bytes(2, 'big'))
    bf.write(c.to_bytes(4, 'big'))
    bf.write(d.to_bytes(4, 'big'))
    bf.write(d.to_bytes(4, 'little'))

with open('binary2', 'br') as bf1:
    for b in bf1:
        print(b)