import os


files = ['cookbook.txt', 'cookbook_new.txt']  


def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)


sorted_files = sorted(files, key=count_lines)


result_file = 'result.txt'


with open(result_file, 'w') as result:
    for file in sorted_files:
        with open(file, 'r') as f:
            result.write(f"{file}\n")
            result.write(f"{count_lines(file)}\n")
            result.write(f.read())
            result.write("\n")

print(f"Файлы объединены в {result_file}")