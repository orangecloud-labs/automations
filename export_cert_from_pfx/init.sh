DIR=/media/data/scripts/certs
mkdir $DIR/data
rm -rf $DIR/data/certificate-file.cer
rm -rf $DIR/data/key-file.key
openssl pkcs12 -in $1 -clcerts -nokeys -out $DIR/data/certificate-file.cer
openssl pkcs12 -in $1 -nocerts -nodes  -out $DIR/data/key-encrypted.key
openssl rsa -in $DIR/data/key-encrypted.key -out $DIR/data/key-file.key
rm -rf $DIR/data/key-encrypted.key
echo "\nCERTIFICATE"
cat -v $DIR/data/certificate-file.cer
echo "\nKEY"
cat -v $DIR/data/key-file.key
if [ "$2" != "" ]; then
echo "**************** YOUR CERT IS BELOW THIS LINE ******************\n\n" >> $DIR/data/tmp
cat $DIR/data/certificate-file.cer >> $DIR/data/tmp
echo "\n\n**************** YOUR KEY IS BELOW THIS LINE ******************\n\n" >> $DIR/data/tmp
cat $DIR/data/key-file.key >> $DIR/data/tmp
mutt -s "cert" $2 < $DIR/data/tmp
rm -rf $DIR/data/tmp
fi
