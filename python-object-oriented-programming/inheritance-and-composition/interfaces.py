from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass
    
class Converter(JSONify):
    def toJSON(self):
        print('JSONIfy')

converter = Converter()
converter.toJSON()