from re import finditer, findall
import sys, getopt, os

PATTERN = r'\ngen => \[.*\]\(.*\)'
FILE = 'MAIN.md'
WITH_TITLE = True
N_HASHES = 3

FILE = os.environ["INPUT_FILE"]
WITH_TITLE = os.environ["INPUT_WITH_TITLE"].strip().lower() == 'true'
N_HASHES = int(os.environ["INPUT_N_HASHES"])

HELP_MESSAGE = """
usage: python3 genREADME.py (optional) (-w true) (optional) (-f MAIN.md) (optional) (-n 3)
"""

def get_file(link):
    file = link
    try:
        file = link[link.rindex('/')+1:]
    except:
        pass
    return file
    
def get_file_name(alt, file):
    if alt.strip() != '':
        return alt;
    file_name = file
    try:
        file_name = file[:file.index('.')]
        file_name = file_name[0].upper() + file_name[1:]
    except:
        pass
    return file_name

def get_file_extension(file):
    file_extension = ''
    try:
        file_extension = file[file.rindex('.')+1:]
    except:
        pass
    return file_extension

if __name__ == "__main__":
    args = sys.argv[1:]
    options = 'hf:w:n:'
    long_options = ['help', 'file=', 'with_title=', 'n_hashes=']
    try:
        arguments, vals = getopt.getopt(args, options, long_options)
        for currArg, currVal in arguments:
            if currArg in ('-h', '--help'):
                print(HELP_MESSAGE)
            elif currArg in ('-f', '--file'):
                FILE = currVal
            elif currArg in ('-w', '--with_title'):
                WITH_TITLE = (currVal.strip().lower() == 'true')
            elif currArg in ('-n', '--n_hashes'):
                N_HASHES = int(currVal)
    except getopt.error as err:
        print(err)
    
    input_file_content = open(FILE, 'r').read()
    for entry in finditer(PATTERN, input_file_content):
        entry = entry.group()
        alt = findall(r'\[.*\]', entry)[0][1:-1]
        link = findall(r'\(.*\)', entry)[0][1:-1]
        file = get_file(link)
        file_name = get_file_name(alt, file)
        file_extension = get_file_extension(file)
        file_content = open(link, 'r').read()
        
        output_file_content = ''
        if WITH_TITLE:
            output_file_content
            for i in range(N_HASHES):
                output_file_content += '#'
            output_file_content += ' ' + file_name + '\n'
        output_file_content += '```' + file_extension + '\n'
        output_file_content += file_content + '\n'
        output_file_content += '```' + '\n'
        input_file_content = input_file_content.replace(entry, output_file_content)
    print(WITH_TITLE, FILE, N_HASHES)
    with open('README.md', 'w') as fp:
        fp.write(input_file_content)