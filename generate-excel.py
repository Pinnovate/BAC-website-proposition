# -*- coding: utf-8 -*-

import xlsxwriter
from os import path
import random
import redis
import json

output_folder = 'output'
r = redis.StrictRedis(host='localhost', port=6379, db=0)

out_file = path.join(output_folder, 'random.xlsx')

workbook = xlsxwriter.Workbook(out_file)
worksheet = workbook.add_worksheet()

# Widen columns to make the text clearer.
worksheet.set_column('A:A', 10)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 20)
worksheet.set_column('F:F', 15)
worksheet.set_column('G:G', 15)
worksheet.set_column('H:H', 15)

# Add a bold format to use to highlight cells.

# Write some simple text.
worksheet.write('A1', 'Matricul')
worksheet.write('B1', 'Nom')
worksheet.write('C1', 'Prenom')
worksheet.write('D1', 'Filiere')
worksheet.write('E1', 'Lieu de naissance')
worksheet.write('F1', 'Date de naissance')
worksheet.write('G1', 'Moyenne')
worksheet.write('H1', 'Mention')


def randomword(length):
    valid_letters = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_letters += u'abcdefghijklmnopqrstuvwxyz'
    valid_letters += u'éèáàâûÁÀÈÉÇÙçÇïÔôîÏ'
    return ''.join(random.choice(valid_letters) for i in range(length))


def randoarabicmword(length):
    valid_letters = u'ءآأؤإئاب'
    valid_letters += u'ةتثجحخدذ'
    valid_letters += u'رزسشصضطظ'
    valid_letters += u'عغفقكلمن'
    valid_letters += u'هوىي'
    return ''.join(random.choice(valid_letters) for i in range(length))

# assuming there are 1750000 candidates
for condidate in range(1750000):
    row = condidate + 1

    matricul = str("%08d" % condidate)
    nom = randoarabicmword(10)
    prenom = randoarabicmword(10)
    filiere = randoarabicmword(20)
    lieu_de_naissance = randoarabicmword(15)
    date_de_naissance = randomword(13)
    moyenne = random.randint(9, 17)

    data = [{'matricule': matricul,
             'nom': nom,
             'prenom': prenom,
             'filiere': filiere,
             'lieu_de_naissance': lieu_de_naissance,
             'date_de_naissance': date_de_naissance,
             'moyenne': moyenne,
             }]

    r.set(matricul, json.dumps(data))

    # worksheet.write('A' + str(row), matricul)
    # worksheet.write('B' + str(row), nom)
    # worksheet.write('C' + str(row), prenom)
    # worksheet.write('D' + str(row), filiere)
    # worksheet.write('E' + str(row), lieu_de_naissance)
    # worksheet.write('F' + str(row), date_de_naissance)
    # worksheet.write('G' + str(row), moyenne)
    # worksheet.write('H' + str(row), mention)

workbook.close()
