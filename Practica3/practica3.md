# Firmar y cifrar PDF

### Emisor: Eve

Eve tiene `eve.key.pem`, `eve.cert.pem`, `bob.cert.pem` y `gdh.pdf`.

Primero, se convierte el PDF a base64:

`openssl base64 -in gdh.pdf -out gdh.pdf.b64`

Firma del pdf:

`openssl smime -sign -in gdh.pdf.b64 -out gdh.pdf.b64.sgn -signer eve.cert.pem -inkey eve.key.pem -text`

Cifrado del PDF:

`openssl smime -encrypt -in gdh.pdf.b64.sgn -out gdh.pdf.b64.sgn.enc bob.cert.pem`

Envía `gdh.pdf.b64.sgn.enc` a bob.

### Receptor: Bob

Bob tiene `bob.key.pem`, `bob.cert.pem`, `eve.cert.pem`.

Bob recibe `gdh.pdf.b64.sgn.enc`.

Descifrado del PDF:

`openssl smime -decrypt -in gdh.pdf.b64.sgn.enc -out gdh.pdf.b64.sgn -recip bob.cert.pem -inkey bob.key.pem`

Comprobación de que el firmante es Eve:

`openssl smime -pk7out -in gdh.pdf.b64.sgn | openssl pkcs7 -print_certs -noout`

Verificación del mensaje:


`openssl smime -verify -text -in gdh.pdf.b64.sgn -noverify -out gdh.pdf.b64`

Decodificación del PDF en base 64:

`openssl base64 -d -in gdh.pdf.b64 -out gdh.pdf`

Lectura del PDF:

`evince gdh.pdf`