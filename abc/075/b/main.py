
def main():

    HW_list = list(map(int,input().split()))

    H = HW_list[0]
    W = HW_list[1]

    befor_mine_detection = []

    for i in range(H):
        befor_mine_detection.append(list(input()))
    
    after_mine_detection = []

    for i in range(H):
        after_mine_detection.append([])
    
    #print(after_mine_detection)


    #print(befor_mine_detection)

    for h in range(H):
        #print(f"H:{h}")
        for w in range(W):
            # #print(f" H:{h} W:{w}")
            if befor_mine_detection[h][w] == ".":
                # #print(befor_mine_detection[h][w])
                #print(f" ditect_coordinate H:{h} W:{w}")
                
                if h == 0:
                    counter = 0
                    for aroud_h in range(0,2):
                        
                        if w == 0:
                            for around_w in range(0,2):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    左端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1   

                        elif w == W - 1:
                            for around_w in range(-1,1):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    右端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}")
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 
                                    
                        else:
                            for around_w in range(-1,2):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    端でない H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}") 

                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 

                    after_mine_detection[h].append(counter)
                
                
                elif h == H - 1:
                    counter = 0
                    for aroud_h in range(-1,1):
                        # #print(f"  h:{h} aroud_h:{aroud_h} ")
                        #print(f"  下{aroud_h}")
                        if w == 0:
                            for around_w in range(0,2):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    左端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1   
                        elif w == W - 1:
                            for around_w in range(-1,1):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    右端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}")
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 
                        else:
                            for around_w in range(-1,2):
                                #print(f"  H:{aroud_h} W:{around_w}")
                                #print(f"    端でない H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 
                        
                    after_mine_detection[h].append(counter)

                else:
                    counter = 0
                    for aroud_h in range(-1,2):
                        #print(f"  上と下の間{aroud_h}")
                        if w == 0:
                            for around_w in range(0,2):
                                #print(f"   H:{aroud_h} W:{around_w}")
                                #print(f"     左端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h+aroud_h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1  
                        elif w == W - 1:
                            for around_w in range(-1,1):
                                #print(f"   H:{aroud_h} W:{around_w}")
                                #print(f"     右端 H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 
                        else:
                            for around_w in range(-1,2):
                                #print(f"   H:{aroud_h} W:{around_w}")
                                #print(f"     端でない H:{aroud_h} W:{around_w} around_mine:{befor_mine_detection[h][w+around_w]}") 
                                if befor_mine_detection[h+aroud_h][w+around_w] == "#":
                                    counter += 1 

                    after_mine_detection[h].append(counter)

            else:
                after_mine_detection[h].append("#")
                    
    #print(*after_mine_detection,sep='\n')

    for i in range(H):
        if i == 0 or i == H:
                a = 0
        else :
            print()
        for j in range(W):
            print(after_mine_detection[i][j], end='')
            





if __name__ == "__main__":
    main()