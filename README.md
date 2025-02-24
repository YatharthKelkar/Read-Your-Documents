<h1>📄 File Reader, Writer & Search Tool</h1>

<h2>🚀 Introduction</h2>

This Python script is a comprehensive file handling tool designed to perform multiple operations on text files. It enables users to read content from a file, write or append text to another file, and search for specific words, alphabets, or sentences within a file. This script is useful for automating text processing tasks, data manipulation, and content management.

File handling is a fundamental aspect of programming, particularly in applications that involve storing and retrieving information. Whether you need to process logs, manage documents, or perform automated text-based searches, this script provides an efficient solution.

<h2>🎯 Features</h2>

Read File – Open and read content from a specified file.

Overwrite File – Completely replace the existing content of a file.

Append to File – Add new content without erasing previous data.

Write to Another Document – Copy text from one file to another.

Search for a Word, Letter, or Sentence – Find specific text occurrences within a file.

Case-Insensitive Search – Locate text regardless of case differences.

Error Handling – Ensure smooth execution even if files are missing or unreadable.

<h2>🏗️ How It Works</h2>

<h3>1️⃣ Reading from a File</h3>

The script first reads content from a source file. This is essential for processing existing data or copying text into another file.

<h3>2️⃣ Writing to a File</h3>

The script can either overwrite or append content to a destination file, depending on the mode used (w for overwrite, a for append).

<h3>3️⃣ Searching within a File</h3>

Users can enter a search term (word, letter, or phrase), and the script will count and display occurrences of that term within the file. This is useful for analyzing text-based data.

<h3>4️⃣ File Closure</h3>

To optimize performance and prevent resource leaks, the script ensures that all opened files are properly closed after execution.

<h2>📜 Example Code</h2>

Here’s a Python implementation of the script:

# Function to search for a keyword in a file
def search_in_file(filename, keyword):
    try:
        with open(filename, "r") as file:
            content = file.read()
            occurrences = content.lower().count(keyword.lower())
            print(f"'{keyword}' found {occurrences} times in {filename}.")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")

# Reading from a source file
try:
    with open("source.txt", "r") as source:
        content = source.read()
except FileNotFoundError:
    print("Error: Source file not found.")
    content = ""

# Writing content to another file
with open("destination.txt", "w") as destination:
    destination.write(content)

# Appending extra data
extra_text = "\nThis is an additional line appended to the file."
with open("destination.txt", "a") as destination:
    destination.write(extra_text)

# Searching for a keyword
search_in_file("source.txt", "example")

<h2>🛠️ Setup and Installation</h2>

<h3>1️⃣ Prerequisites</h3>

Ensure that you have Python installed on your system. If not, download it from Python.org.

<h3>2️⃣ Running the Script</h3>

Clone the repository or copy the script to your local system.

Create a sample text file (source.txt) with some content.

Run the script using the following command:

python file_handler.py

📂 Folder Structure

📁 file-handler
 ┣ 📜 editing.py
 ┣ 📜 source.txt
 ┣ 📜 README.md

<h3>🌍 Use Cases</h3>

This script is useful in various scenarios, including:

Log File Analysis – Search for error messages in server logs.

Data Extraction – Read and process text-based datasets.

Document Editing – Modify and update textual content in files.

Text-Based Search Engines – Implement simple search mechanisms.

Backup Management – Copy and store file data securely.

<h2>📝 Understanding File Modes</h2>

Mode

Description

r

Read mode: Opens a file for reading (default).

w

Write mode: Overwrites existing content.

a

Append mode: Adds data without removing existing content.

r+

Read and write mode: Reads and writes to a file.

w+

Write and read mode: Overwrites and allows reading.

a+

Append and read mode: Appends data and allows reading.

<h2>🔍 Searching for Text in a File</h2>

The search function in this script is case-insensitive, meaning that searching for "Python" will match occurrences of "python," "PYTHON," or "PyThOn." This flexibility ensures accurate search results regardless of text formatting.

Example Usage

If source.txt contains the following text:

Python is a powerful language.
Learning Python is fun!
PYTHON is widely used in AI and Machine Learning.

Running:

python file_handler.py

With the search term "python," the output will be:

'python' found 3 times in source.txt.

<h2>⚠️ Important Considerations</h2>

Always verify file paths before running the script.

Use try-except blocks to handle file errors.

Remember that w mode erases existing content, so use a mode if you need to retain data.

Large file handling may require optimizations such as reading line by line instead of loading the entire file into memory.

<h2>🤝 Contributing</h2>

We welcome contributions! To contribute:

Fork the repository 📌

Create a new branch (feature-xyz)

Make your changes 🛠

Commit and push 🚀

Create a Pull Request ✅

✨ Contributors

Thanks to everyone who contributed to this project!

Yatharth Kelkar

<h2>📧 Contact</h2>

For queries, feel free to reach out:

<h3>📧 Email: </h3>
<li>kelkaryatharth@gmail.com</li>
<li>kelkaryatharth1@gmail.com</li>

🔥 Star this repository if you found it useful!

