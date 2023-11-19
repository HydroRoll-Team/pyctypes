# pyctypes
Compile the cpp dynamic library and allow Python calls.

> [!IMPORTANT]  
> 需要如下环境:
> * Visual Studio 2019+
> * Python 3.8+ _(better with Visual Studio Code)_
> * gcc/g++ 编译器

这只是一个示例仓库，最终目的是兼容一些动态链接库，也就不需要重复编写代码了。

## 复现步骤

1. 克隆存储库并进入根目录

```
git clone https://github.com/HydroRoll-Team/pyctypes
```

2. Visual Studio 打开 `PCH_H.sln` 文件，使用 `ctrl+B` 生成项目。

> [!NOTE]  
> 生成好的 `PCH_H.dll` 会在 `./x64/debug` 目录出现。

`pch.cpp` 用于定义一个可供 Python 环境调用的函数。

```cpp
// pch.cpp: 与预编译标头对应的源文件

#include "pch.h"

// 当使用预编译的头时，需要使用此源文件，编译才能成功。
int func(int a) {
	return a * a;
}
```

`pch.h` 用于申明可以在外部调用的函数。

```cpp
// pch.h: 这是预编译标头文件。
// 下方列出的文件仅编译一次，提高了将来生成的生成性能。
// 这还将影响 IntelliSense 性能，包括代码完成和许多代码浏览功能。
// 但是，如果此处列出的文件中的任何一个在生成之间有更新，它们全部都将被重新编译。
// 请勿在此处添加要频繁更新的文件，这将使得性能优势无效。

#ifndef PCH_H
#define PCH_H

// 添加要在此处预编译的标头
#include "framework.h"

#endif //PCH_H

extern "C" _declspec(dllexport) int func(int a);
```

3. 运行 `examples/test_dll.py`

```py
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from ctypes import cdll
from os.path import abspath, dirname, join

DIR = dirname(abspath(__file__))

def main():
    p = join(DIR, '..', 'x64', 'debug', 'PCH_H.dll')
    f = cdll.LoadLibrary(p)
    print(f.func(33))


if __name__ == '__main__':
    main()
```
