# Primeiros testes
```
$ source venv/bin/activate
$ python
```

```
>>> import io
>>> # Imports the Google Cloud client library
>>> from google.cloud import vision
>>> from google.cloud.vision import types
>>> def detect_text(path, uri=None):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    if uri:
        image.source.image_uri = uri 
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts: {}'.format(texts))
    return texts
```

```
>>> text = detect_text('/home/user/Projects/git/ocr-ticket-to-cloud/images/ticket.jpg')
>>> text.__getitem__(0)
locale: "pt-PT"
description: "COMPROVANTE DE REGISTRO DE PON\304\260O\nDO TRABAL HADOR\nRSOC\304\260ALABGRAUS TECNOLOGIA DA INFO\nRMACAD LTDA M\nOCAL AV. CARL US GME S, 0000 SAL A\n001 AXILIADORA PORTO ALEGRE\nNREP: 00014003750006110\nMODELO: IDCLASS BIO PROX\nCNPJ: 00.000.000/0001-0\nCEI:00.000.00000/00\nNOME: CARLOS EDUARDO\nPIS: xxxx.xxxxx.xx-x\nNSR: xxxxxxxxx\nDATA: 21/04/2018 HORA: 19:53\nDDMSMAYX7HG43K53XLI4WULLBEF 7AI45BZV\nTSGN455XT6YF BNRWVDVKIBB4TLKIREDYXA\n1\nABY\nA6\n5B4\nID\nLVI (\n0010C1021\n4M\nA5-\343\203\257\343\203\274\nC\nRRI 80 RRMCENIN DADSY\n"
bounding_poly {
  vertices {
    x: 1215
    y: 342
  }
  vertices {
    x: 3254
    y: 342
  }
  vertices {
    x: 3254
    y: 1859
  }
  vertices {
    x: 1215
    y: 1859
  }
}

>>> text.__getitem__(1)
description: "COMPROVANTE"
bounding_poly {
  vertices {
    x: 1271
    y: 1753
  }
  vertices {
    x: 1252
    y: 1313
  }
  vertices {
    x: 1365
    y: 1308
  }
  vertices {
    x: 1384
    y: 1748
  }
}

>>> text.__getitem__(2)
description: "DE"
bounding_poly {
  vertices {
    x: 1273
    y: 1263
  }
  vertices {
    x: 1270
    y: 1194
  }
  vertices {
    x: 1355
    y: 1190
  }
  vertices {
    x: 1358
    y: 1259
  }
}

>>> def get_words(text):
    words = []
    for t in text:
        words.append(t.description.encode('utf-8'))
    return words

>>> def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except:
        return False
    return True

>>> def is_valid_time(time):
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except:
        return False
    return True

>>> get_words(text)
['COMPROVANTE DE REGISTRO DE PON\xc4\xb0O\nDO TRABAL HADOR\nRSOC\xc4\xb0ALABGRAUS TECNOLOGIA DA INFO\nRMACAD LTDA M\nOCAL AV. CARL US GME S, 1000 SAL A\n001 AXILIADORA PORTO ALEGRE\nNREP: 000000000000000\nMODELO: IDCLASS BIO PROX\nCNPJ: 00.000.000/0001-0\nCEI:00.000.00000/00\nNOME: CARLOS EDUARDO\nPIS: xxxx.xxxxx.xx-x\nNSR: xxxxxxxxx\nDATA: 21/04/2018 HORA: 19:53\nDDMSMAYX7HG43K53XLI4WULLBEF 7AI45BZV\nTSGN455XT6YF BNRWVDVKIBB4TLKIREDYXA\n1\nABY\nA6\n5B4\nID\nLVI (\n0010C1021\n4M\nA5-\xe3\x83\xaf\xe3\x83\xbc\nC\nRRI 80 RRMCENIN DADSY\n', 'COMPROVANTE', 'DE', 'REGISTRO', 'DE', 'PON\xc4\xb0O', 'DO', 'TRABAL', 'HADOR', 'RSOC\xc4\xb0ALABGRAUS', 'TECNOLOGIA', 'DA', 'INFO', 'RMACAD', 'LTDA', 'M', 'OCAL', 'AV.', 'CARL', 'US', 'GME', 'S,', '1610', 'SAL', 'A', '802', 'AXILIADORA', 'PORTO', 'ALEGRE', 'NREP:', '000000000000000', 'MODELO:', 'IDCLASS', 'BIO', 'PROX', 'CNPJ:', '00.000.000/0001-0', 'CEI:00.000.00000/00', 'NOME:', 'CARLOS', 'EDUARDO', 'BERTON', 'PIS:', 'xxxx.xxxxx.xx-x', 'NSR:', 'xxxxxxxxx', 'DATA:', '21/04/2018', 'HORA:', '19:53', 'DDMSMAYX7HG43K53XLI4WULLBEF', '7AI45BZV', 'TSGN455XT6YF', 'BNRWVDVKIBB4TLKIREDYXA', '1', 'ABY', 'A6', '5B4', 'ID', 'LVI', '(', '0010C1021', '4M', 'A5-', '\xe3\x83\xaf\xe3\x83\xbc', 'C', 'RRI', '80', 'RRMCENIN', 'DADSY']

>>> for word in get_words(text):
    if is_valid_date(word):
        print('Date: {}'.format(word))
    if is_valid_time(word):
        print('Time: {}'.format(word))

Date: 21/04/2018
Time: 19:53

>>> def check_label(words, labels=[]):
    for index, word in enumerate(words):
        if is_valid_date(word) and words[index-1] in labels:
            print('Date: {}'.format(word))
        if is_valid_time(word) and words[index-1] in labels:
            print('Time: {}'.format(word))

>>> check_label(words, labels=['TIME:'])
>>>
>>> check_label(words, labels=['DATA:'])
Date: 21/04/2018
>>> check_label(words, labels=['DATA:', 'HORA:'])
Date: 21/04/2018
Time: 19:53

```

## Using Datastore API
```
import ticket
from google.cloud import datastore
client = datastore.Client('mycalendar-158220')
ticket.get_today_start_time(client)

```