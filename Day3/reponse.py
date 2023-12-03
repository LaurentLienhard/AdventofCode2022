characters = ["0","1","2","3","4","5","6","7","8","9"]
array = []
flag_fin = 0
sum = 0

def Day3part1():
    print("Day3 part1")

    with open('./Day3/puzzle.txt') as file:
        for line in file:
            array.append(list(line))

    coor = []
    sum = 0
    for coor_ligne, line in enumerate(array):
        flag_debut = 0
        flag_fin = 0
        coor = []
        for coor_colonne, char in enumerate(line):
            if char in characters and flag_debut == 0:
                coor = [coor_ligne, coor_colonne]
                flag_debut = 1
            if (char not in characters or char in ['.', '\n']) and flag_debut == 1:
                if coor[0] != 0:
                    if check_before_or_after(array[coor_ligne - 1], coor, coor_colonne):
                        sum += list_to_int(line[coor[1]:(coor_colonne)])
                        flag_fin = 1
                if check_around(array[coor_ligne], coor, coor_colonne):
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                if char not in characters and char not in ['.', '\n']:
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                if coor_ligne < (len(array)-1) and check_before_or_after(array[coor_ligne+1], coor, coor_colonne):
                    sum += list_to_int(line[coor[1]:(coor_colonne)])
                    flag_fin = 1
                else:
                    flag_fin = 1
                    
            if flag_fin == 1 or char == '\n':
                coor = []
                flag_debut = 0
                flag_fin = 0
    print(sum)
                        
def list_to_int(list):
    temp_string = ''
    for chiffre in list:
        temp_string+=chiffre
    return int(temp_string)

def check_before_or_after(list, coor, coor_colonne):
    coor_avant = int(coor[1]) - 1 if (int(coor[1]) - 1) >= 0 else 0
    taille_ligne = len(list) - 1
    coor_apres = int(coor_colonne) + 1 if (int(coor_colonne) + 1) < taille_ligne else taille_ligne
    for char_lign_avant in list[coor_avant:coor_apres]:
        if char_lign_avant not in characters and char_lign_avant not in ['.', '\n']:
            return True
    return False

def check_around(list, coor, coor_colonne):
    coor_avant = int(coor[1]) - 1 if (int(coor[1]) - 1) > 0 else 0
    if coor[1] > 0 and list[coor_avant] not in characters and list[coor_avant] not in ['.', '\n']:
        return True
    return False




# Day3part1()


def Day3part2():