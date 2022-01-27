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
from PIL import Image


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


class TextTweaker(ZipProcessor):
    def __init__(self, archive: Path) -> None:
        super().__init__(archive)
        self.find: str
        self.replace: str

    def find_and_replace(self, find: str, replace: str) -> 'TextTweaker':
        self.find = find
        self.replace = replace
        return self

    def transform(self, extracted: Path) -> None:
        input_text = extracted.read_text()
        output_text = re.sub(self.find, self.replace, input_text)
        extracted.write_text(output_text)


class ImgTweaker(ZipProcessor):
    def transform(self, extracted: Path) -> None:
        image = Image.open(extracted)
        scale = image.resize(size=(640, 960))
        scale.save(extracted)


class SampleReader:
    '''
    See gh.names for attribute ordering in data file.
    '''
    target_class = Sample
    header = [
        'sepal_length', 'sepal_width',
        'petal_length', 'petal_width', 'class'
    ]

    def __init__(self, source: Path) -> None:
        self.source = source

    def sample_iter(self) -> Iterator[Sample]:
        target_class = self.target_class
        with self.source.open() as source_file:
            reader = csv.DictReader(source_file, self.header)
            for row in reader:
                try:
                    sample = target_class(
                        sepal_length=float(row['sepal_length']),
                        sepal_width=float(row['sepal_width']),
                        petal_length=float(row['petal_length']),
                        petal_width=float(row['petal_width']),
                    )
                except ValueError as ex:
                    raise BadSampleRow(f'Invalid {row!r}') from ex
                yield sample


class BadSampleRow(ValueError):
    pass


class Purpose(enum.IntEnum):
    Classification = 0
    Testing = 1
    Training = 2


class KnownSample(Sample):

    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float, 
        purpose: int, 
        species: str) -> None:
        purpose_enum = Purpose(purpose)
        if purpose_enum not in {Purpose.Training, Purpose.Testing}:
            raise ValueError(
                f'Invalid purpose: {purpose!r}: {purpose_enum}'
            )
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_width=petal_width,
            petal_length=petal_length
        )
        self.purpose = purpose_enum
        self.species = species
        self._classification: Optional[str] = None 

    def matches(self) -> bool:
        return self.species == self.classification

    @property
    def classification(self) -> Optional[str]:
        if self.purpose == Purpose.Testing:
            return self._classification
        else:
            raise AttributeError(f'Training samples have no classification')

    @classification.setter
    def classification(self, value: str) -> None:
        if self.purpose == Purpose.Testing:
            self._classification = value
        else:
            raise AttributeError(f'Training samples cannot be classified')

# TextTweaker(zp_data)\
#     .find_and_replace('xyzzy', 'plover"s egg')\
#         .process_files('**.md')