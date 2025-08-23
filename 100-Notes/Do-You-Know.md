# Do You Know?

### Where is python default packages or libraries located?

`C:\Users\<user_name>\AppData\Local\Programs\Python\Python3xx\Lib\`

To know where is pip packages install use this command

```bash
pip show package-name
pip show matplotlib
```

### What is difference between relative and absolute path?

A relative path is a relative to current folder, often called as current working directory. 

:LiNotebook: In path string, folder names are separated by the slash  (/) character.

An Absolute path is one that starts from the root of the filesystem and includes the full hierarchy of folders to your file.

### How to uninstall pip package?

```bash
py -m pip uninstall package_name
```