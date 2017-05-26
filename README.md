# Python Obfuscator
A python byte code obfuscator, built as part of the course Language Based
Security(TDA602) at Chalmers University of Technology.

## Installing
All dependencies are defined in the `requirements.txt` file. To install them
either run `pip install -r requirements.txt` or use the shortcut `make dep`.

## Usage
```
Usage:
    obfuscator.py [-o NAME] [-k KEY] [--quiet | --verbose | --encrypt | --debug] FILE...
    obfuscator.py (-h | --help)
    obfuscator.py --version

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME
    -k KEY      decrypt file with KEY
```

**Example:**
```
python obfuscator.py -o new_file file.py
```

This will result in an obfuscated file named `new_file_obfuscated.py`. It will
runnable but very hard to read. Furthermore, the file size will have increased
due to the fact that we add some random code spread across the whole file. This
code will never be referenced or run so no worries.

## Encryption
The obfuscator can also encrypt each line of the file, making it completely
unusable for the python interpreter, unless decrypted. To encrypt a file run:

```
python obfuscator.py --encrypt file.py
```

This will obfuscate and encrypt your file. A key will be outputted once this is
done and you need to store that key to be able to decrypt.

To decrypt, simply use the decrypt flag and they key from before:

```
python obfuscator.py -k VERYCOOLKEY file_obfuscated.py
```

## Authors
* Jonathan Nilsfors - __nilsfors@student.chalmers.se__
* Johan Backman - __johback@student.chalmers.se__
