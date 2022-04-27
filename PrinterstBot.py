# -*- coding: utf-8 -*-
"""

Wejscie:
    plik txt z id kazdy kolejny wiersz to nowe id
    
Proces:
    otwiera chrome 
    wpisuje link (webbrowser)
    poibiera zdjecie (uzywa pyautosearch)
    
Wyjscie:
    Pliki .jpg/.png

@author: Wojtek







Dziala tylko na lewym ekranie (Głównym)



"""

import webbrowser
import time

# wybrac z tych te ktore potrzebuje
from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch_region_loop, region_grabber, imagesearch_numLoop, imagesearch
import pyautogui
import keyboard

x1 =  2880
y1 = 0
x2 = 5399
y2 = 1574
is_retina = False # chuj wie po co to ale cos z jakoscia chyba

def read_ids(filepath):
    '''
    filepath - path to ids
    return array of ids
    '''
    with open(filepath) as f:
        content = f.read().splitlines()
    return content

def move(ikona):
    '''
    Move mouse on given icon
    '''

    pos = imagesearch(ikona)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])


def action(ikona,click=True):
    '''
    wymyslic cos lepszego do czekania jak mi wkurw zejdzie
    '''
    
    move(ikona)
    if click ==True:
        pyautogui.click()

def open_url(ids):
    '''
    ids - array of id
    '''
    for id in ids: 
        url = 'https://pl.pinterest.com/pin/{}/'.format(id)
        webbrowser.register('chrome',
        	None,
        	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url,new=0)
        time.sleep(4.5)
        download_pin()
        

def download_pin():
    posa = imagesearch_numLoop("trzykropek.jpg", 1, 2)
    if posa[0] != -1:
        pyautogui.moveTo(posa[0], posa[1])
        pyautogui.click()
    else:
        return
    time.sleep(0.8)
    action("Pobierz_obraz.jpg")
    time.sleep(0.8)
    pos = imagesearch_numLoop("Zapisz.jpg", 1, 2)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        #1056 441
        pyautogui.moveTo(1056, 441)
        pyautogui.click()
        keyboard.press_and_release('ctrl+w')

        
if __name__ == "__main__":
    ids = read_ids('Ids.txt')
    open_url(ids)

    #action("trzykropek.jpg")
    #pos = imagesearch_numLoop("trzykropek.jpg", 1, 2)
    #print(pos)
    #pyautogui.moveTo(pos[0], pos[1])
