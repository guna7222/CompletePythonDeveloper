class Transport:
    def worlds_transport_system(self):
        print("cycle is the first transport system")

class New_Transport(Transport):
    def worlds_transport_system(self):
        print("Fastest Bike")

new_transport_object = New_Transport() # New Transport object
new_transport_object.worlds_transport_system()

