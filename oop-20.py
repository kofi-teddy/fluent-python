# oop
# More advance concepts oop   
# Properties in detail
# Using decorators to create properties
# when to use properties
# chaching a web page example 
# Manager objects
from __future__ import annotations
import fnmatch
import imp
from pathlib import Path
import re
import zipfile
from abc import ABC, abstractmethod


class ZipProcessor(ABC):
    def __init__(self, archive: Path) -> None:
        self.archive = archive
        self._pattern: str

    def process_files(self, pattern: str) -> None:
        self._pattern = pattern

        input_path, output_path = self.make_backup()

        with zipfile.ZipFile(output_path, 'w') as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)

    def make_backup(self) -> tuple[Path, Path]:
        input_path = self.archive_path.with_suffix(
            f'{self.archive_path.suffix}.old'
        )
        output_path = self.archive_path 
        self.archive_path.rename(input_path)
        return input_path, output_path

    def copy_and_transform(
        self, input: zipfile.ZipFile, output: zipfile.ZipFile
        ) -> None:
        for item in input.infolist():
            extracted = Path(input.extract(item))
            if self.matches(item):
                print(f'Transform {item}')
                self.transform(extracted)
            else:
                print(f'Ignore    {item}')
            output.write(extracted, item.filename)
            self.remove_under_cwd(extracted)

    def matches(self, item: zipfile.ZipInfo) -> bool:
        return (
            not item.is_dir()
            and fnmatch.fnmatch(item.filename, self._pattern)
        )
    
    def remove_under_cwd(self, extracted: Path) -> None:
        extracted.unlink()
        for parent in extracted.parents:
            if parent == Path.cwd():
                break
            parent.rmdir()

    @abstractmethod
    def transform(self, extracted: Path) -> None:
        pass
