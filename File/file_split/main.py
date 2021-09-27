
import mmap
from pathlib import Path
import time


newfile = "test_{}.txt"
file_path = "The_Great_Qin_Empire.txt"
# file_path = "test_1.txt"


file = Path(file_path)


# 文件绝对路径
print(file.absolute())
# 文件当前路径
print(file.cwd())


# 文件状态
print(file.stat())

# 文件大小
print(file.stat().st_size/1024/1024)

split_size = 1024 * 1024 * 1024 * 6.5

# 拆多少份
split_cnt = file.stat().st_size // split_size + 1

start_order = 1


# 上次访问的时间
struct_time = time.localtime(file.stat().st_atime)
format_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(format_time)

# 最后一次修改的时间Î
struct_time = time.localtime(file.stat().st_mtime)
format_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(format_time)

# 最新的元数据更改的时间
struct_time = time.localtime(file.stat().st_ctime)
format_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(format_time)


def file_write(file, line):
    with open(file, "a", encoding="utf-8") as f:
        f.write(line)


def write_file(point=0, split_file=newfile.format(start_order)):
    with open(file_path, mode="r", encoding="utf-8") as rf:
        rf.seek(point)
        global start_order
        with open(split_file, mode="w", encoding="utf-8") as wf:
            while Path(split_file).stat().st_size < 1024*1024:
                line = rf.readline()
                if not line:
                    return None
                wf.write(line)
        point = rf.tell()

    print(f"拆完第{start_order}个文件")
    start_order += 1
    
    new_split_file = newfile.format(start_order)
    return write_file(point, new_split_file)


splitfile = newfile.format(start_order)

print(splitfile)


write_file(0, splitfile)
# print(tell)
