from pathlib import Path


def save_avatar(username, file):
    base_dir = Path(__file__).resolve().parent.parent
    new_directory = base_dir / 'static' / 'users' / 'avatars' / username
    if not(new_directory.exists()):
        new_directory.mkdir()
    image = new_directory / file.name
    with open(image, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    db_destination = Path(f'users/avatars/{username}/{file.name}')
    return db_destination

