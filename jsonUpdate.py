import shutil
import os

JsonFile = "config.json"
Target = "build/dist/main"

if __name__ == "__main__":
    try:
        try:
            os.remove(Target+"/"+JsonFile)
        except (FileNotFoundError,FileExistsError):
            print("Cannot Update JSON file")
        except Exception as Error:
            print("[ERROR]: ",Error)
        shutil.copy(JsonFile,Target)
        print(f"File {JsonFile} has been copied to {Target}")
    except Exception as Error:
        print("[ERROR]: ",Error)