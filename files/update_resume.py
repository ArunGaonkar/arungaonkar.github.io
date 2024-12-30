"""
Run this script to update the resume on the GitHub repository.
This script copies the latest resume file to the local repository, 
commits the changes, and pushes the changes to the remote repository.
"""

import os
import shutil
import subprocess
from datetime import date

def is_file_modified(repo_resume_path):
    try:
        repo_path = os.path.dirname(repo_resume_path)
        os.chdir(repo_path)

        # Check if the file has been modified
        command = ["git", "status", "--porcelain", os.path.basename(repo_resume_path)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()

        return True
        # return len(output) > 0

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

# def commit_and_push_file(repository_path, file_relative_path, commit_message):
def commit_and_push_file(repository_path, repo_resume_path, resume_file_path, commit_message):

    try:
        os.chdir(repository_path)

        shutil.copyfile(resume_file_path, repo_resume_path)

        if not is_file_modified(repo_resume_path):
            print(f"{repo_resume_path} has not been modified. No commit needed.")
            return
        
        subprocess.run(["git", "add", repo_resume_path])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", "origin", "master"])

        # print(f"{repo_resume_path} updated and pushed to GitHub successfully!")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    local_repository_path = "C:/Arun/arungaonkar.github.io"
    local_repo_resume_path = "C:/Arun/arungaonkar.github.io/files/Resume_Arun_Gaonkar.pdf"
    resume_file_path = "C:/Users/Arun/Desktop/resume/Resume_Arun_Gaonkar.pdf"
    commit_message = "resume updated on "+str(date.today())


    # Call the function to copy the file, commit, and push
    commit_and_push_file(local_repository_path, local_repo_resume_path, resume_file_path, commit_message)
