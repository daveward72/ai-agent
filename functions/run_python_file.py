import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)

        abs_path = os.path.abspath(full_path)
        abs_path_working = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_path_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        cmd_args = ["python3", file_path] + args
        completed_process = subprocess.run(cmd_args, timeout=30, capture_output=True, cwd=working_directory, text=True)

        retval = ""
        if completed_process.stdout:
            retval += f"STDOUT: {completed_process.stdout}\n"

        if completed_process.stderr:
            retval += f"STDERR: {completed_process.stderr}\n"

        if not completed_process.stdout and not completed_process.stderr:
            retval += "No output produced."

        return retval
    except Exception as e:
        return f"Error: executing Python file: {e}"