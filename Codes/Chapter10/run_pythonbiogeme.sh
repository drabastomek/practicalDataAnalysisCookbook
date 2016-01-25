#/bin/sh

rm $1.html
rm $1.log
rm $1_param*
rm $1.tex
rm *.lis
rm headers.py
rm pythonparam.html

pythonbiogeme $1 $2