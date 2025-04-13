# InviScript

![License](https://img.shields.io/badge/license-MIT-blue.svg)

InviScript is a powerful tool that converts JavaScript code into an invisible format using Unicode characters. This tool allows you to obfuscate your JavaScript code in a unique way, making it appear empty while still maintaining full functionality.

## Features

- Convert JavaScript code to invisible Unicode characters
- Maintains full functionality of the original code
- Simple command-line interface
- Customizable output file name
- Built-in safety checks and user confirmations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GGal1leo/InviScript.git
cd InviScript
```

2. Make sure you have Python 3.x installed on your system.

## Usage

Basic usage:
```bash
python inviscript.py -f <input_file> -o <output_file>
```

### Arguments

- `-f, --file`: Specify the input JavaScript file to be converted
- `-o, --output`: Specify the output HTML file name (default: malcode.html)
- `-v, --version`: Show version information
- `-h, --help`: Show help message

### Example

Converting a JavaScript file:
```bash
python inviscript.py -f sample.js -o output.html
```

## How It Works

InviScript works by:
1. Reading the input JavaScript file
2. Converting the code to binary
3. Replacing binary digits with invisible Unicode characters
4. Wrapping the result in a self-executing proxy
5. Generating an HTML file with the obfuscated code

## Sample Input/Output

Input (sample.js):
```javascript
var i = 5;
sum = 0;
for (var i = 0; i < 10; i++) {
  sum += i;
}
alert(sum);
```

The output will be an HTML file containing the code in invisible format that executes exactly the same way as the input.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [GGal1leo](https://github.com/GGal1leo)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
