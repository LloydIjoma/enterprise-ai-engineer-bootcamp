def save_text(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def read_text(filename):
    with open(filename, "r") as f:
        return f.read()
