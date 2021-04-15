def formatCustomer(firstName, lastName, location= None):
    fullname = list(zip(firstName,lastName))
    if (location!=None):
        return dict(zip(fullname,location))
    
    

if __name__ == '__main__':
    print(formatCustomer("John","Smith","Canada"))