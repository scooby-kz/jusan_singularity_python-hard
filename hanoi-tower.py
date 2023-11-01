def hanoiTower(n, from_rod, to_rod, aux_rod): 
    if n == 0: 
        return
    hanoiTower(n-1, from_rod, aux_rod, to_rod) 
    print("Диск", n, "с башни", from_rod, "в башню", to_rod) 
    hanoiTower(n-1, aux_rod, to_rod, from_rod) 
  
  
N = 5

hanoiTower(N, '1', '3', '2') 
