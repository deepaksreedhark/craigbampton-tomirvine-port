#generates partitioned stiffness and mass matrices - utility2
#function[M11,M12,M21,M22,K11,K12,K21,K22]=CB_partition(dof_boundary,dof_interior,m,k)
def CB_partition(dof_boundary,dof_interior,m,k):
  print('####################################################################################### ')
  print('CB_partition.m  Tom Irvine ver 1.0  April 30, 2013')
  print('ported to python 3  Deepak Sreedhar K June 20, 2020')
  print('####################################################################################### ')

  dof_global=np.concatenate((dof_boundary,dof_interior))
  #print(dof_global)
  print('-------------------------------------------------------------')
  print('input mass matrix')
  print(m)
  print('input stiffness matrix')
  print(k)

  num_boundary=max(np.shape(dof_boundary))
  print('-------------------------------------------------------------')
  print('number of boundary nodes ' + str(num_boundary))
  num_interior=max(np.shape(dof_interior))
  print('number of interior nodes ' + str(num_interior))
  
  #total dof in model
  num=num_boundary+num_interior
  print('-------------------------------------------------------------')
  print('total no. of dof in model ' + str(num))
  
  M11=np.zeros([num_interior,num_interior])
  M12=np.zeros([num_interior,num_boundary])
  M21=np.zeros([num_boundary,num_interior])
  M22=np.zeros([num_boundary,num_boundary])
  K11=np.zeros([num_interior,num_interior])
  K12=np.zeros([num_interior,num_boundary])
  K21=np.zeros([num_boundary,num_interior])
  K22=np.zeros([num_boundary,num_boundary])
  
  #print('M11')
  #print(M11)
  #print('M12')
  #print(M12)
  #print('M21')
  #print(M21)
  #print('M22')
  #print(M22)
  
  #######################################################################################
  #M11 K11 - interior-interior - order (num_interior x num_interior)
  #######################################################################################
  ic=0;
  #loop through all dofs in model
  for i in range(0,num):
    #interior flag
    iflag=0;
    #search if considered dof is present in interior dof list
    #if present interior flag will be active
    for nv in range(0,num_interior):
        if dof_global[i]==dof_interior[nv]:
          #interior flag active
          iflag=1
          break
      
    #if considered dof is interior dof (flag active)-->
    if iflag==1:
        jc=0
        #loop through all dofs
        for j in range(0,num):
            jflag=0
            for nv in range(0,num_interior):
              if dof_global[j]==dof_interior[nv]:
                  jflag=1
                  break
            if jflag==1:
              #print('i='+str(i)+' j='+str(j)+' ic='+str(ic)+' jc='+str(jc))
              M11[ic,jc]=m[i,j]
              K11[ic,jc]=k[i,j]
              jc=jc+1
            #print('i='+str(i)+' j='+str(j)+' iflag='+str(iflag)+' jflag='+str(jflag))
    if iflag==1:
        ic=ic+1;
  #print('-------------------------------------------------------------')  
  #print('M11')
  #print(M11)
  #print('K11')
  #print(K11)
  #######################################################################################
  #M12 K12 - interior-boundary - order (num_interior x num_boundary)
  #######################################################################################
  ic=0
  for i in range(0,num):
    iflag=0          
    for nv in range(0,num_interior):
        if dof_global[i]==dof_interior[nv]:
          iflag=1
          break
    if iflag==1:
        jc=0      
        for j in range(0,num):
            jflag=0
            for nv in range(0,num_interior):
              if dof_global[j]==dof_interior[nv]:
                  jflag=1
                  break
            if jflag==0:
              #print('i='+str(i)+' j='+str(j)+' ic='+str(ic)+' jc='+str(jc))             
              M12[ic,jc]=m[i,j]
              K12[ic,jc]=k[i,j]
              jc=jc+1
            #print('i='+str(i)+' j='+str(j)+' iflag='+str(iflag)+' jflag='+str(jflag))
    if iflag==1:
        ic=ic+1
  #print('-------------------------------------------------------------')
  #print('M12')
  #print(M12)
  #print('K12')
  #print(K12)
  #######################################################################################
  #M21 K21 - boundary-interior - order (num_boundary x num_interior)
  #######################################################################################
  ic=0
  for i in range(0,num):
    iflag=0;          
    for nv in range(0,num_interior):
        if dof_global[i]==dof_interior[nv]:
          iflag=1
          break
    if iflag==0:
        jc=0      
        for j in range(0,num):
            jflag=0
            for nv in range(0,num_interior):
              if dof_global[j]==dof_interior[nv]:
                  jflag=1
                  break
            if jflag==1:
              #print('i='+str(i)+' j='+str(j)+' ic='+str(ic)+' jc='+str(jc))             
              M21[ic,jc]=m[i,j]
              K21[ic,jc]=k[i,j]
              jc=jc+1
            #print('i='+str(i)+' j='+str(j)+' iflag='+str(iflag)+' jflag='+str(jflag))
    if iflag==0:
        ic=ic+1
  #print('-------------------------------------------------------------')
  #print('M21')
  #print(M21)
  #print('K21')
  #print(K21)
  #######################################################################################
  #M22 K22 - boundary-boundary - order (num_boundary x num_boundary)
  #######################################################################################
  ic=0
  for i in range(0,num):
    iflag=0          
    for nv in range(0,num_interior):
        if dof_global[i]==dof_interior[nv]:
          iflag=1
          break
    if iflag==0:
        jc=0      
        for j in range(0,num):
            jflag=0
            for nv in range(0,num_interior):
              if dof_global[j]==dof_interior[nv]:
                  jflag=1
                  break
            if jflag==0:
              #print('i='+str(i)+' j='+str(j)+' ic='+str(ic)+' jc='+str(jc))             
              M22[ic,jc]=m[i,j]
              K22[ic,jc]=k[i,j]
              jc=jc+1
            #print('i='+str(i)+' j='+str(j)+' iflag='+str(iflag)+' jflag='+str(jflag))
    if iflag==0:
        ic=ic+1
  #print('-------------------------------------------------------------')      
  #print('M22')
  #print(M22)
  #print('K22')
  #print(K22)
  
  return [M11,M12,M21,M22,K11,K12,K21,K22]

#Cb_partition(dof_boundary,dof_interior,m,ks)
