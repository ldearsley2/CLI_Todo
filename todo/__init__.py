__app_name__ = "CLTodo"
_version_ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)


ERRORS = {
    DIR_ERROR: "Config directory error",
    FILE_ERROR: "Config file error",
    DB_READ_ERROR: "Database read error",
    DB_WRITE_ERROR: "Database write error",
    ID_ERROR: "To-do ID error",
}
