import os

path = "task8\\text.txt"
if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
    os.remove(path)