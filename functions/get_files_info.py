import os

def get_files_info(working_directory, directory='.'):
    try:
        full_path = os.path.join(working_directory, directory)

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        abs_path = os.path.abspath(full_path)
        abs_path_working = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_path_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        files_info_parts = []
        with os.scandir(full_path) as entries:
            for entry in entries:
                files_info_parts.append('- ')
                files_info_parts.append(entry.name)
                files_info_parts.append(': file_size=')
                files_info_parts.append(str(entry.stat().st_size))
                files_info_parts.append(' bytes, is_dir=')
                files_info_parts.append(str(entry.is_dir()))
                files_info_parts.append('\n')

        return "".join(files_info_parts)
    except Exception as e:
        return "Error: " + str(e)