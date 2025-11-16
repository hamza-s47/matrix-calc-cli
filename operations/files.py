# import os
import numpy as np
from utils.tools import help_msg

class FileSystem:
    # Load .npy file
    def load_npy(self, file):
        try:
            data = np.load(file, allow_pickle=True)
            return data
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error while loading '{file}': {e} \n{help_msg('loadNpy')}"
    
    # Save .npy file
    def save_npy(self, file, arr):
        try:
            # os.makedirs("./outputs", exist_ok=True)
            np.save(f"{file}", arr)
            return f"File saved successfully as '{file}'"
        except Exception as e:
            return f"Error while saving file: {e} \n{help_msg('saveNpy')}"

    # Load .txt file
    def load_txt(self, file, delimiter=None):
        try:
            return np.loadtxt(file, delimiter=delimiter)
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error while loading text file '{file}': {e} \n{help_msg('loadTxt')}"

    # Save .txt file
    def save_txt(self, file, arr, delimiter=" "):
        try:
            # os.makedirs("./outputs", exist_ok=True)
            if not file.endswith(".txt"):
                file+=".txt"
            np.savetxt(f"{file}", arr, delimiter=delimiter, fmt="%s")
            return f"File saved successfully as '{file}'"
        except Exception as e:
            return f"Error while saving text file: {e} \n{help_msg('saveTxt')}"

