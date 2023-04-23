def crc16(data):
    data = data.encode('utf-8')
    crc = 0xFFFF
    for i in range(len(data)):
        crc = crc ^ (data[i] << 8)
        for j in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
        crc = crc & 0xFFFF
    return crc
