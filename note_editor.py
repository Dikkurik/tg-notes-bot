# -*- coding: utf-8 -*-
import os
from config import config



class Note():
    def __init__(self, ):
        """
        Define notes folder and extension for file.
        """
        self._path_to_folder = config.NOTE_FOLDER
        self._ext = config.FILE_EXT

    def createNote(self, message: str):
        """
        When this metod called it create file with name
        """
        self.name = message.split('\n')[0]
        self.note = message.removeprefix(f"{self.name}\n")
        
    def saveToFile(self,):
        """
        Saving file to folder defined in config.cfg
        """
        with open(f"{self._path_to_folder}\{self.name}.{self._ext}", "w", encoding="UTF-8") as note_file:
            note_file.write(self.note)
        print(f"Note saved to {self._path_to_folder}")

    def getNotes(self):
        """
        Return list of all files in folder
        """
        listfile = os.listdir(self._path_to_folder)
        note_list = ""
        for file in listfile:
            note_list=note_list+f"{file}\n"
        return note_list
    
    def readNote(self, filename):
        with open(f"{self._path_to_folder}\{filename}.{self._ext}", "r", encoding="UTF-8") as note:
            note_text = note.read()
        print(note_text)
        return note_text

    def editNote(self, filename: str, text: str):
        with open(f"{self._path_to_folder}\{filename}.{self._ext}", "r", encoding="UTF-8") as note:
            note_text = note.read()
        note_text = note_text+f"{text}\n"

        with open(f"{self._path_to_folder}\{filename}.{self._ext}", "w", encoding="UTF-8") as note:
            note.write(note_text)

        return note_text

    




