import os
from google.genai import types

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
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the string content from a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='The path to the file, relative to the working directory.'   
            )
        }
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='The path to the Python file, relative to the working directory.'   
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description='Optional array of command line arguments for the Python program.',
                items=types.Schema(
                    type=types.Type.STRING,
                    description='A single string command line argument.'
                )
            )
        }
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='The file path to write.'   
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description='The string content to write to the file.',
            )
        }
    )
)