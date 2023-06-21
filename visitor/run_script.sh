#!/bin/bash

log_file="/root/seuVisitor/log.txt"

# 检查日志文件是否存在，不存在则创建
if [ ! -f "$log_file" ]; then
    touch "$log_file"
fi

# 运行Python脚本并获取输出
output=$(python3 /root/seuVisitor/auto_linux.py)

# 获取当前日期
current_date=$(date +"%Y-%m-%d")

# 判断输出中是否包含"Successfully"
if [[ $output == *"Successfully"* ]]; then
    # 记录成功日志
    echo "${current_date} Successful" >> "$log_file"
else
    # 记录失败日志
    echo "${current_date} Error" >> "$log_file"
fi
