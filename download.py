import subprocess

url = "https://huggingface.co/Rejekts/project/resolve/main/rmvpe.pt"
output_file = "rmvpe.pt"

url2 = "https://huggingface.co/Rejekts/project/resolve/main/hubert_base.pt"
output_file2 = "hubert_base.pt"

subprocess.run(["wget", "-O", url])
subprocess.run(["wget", "-O", url2])
