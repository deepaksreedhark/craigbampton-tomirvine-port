#!!!dit - eigenvalues and vectors are interchanged
#generates mode shapes and natural frequencies - utility1
def Generalized_Eigen(S2,M2,ijk):
  print('####################################################################################### ')
  print('Craig-bampton transformation matrix:')
  print('Generalized_Eigen.m  ver 2.2  May 3, 2010 by Tom Irvine')
  print('Ported to python3 by Deepak Sreedhar K June 9th, 2020')
  print('####################################################################################### ')

  np.set_printoptions(precision=4,suppress=True)

  #equation for harmonic motion of MDOF system
  # K*X = (omega^2)*M*X
  # K*X = lambda*M*X - generalized eigen value problem
  # where lambda = omega^2 (natural frequency)
  #Eigen vectors - Modal frequency squared
  #Eigen values - Mode shapes (intial displacements required to achieve harmonic motion)
  
  #generating dynamic matrix D
  D=np.dot((np.linalg.inv(M2)),S2)
  #print('Dynamic matrix eigen')
  [Eigenvectors,Eigenvalues]=np.linalg.eig(D)

  #matlab eigen problem algorithm generates eigenvalues with some internal scaling. Numpy output is different#
  #print('Eigen values - raw mode shapes')
  #print(Eigenvalues)
  
  #print('-------------------------------------------------Raw calculated')
  #print('Eigen vectors')
  #print(Eigenvectors)
  #print('Eigen values')
  #print(Eigenvalues)

  #print('Freq sq')
  #print(Eigenvectors)
  #print('Mode shapes')
  #print(Eigenvalues)

  ############################################################################################
  #sorting matrices from least to greatest frequency (row 1)
  ############################################################################################
  dof=max(np.shape(Eigenvectors))
  globmatrix=np.zeros([dof,dof+1])

  for i in range(0,dof):
    globmatrix[i,0]=abs(Eigenvectors[i])
  globmatrix[0:dof,1:dof+1]=np.transpose(Eigenvalues)
  sortedindices=np.argsort(globmatrix,axis=0,kind='quicksort')
  #print(sortedindices)
  globmatrix=globmatrix[sortedindices[0:dof,0]]
  #print(globmatrix)
  Eigenvectors=globmatrix[0:dof,0]
  Eigenvalues=np.transpose(globmatrix[0:dof,1:dof+1])
  #print('-------------------------------------------------Sorted')
  #print('Eigen vectors')
  #print(Eigenvectors)
  #print('Eigen values - raw mode shapes')
  #print(Eigenvalues)
  ############################################################################################
  #operate on natural frequencies (eigen vectors)
  ############################################################################################
  omega = np.sqrt(Eigenvectors);
  #print('Natural frequencies:')
  #print(omega)
  dof=max(np.shape(omega))
  print('-------------------------------------------------------------')
  print('number of dofs in system')
  print(dof)

  print('-------------------------------------------------------------')
  if ijk==1 or ijk==3:
    print(' Natural Frequencies ')
    print(' No.      f(Hz)')
  
  fn=np.ones((dof,1))
  #calculating modal frequency values in Hz
  for i in range(0,dof):
        fn[i]=round((omega[i])/(2*math.pi),4)
        if ijk==1 or ijk==3:
            print(str(i) + '      ' + str(fn[i]))
          
  #############################################################################################
  ##operating on mode shape eigenvalues
  #############################################################################################
  #ftp://ftp.svibs.com/Download/Literature/Papers/2005/2005_3.pdf
  #mode shape normalisation based on mass
  # eigT * M * eig = I
  MST=np.transpose(Eigenvalues)
  #print(MST)
  temp=np.zeros([dof,dof])
  #print(temp)
  temp=M2*Eigenvalues
  #print(temp)
  QTMQ=MST*temp
  #print(QTMQ)

  scale=np.ones([dof,dof])
  #print(scale)
  #print('------------------------------------------------------mass scale factors')
  for i in range(0,dof):
      scale[i,i]=1.0/(math.sqrt(QTMQ[i,i]))
      #print(scale[i,i])
      if np.sum(Eigenvalues[0:dof,i])<0:
        scale=-scale
      Eigenvalues[0:dof,i] = Eigenvalues[0:dof,i]*scale[i,i]    
  #print(Eigenvalues)
  #print(scale)
  MST=np.transpose(Eigenvalues)
  
  print('-------------------------------------------------------------')
  if ijk==1:
   print('  Modes Shapes mass normalized (column format)');
   print(Eigenvalues)
  
  return [fn,omega,Eigenvalues,MST]
  #############################################################################################

#Generalized_Eigen(ks,m,1)
