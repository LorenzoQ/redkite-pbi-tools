import os
from git import Repo

def check_file_modified(filepath):
    """Checks whether the given file was modified in the most recent commit. Only works if the file is within a git repo.

    :param filepath: path to the file being examined
    :return: a boolean indicating whether the file was modified in the most recent commit
    """
    print("entry line")
    print("printing filepath")
    print(filepath)
    repo = Repo(filepath, search_parent_directories=True).git #changed line +.git
   
    print("printing repo\n")
    print(repo)
    
    diff = repo.head.commit.diff('HEAD~1')
    print("diff")
    print(diff)
          
    filepath_end = filepath.replace('\\', '/').split('pbi/')[-1]
    print("filepath_end")
    print(filepath_end)
    return any(f.b_path.split('pbi/')[-1] == filepath_end and f.change_type in ['A', 'M', 'R'] for f in diff)

def open_branches():
    """Returns a list of open git branches. Only works if the current working directory is within a git repo.
    
    :return: an array of branch names
    """

    return [b.remote_head for b in Repo(os.path.abspath(__file__), search_parent_directories=True).remotes.origin.refs]
