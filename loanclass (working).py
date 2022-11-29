# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:21:38 2022

@author: nelso
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:43:35 2022

@author: 16617
"""
import numpy as np

class loan(object): #loanpy
    def __init__ (self, name):  # initialize with a name, thie permits
                                # easier manamgement of multiple instances
        """
        loanpy is a class object to implement computations of 
        loan parameters
        
        name documents data set

        Returns
        -------
        None.

        """
        #initialization
        self._name = name
        self._Pv = 0
        self._intAPR = 0
        self._Pmt = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nname on this instance: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("options: Pmt, Pv, intAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Pmt", "Pv", "intAPR", "nMonths"):
            choice = input("enter choice ")
            
        if choice == "Pmt":
            self.getPmt()
        elif choice == 'Pv':
            self.getPv()
        elif choice == 'rateAPR':
            self.getIntRate()
        else:
            self.get_nMonths()


    def getIntRate(self):#replace with functions listed in assignment#
        ''' Solve for interest rate, APR  '''
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        # The solution will be r where using Pmt, n, and Pv works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: self._Pmt*(1-(1+r)**(-self._nMonths)) - self._Pv*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%") # convert back to APR
            rTry = None
        
        print(f"interest rate ={_rTry}")
        return _rTry*1200

    def getPmt(self):#replace with functions listed in assignment##
        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter APR '))
        self._nMonths = int(input('Enter number of months '))
        #assumes you entered interest rates as APR
        
        _r = self._intAPR/1200
        self._Pmt = _r *self._Pv/(1-(1+_r)**-self._nMonths)

        print(f'{self._Pmt}')
        print('left for you to do')
        pass
    
    def get_nMonths(self):
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._intAPR = float(input('Enter APR '))
        #self._nMonths = -np.log(1-self._PV*_r/self._Pmt)/np.log(1+_r)
        #self._nMonths = -np.log(1-self._PV/(_r*self._PV))/np.log((1+_r))
        
        _r = self._intAPR/1200
      
        self._nMonths = -np.log(1-self._Pv*_r/self._Pmt)/np.log(1+_r)

        print(f'{self._nMonths}')
        #print('left for you to do')
        pass
    
    def getPv(self):
        self._Pmt = float(input('Enter Pmt '))
        self._intAPR = float(input('Enter APR '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR/1200
        self._Pv = (self._Pmt / _r) * (1 - (1 + _r)**(-self._nMonths))
        
        print(f'{self._Pv}')
        pass
    
    
    
    
    
    """
    1  given PV, nMonths, intAPR, compute the monthly payment   name this function computePmt(PV, intAPR, nMonths)
    
    2  given PV, nMonths and monthly payment, Pmt, compute intAPR  name this function compute_intAPR(PV, nMonths, Pmt)
    
    3. given PV, Pmt, intAPR compute the number of months, nMonths name this function compute_nMonths(PV, Pmt, intAPR)
    
    4. given Pmt, intApr, nMonths compute PV, name this function computePV(Pmt, intAPR, nMonths)
    
    For example if I wanted to compute Pmt I would use loan.computePmt(PV, intAPR, nMonths)
    """

    def computePmt(self, Pv, intAPR, nMonths):
        r = intAPR/1200
        Pmt = r*Pv/((1-(1+r)**(-nMonths)))
        print(f'\npayemnt is equal to {Pmt: .2f}\n')
        return Pmt
        
    def compute_intAPR(self, Pv, nMonths, Pmt):
       ''' Solve for interest rate, APR  '''
       # Pv = float(input('Enter PV '))
       # Pmt = float(input('Enter Pmt '))
       # nMonths = int(input('Enter number of months '))
       
       # The solution will be r where using Pmt, n, and Pv works
       ## bisection algorithm finds the two sides of the equation are equal
       ## that is, the difference is 0
       ## side 1: Pmt*(1-(1+r)**(-n))
       ## side 2:  Pv*r
       
       #example of an in-line (lambda) function
       fIntRate = lambda r: Pmt*(1-(1+r)**(-nMonths)) - Pv*r
       
       # low and high possible interest rates, APR
       # the actual rate is between 
       
       _rlow =0
       _rhigh = 50 
       
       _rl = _rlow/1200
       _rh = _rhigh/1200
       _count = 0
       
       while(_count < 20): # in case there is no solution
           _rTry = (_rl+_rh)/2
           if abs(fIntRate(_rTry)) < 0.001: break
           
           if fIntRate(_rTry) > 0: _rl = _rTry
           else: _rh = _rTry
           
           _count += 1
           
       if(_count >=20):
           print("no solution: try again")
           print(f"interest rate APR is > {_rTry*1200:.4f}%") # convert back to APR
           rTry = None
       
       print(f"Interest rate = {(_rTry*1200):.2f}\n")
       return _rTry*1200
        
    
    def compute_nMonths(self,Pv ,Pmt , intAPR):
        #formula for _nMonths:
        r = intAPR/1200
        #nMonths = (-np.log(1-(_r*Pv/Pmt)/np.log((1+_r))))
        nMonths = -np.log(1-(r*Pv/Pmt))/np.log((1+r))
        print(f"{nMonths:.2f} months to pay off loan\n")
        #pass
        return nMonths
    
    def computePV(self,Pmt,intAPR,nMonths):
        #formula for PV:
        # self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
        r = intAPR/1200
        Pv = (Pmt *(1-(1+r)**(-nMonths)))/r
        print(f'present value is {Pv:.2f}')#pass
        
        return Pv

####################################################################
"""THIS ONE IS NOT FINISHED"""
#####################################################################     
  
if __name__ == '__main__':
    
    # testloan = loan('example1')
    
    # testloan.getName()
    
    # testloan.getChoice()
    
    
    loan1 = loan('fuck')
    loan1.computePmt(1, 37.5, 12)
    loan1.compute_intAPR(300, 12, 100)
    loan1.compute_nMonths(300, 100, 5)
    loan1.computePV(100,5, 12)
    
    
    #loan1.setPV()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """ def computePmt(self,Pv, intAPR, nMonths):
         # r = self._ratePct/100/12
         # self._Pmt = r*self._Pv/ 
         # print("idk what elst to dp")
         _r = intAPR/1200
        
         Pmt = _r*Pv/((1-(1+_r)**(-nMonths)))
         print(f'payemnt is equal to {self._Pmt: .2f}')
         # _r = self._intRate/1200
        
         # self._Pmt = _r*self._Pv/((1-(1+_r)**(-self._nMonths)))
         # print(f'payemnt is equal to {self._Pmt: .2f}')
        
         # pass
         pass
         
         
     def compute_intAPR(self,Pv, nMonths, Pmt):
         print("idk what else to do")
         
     # def compute_nMonths(PV,Pmt,intAPR):
     #     print("idk what else to do")
         
     # def computePV(Pmt, intAPR,nMonths):
     #     print("idk what else to do")
         
         
     # def computePmt(self ):
     #     self._Pv = float(input('Enter Pmt '))
     #     self._intAPR = float(input('Enter APR '))
     #     self._nMonths = int(input('Enter number of months '))
     #     # Pmt =  r/1200*PV/(1-(1+(r/1200))**(-n)) 
     #     # assumes you entered interest rate as APR
     #     _r = self._intRate/1200
         
     #     self._Pmt = _r*self._Pv/(1-(1+_r)**self._nMonths)
     #     print(f'payemnt is equal to {self._Pmt: .2f}')
         
     #     pass
     
     def compute_nMonths(Pv,Pmt,intAPR):
         #formula for _nMonths:
         _r = intAPR/1200
         nMonths = (-np.log(1-(_r*Pv/Pmt)/np.log((1+_r))))
         print(f"{nMonths} months to pay off loan")
         pass
     
     def computePV(Pmt, intAPR,nMonths):
         #formula for PV:
         # self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
         _r = intAPR/1200
         Pv = Pmt/_r *(1-(1+_r)**(-nMonths))
         print('left for you to do')
         pass
"""