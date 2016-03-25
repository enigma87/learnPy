fout = open('out.txt', 'w')

fout.write('go go\n')
fout.write("let go\n")

import os.path;




try:
    f = open("asdf.txt")
    f.close()
except:
    print "something wrong?"


def sed(file1, file2, str1, str2):
    try:
        f1 = open(file1, "r")
        f2 = open(file2, "w")
        for line in f1:
            f2.write(line.replace(str1, str2))
    except:
        print "file error!"

    f1.close()
    f2.close()

#sed("inp.txt", "sed.txt", "database", "ORACLE")


def main(name, *params):
    sed(params[0], params[1], params[2], params[3])

print __name__

import sys
if __name__ == '__main__':
    print sys.argv
    main(*sys.argv)
    print os.path.exists('out.txt')
    print os.path.abspath('out.txt')
    print os.path.isdir('out.txt')
    print os.path.isfile('out.txt')

    print os.listdir(os.getcwd())
