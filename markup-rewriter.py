import sys
import os

def process_file_for_urls(filename):
    """
    Reads a file line by line, formats lines starting with http/https
    as Markdown links, and prints all lines to stdout.
    """
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Remove leading/trailing whitespace (including newline) for the check
                stripped_line = line.strip()

                # Check if the stripped line starts with http or https
                if stripped_line.startswith('http') or stripped_line.startswith('https'):
                    # Format the line as a Markdown link [URL](URL)
                    # print adds its own newline by default
                    print(f"[{stripped_line}]({stripped_line})")
                else:
                    # Print the original line as is.
                    # Use end='' because the 'line' variable already includes
                    # the newline character from the file reading.
                    print(line, end='')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1) # Exit with an error code
    except Exception as e:
        print(f"An error occurred while reading or processing the file: {e}")
        sys.exit(1) # Exit with an error code

if __name__ == "__main__":
    # Check if a command-line argument (the filename) was provided
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <input_filename>")
        sys.exit(1) # Exit with an error code

    input_filename = sys.argv[1]

    # Check if the provided argument is a valid file
    if not os.path.isfile(input_filename):
         print(f"Error: '{input_filename}' is not a valid file.")
         sys.exit(1) # Exit with an error code


    # Process the file
    process_file_for_urls(input_filename)

    sys.exit(0) # Exit successfully
