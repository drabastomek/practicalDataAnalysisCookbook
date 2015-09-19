#/bin/bash

for f in *.dot;
    do echo Processing ${f%.*};
    dot -Tpdf $f -o ${f%.*}.pdf
done