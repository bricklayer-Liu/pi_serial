import serial
import time

if __name__ == '__main__':

    ser = serial.Serial("/dev/ttyS0", 115200)
    ser.flushInput()  # 清空缓冲区域
    ser.write("begin".encode("utf-8"))  # 位置3

    while True:
        count = ser.inWaiting()  # 得到当前未接收的数据有多少个
        if count != 0:
            recv = ser.read(count)  # 将这么多数据全部读取出来
            ser.write("Recv some data is : ".encode("utf-8"))  # 回显接收的数据
            ser.write(recv)  # 位置7
            ser.flushInput()
        time.sleep(0.1)

