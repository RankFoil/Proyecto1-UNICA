import csv
class Lector:
    @staticmethod
    def ID(id):
        Null=[]
        with open("data.csv") as f:
            lista=csv.reader(f)
        f.close()
        for i in lista:
            data=i.split(",")
            if id in data:
                return data
        return Null
    
    @staticmethod
    def ReadID():
        while (True):
            id=input("Escriba el código del producto: ")
            f=open("data.csv","r+")
            lista=f.readlines()
            f.close()
            for i in lista:
                data=i.split(",")
                if id in data:
                    return id
                
class Maquina:
    @staticmethod
    def darProducto(producto):
        f=open("data.csv","r+")
        lista=f.readline()
        data=lista.split(",")
        if producto[3]>0:
            flag=True
            while(flag):
                
                if id in data:
                    f.close
                    f=open("data.csv","w")
                    data[3]=int(data[3])-1
                    f.write(data[0]+","+data[1]+","+data[2]+","+data[3]+","+data[4])
                    flag=False
                    print(data[1]+ " Entregado")
            
Lector.ID("001")

