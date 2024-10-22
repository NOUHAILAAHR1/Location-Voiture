
from datetime import date,time
class Voiture:
    def __init__(self,immatriculation="l2345", marque="bm", carburant="dsl", modle=2007, puissancefiscale=0):
         self._immatriculation=immatriculation
         self._marque=marque
         self._carburant=carburant
         self._modèle= modle
         self._puissancefiscale= puissancefiscale

    @property
    def immatriculation(self):
        return self._immatriculation
    @immatriculation.setter
    def immatriculation(self,im):
         self._immatriculation=im
    @property
    def marque(self):
        return self._marque
    @marque.setter
    def marque(self,ma):
         self._marque=ma
    @property
    def carburant(self):
        return  self._carburant
    @carburant.setter
    def carburant(self,ca):
        self._carburant=ca
        
    @property
    def modle(self):
        return  self._modle
    @ modle.setter
    def modèle(self,m):
         self._modle=m
    @property
    def puissancefiscale(self): 
        return self._puissancefiscale
    @puissancefiscale.setter
    def puissancefiscale (self,puis):
        self._puissancefiscale=puis
   
    def __str__(self):
        return f": immatriculation:{self.immatriculation}, marque:{self.marque},carburant:{self.carburant}, modèle:{self.modle}, puissancefiscale:{self. puissancefiscale}"

class VoitureVip (Voiture):
    def __init__(self, immatriculation="l2345", marque="bm", carburant="dsl", modle=2007, puissancefiscale=0,t="4*4"):
       super().__init__(immatriculation, marque, carburant, modle, puissancefiscale)
       self.__Type=t
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self,t):
        if t=="4*4" or t=="SUV" or t=="minibus" or t=="limousine":
            self.__Type=t
    
    def __str__(self):
        return f"{super().__str()}-type{self.Type}"
    
class VoitureCitadinne(Voiture):
    def __init__(self, immatriculation="l2345", marque="bm", carburant="dsl", modle=2007, puissancefiscale=0,g="A"):
       super().__init__(immatriculation, marque, carburant, modle, puissancefiscale)
       self.__gamme=g
    @property
    def gamme(self):
        return self.__type
    @gamme.setter
    def gamme(self,g):
        if g=="A" or g=="B" or g=="C" :
            self.__gamme=g
    
    def __str__(self):
        return f"{super().__str()}-gamme{self.gamme}"
class ListVoitur :
    def __init__(self,LV=[]):
        self.__LV=LV
    @property
    def LV(self):
        return self.__LV
    @LV.setter
    def LV(self,lvv):
        self.__LV=lvv
    def AjouterVoiture(self,Voiture):
        if Voiture in self.__LV:
            print("voiture deja exist")
            return False
        else:
            self.LV.append(Voiture)
            return True
    
    def Supprimer(self,immatricule):
        exist=False
        for i in  self.LV:
            if i.immatriculation == immatricule :
                exist=True
                self.LV.remove(i)
                break
        if exist==False:
            print("cette  voiture nexiste pas")
        
    def ModifierVouture(self,Voiture):
        for i in self.LV:
                if Voiture in self.LV:
                    i.immatriculation=Voiture.immatriculation
                    i.marque=Voiture.marque
                    i.carburant=Voiture.carburant
                    i.modle=Voiture.modle
                    i.puissancefiscal=Voiture.puissancefiscal
                
           
            
        
class Personne:
    def __init__(self,cin="l42536",n="nom",p="prenom"):
        self._cin=cin
        self._nom=n
        self._prenom=p
    @property
    def cin(self):
        return self._cin
    @cin.setter
    def cin(self,c):
        self._cin=c
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,n):
        self._nom=n
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self,p):
        self._prenom=p
    def __str__(self):
        return f"cin:{self.cin}-nom:{self.nom}-prenom:{self.prenom}"
        
    
        

class Client(Personne):
    def __init__(self,cin="l42536",n="nom",p="prenom",nump=12345,tele=5365178349 ):
        self.__numper=nump
        self.__tele=tele
        super().__init__(cin,n,p)
    @property
    def numper(self):
        return self.__numper
    @numper.setter
    def numper(self,np):
        return self.__numper
    @property
    def tele(self):
        return self.__tele
    @tele.setter
    def tele(self,g):
        return self.__tele
    
    def __str__(self):
        return f" {super().__str()}-numpermi:{self.numper}-tele:{self.tele}-Lc:{self.Lc}"
class ListeClient:
    def __init__(self,Lc=[]):
         self.__Lc=Lc
    @property
    def Lc(self):
        return self.__Lc
    @Lc . setter
    def Lc (self,lc):
        self.__Lc-lc
    def AjouterClient(self ,client) :
         if client in self.Lc:
             print("client deja existe")
             return False
         else:
             self.Lc.append(client)
             
             return True
    def supprimerclient(self,cin):
        
        exist=False
        for i in  self.Lc:
            if i.cin == cin :
                exist=True
                self.Lc.remove(i)
                break
        if exist==False:
            print("client nexiste pas")
    def Modifierclient(self,client):
        for i in self.Lc:
            if i.cin == client.cin:
                i.nom=client.nom
                i.prenom=client.prenom
                i.numper=client.numper
                i.tele=client.tele
                
        
         
    
