import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = working_directory
    working_directory_absolute = os.path.abspath(working_directory)
    directory_absolute = os.path.abspath(directory)
    if directory_absolute.startswith(working_directory_absolute) == False:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        if not os.path.isdir(directory):
            return(f'Error: "{directory}" is not a directory')
        try:
            directory_contents = os.listdir(directory)
        except:
            return(f'Error: "{directory}" is not currently accessible')
        directory_files_list = []
        for content in directory_contents:
            full_path = os.path.join(directory, content)
            try:
                content_size = os.path.getsize(full_path)
            except:
                return(f'Error: "{full_path}" is not currently accessible')
            try:
                content_is_directory = os.path.isdir(full_path)
            except:
                return(f'Error: "{full_path}" is not currently accessible')
            content_output = f"- {content}: file_size={content_size} bytes, is_dir={content_is_directory}"
            directory_files_list.append(content_output)
        return "\n".join(directory_files_list)

        
