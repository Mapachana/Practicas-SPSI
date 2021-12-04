# Firmar y cifrar PDF

### Emisor: Eve

Eve tiene `eve.key.pem`, `eve.cert.pem`, `bob.cert.pem` y `gdh.pdf`.

Primero, se convierte el PDF a base64:

`openssl base64 -in gdh.pdf -out gdh.pdf.b64`

Firma del pdf:

`openssl smime -sign -in gdh.base -out gdh.base.sgn -signer eve.cert.pem -inkey eve.key.pem -text`

Cifrado del PDF:

`openssl smime -encrypt -in gdh.base.sgn -out gdh.base.sgn.enc bob.cert.pem`

Envía `gdh.base.sgn.enc` a bob.

### Receptor: Bob

Bob tiene `bob.key.pem`, `bob.cert.pem`, `eve.cert.pem`.

Bob recibe `gdh.base.sgn.enc`.

Descifrado del PDF:

`openssl smime -decrypt -in gdh.base.sgn.enc -out gdh.base.sgn -recip bob.cert.pem -inkey bob.key.pem`

Comprobación de que el firmante es Eve:

`openssl smime -pk7out -in gdh.base.sgn | openssl pkcs7 -print_certs -noout`

Verificación del mensaje:


`openssl smime -verify -text -in gdh.base.sgn -noverify -out gdh.base`

Decodificación del PDF en base 64:

`openssl base64 -d -in gdh.base -out gdh.pdf`

Lectura del PDF:

`evince gdh.pdf`