class Location:
    auto=0
    def __init__(self,d=date(1,1,1), dure=time(0,0,0) , prix=123456,c=Client(),v=Voiture()):
        self.__date=d
        self.__dure=dure
        self.__prix=prix
        self.__client=Client
        self.__voiture=Voiture
        self.__idlocation=Location.auto
        Location.auto+=1
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,d):
        self.__date=d
    @property
    def dure(self):
        return self.__dure
    @dure.setter
    def dure(self,du):
        self.__dure=du
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,p):
        self.__prix=p
    @property
    def client(self):
        return self.__client
    @client.setter
    def client(self,c):
        self.__client=c
    @property
    def voiture(self):
        return self.__voiture
    @voiture.setter
    def voiture(self,v):
        self.__voiture=v
    @property
    def idlocation(self):
        return self.__idlocation
    def __str__(self):
        return f"date:{self.date}-dure:{self.dure}-idlocation:{self.idlocation} -client:{self.client}-voiture:{self.voittre}-prix:{self.prix}"
class ListeLocations:
    def init(self,LL=[]):
        self.__L_location=LL
    def getLlocation(self):
        return self.__L_location
    def setLlocation(self,LL):
        self.__L_location=LL
    L_location=property(getLlocation,setLlocation)
    
    def _str_(self):
        return f"liste locations:{self.L_location}"
    def AfficherListeLocation(self):
        for i in self.L_location:
            print(i)
    def AfficherListeLocationCitadine(self):
        LC=[]
        for i in self.L_location:
            if isinstance(i,VoitureCitadinne)==True:
                LC.append(i)
        return LC
    def AfficherListeLocationVip(self):
        LV=[]
        for i in self.L_location:
            if isinstance(i,VoitureVip)==True:
                LV.append(i)
        return LV
    def AfficherLocationMarque(self,marq):
        LL=[]
        for i in self.L_location:
            if i.Voiture.Marque==marq:
                LL.append(i)
        return LL
    def AfficherLocationImma(self,imma):
        LL=[]
        for i in self.L_location:
            if i.Voiture.immatriculation==imma:
                LL.append(i)
        return LL
    def AfficherLocationClient(self,cin):
        LL=[]
        for i in self.L_location:
            if i.Client.Cin==cin:
                LL.append(i)
        return LL
    def AjouterLocation(self,Location):
        if Location in self.L_location:
            print("location  deja exist")
            return False
        else:
            self.L_location.append(Location)
            return True
    def SupprimerLocation(self,Location):
        if Location in self.L_location:
            self.L_location.remove(Location)
            return True
            
        else:
            print("location n'exist pas")
            return False
    def FiltrerLocationDate(self,date):
         LL=[]
         for i in self.L_location:
             if i.DateLocation==date:
                 LL.append(i)
         return LL










    

class Utilisateur(Personne):
    def __init__(self,cin="l42536",n="nom",p="prenom",log="login",modp="4235672",email="email" ):
        self.__login=log
        self.__modp=modp
        self.__email=email
        super().__init__(cin,n,p)
        
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self,l):
        self.__login=l
    @property
    def modp(self):
        return self.__modp
    @modp.setter
    def modp(self,m):
        self.__modp
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,e):
        self.__email=e
    def __str__(self):
        return f"login:{super().__str()}-{self.login}-mpdp:{self.modp}-email:{self.email}"
class Listutilisateur:
    def __init__(self,Lut=[]):
        self.__Lut=Lut
    @property
    def Lut(self):
        return self.__Lut
    @Lut.setter
    def Lut(self,lu):
        self.__Lut=lu
    def __str__(self):
        return f"Lut:{self.Lut}"
    def Authentifier(self,log,mdp):
        
       
        for i in self.Lut:
            if i.login == log and i.modp ==  mdp:
                print("Authentification réuss")
                return True
                
        else:
            print("Echec d’Authentification")
            return False
        
    def Ajouter(self ,Utilisateur) :
         if Utilisateur in self.Lut:
             print("Utilisateur deja existe")
             return False
         else:
             self.Lut.append(Utilisateur)
            
             return True
    def supprimer(self,log):
        
        exist=False
        for i in  self.Lut:
            if i.login == log :
                exist=True
                self.Lut.remove(i)
                break
        if exist==False:
            print("login nexiste pas")
    def Modifier(self,Utilisateur):
        for i in self.Lut:
            if i.login == Utilisateur.login:
                i.cin=Utilisateur.cin
                i.nom=Utilisateur.nom
                i.prenom=Utilisateur.prenom
                i.modp=Utilisateur.modp
                i.email=Utilisateur.email
     







                           
        
        
        
    
    
    
    
        
            
    
            

       
       













        
