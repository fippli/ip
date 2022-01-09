# IP
Terminal command to display your ip in a nice way.

## Installation
Install with [climate](https://fippli.se/cli-mate.sh/)
```
climate install 
```

## Usage
## Both local and global
```bash
ip
```
```bash
LOCAL            GLOBAL
123.456.789.012  123.456.789.012
```

## Local only
```bash
ip --local
```
```bash
123.456.789.012
```

## Global only
```bash
ip --global
```
```bash
123.456.789.012
```

## Help
```bash
ip --help
```
```txt
IP
Display your ip

Usage
ip [options]

Available options
 --help                        Display this message
 --global | -g                 Print global ip only
 --local  | -l                 Print local ip only
```
