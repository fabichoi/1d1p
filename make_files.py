import hashlib
import shutil
from datetime import datetime
from pathlib import Path


def generate_date_suffix():
    return datetime.now().strftime("%m%d")


def generate_hash():
    hash_object = hashlib.md5(generate_date_suffix().encode())
    return hash_object.hexdigest()[:8]


def copy_folder(src, dest):
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists():
        print(f"오류: 소스 폴더 '{src}' 없음")
        return False

    dest_path.mkdir(parents=True, exist_ok=True)
    date_suffix = generate_hash()

    for item in src_path.rglob('*'):
        relative_path = item.relative_to(src_path)

        if item.is_file():
            file_stem = item.stem
            file_suffix = item.suffix

            new_filename = f"{file_stem}_{date_suffix}{file_suffix}"
            dest_file_path = dest_path / relative_path.parent / new_filename
            dest_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_file_path)

        elif item.is_dir():
            dest_dir_path = dest_path / relative_path
            dest_dir_path.mkdir(parents=True, exist_ok=True)

    return True


def main(path):
    if not path:
        print("오류: 폴더 경로 없음")
        return

    src = path + '0000'
    dest = path + generate_date_suffix()
    success = copy_folder(src, dest)

    if success:
        print(f"src: {src} dest: {dest} | 복사 완료")
    else:
        print("복사 실패")


if __name__ == "__main__":
    main(path='./2025/')
