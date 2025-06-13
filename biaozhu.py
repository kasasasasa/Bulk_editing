import os


def replace_zero_with_filename(directory):
    """
    遍历指定目录中的所有txt文件，将每行开头的0替换为文件名（不带扩展名）
    """
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 只处理txt文件
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # 获取文件名（不带扩展名）
                base_name = os.path.splitext(filename)[0]

                # 替换每行开头的0为文件名
                updated_lines = []
                for line in lines:
                    # 检查行是否以"0 "开头
                    if line.startswith("0 "):
                        # 替换开头的"0 "为文件名和空格
                        updated_line = f"{base_name} {line[2:]}"
                        updated_lines.append(updated_line)
                    else:
                        # 保留原行
                        updated_lines.append(line)

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(updated_lines)

                print(f"已处理文件: {filename}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")


if __name__ == "__main__":
    # 指定要处理的目录
    target_directory = input("请输入要处理的目录路径: ")

    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        replace_zero_with_filename(target_directory)
        print("所有文件处理完成!")
    else:
        print("指定的路径不存在或不是一个目录!")