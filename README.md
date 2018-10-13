# Python examples

This project is showing how to use python to parse, interpret and generate ESDL files. At the moment we're experiencing
problems with the generated python classes. It's currently not generating valid ESDL. Parsing a valid ESDL file seems
to go right.

## How to generate the python classes

Using GenerateDS (see https://pypi.org/project/generateDS/ and http://www.davekuhlman.org/generateDS.html)

### Install GenerateDS

```bash
pip install generateds
```

### Generate the classes

```bash
generateDS -o esdl_sup.py -s esdl_sub.py --no-namespace-defs --root-element="EnergySystem" --export="write etree" esdlXML.xsd
```

## How to use the python classes

## Two examples

### Reading and parsing an ESDL description

TODO

### Generating and writing an ESDL description

TODO

