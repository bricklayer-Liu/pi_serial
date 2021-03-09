import struct


def to_bytes(data):
    hex_byte = b''
    for i in data:
        hex_byte += struct.pack('B', i)
    return hex_byte


def send_data(ser, data):
    print(str(type(data)))
    if type(data) == list:
        ser.write(to_bytes(data))
    elif type(data) == str:
        ser.write(data.encode("gbk"))


def read_data(ser, stop):
    data_hex = ser.read_until(to_bytes(stop)).hex()
    hex_list = []
    for i in range(0, len(data_hex), 2):
        print(i)
        hex_list.append(int(data_hex[i: i + 2], 16))
    return hex_list


def read_str(ser):
    return ser.read_until().decode("gbk")
