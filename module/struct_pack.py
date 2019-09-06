import struct

# Define a format string understandable to the struct module, which tells the
# module how the data in one of your records is packed
record_format = 'hd4s'

# struct module provides the ability to take Python values and convert them to
# packed byte sequences through the struct.pack function.
output = struct.pack(record_format, 7, 3.14, b'gbye')
print(output)
out = open('../data/myfile7.txt', 'wb')
out.write(output)
out.close()
