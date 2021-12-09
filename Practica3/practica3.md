# Firmar y cifrar PDF

### Emisor: Eve

Eve tiene `eve.key.pem`, `eve.cert.pem`, `bob.cert.pem` y `gdh.pdf`.

Primero, se convierte el PDF a base64:

`openssl base64 -in gdh.pdf -out gdh.pdf.b64`

Firma del pdf:

-signer: indica quién es el firmante (certificado/llave publica, va incluida en el mensaje firmados)
-inkey: indica la llave privada
-text: lo hace en modo texto

`openssl smime -sign -in gdh.pdf.b64 -out gdh.pdf.b64.sgn -signer eve.cert.pem -inkey eve.key.pem -text`

Cifrado del PDF:

El certificado que se usa es el de a quién va dirigido.

Nota: Esto es equivalente a cifrar usando aes256, porque es la opcion por defecto. Se puede elegir el metodo de cifrado, el comando sería openssl smime -encrypt -aes256 -in gdh.pdf.b64.sgn -out gdh.pdf.b64.sgn.enc bob.cert.pem


`openssl smime -encrypt -in gdh.pdf.b64.sgn -out gdh.pdf.b64.sgn.enc bob.cert.pem`

Envía `gdh.pdf.b64.sgn.enc` a bob.

### Receptor: Bob

Bob tiene `bob.key.pem`, `bob.cert.pem`, `eve.cert.pem`.

Bob recibe `gdh.pdf.b64.sgn.enc`.

Descifrado del PDF:

`openssl smime -decrypt -in gdh.pdf.b64.sgn.enc -out gdh.pdf.b64.sgn -recip bob.cert.pem -inkey bob.key.pem`

Comprobación de que el firmante es Eve:

-pk7out: indica un formato
-noout: Para que imprima los datos por pantalla

`openssl smime -pk7out -in gdh.pdf.b64.sgn | openssl pkcs7 -print_certs -noout`

Verificación del mensaje:

- El noverify es para que no vaya a la web donde estan las vigencias de los certificados


`openssl smime -verify -text -in gdh.pdf.b64.sgn -noverify -out gdh.pdf.b64`

Decodificación del PDF en base 64:

`openssl base64 -d -in gdh.pdf.b64 -out gdh.pdf`

Lectura del PDF:

`evince gdh.pdf`