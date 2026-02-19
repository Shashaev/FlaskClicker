
def save_image(image: bytes, path: str) -> None:
    with open(path, 'bw') as f:
        f.write(image)
