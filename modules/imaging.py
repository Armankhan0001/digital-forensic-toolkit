import shutil, subprocess

def create_disk_image(source, output):
    tool = shutil.which("dcfldd") or shutil.which("dd")
    
    if not tool:
        raise Exception("Missing dd or dcfldd")

    cmd = [tool, f"if={source}", f"of={output}", "bs=4M", "status=progress"]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd)
