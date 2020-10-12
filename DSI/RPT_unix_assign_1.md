# Part 1: 
## Aliases
* Add to ~/.zshrc using vim
* run source ~/.zshrc or . ~/.zshrc or restart terminal to apply changes
* alias [custom-alias]="[command]"

## Shell scripts
* in ~/.zshrc, added (head -n 5 ; echo "==========" ; tail -n 5) as alias 'inspect'
* tested on the xml file, it works. 


# Part 2: Wikipedia Data
* wget downloads and reads a file from the internet
* [curl vs wget](https://www.baeldung.com/linux/curl-wget)
    * We can treat curl as a general-purpose tool for transferring data to or from a server.
    * On the other hand, wget is basically a network downloader.
    * curl does not provide recursive download
    * wget can be used to download a local copy of remote websites, including all sublinks
    * default depth 5, override with -l
* Can curl be used instead of wget? 
    * yes, but you would need to pipe it to a file, whereas wget automatically pipes to a file
* file type? how to unzip
    * file cvwiki_20160405_testsamples.xml.bz2
    * bzip2 (binary zip file)
    * bzip2 -d filename.bz2
    * once unpacked, this is an xml file
        * HTML document test, UTF-8 Unicode text
* file size? number of lines? 
    * ls -lh file name 
        * 1.8M
    * wc -l or grep -c ".*" [filename]
        * 33805 lines

# Examining the file
* head/tail 
* structure is code for a webpage
*  sed -n '4,8'p thegeekstuff.txt

# Exploratory Analysis
* how many contributors?
    * grep -o 'search term' file | wc -l
    * 546
* how many users identified by 'username'?
    * 542

* Who are the most common contributors by username?
    * sed '/username/!d' cvwiki_20160405_testsamples.xml | sort | uniq -c | sort -nr | head  -100
    * 157       <username>Viktor</username>
    * 77         <username>Addbot</username>
    * 64         <username>Chuvash2014</username>
    * 53         <username>EmausBot</username>
    * 49         <username>YiFeiBot</username>

* How many of the contributors are bots?
    * grep -i 'bot' cvwiki_20160405_testsamples.xml | wc -l
    * 396

* Advanced: What are the other contributors -- i.e., those entries which have a <contributor> tag but not a nested <username> tag? Hint: use sed or perl. How many of these contributors are there? Do they explain all of the missing contributors?
* sed -e '/contributor/,/[\/]contributor/!d' cvwiki_20160405_testsamples.xml
* this did not exclude username tags
    
<contributor>
        <username>EmausBot</username>
        <id>4769</id>
    </contributor>
    <contributor>
        <username>YiFeiBot</username>
        <id>15021</id>
    </contributor>

* sed -e '/contributor/,/[\/]contributor/!d' cvwiki_20160405_testsamples.xml | wc -l
    * 2180 lines
    * 2180/4 = 545
    * This approach doesn't work
* From Ryan: for the kind of regex match you want above, the two approaches I can think of are to use a negative character match [^<]* would match any number of characters that aren't <  which would help you avoid additional tags before the end tag.
The other approach is to use negative lookaheads: (?!.*username).* means "don't match any characters followed by username, but DO match any characters otherwise".
    * I couldn't get the syntax to work. Played around on regex101 and was getting error messages even on scripts that worked in previous parts of the exercise. 
