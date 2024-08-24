# Задание 2. Чтение, преобразование и сериализация данных
import os
import logging
import chardet
import datetime
import json

logger = logging.getLogger(__name__)
log_filename = 'project_root/logs/project_setup.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# 2.1 Чтение и обработка данных
def process_files():
    raw_dir = 'project_root/data/raw'
    processed_dir = 'project_root/data/processed'

    for filename in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, filename)

        # Определение кодировки
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        encoding = result['encoding']

        # Чтение и преобразование данных
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
            transformed_content = content.swapcase()

        # Сохранение обработанных данных
        processed_filename = filename.replace('.txt', '_processed.txt')
        with open(os.path.join(processed_dir, processed_filename), 'w', encoding='utf-8') as f:
            f.write(transformed_content)
        logger.info(f'Файл {filename} обработан и сохранён как {processed_filename}')


process_files()


# 2.2 Сериализация данных
def serialize_processed_files():
    raw_dir = 'project_root/data/raw'
    processed_dir = 'project_root/data/processed'
    output_dir = 'project_root/output'
    output_file = os.path.join(output_dir, 'processed_data.json')

    data = []

    for filename in os.listdir(processed_dir):
        file_path = os.path.join(processed_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        file_info = {
            "filename": filename,
            "original_text": content.swapcase(),  # Оригинальный текст до преобразования
            "transformed_text": content,
            "file_size_bytes": os.path.getsize(file_path),
            "last_modified": datetime.date.fromtimestamp(os.path.getmtime(file_path)).isoformat()
        }
        data.append(file_info)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.info(f'Сериализованные данные сохранены в {output_file}')


serialize_processed_files()
