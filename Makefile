
.PHONY: dep build

dep: build

build:
	pip install -r requirements.txt

version:
	@python src/obfuscator.py --version
