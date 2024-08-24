# Задание 1. Управление проектной структурой и файловой системой
import os
import logging


# Установка логгера, для начала создаем и ведем лог-файл в корневой директории, так как других еще не создано,
# а логгировать уже надо
logger = logging.getLogger(__name__)
os.makedirs('project_root/logs', exist_ok=True)  # True : чтоб не вызывать ошибку при многократных запусках
log_filename = 'project_root/logs/project_setup.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# 1.1 Создаем структуру директорий проекта
def create_directories():
    project_root = 'project_root'
    directories = [
        os.path.join(project_root, 'data', 'raw'),
        os.path.join(project_root, 'data', 'processed'),
        os.path.join(project_root, 'backups'),
        os.path.join(project_root, 'output')
    ]

    for directory in directories:
        try:
            os.makedirs(directory)
            logging.info(f'Создана директория: {directory}')
        except FileExistsError:
            logger.info(f'Директория {directory} уже существует')


create_directories()


# 1.2 Создание и запись данных в файлы
def create_sample_files():
    samples = {
        "file1_utf8.txt": ("Привет, мир!", "utf-8"),
        "file2_iso.txt": ("Bonjour le monde!", "iso-8859-1"),
        "file3_utf16.txt": ("Hello, world!", "utf-16")
    }

    raw_dir = 'project_root/data/raw'
    for filename, (content, encoding) in samples.items():
        with open(os.path.join(raw_dir, filename), 'w', encoding=encoding) as f:
            f.write(content)
        logger.info(f'Создан файл: {filename} с кодировкой {encoding}')


create_sample_files()
