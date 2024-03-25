Open SSL Training and Commands
==============================

Basics of Certificates
----------------------

Create RSA Key
**************

.. code-block:: console

    $ openssl genrsa

The output prints the private key generated using the openssl command.

.. code-block:: console

    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCy/6PiA5XDKdpd
    q00vBsBss8gBtqaKf6cKzHWyXacSyonjsHNTcQ4a1PEG4SkGPBZvWDKm8Uz9C6nY
    and ********************* and so on...
    KxEkcgmqXojldD0ow/G7j6OWUlN92H54HYsH+dntJZ5Y7QpkcyfsQ9ZJ4DfnFV0J
    5ZdqS5/MKePxKl40uWu/qyJH
    -----END PRIVATE KEY-----

.. caution::

    The above key was generated with out any pass phrase. Which means it can be copied and re used. 

RSA pvt key with encryption
***************************
In this method we use the same command but with additional flags. 

.. code-block:: console

    $ openssl genrsa --aes256

Upon running above command, you will be asked for passphrase. This pass phrase is used to encrypt the generated private key. 

.. code-block:: console

    Enter PEM pass phrase:
    Verifying - Enter PEM pass phrase:

.. note::
    
    The final generated output is the encrypted private key. And AES 256 bit algorithm is used to encrypt the rsa pvt key. Remember AES is still a symetric key encryption algorithm. 


Pvt Key Generation To File
**************************

.. code-block:: console

    $ openssl genrsa -aes256 -out private.pem

.. note::

    .pem file extension is used to store certificate related information or private keys. 

.. note:: -out

    This flag allows to write output directly to file. -out <filename>


Public Key from Pvt Key
***********************
In the above section we have generated private key. Now lets generate the public key from the generated private key

.. code-block:: console

    $ openssl rsa -in private.pem -outform PEM -pubout -out public.pem

.. note:: 

    Above command requires two things. 1. input private key and 2. Passphrase used to generate the private key. The final public key is written to public.pem file.

RSA key 4096 Generation
***********************
To create a more stronger 4096 bit encrypted pvt key without encryption

.. code-block:: console

    $ openssl genrsa 4096

Since its 4096 bits, the time taken to create the key is longer. And the final generated key is not encrypted. 


Understanding Cert Chains
-------------------------

Types of certs
**************

**Root Cert:** This cert does not issue certs. It is the root entity in the chain of trust
**Intermediate Cert:** Intermediate CA issues the certs. 

**Domain Cert:** All the SANs or wildcard domain is mentioned over here in this certificate. When you check the issuer information, you will find the intermediate cert CA as the issuer. 

.. image:: _static/images/pki.svg
    :width: 700

Here the Root CA is Self-signed (:ref:`Definitions`).
- Every certificate, Root, Intermediate, & Server will have its own private and public keys. 
- Only Root key signature is created using its own private key which is called self-signing :ref:`Definitions`
- Intermediate cert is signed using Root CA's private key. 
- Server cert is signed using Intermediate CA's private key.


.. _Definitions:
        
Keyword Definitions
-------------------

.. list-table:: Key Words & Definitions
   :widths: 25 75
   :header-rows: 1

   * - Term
     - Definition
   * - Self-Signed certificate
     - When the signature is created from its own pvt key, its called self-signed. Usually root certs are self signed. But, intermediate certs are signed using the Root CA's pvt key.


