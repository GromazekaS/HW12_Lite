# Задание 3. Управление проектной структурой и файловой системой
import os
import logging
import shutil
import datetime
import time


# Установка логгера
logger = logging.getLogger(__name__)
log_filename = 'project_root/logs/project_setup.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 3.1 Создание резервного архива
def create_backup():
    source_dir = 'project_root/data'
    backup_dir = 'project_root/backups'
    backup_filename = f'backup_{datetime.date.fromtimestamp(time.time()).strftime("%Y%m%d")}.zip'
    backup_path = os.path.join(backup_dir, backup_filename)

    shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_dir)
    logger.info(f'Резервная копия создана: {backup_filename}')


create_backup()


# 3.2 Восстановление файлов из резервного архива
def restore_backup(backup_filename):
    backup_dir = 'project_root/backups'
    restore_dir = 'project_root/data_restore'

    backup_path = os.path.join(backup_dir, backup_filename)
    shutil.unpack_archive(backup_path, restore_dir)
    logger.info(f'Резервная копия {backup_filename} восстановлена в {restore_dir}')


# Пример вызова восстановления
restore_backup('backup_20240824.zip')
