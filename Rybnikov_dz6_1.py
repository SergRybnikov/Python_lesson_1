
with open('nginx_logs.txt', encoding='utf-8') as log_file:
    data_list = []
    for line in log_file:
        item = line.split()
        data_list.append((item[0], item[5].strip('"'), item[6]))
print(*data_list, sep='\n')