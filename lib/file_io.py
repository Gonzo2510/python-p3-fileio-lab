def write_file(file_name, file_content = 'This is a test content.'):
    with open(f'{file_name}.txt', mode='w') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content='Appended content.'):
    with open(f'{file_name}.txt', mode='a') as log_file:
        log_file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as file:
        content = file.read()
        return content
