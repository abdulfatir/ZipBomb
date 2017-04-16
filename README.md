# ZipBomb

This is for the people who watch Silicon Valley. In Season 3 Episode 7, Gilfoyle sends a sort of recursive program to Gavin Belson’s laptop and cellphone which forces him to shut down the power at Hooli. Watch [here](https://www.youtube.com/watch?v=UdAqU4GRR9Y). Such a program is called a *zip bomb*.

![ZipBomb](https://raw.githubusercontent.com/abdulfatir/ZipBomb/master/images/zipbomb.png)

What it is basically is a huge file with dummy data compressed to many levels to generate a very small compressed file. For example in a test run, this script of mine generates a compressed file of size **30.58 KB** which when decompressed is actually **10000000000 GB**. This is done to drain out a computer’s memory until it shuts down. Read More on [Wikipedia](https://en.wikipedia.org/wiki/Zip_bomb#Details_and_use).

This is a small script written in Python which generates such a zip bomb.

## Usage
`zipbomb.py n_levels out_zip_file`

## Sample Run

```bash
python zipbomb.py 10 out.zip  
```
### Output
```
Compressed File Size: 30.58 KB  
Size After Decompression: 10000000000 GB  
Generation Time: 10.40s
```



