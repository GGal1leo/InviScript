import sys
import os
import argparse
import colorama

# create a parser
parser = argparse.ArgumentParser(description='InviScript Converter')
parser.add_argument('-f', '--file', type=str, help='Specify the file to be converted to InviScript')
parser.add_argument('-o', '--output', type=str, help='Specify the output file name (default: malcode.html)')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("==========================")
    print("InviScript Converter")
    print("Usage: python main.py -f <file> -o <output>")
    print("\t-f, --file     Specify the file to be converted to InviScript")
    print("\t-o, --output   Specify the output file name (default: malcode.html)")
    print("\t-v, --version  Show version")
    print("\t-h, --help     Show this help message")
    print("Example: python main.py -f test.txt -o output.html")
    print("InviScript Converter")
    print("Created by GGal1leo")
    print("==========================")
    sys.exit()

#test = "alert('Hello, World!')"
credit = " // https://github.com/GGal1leo/InviScript"

if args.file:
    if os.path.isfile(args.file):
        with open(args.file, 'r') as f:
            test = f.read()
    else:
        print("File not found. Please check the file path.")
        sys.exit()
else:
    print("No file specified. Please use -f or --file to specify the file.")
    sys.exit()

# check if output file is specified
if args.output:
    output_file = args.output 
else:
    output_file = "malcode.html"
# check if output file already exists
if os.path.isfile(output_file):
    print(f"Output file {output_file} already exists. Do you want to overwrite it? (y/n)", end=' >> ')
    choice = input()
    if choice.lower() != 'y':
        print("Exiting...")
        sys.exit()

# check if the file is empty
if os.path.getsize(args.file) == 0:
    print("File is empty. Please check the file.")
    sys.exit()


# convert to binary
binary = ''.join(format(ord(i), '08b') for i in test)
#print(binary)
binary2 = ''.join(format(ord(i), '08b') for i in credit)

# convert 1 and 0 to \u3164 and \uFFA0 characters
invisiScript = binary.replace('1', '\u3164').replace('0', '\uFFA0')
invisiScript += binary2.replace('1', '\u3164').replace('0', '\uFFA0')
#invisiScript = ""


malcode = """new Proxy({},{get:(_,n)=>eval([...n].map(n=>+("ﾠ">n)).join``.replace(/.{8}/g,n=>String.fromCharCode(+("0b"+n))))}).\n""" + invisiScript + """\n"""
#print(malcode)
script = "<script>" + malcode + "</script>"

# write script to output File
with open(output_file, 'w') as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>InviScript</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write(script)
    f.write("\n</body>\n")
    f.write("</html>\n")


print(f"File converted to InviScript and saved as {colorama.Fore.GREEN}{output_file}{colorama.Style.RESET_ALL}")

