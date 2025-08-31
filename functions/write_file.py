import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    abs_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)

    if not abs_path.startswith(abs_path_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dir_path = os.path.dirname(full_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(full_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'