from abc import ABC, abstractmethod, abstractstaticmethod
import hashlib

class HashEncripter(ABC):
    """Reprensetacion basica de un Encripter"""

    @abstractstaticmethod
    def prepare_encript(file):
        """Prepares file data for encripting."""

    @abstractstaticmethod
    def do_encript(file):
        """Encripts the file data and print it."""

class MD5Encripter(HashEncripter):

    def prepare_encript(file):
        file = open(file, 'r')
        return file.read().encode()

    def do_encript(file):
        text = hashlib.md5(file)
        return text.hexdigest()

class SHA3Encripter(HashEncripter):


    def prepare_encript(file):
        file = open(file, 'r')
        return file.read().encode()

    def do_encript(file):
        text = hashlib.sha384(file)
        return text.hexdigest()

class SHA256Encripter(HashEncripter):


    def prepare_encript(file):
        file = open(file, 'r')
        return file.read().encode()

    def do_encript(file):
        text = hashlib.sha256(file)
        return text.hexdigest()


def read_factory() -> HashEncripter:
    """Constructs an exporter factory based on the user's preference."""

    factories = {
        'MD5': MD5Encripter,
        'SHA3': SHA3Encripter,
        'SHA256': SHA256Encripter
    }

    while True:
        option = str(input('Ingrese la codificacion que desea darle a su archivo (MD5, SHA3, SHA256): '))
        if option in factories:
            return factories[option]
        else:
            print('Esa opcion no corresponde')

def main(factory: HashEncripter) -> None:
    """Main function"""

    file = factory.prepare_encript('file.txt')
    print(factory.do_encript(file))


if __name__ == '__main__':

    while True:
        factory = read_factory()
        main(factory)