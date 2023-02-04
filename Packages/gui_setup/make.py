import os
import sys
import msvcrt
print()
print("[\033[32m信息\033[0m]：程序运行...")
print()
filelist = []
filepy = []
filepyc = []
filepyo = []
filepyi = []
filepyw = []
filepyd = []
filepyx = []
fileother = []


def press_anykey_to_continue():
    print("按任意键继续......")
    ord(msvcrt.getch())

# 试导入Pyinstaller，已检查用户是否安装了Pyinstaller.
try:
    import PyInstaller
except:
    print("[\033[31m错误\033[0m]: 没有找到模块\033[4mPyinstaller\033[0m，若要使用此程序，请\033[41m安装\033[0mPyinstaller")
    print()
    print("你可以尝试安装Pyinstaller:")
    print("    pip install Pyinstaller")
    print()
    print()
    press_anykey_to_continue()
    sys.exit(1) # 程序退出，不在执行后面的语句。

# print(os.getcwd() + '\\package')

# 扫描 packages 文件夹的内容。
def scrach_file():
    print("扫描的文件\n===============")
    for filepath, dirnames, filenames in os.walk(os.getcwd() + '\\packages'):
        # print(filepath, filenames)
        for filename in filenames:
            if filename.endswith('.py'):
                filepy.append(filename)
            elif filename.endswith('.pyc'):
                filepyc.append(filename)
            elif filename.endswith('.pyi'):
                filepyi.append(filename)
            elif filename.endswith('.pyo'):
                filepyo.append(filename)
            elif filename.endswith('.pyw'):
                filepyw.append(filename)
            elif filename.endswith('.pyd'):
                filepyd.append(filename)
            elif filename.endswith('.pyx'):
                filepyx.append(filename)
            else:
                fileother.append(filename)
            filelist.append(filepath + "\\" + filename)

def fie():
    global math
    math = 0
    py = 0
    pyc = 0
    pyo = 0
    pyi = 0
    pyw = 0
    pyd = 0
    pyx = 0
    other = 0
    print("分类的文件\n===============")
    for i in filepy:
        #print("\033[32m"+i+"\033[0m")
        math += 1
        py += 1
    for i in filepyc:
        #print("\033[31m"+i+"\033[0m")
        math += 1
        pyc += 1
    for i in filepyo:
        #print("\033[32m"+i+"\033[0m")
        math += 1
        pyo += 1
    for i in filepyi:
        #print("\033[34m"+i+"\033[0m")
        math += 1
        pyi += 1
    for i in filepyw:
        #print("\033[32m"+i+"\033[0m")
        math += 1
        pyw += 1
    for i in filepyd:
        #print("\033[35m"+i+"\033[0m")
        math += 1
        pyd += 1
    for i in filepyx:
        #print("\033[32m"+i+"\033[0m")
        math += 1
        pyx += 1
    for i in fileother:
        #print(i)
        math += 1
        other += 1
    print()
    global mathlist, mathliststr
    mathlist = [py, pyc, pyo, pyi, pyw, pyd, pyx, other]
    mathliststr = [".py", ".pyc", ".pyo", ".pyi", ".pyw", ".pyd", ".pyx", "other"]
    print("文件占比\n===============")
    for mat in range(len(mathlist)):
        print(mathliststr[mat], ":", round((mathlist[mat] / math) * 100), "%", end=' | ')
    print()

def sgan():
    global mathlist, mathliststr, math
    print("[\033[32m信息\033[0m]：正在扫描文件 ...\n")
    scrach_file()
    for i in filelist:
        print(i)
    print()
    print("[\033[32m信息\033[0m]：正在分类文件 ...\n")
    fie()


if __name__ == "__main__":
    print(".exe生成程序\n==========\n\n")
    print("欢迎使用.exe生成程序！\n\n")
    print("若要继续，请按下任意键...")
    press_anykey_to_continue()

    print()