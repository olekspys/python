import os
import fnmatch

# List of file name patterns to exclude from scanning (now supports wildcards and is case-insensitive)
excluded_files = [
    '*.3gp',
    '*.7z',
    '*.aps',
    '*.avi',
    '*.bin',
    '*.bmp',  
    '*.chm',
    '*.cur',
    '*.dat',
    '*.def',
    '*.dll',
    '*.doc',
    '*.docx',
    '*.eot',
    '*.emz',
    '*.exe.local',
    '*.exe',        
    '*.gif',
    '*.gz',
    '*.hlp',
    '*.ico',  
    '*.jasper',
    '*.jar',
    '*.jpeg', 
    '*.jpg', 
    '*.lib',
    '*.log',
    '*.model',
    '*.mp3',
    '*.msi',
    '*.noexp',
    '*.nupkg',
    '*.ocd',
    '*.otf',
    '*.pak',
    '*.pbix',
    '*.pdf',
    '*.png',
    '*.ppt',
    '*.pptx',
    '*.reg',
    '*.rgs',
    '*.rtf', 
    '*.sha512',
    '*.sln',
    '*.snupkg',
    '*.swf',
    '*.tgz',
    '*.tiff',
    '*.thmx',
    '*.tlb',
    '*.ttf',
    '*.txt',    
    '*.vsd',    
    '*.wav',
    '*.woff',
    '*.woff2',
    '*.ws',
    '*.xls',
    '*.xlsx',
    '*.xpi',
    '*.xz',
    '*.zip',
    'pom.xml',
    'readme'
]

# Mapping file name patterns (mask) to programming languages
file_masks = {
    # ActionScript
    '*.as': 'ActionScript',    
    # Assembly Language
    '*.asm': 'Assembly Language',
    '*.S': 'Assembly Language',
    # AIDL
    '*.aidl': 'AIDL',
    # AWK
    '*.awk': 'AWK',
    # Batch Script
    '*.bat': 'Batch Script',
    '*.cmd': 'Batch Script',
    # Bean Shell
    '*.bsh': 'Bean Shell',    
    # Bison
    '*.yy': 'Bison',
    # C/C++
    '*.c': 'C/C++',
    '*.cc': 'C/C++',
    '*.cpp': 'C/C++',
    '*.cxx': 'C/C++',
    '*.h': 'C/C++',
    '*.hpp': 'C/C++',
    '*.hxx': 'C/C++',
    '*.inl': 'C/C++',
    '*.ixx': 'C/C++',
    '*.rc': 'C/C++',
    '*.rc2': 'C/C++',
    '*.vcxproj': 'C/C++',
    '*.vcxproj.filters': 'C/C++',
    # C#
    '*.cs': 'C#',
    '*.cshtml': 'C#',
    '*.csproj': 'C#',
    # Clarion
    '*.clw': 'Clarion',
    '*.clx': 'Clarion',
    # CoffeeScript
    '*.coffee': 'CoffeeScript',
    # CSS
    '*.css': 'CSS',
    '*.less': 'CSS',
    '*.scss': 'CSS',
    # Extensible Hypertext Markup Language
    '*.xhtml': 'Extensible Hypertext Markup Language',    
    # Extensible Stylesheet Language
    '*.xlst': 'Extensible Stylesheet Language',
    '*.xsl': 'Extensible Stylesheet Language',
    # Flavored Markup Language
    '*.fml': 'Flavored Markup Language',
    # Groovy
    '*.groovy': 'Groovy',
    # Handlebars
    '*.hbs': 'Handlebars',
    # Hack
    '*.hhi': 'Hack',
    # HQL
    '*.hql': 'HQL',
    # HTML
    '*.htm': 'HTML',
    '*.html': 'HTML',
    # Interface Definition Language
    '*.idl': 'Interface Definition Language',
    # Java
    '*.ja': 'Java',
    '*.jav': 'Java',
    '*.java': 'Java',
    '*.jsp': 'Java',
    # JavaScript
    '*.js': 'JavaScript',
    # JSON Schema
    '*schema*json': 'JSON Schema',
    # JSON
    '*.json': 'JSON',
    # LLVM IR
    '*.ll': 'LLVM IR',
    # M4 Macro
    '*.m4': 'M4 Macro',
    # Makefile (all variations)
    'makefile': 'Makefile',
    'makefile*': 'Makefile',
    'make.*': 'Makefile',
    '*.mak': 'Makefile',
    '*.makefile': 'Makefile',
    # Object Description Language
    '*.odl': 'Object Description Language',
    # Perl
    '*.pl': 'Perl',
    '*.pm': 'Perl',
    # PHP
    '*.php': 'PHP',
    '*.phps': 'PHP',
    '*.phpt': 'PHP',
    '*.phtml': 'PHP',
    # PowerShell Script
    '*.ps1': 'PowerShell Script',
    # Python
    '*.py': 'Python',
    # Ruby
    '*.rb': 'Ruby',
    # SQL
    '*.sql': 'SQL',
    # Typescript
    '*.ts': 'Typescript',
    # Unified Modeling Language
    '*.uml': 'Unified Modeling Language',
    # Unix Shell Script
    '*.sh': 'Unix Shell Script',
    '*.bash': 'Unix Shell Script',
    # VB Script
    '*.vbs': 'VB Script',
    # Velocity Template Language
    '*.vm': 'Velocity Template Language',
    # XAML
    '*.xaml': 'XAML',
    # XML
    '*.jrxml': 'XML',
    '*.wsdl': 'XML',
    '*.xml': 'XML',
    '*.xmlt': 'XML',
    '*.xsc': 'XML',
    '*.xsd': 'XML',
    # XQuery
    '*.xquery': 'XQuery',
    # XSLT
    '*.xslt': 'XSLT',
    '*.xss': 'XSLT',
    # Yacc
    '*.y': 'Yacc',
    # YAML
    '*.yaml': 'YAML',
    '*.yml': 'YAML'
}

