#!/usr/bin/python3
"""THis module instantiates an instance of the storage to be used"""

from os import getenv

storage_type = getenv('MQ_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
