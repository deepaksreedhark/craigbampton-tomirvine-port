#to assemble a spring mass system M and K matrices
def spring_mass_series():

  print(' spring_mass_series.m  ver 1.6   January 8, 2014')
  print(' By Tom Irvine  Email: tom@vibrationdata.com')
  print(' Ported to python3 by Anjali Mukherjee & Deepak Sreedhar K June 9, 2020 Email: sonuanjali2005@gmail.com deepakloyola2k9@gmail.com)
  
  k = []
  m = []
  v = []
  #clear pf;
  #clear pff;
  #clear emm;
  #clear mmm;
  mv = []
  ks = []
  #clear fn;
  #clear omega;
  #clear ModeShapes;
  #clear MST;
  #clear nn;
  #clear size;

  #######################################################################################
  print(' ')
  print(' Enter the units system ')
  print(' 1=English  2=metric ')
  #selecting the units system
  iu=int(int(input()))
  print(' Assume symmetric mass and stiffness matrices. ')
  mass_scale=1

  #selecting the input mass unit
  if(iu==1):
      print(' Select input mass unit ')
      print('  1=lbm  2=lbf sec^2/in  ')
      imu=int(input())
      if(imu==1):
          mass_scale=386
  else:
      print(' mass unit = kg ')
  #selecting the input stiffness unit
  print(' ')
  if(iu==1):
      print(' stiffness unit = lbf/in ')
  else:
      print(' stiffness unit = N/m ')
  #######################################################################################

  #######################################################################################
  #selecting number of masses in the system
  print(' Enter number of masses')
  n= int(input())
  m=np.zeros((n,n))
  #######################################################################################

  ####################################################################################### 
  #selecting BCS type
  print(' Enter the boundary conditions ')
  print('  1=fixed-fixed  ')
  print('  2=fixed-free   ')
  print('  3=free-free    ')
  ibc= int(input())
  #######################################################################################

  #######################################################################################
  #selecting input method
  print(' ')
  print(' Select input method ')
  print(' 1=manual  2=mass & stiffness vectors ')
  imethod= int(input())
  #######################################################################################

  #######################################################################################
  if(ibc==1): #fixed-fixed
          out1='\n The boundary nodes are '+ str(n+1)
          print(out1)
  inum=1
  if(ibc==2): # fixed-free
          if(n>1):
              print(' Select numbering ')
              print('  1=  node 1 is next to fixed boundary (typical) ')
              print('  2=  node 1 is at free end ')
              inum= int(input())  
  if(ibc==1): #fixed-fixed
          nn=n+2
  if(ibc==2): #fixed-free
          nn=n+1
  if(ibc==3): # free-free
          nn=n    
  #######################################################################################

  #######################################################################################
  #routine for manual entry
  if(imethod==1):
      #get all masses from user
      for i in range(1,n+1):
          out1='\n Enter mass at node'+str(i)
          print(out1)
          m[i-1,i-1]= int(input())
      #get all stiffnesses from user for fixed-fixed            
      if(ibc==1): #fixed-fixed
          for i in range(1,n+2):
              print(' ')        
              print(' Enter stiffness for spring ')
              out1=' between nodes '+str(i-1)+" & "+str(i)
              print(out1)
              ks.append(int(input()))
          NS=n+1;
      #get all stiffnesses from user for fixed-free    
      if(ibc==2): # fixed-free      
          for i in range(1,n+1):
              print(' ')
              print(' Enter stiffness for spring ')     
              if(inum==1):
                  if(i==1):
                      out1=' between fixed boundary and node '+str(i)
                  else:
                      out1=' between nodes '+str(i-1)+" "+str(i)               
              else:
                  if(i==n):
                      out1=' between node ' + str(i) + ' and fixed boundary ';
                  else:
                      out1=' between nodes ' + str(1) + ' & '+ str(i+1); 
                                            
              print(out1)
              ks.append(int(input()))                        
          NS=n
      #get all stiffnesses from user for free-free
      if(ibc==3): # free-free
          for i in range(1,n):
              print(' ')
              print(' Enter stiffness for spring ')
              out1=' between nodes '+ str(i)+' & '+str(i+1)
              print(out1)
              ks.append(int(input()))
          
          NS=n-1
          
      k=np.zeros((nn,nn))
  #######################################################################################

  #######################################################################################  
  #routine for matrix input by user
  else:
      mv=input(' Enter mass vector ')
      ks=input(' Enter stiffness vector ')
      for i in range(1,n+1):
          m[i-1,i-1]=mv[i-1]
      
      NS=max(ks.shape)   
      k=np.zeros((nn,nn))    
  #######################################################################################

  #######################################################################################
  print('####################################################################################### ')
  print('Your spring-mass system definition:')
  print('####################################################################################### ')
  print(' ')
  print('Stiffness matrix')
  print(ks)
  print(' ')
  print('Mass matrix')
  print(m)

#spring_mass_series()
