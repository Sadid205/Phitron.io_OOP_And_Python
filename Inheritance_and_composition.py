class Processor:
    def __init__(self,core,clock_speed,origin) -> None:
        self.core = core
        self.clock_speed = clock_speed
        self.origin = origin


class Display:
    def __init__(self,regulation,size,aspect_ratio) -> None:
        self.regulation = regulation
        self.size = size
        self.aspect_ratio = aspect_ratio

class RAM:
    def __init__(self,frequency,size) -> None:
        self.frequency = frequency
        self.size = size

class Motherboard:
    def __init__(self,board_size,) -> None:
        self.board_size = board_size


# Here I want to create a phone
# It is an Example of Composition
class Phone:
    def __init__(self,casing,speaker,microphone) -> None:
        self.casing = casing 
        self.speaker = speaker
        self.microphone  = microphone
        self.Processor = Processor() # This Phone has a Processor but this phone is not a processor
        self.Display = Display() # This Display has a Processor but this phone is not a Display
        self.RAM = RAM() # This RAM has a Processor but this phone is not a RAM
        self.Motherboard = Motherboard() # This Motherboard has a Processor but this phone is not a Motherboard

# But if i want to create a Processor
class Mediatech(Processor):
    def __init__(self,processor_name,technology) -> None:
        self.processor_name = processor_name
        self.technology = technology

