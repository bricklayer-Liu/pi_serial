#树莓派串口

###打开serial0端口
用命令ls -l /dev查看serial0是否已打开，如果没打开需要打开。

执行sudo raspi-config命令

选择Interfacing Options

选择serial，再选择【否】，禁用串口登录功能，将串口用于通信。再选择【是】，启动串口硬件。

再次使用命令ls -l /dev查看serial0是否已打开
