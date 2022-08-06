import os
import typing as t

from korrektor_py.exceptions import WrongFileFormat


def get_file_info(file_path: str) -> t.Tuple[str, str]:
    """Get file's name & extension
    """
    base_name: tuple = os.path.splitext(
        os.path.basename(file_path)
    )
    file_name, file_format = base_name[0], \
        base_name[1].replace(".", "")

    check_file_format(file_format)

    return file_name, file_format


def check_file_format(format: str):
    allowed_formats: list[str] = [
        "docx", "xlsx", "pptx",
        "epub", "html"
    ]

    if format.lower() not in allowed_formats:
        raise WrongFileFormat(
            "File format should be: {}".format(
                ",".join(allowed_formats)
            )
        )
