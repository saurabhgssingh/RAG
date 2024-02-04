import re
import os
from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class Document:
     content:str
     metadata:dict


class BaseLoader:
    def __init__(self,file_path:str):
        self.file_path=file_path

        #if file exists load the file
        if not os.path.isfile(self.file_path):
            raise ValueError("Invalid file path")


    @abstractmethod
    def load(self):
        pass

class PDFLoader(BaseLoader):
        
        def load(self) -> Document:          
            #Logic to read pdf
             from pypdf import PdfReader
             reader = PdfReader(self.file_path)

             #loop over each page and store it in a variable
             text=""


             for page in reader.pages:
                  text += page.extract_text()
            
             return Document(content=text,
                             metadata=self._generate_metadata(reader))
        
        @staticmethod
        def _generate_metadata(reader)->dict:
             meta = reader.metadata 
             num_pages = len(reader.pages)
             return {'producer':meta.producer,
                    'author':meta.author,
                    'title':meta.title,
                    'num_pages':num_pages}
        
             


                


