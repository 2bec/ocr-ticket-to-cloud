# ocr-ticket-to-cloud
A partir de uma foto do ticket guardamos as informações na nuvem.

# Requirements
- ImageMagick
- Textcleaner
- Tesseract

# Textcleaner
USAGE: ` textcleaner [-r rotate] [-l layout] [-c cropoff] [-g] [-e enhance ] [-f filtersize] [-o offset] [-u] [-t threshold] [-s sharpamt] [-s saturation] [-a adaptblur] [-T] [-p padamt] [-b bgcolor] infile outfile `

# Convert
USAGE: ` convert -respect-parenthesis \( files/original/original.png -set colorspace RGB -colorspace gray -type grayscale -set colorspace RGB -normalize \) \( -clone 0 -set colorspace RGB -colorspace gray -negate -lat 35x35+8% -contrast-stretch 0 -blur 0.05x65535 -level 25x90% \) -compose copy_opacity -composite -fill white -opaque none +matte -sharpen 0x0.2 -antialias -black-point-compensation -black-threshold 70% files/to_ocr/final.png `

# Tesseract
USAGE: ` tesseract files/to_ocr/final.png output.txt -l por+eng `

# Referências
1. [http://www.fmwconcepts.com/imagemagick/textcleaner/index.php](http://www.fmwconcepts.com/imagemagick/textcleaner/index.php)
2. [http://tpgit.github.io/Leptonica/skew_8c_source.html](http://tpgit.github.io/Leptonica/skew_8c_source.html)
3. [https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality)
