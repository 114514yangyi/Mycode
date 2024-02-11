
# Python script to rename multiple files in a directory
import os
import sys
import json

def desparate(filename:str):
    index=filename.find(".")
    rest=filename[index:]
    first=filename[0:index]
    return (first,rest)


if __name__ == '__main__' :
    arguments=sys.argv
    if len(arguments)==2:
        director_path=arguments[1]
        index=0
        
        for filename in os.listdir(director_path):
            index+=1
            separate_file=desparate(filename)
            print(f"{filename}->{index}{separate_file[1]}")
            os.rename(os.path.join(director_path,filename),os.path.join(director_path,f"{index}{separate_file[1]}"))
        print(f"已经修改了{index}个文件！")
            
    elif len(arguments)==3:
        director_path=arguments[1]
        configure=arguments[2]
        index=0
        with  open(f"{configure}","r") as fp:
            conf_name=json.load(fp)
        for filename in zip(os.listdir(director_path),conf_name):
            index+=1
            separate_file=desparate(filename[0])
            os.rename(os.path.join(director_path,filename[0]),os.path.join(director_path,f"{filename[1]}{separate_file[1]}"))
        print(f"已经修改了{index}个文件！")
    else:
        print("错误的参数数量")
        print("用法: rn 目录路径 [配置文件]")
        print("参数说明:")
        print("  目录路径: 要重命名文件的目录路径")
        print("  配置文件: 可选参数，包含新文件名的配置文件路径")