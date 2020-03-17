from argparse import ArgumentParser
from re import findall, M, compile, match
from os import path, listdir
import gui


def parse_test():
    parser = ArgumentParser(description="Process integers.")
    parser.add_argument('-c', action='store_true', help="Return number of characters.")
    parser.add_argument('-w', action='store_true', help="Return number of words.")
    parser.add_argument('-l', action='store_true', help="Return number of lines.")
    parser.add_argument('-s', action='store_true', help="Recursively processes all files in the directory.")
    parser.add_argument('-a', action='store_true', help="Return more complex data.")
    parser.add_argument('-x', action='store_true', help="Graphical interface.")
    # Add path argument
    parser.add_argument('directory', type=str, help="Directory of files.")
    args = parser.parse_args()
    return args


class WC:
    def __init__(self, args):
        # Save all checked files information
        self.info = []
        # Save file path to be checked
        self.file_list = []
        # Save all arguments
        self.args = args
        # On command line mode whether or not
        self.flag = True

    # Get numbs of Character,words,lines,'Code lines','Space line','Note lines'
    def CountFunc(self):
        if len(self.file_list) == 0:
            self.info.append("找不到该文件.")
        for file in self.file_list:
            note_count = 0
            code_count = 0
            space_count = 0
            flag = False
            base_name = path.basename(file)
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    f_read = f.read()
                    if self.args.c:
                        char_num = len(f_read.replace(" ", "").replace("\n", ""))
                        self.info.append(base_name + " --Char: " + str(char_num))
                    if self.args.w:
                        word_num = len(findall(r'[a-zA-Z]+', f_read, M))
                        self.info.append(base_name + " --Word: " + str(word_num))
                    f.close()
            except:
                self.info.append(base_name + " open error.")

            try:
                with open(file, 'r', encoding='utf-8') as f:
                    f_readline = f.readlines()
                    if self.args.l:
                        line_num = len(f_readline)
                        self.info.append(base_name + " --lines: " + str(line_num))
                    for line in f_readline:
                        if "/*" in line:
                            note_count = note_count + 1
                            flag = True
                            if "*/" in line:
                                flag = False
                        elif flag:
                            note_count = note_count + 1
                            if "*/" in line:
                                flag = False
                        elif "//" in line:
                            note_count = note_count + 1
                        elif len(line.strip()) > 1:
                            code_count = code_count + 1
                        else:
                            space_count = space_count + 1
                    f.close()
            except:
                self.info.append(base_name + " open error.")

            if self.args.a:
                self.info.append(base_name + " --code line : " + str(code_count))
                self.info.append(base_name + " --space line: " + str(space_count))
                self.info.append(base_name + " --note line:  " + str(note_count))

    # Recursion
    def Recursion(self):
        dir_path = path.dirname(self.args.directory)
        file_name = path.basename(self.args.directory)
        if '*' in file_name:
            if '.' in file_name:
                match_format = compile('{}{}'.format(file_name.replace('.', '\.').replace('*', '\w+'), '$'))
                for file in listdir(dir_path):
                    if match(match_format, file):
                        self.file_list.append(path.join(dir_path, file))
        elif '?' in file_name:
            if '.' in file_name:
                match_format = compile('{}{}'.format(file_name.replace('.', '\.').replace('*', '\w'), '$'))
                for file in listdir(dir_path):
                    if match(match_format, file):
                        self.file_list.append(path.join(dir_path, file))
        if len(self.file_list) == 0:
            if path.exists(self.args.directory):
                self.file_list.append(self.args.directory)

    def main(self):
        dir_path = path.dirname(self.args.directory)
        if dir_path:
            self.info.append("Path: " + dir_path)
        else:
            self.info.append("Route error.")
        # on command line mode
        if self.flag:
            if self.args.s is True:
                self.Recursion()
                self.CountFunc()
            else:
                if path.exists(self.args.directory):
                    self.file_list.append(self.args.directory)
                    self.CountFunc()
                else:
                    self.info.append(path.basename(self.args.directory) + ". File not exist")
        # GUI mode
        else:
            self.CountFunc()

        if self.args.x is False:
            for info in self.info:
                print(info)
        return self.info


def wc_main():
    args = parse_test()
    if args.x:
        # Set default
        args.c = True
        args.w = True
        args.l = True
        args.a = True
        args.directory = ""
        gui.GUI(args)
    else:
        wc = WC(args)
        wc.main()


if __name__ == '__main__':
    wc_main()
