import os
import config

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)

        abs_path = os.path.abspath(full_path)
        abs_path_working = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_path_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)

        return file_content_string
    except Exception as e:
        return "Error: " + str(e)