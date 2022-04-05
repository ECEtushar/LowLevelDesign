
class ParkingLot:
    def __init__(self,n):
        self.totalSlots=n
        self.slots=n
        self.details={i:None for i in range(1,n+1)}
        self.availableSlots=[i for i in range(1,n+1)][::-1]

    #Method for park car in parking lot
    def park(self,regNum,color):

        if self.slots>0:
            slot=self.availableSlots.pop()
            self.details[slot]=[regNum,color]
            self.slots-=1
            print(f'Allocated Slot Number: {slot}')
            return slot
        else:
            print('Sorry!, Parking Lot is currently full')

    #Method for leave the parking space
    def leave(self,slotNum):

        if slotNum <= self.totalSlots and self.details[slotNum]!=None:
            self.details[slotNum]=None
            self.availableSlots.append(slotNum)
            self.slots+=1
            print(f'Slot no. {slotNum} is Free')
        else:
            print('Invalid Slot Number!')

    #Method for showing the status of parking lot 
    def status(self):
        print('\nSlot Number\n')
        for slotNumber in self.details:
            print(slotNumber)

        print('\nRegistration Number\n')
        for slot in self.details:
            if self.details[slot]==None:
                print('Free')
            else:
                print(self.details[slot][0])
        
        print('\nColour\n')
        for slot in self.details:
            if self.details[slot]==None:
                print('Free')
            else:
                print(self.details[slot][1])

    #Method for getting the registration numbers of a given colour 
    def registration_numbers_for_cars_with_colour(self,color):
        res=[]
        for i in self.details:
            if self.details[i]!=None:
                if self.details[i][1]==color:
                    res.append(self.details[i][0])
        if len(res)==0:
            return print(f'No Car/s parked having {color} colour')
        return res

    # Method for getting the slot numbers of a given colour
    def slot_numbers_for_cars_with_colour(self,color):
        res=[]
        for i in self.details:
            if self.details[i]!=None:
                if self.details[i][1]==color:
                    res.append(i)
        if len(res)==0:
            return print(f'No Car/s parked having {color} colour')
        return res
        
    # Method for getting the slot number of a given Car
    def slot_number_for_cars_with_registration(self,regNum):
        res='Not Found'
        for i in self.details:
            if self.details[i]!=None:
                if self.details[i][0]==regNum:
                    res=i
                    break
        print(res)


if __name__=='__main__':
    p=ParkingLot(6)
    p.park('KA-01-HH-1234','White')

    p.park('KA-01-HH-9999','White')
    p.park('KA-01-BB-0001','Black')
    p.park('KA-01-HH-7777','Red')
    p.park('UP-65-BZ-6561','Blue')
    p.park('UP-32-DX-3454','Red')
    p.park('UP-32-DX-3453','Red')
    p.leave(5)
    p.status()
    p.leave(1)
    p.status()
    p.registration_numbers_for_cars_with_colour('Red')
    p.slot_numbers_for_cars_with_colour('White')
    p.slot_number_for_cars_with_registration('UP-32-DX-3453')

    p.slot_number_for_cars_with_registration('KA-01-HH-3141')