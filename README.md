<h1 align="center">
  <br>
  <a href="https://github.com/SizzlinCheeks/HashTag"><img src="https://github.com/SizzlinCheeks/HashTag/assets/72412221/7ad47d70-69a8-4039-a854-1eaf01e9313b" alt="HashTag"></a>
  <br>
  HashTag
  <br>
</h1>

<p align="center">
  <a href="https://github.com/SizzlinCheeks/HashTag/releases">
    <img src="https://img.shields.io/github/v/release/SizzlinCheeks/HashTag.svg">
  </a>
  <a href="https://github.com/SizzlinCheeks/HashTag/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/SizzlinCheeks/HashTag.svg">
  </a>
</p>


<img width="576" src="https://github.com/SizzlinCheeks/HashTag/assets/72412221/295d2026-f4da-4def-bb26-3e2f3cfec2ad">


# HashTag

HashTag is a command-line tool for cracking hash values using various techniques, such as wordlist-based attacks and brute-force attacks. It supports multiple hash formats and provides flexibility in configuring the cracking process.

## Features

- Automatically finds hash formats
- Crack hash values using wordlist-based attacks
- Perform brute-force attacks to crack hash values
- Support for multiple hash formats
- Customizable options for hash cracking
- Cross-platform compatibility (Windows, macOS, Linux)

## Installation

To install HashTag, follow these steps:

1. Clone the repository:
```
git clone https://github.com/SizzlinCheeks/HashTag
```
2. Change into the project directory
```
cd HashTag
```
3. Run the installation script:

  - For Linux and macOS:
```
python3 install_hashtag.py
```
   
  - For Windows:
```
python install_hashtag.py
```

4. Follow the on-screen instructions to complete the installation.
5. You can now use 'hashtag' in your terminal!

## Usage

To use HashTag, run the `hashtag` command followed by the required options and arguments.

```
hashtag [-w WORDLIST] [-p HASHFILE] [-f FORMAT] [-show] [-b BRUTE_FORCE] [-bb FULL_BRUTE] [-k KEEP] [hash]
```

| Short | Long           | Argument      | Description                                                      
|-------|----------------|---------------|------------------------------------------------------------------
| -w    | --wordlist     | [WORDLIST]    | Path to the wordlist file                                        
| -p    | --hashfile     | [HASHFILE]    | Path to the file containing hashes                               
| -f    | --format       | [FORMAT]      | The Hash format to crack                                         
| -b    | --brute        | [BRUTE_FORCE] | String for brute-force (@:lowercase, $:uppercase, %:special, #:numeric, ^:lower + uppercase) |
| -k    | --keep         | [KEEP]        | Keep the hash file (Used in conjunction with --brute)            
| -show | --show         | [SHOW]        | Display help information                                         
| -bb   | --full-brute   | [BRUTE_FORCE] | Will run through every possibility of passwords (>3 char). Specify the max len of the password.
| -W    | --wordlist-sub | [WORDLIST_SUB]| Path to the Wordlist that will be used to create another wordlist
| -s    | --substring    | [SUBSTRING]   | Creates a string with '(WORD)' that will be used to substitute words from [WORDLIST_SUB].


## Examples

> **Note:** For more information and additional options, run `hashtag -show`.


1. Crack multiple hashes:
 ```
hashtag -w wordlist.txt -p hashes.txt
 ```
3. Crack a single hash:
 ```  
hashtag -w wordlist.txt 48bb6e862e54f2a795ffc4e541caed4d
 ```
3. Crack a list of hashes in a specific format:
 ```
hashtag -w wordlist.txt -f MD5 -p hashes.txt
 ```
4. Full-Brute Force doing all possible combinations from 3 - 5 chars:
```
hashtag -bb 5 48bb6e862e54f2a795ffc4e541caed4d
```
6. Brute-Force a hash with specific char and wildcards:
```
hashtag -b kang@@@@ 1A732667F3917C0F4AA98BB13011B9090C6F8065
hashtag -b kang@@@@ 1A732667F3917C0F4AA98BB13011B9090C6F8065 -k
```
7. Creates a Wordlist based off another Wordlist:
```
hashtag -W example.lst -s '(WORD)###'
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please check the [Contributing Guidelines](CONTRIBUTING.md) for more details.

## Authors

- John Hilde








