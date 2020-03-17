# WC.py
```
Another WC edition base on python 3.x
```

## Funtion realization
* **[character]**
* **[word]**
* **[line]**
* **[code line]**
* **[blank line]**
* **[comment line]**
* **[GUI]**

## Usage
### Grammar
```
Type "python wc.py [-argument] [-object]
```
### Ordinary usage
```
$$ -argument
        𠃊 -c    {Returns the number of characters in [object]}
        𠃊 -w    {Returns the number of words in [object]}
        𠃊 -l    {Returns the number of lines in [object]}
        𠃊 -a    {Returns more complex 
                 (code line/blank line/comment line)}
        𠃊 -x    {Display graphical user interface}
```

### Extra usage

#### Recursively processes qualified files in the directory
```
$ python wc.py -c -w -l -a -s "C:/*.c"
```

#### Display graphical interface
```
$ python wc.py -x " "
```

## Environment
* Windows7/8/10, Linux, MacOS
* Python 3.x
* Pip package: PyQt5

## Running Screenshot

![image](https://github.com/P4XL/Word-Count/blob/master/image/command.png)
![image](https://github.com/P4XL/Word-Count/blob/master/image/gui-display.png)

## Bugs
* **Target file is needed when on GUI mode.**
```
python wc.py -x file 
```
