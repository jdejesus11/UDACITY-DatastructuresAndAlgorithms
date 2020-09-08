import os.path 

class FileExtractor(object):
    def __init__(self):
        self.pattern = ".c"
    
    def extractFiles(self,path_root = None):
        result = []
        result = self._extractFiles(path_root)
        return result
            
    def _extractFiles(self, path): 
        result = []
        current_content = os.listdir(path)
        for content in current_content:
            content_path = self._get_current_path(path,content)
            is_file = os.path.isfile(content_path)
            if (is_file):
                if (self._file_checked_pattern(content)):
                    result.append(content)
            
            is_directory = os.path.isdir(content_path)
            if (is_directory):
                result = result + self._extractFiles(content_path)

        return result
    
    def _get_current_path(self,path,content):
        result = ""
        if (path is None):
            result = content
        else:
            result = path + "/" + content
        return result
    
    def _file_checked_pattern(self,file_name):
        size = len(file_name)
        return file_name[size-2:] == self.pattern



