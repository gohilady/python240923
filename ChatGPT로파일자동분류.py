import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\temp1'

# 이동할 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더가 없으면 생성
folders = [image_folder, data_folder, docs_folder, archive_folder]
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일을 이동할 조건
file_types = {
    image_folder: ['.jpg', '.jpeg', 'JPG', 'JPEG'],
    data_folder: ['.csv', '.xlsx'],
    docs_folder: ['.txt', '.doc', '.pdf'],
    archive_folder: ['.zip']
}

# 다운로드 폴더의 파일들 이동
for file_name in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file_name)

    # 파일일 경우에만 이동 작업 수행
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1].lower()
        
        # 파일 확장자에 따라 해당 폴더로 이동
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                try:
                    shutil.move(file_path, os.path.join(folder, file_name))
                    print(f'Moved {file_name} to {folder}')
                except Exception as e:
                    print(f'Error moving {file_name}: {e}')
                break
