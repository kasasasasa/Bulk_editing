import os
import shutil

# 指定要操作的文件夹路径
folder_path = r'D:\数据集\herb_medicine_images_95_categories\抽样\抽样（木桌版）\桑葚（木桌版）'

# 获取文件夹中所有的文件
files = os.listdir(folder_path)

# 筛选出图片文件
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# 按照文件名进行排序
image_files.sort()

# 设置新的命名前缀
prefix = "sangshen_"

# 从 1 开始为图片重新命名
for index, image_file in enumerate(image_files, start=51):
    old_path = os.path.join(folder_path, image_file)
    _, extension = os.path.splitext(image_file)
    new_name = f"{prefix}{index}{extension}"
    new_path = os.path.join(folder_path, new_name)
    shutil.move(old_path, new_path)
    print(f"已将 {image_file} 重命名为 {new_name}")

print("所有图片重命名完成！")