def tower_hanoi(n,source,auxiliary,destination):
   if n==1:
     print(f"Move the disk from source {source} to destination {destination}")
     return
     
   tower_hanoi(n-1 , source , destination , auxiliary)
   
   print(f" Move largest disk from A to C ")
   
   tower_hanoi(n-1 , auxiliary , source , destination)
   
n = int(input("Enter no of disks :"))
tower_hanoi(n , 'A', 'B' , 'C')

print("\n Total Moves = " , 2**n-1)
