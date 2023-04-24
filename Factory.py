from abc import ABC, abstractmethod

class Detection:
    def createRoadTrip(self):
        pass

    def planDetection(self):
        RoadTrip = self.createRoadTrip()

        result = f"Detection: Alerta emitido...\n{RoadTrip.alerta()}"

        return result

class Pothole(Detection):
    def __init__(self, name):
        self.name = name

    def createRoadTrip(self):
        return Fixed(self.name)

class GenericObstacle(Detection):
    def __init__(self, name):
        self.name = name

    def createRoadTrip(self):
        return Temp(self.name)

class RoadTrip(ABC):
    @abstractmethod
    def alerta(self):
        pass

class Fixed(RoadTrip):
    def __init__(self, name):
        self.name = name
        self.category = "Obstaculo Fixo" 
    
    def alerta(self):
        result = (f"{self.category} Detection: {self.name}",
                "Alerta registrado....")
        return result

class Temp(RoadTrip):
    def __init__(self, name):
        self.name = name
        self.category = "Obstaculo temporário" 

    def alerta(self):
        result = (f"{self.category} Detection: {self.name}",
                "Não é necessário registrar no banco de dados....")
        return result

def object_code(Detection: Detection):
  print(f"App: Carregado com {Detection.__class__.__name__}.",
        f"{Detection.planDetection()}")

if detections:
    for phothole in Detection:
        with open('/content/gdrive/MyDrive/Reaper/Yolo_Darknet_Ford/alert.txt','w') as arquivo:
            dtc += 1
            arquivo.write("Detection\n")
            arquivo.write(f'{str(dtc)}')
        arquivo.close()
        object_code(Pothole("code_0"))
        print("\n")

    for person, car, truck in Detection:
        with open('/content/gdrive/MyDrive/Reaper/Yolo_Darknet_Ford/alert.txt','w') as arquivo:
            arquivo.write("Detection\n")
            arquivo.write(f'{str(dtc)}')
        arquivo.close()
        object_code(GenericObstacle("code_x"))
       
else:
    with open('/content/gdrive/MyDrive/Reaper/Yolo_Darknet_Ford/alert.txt','w') as arquivo:
        arquivo.write("Nada ainda\n")
        arquivo.write(f'{str(dtc)}')
        arquivo.close()