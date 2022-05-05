"""
This little script can generate a valid .vcf (vCard). It will ask you to fill
in some details and write the vcf-file.
"""

import qrcode

first_name = 'Amna'
last_name = 'Alnour'
email = 'amna@jollytours.ro'
company = 'Jolly Tours & Holiday SRL'
company_role = 'Tourism Agency'
title = 'Visa Consultant'
phone_number = '+40753015047'
phone_number2 = '+40213215240'
address_street = 'Str. Polona 10 Etj 2 Ap 3'
address_city = 'Bucharest'
address_zip = '010502'
address_country = 'Romania'
website = 'www.jollytours.ro'
data = f'''BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name}
FN:{first_name} {last_name}
ORG:{company}
TITLE:{title}
EMAIL;WORK;PREF;INTERNET:{email}
TEL;WORK:{phone_number}
TEL;WORK:{phone_number2}
ADR;TYPE=WORK:;;{address_street};{address_city};;{address_zip};{address_country}
ROLE:{company_role}
URL;TYPE=pref:{website}
END:VCARD'''

img = qrcode.make(data)
img.save(f'{first_name}.png')


