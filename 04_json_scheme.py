# Задание 4. Дополнительные задачи с сериализацией и JSON Schema
import os
import logging
import datetime
import json
from jsonschema import validate, ValidationError



# Установка логгера
logger = logging.getLogger(__name__)
log_filename = 'project_root/logs/project_setup.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# 4.1 Работа с пользовательскими классами и JSON
class FileInfo:
    def __init__(self, filename, full_path):
        self.filename = filename
        self.full_path = full_path
        self.file_size = os.path.getsize(full_path)
        self.creation_time = datetime.date.fromtimestamp(os.path.getctime(full_path)).isoformat()
        self.last_modified = datetime.date.fromtimestamp(os.path.getmtime(full_path)).isoformat()

    def to_dict(self):
        return {
            "filename": self.filename,
            "full_path": self.full_path,
            "file_size": self.file_size,
            "creation_time": self.creation_time,
            "last_modified": self.last_modified
        }


def serialize_file_info():
    processed_dir = 'project_root/data/processed'
    output_dir = 'project_root/output'
    output_file = os.path.join(output_dir, 'file_info.json')

    file_info_list = []

    for filename in os.listdir(processed_dir):
        file_path = os.path.join(processed_dir, filename)
        file_info = FileInfo(filename, file_path)
        file_info_list.append(file_info.to_dict())

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(file_info_list, f, ensure_ascii=False, indent=4)
    logger.info(f'Информация о файлах сохранена в {output_file}')


serialize_file_info()


# 4.2 Валидация JSON с использованием JSON Schema
# Пример JSON Schema
file_info_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "filename": {"type": "string"},
            "full_path": {"type": "string"},
            "file_size": {"type": "integer"},
            "creation_time": {"type": "string", "format": "date-time"},
            "last_modified": {"type": "string", "format": "date-time"}
        },
        "required": ["filename", "full_path", "file_size", "creation_time", "last_modified"]
    }
}


def validate_json():
    output_dir = 'project_root/output'
    output_file = os.path.join(output_dir, 'file_info.json')

    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    try:
        validate(instance=data, schema=file_info_schema)
        logging.info('JSON-файл прошел валидацию.')
    except ValidationError as e:
        logger.error(f'Ошибка валидации JSON-файла: {e}')


validate_json()
