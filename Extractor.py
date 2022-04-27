# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:15:00 2021

@author: Wojtek
"""

#import os


#string = 'asdsda"asdda" jebac "policje" jebac "kurwy" jebac "pis" test 10 zankow zeby nie wyjebalo calogun'
#string = '<div data-test-id="pin" data-test-pin-id="20266267062020719" style="height: 100%;"><div class="zI7 iyn Hsu" style="height: 100%;"><div data-test-id="pinWrapper" class="Jea XiGight: 336px;"><div style="padding-bottom: 16px; padding-left: 8px; padding-right: 8px;"><div data-test-id="pin" data-test-pin-id="93660867241256801" style="height: 100%;"><div class="zI7: 8px;"><div data-test-id="pin" data-test-pin-id="460141286915820762" style="height: 100%;"><div class="zI'
#strings = 'nieznajdz'

import numpy as np

def extract_id(string,string_to_find):
    '''
    .find (value, start, end)
    Finds Pin ID from string
    zwraca id
    jesli nie ma id w string zwraca False
    '''

    index = (string.find(string_to_find))
    if index != -1:
        txt_number_add = len(string_to_find)
        #txtk = index+10
        print(index) # odjac 1 bo indexowanie od 0
        print(txt_number_add)
        index_poczatkowy = index+txt_number_add
        print("Pierwsza cyfra ID to: ",string[index_poczatkowy]) # pierwsza cyfra z pinId

        # zeby znalezc ostatnia wyszukac od pierwszej do "
        index_koncowy = index+txt_number_add+22
        koncowa_cyfra_id_index = string.find('"',index_poczatkowy,index_koncowy)#dluzsze niz 22cyfry nie powinno byc Id
        print("koncowa cyfra Id to: ",string[koncowa_cyfra_id_index])
        id = string[index_poczatkowy:koncowa_cyfra_id_index]
        return id
        #test_string = string.replace('jebac "',"",1) # USUWA WSZYSTKIE JEBAC NIEDOBRZE
        #print(test_string)
    else:
        return False



def delete_extracted(string,string_to_find):
    '''
    Deletes extracted before pin ID
    Przyjmuje string i zwraca string usuniety
    ** Na poczatku moze usunac wszystkie nieistotne z poczatku(optymalizacja)
    '''
    tab = []
    while True:
        index = (string.find(string_to_find))
        if index != -1:
            txt_number_add = len(string_to_find)
            #txtk = index+10
            #print(index) # odjac 1 bo indexowanie od 0
            #print(txt_number_add)
            index_poczatkowy = index+txt_number_add
           # print("Pierwsza cyfra ID to: ",string[index_poczatkowy]) # pierwsza cyfra z pinId

            # zeby znalezc ostatnia wyszukac od pierwszej do "
            index_koncowy = index+txt_number_add+22
            koncowa_cyfra_id_index = string.find('"',index_poczatkowy,index_koncowy)#dluzsze niz 22cyfry nie powinno byc Id
            #print("koncowa cyfra Id to: ",string[koncowa_cyfra_id_index])
            id = string[index_poczatkowy:koncowa_cyfra_id_index]
            if len(id)>30: #zle zrobione jest cos i dodaje w chuj tekstu w niektorych przypadkach
                pass
            else:
                tab.append(id)
            string = string.replace(string_to_find,"",1)
        else:
            print("wykonano")
            break
    return tab


def open_file(filepath):
    tab = []
    with open(filepath, 'r',encoding='utf8') as inF:
        for line in inF:
            if 'n-id="' in line:
                tab_append = delete_extracted(line,'n-id="')
                tab.append(tab_append)

    return tab

def save_to_file(array):
    with open('Ids.txt', 'w') as f:
        for item in array:
            f.write("%s\n" % item)

def main():

    id_array = []
    id = extract_id(string,'n-id="')
    print(id)
    id_array.append(id)
    tab = delete_extracted(string,'n-id="')
    print(len(tab))
    print(tab)

    filepath = "C:/Users/Wojtek/Desktop/wojtek/Instagram_Database/pinterest/extractPinId/PinterestMainScaleUnzoomMax.html"
    tab = open_file(filepath)
    flat_list = []
    for sublist in tab:
        for item in sublist:
            flat_list.append(item)

    # USUWA POWTORZENIA (CHOC I TAK NIE POWINNO ICH BYC)
    flat_list = list(set(flat_list))
    print(flat_list)
    print(len(flat_list))
    save_to_file(flat_list)

main()
