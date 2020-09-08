import time
from FileRecursion import FileExtractor

"""
TEST #1: GETS FILES FROM test_directory
"""
print("-----------------------------------------------")
print("Test #1: RETRIEVE ALL .c FILES INSIDE test_directory")
path_root = "test_directory"
file_extractor = FileExtractor()
files = file_extractor.extractFiles(path_root)
print(files)
print("-----------------------------------------------")

"""
TEST #2: GETS EMPTY LIST OF FILES FROM test_empty_directory
"""
print("TEST #2: GETS EMPTY LIST OF FILES FROM test_empty_directory")
path_root = "test_empty_directory"
file_extractor = FileExtractor()
files = file_extractor.extractFiles(path_root)
print(files)
print("-----------------------------------------------")

"""
TEST #3: GETS 'my_file.c' FROM test_recursive_directory
"""
print("TEST #3: GETS 'my_file.c' FROM test_recursive_directory")
path_root = "test_recursive_directory"
file_extractor = FileExtractor()
files = file_extractor.extractFiles(path_root)
print(files)
print("-----------------------------------------------")

"""
TEST #4: GETS EMPTY LIST OF FILES FROM test_onefile_directory
"""
print("TEST #4: GETS EMPTY LIST FROM test_onefile_directory")
path_root = "test_onefile_directory"
file_extractor = FileExtractor()
files = file_extractor.extractFiles(path_root)
print(files)