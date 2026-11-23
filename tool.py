from typing import Any

def get_crc32(data: bytes | bytearray) -> list[int | Any]:
    """
    计算字节数据的 CRC32 校验值（兼容 bytes/bytearray 输入）

    参数:
        data: 输入的字节数据（bytes 或 bytearray）

    返回:
        4 字节的数组（例如 [0x12, 0x34, 0x56, 0x78]）
    """
    # 生成 CRC32 查询表（预计算以提高性能）
    crc32_table = []
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
        crc32_table.append(crc)

    # 计算 CRC32
    crc = 0xFFFFFFFF
    for byte in data:
        crc = (crc >> 8) ^ crc32_table[(crc & 0xFF) ^ byte]

    crc ^= 0xFFFFFFFF
    crc &= 0xFFFFFFFF  # 确保为 32 位无符号整数

    # 将 CRC32 拆分为 4 字节的数组（大端序）
    return list([
        (crc >> 24) & 0xFF,  # 高位字节
        (crc >> 16) & 0xFF,
        (crc >> 8) & 0xFF,
        crc & 0xFF  # 低位字节
    ])

def int2bool(num, bit_length=8):
    """
    返回高位在前的布尔数组（可指定固定位数）
    """
    return [(num >> i) & 1 for i in reversed(range(bit_length))]


def bool2int(bool_array):
    """
    将布尔数组还原为整数（高位在前）

    参数:
        bool_array: 布尔值列表（如 [True, True, False, True]）

    返回:
        还原后的整数
    """
    result = 0
    bit_length = len(bool_array)
    for i, bit in enumerate(bool_array):
        if bit:
            result += (1 << (bit_length - 1 - i))  # 从高位计算权重
    return result

def int_to_hex_bytes(num):
    # 转换为 4 字节的大端序字节串，再转为列表
    byte_list = list(num.to_bytes(4, byteorder='big', signed=False))
    return byte_list

def hex_bytes_to_int(byte_list):
    a, b, c, d = byte_list  # 解包 4 个字节
    # 按大端序组合（a 是最高字节，d 是最低字节）
    num = (a << 24) | (b << 16) | (c << 8) | d
    return num