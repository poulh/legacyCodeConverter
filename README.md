# Legacy Code Converter

## Overview
The **Legacy Code Converter** is a Python script that uses the OpenAI API's chat completion to translate legacy code written in a specified legacy language into a modern programming language. It is particularly useful for converting outdated codebases to a more contemporary language while harnessing the capabilities of artificial intelligence.

## Business Problem
Many organizations face the challenge of maintaining or migrating legacy codebases. As technologies evolve, legacy languages can become outdated and less maintainable. The Legacy Script Converter addresses this problem by automating the process of translating legacy code into a more modern language, reducing the manual effort and minimizing errors in the migration process.

## Usage
To run the Legacy Script Converter, use the following command format:

```shell
Legacy Script Converter

optional arguments:
  -h, --help            show this help message and exit
  --legacy-path LEGACY_PATH
                        Path to the legacy code file(s) using a glob pattern
  --output-path OUTPUT_PATH
                        Path to the parent directory for saving the updated scripts
  --convert-to CONVERT_TO
                        Target language to convert to
```

### Example
```shell
python lcc.py --legacy-path legacy_examples/*.cpp --output-path . --convert-to python
```

