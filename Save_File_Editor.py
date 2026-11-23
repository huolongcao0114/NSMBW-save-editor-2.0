from tool import *
import yaml
import os
import shutil

class SaveFileEditor:
    def __init__(self, conf_path = "wii.yaml"):
        self.config = None
        with open(conf_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)  # safe_load 避免代码执行风险
        self.file_path = None
        self.file_data = None
        self.data = None
        self.save_index = 0
        self.save_data = None
        self.backups = 1

    def filedata2data(self):
        segment_name = self.config["segment_name"]
        segment_len = self.config["segment_len"]
        segment_crc = self.config["segment_crc"]
        data = {}
        current_pos = 0
        for seg_name, seg_len, seg_crc in zip(segment_name, segment_len, segment_crc):
            data[seg_name] = {
                "data": self.file_data[current_pos: current_pos + seg_len],
                "crc": self.file_data[current_pos + seg_len: current_pos + seg_len + seg_crc],
            }
            current_pos += seg_len + seg_crc  # 更新位置
        if sum(segment_len) + sum(segment_crc) != len(self.file_data):
            raise Exception("不是存档文件")
        self.data = data
        return self.data

    def data2filedata(self):
        segment_name = self.config["segment_name"]
        segment_len = self.config["segment_len"]
        segment_crc = self.config["segment_crc"]
        file_data = []
        for seg_name, seg_len, seg_crc in zip(segment_name, segment_len, segment_crc):
            file_data.extend(self.data[seg_name]["data"])
            if seg_crc > 0:
                self.data[seg_name]["crc"] = get_crc32(self.data[seg_name]["data"])
                file_data.extend(self.data[seg_name]["crc"])
        if len(self.file_data) != sum(segment_len) + sum(segment_crc):
            raise Exception("产生存档文件出错")
        self.file_data = file_data
        return self.file_data

    def load_file(self, file_path):
        self.file_path = file_path
        with open(file_path, 'rb') as f:
            binary_data = f.read()
        self.file_data = list(binary_data)
        segment_len = self.config["segment_len"]
        segment_crc = self.config["segment_crc"]
        if len(self.file_data) != sum(segment_len) + sum(segment_crc):
            raise Exception("不是存档文件")
        self.filedata2data()
        return self.data

    def set_save_index(self, index = 0):
        sl = self.config["save_list"]
        qsl = self.config["quick_save_list"]
        segment_name = self.config["segment_name"]
        if index in sl:
            self.save_index = index
            self.save_data = self.data[segment_name[index]]["data"].copy()
        elif index in qsl:
            ls = self.config["save_data"]["stars"]
            ii = None
            for i in range(0, len(qsl)):
                if qsl[i] == index:
                    ii = i
                    break
            self.save_index = index
            self.save_data = self.data[segment_name[index]]["data"].copy()
            self.save_data[ls] = self.data[segment_name[sl[ii]]]["data"][ls]
        else:
            raise Exception("存档索引错误")

    def update_data(self, index = None):
        if index is None:
            index = self.save_index
        sl = self.config["save_list"]
        qsl = self.config["quick_save_list"]
        segment_name = self.config["segment_name"]
        if index in sl:
            self.data[segment_name[index]]["data"] = self.save_data
        elif index in qsl:
            ls = self.config["save_data"]["stars"]
            self.save_index = index
            self.data[segment_name[index]]["data"] = self.save_data
            self.data[segment_name[index]]["data"][ls] = 0
        else:
            raise Exception("存档索引错误")


    #修改self.save里的数据
    def get_val(self, pos):
        segment_len = self.config["segment_len"]
        if pos >= segment_len[self.save_index] or pos < 0:
            raise Exception("引用数组越界")
        return self.save_data[pos]

    def set_value(self, val, pos):
        segment_len = self.config["segment_len"]
        if pos >= segment_len[self.save_index] or pos < 0:
            raise Exception("引用数组越界")
        if val > 255 or val < 0:
            raise Exception("修改参数非法")
        self.save_data[pos] = int(val)

    def save_file(self, file_path = None):
        if file_path is None:
            file_path = self.file_path
        #确保目录存在
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if self.backups:
            backup_path = self.file_path + ".bak"
            shutil.copy2(file_path, backup_path)  # 保留元数据
        self.data2filedata()
        try:
            with open(file_path, "wb") as f:
                f.write(bytes(self.file_data))  # 直接转换
        except ValueError as e:
            print("错误：数组包含无效值（必须是 0-255 的整数）", str(e))
        except Exception as e:
            print("写入文件时出错:", str(e))