# Function to detect the programming language of a file
def detect_language(file_path):
    filename = os.path.basename(file_path).lower()  # Convert filename to lowercase for case-insensitive matching
    
    # Check if the file name matches a predefined mask (pattern)
    for mask, language in file_masks.items():
        # Convert mask to lowercase for case-insensitive matching
        if fnmatch.fnmatch(filename, mask.lower()):
            return language
    
    # If no match by name or extension, analyze the file's content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Convert content to lowercase for case-insensitive content matching

            # Simple content-based analysis (add more signatures if needed)
            if '/bin/awk' in content:
                return 'AWK'
            elif '/bin/bash' in content:            
                return 'Unix Shell Script'
            elif 'bin/env ksh' in content:
                return 'Unix Shell Script'
            elif 'bin/ksh' in content:
                return 'Unix Shell Script'
            elif 'usr/bin/env sh' in content:
                return 'Unix Shell Script'
            elif 'bin/env perl' in content:
                return 'Perl'
            elif '/usr/bin/python' in content:
                return 'Python'
            elif '/bin/expect' in content:            
                return 'Expect Script'
            elif '/bin/ksh' in content:
                return 'Unix Shell Script'
            elif 'bin/perl' in content:
                return 'Perl'
            elif '/bin/sh' in content:
                return 'Unix Shell Script'
            elif '<?php' in content:
                return 'PHP'
            # Add other content-based language signatures if needed
    except:
        return None

    return None

# Function to check if a file should be excluded based on patterns (now case-insensitive)
def is_excluded(file_path):
    filename = os.path.basename(file_path).lower()  # Convert filename to lowercase for case-insensitive matching
    
    # Exclude based on extension or specific filename using patterns
    for mask in excluded_files:
        # Convert mask to lowercase for case-insensitive matching
        if fnmatch.fnmatch(filename, mask.lower()):
            return True
    return False

# Main function to scan the directory
def scan_directory(directory):
    language_usage = {}
    unknown_files = []  # List to store files with undetermined languages
    
    for root, dirs, files in os.walk(directory):
        # Exclude the .svn directory from the scan
        if '.svn' in dirs:
            dirs.remove('.svn')
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip excluded files based on patterns
            if is_excluded(file_path):
                print(f"Skipping excluded file: {file_path}")
                continue
            
            language = detect_language(file_path)
            
            if language:
                # Dynamic output of each file being processed
                print(f"File: {file_path} -> Language: {language}")
                
                if language in language_usage:
                    language_usage[language] += 1
                else:
                    language_usage[language] = 1
            else:
                # Store files with undetermined languages
                unknown_files.append(file_path)

     # Sort unknown files first by their extension and then by the full file path
    unknown_files_sorted = sorted(unknown_files, key=lambda f: (os.path.splitext(f)[1], f.lower()))

    return language_usage, unknown_files_sorted

# Ask the user to input the path to the directory
directory_path = input("Enter the path to the source code directory: ")

# Check if the provided path is valid
if not os.path.isdir(directory_path):
    print(f"Directory '{directory_path}' not found.")
else:
    # Analyze the specified directory
    languages_detected, unknown_files = scan_directory(directory_path)

    # Output list of files with undetermined language first
    if unknown_files:
        print("\nFiles for which the programming language could not be determined:")
        for file in unknown_files:
            print(file)
        print(f"\nTotal number of files with undetermined language: {len(unknown_files)}")
    else:
        print("\nAll files were successfully analyzed.")

    # Final output of the summary, sorted alphabetically
    print("\nProgramming languages used (final result, sorted alphabetically):")
    for lang in sorted(languages_detected):
        print(f"{lang}: {languages_detected[lang]} files")
