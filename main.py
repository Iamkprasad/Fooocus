
import os
import subprocess
import sys

def install_packages():
    packages = [
        "pygit2==1.12.2",
        "einops",
        "safetensors",
        "torchsde",
        "transformers",
        "opencv-python"
    ]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def clone_repo():
    repo_url = "https://github.com/lllyasviel/Fooocus.git"
    subprocess.check_call(["git", "clone", repo_url])

def change_directory():
    os.chdir("Fooocus")

def download_file():
    file_url = "https://huggingface.co/gsdf/CounterfeitXL-V2.0/resolve/main/CounterfeitXL-V2.5.safetensors"
    destination_dir = "/teamspace/studios/this_studio/Fooocus/models/checkpoints/"
    os.makedirs(destination_dir, exist_ok=True)
    subprocess.check_call(["wget", "-P", destination_dir, file_url])

def run_entry_script():
    entry_script = "entry_with_update.py"
    subprocess.check_call([sys.executable, entry_script, "--share", "--always-high-vram"])

def main():
    install_packages()
    clone_repo()
    change_directory()
    download_file()
    run_entry_script()

if __name__ == "__main__":
    main()
