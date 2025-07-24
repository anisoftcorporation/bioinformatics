# functions.py>
from collections import defaultdict
import random
def PatternCount(text,pattern):
    count = 0
    pattern_len = len(pattern)
    text_len = len(text)
    #print(text_len)
    #print(pattern_len)
    index = 0
    while index < (text_len - pattern_len):
        data = text[index:(index+len(pattern))]
        #print(data)
        if data == pattern:
            count = count+1
        index = index+1
    return count

def FrequencyTable(text,k):
    frequencyMap = {}
    index = 0
    text_len = len(text)
    while index < (text_len - k):
        pattern = text[index:index+k]
        if frequencyMap.get(pattern) is not None:
            old_value = frequencyMap.get(pattern)
            new_value = old_value + 1
            frequencyMap[pattern] = new_value
        else:
            frequencyMap[pattern] = 1
        index = index+1
    return frequencyMap

def MaxMap(frequencyMap):
    maxvalue = max(frequencyMap.values())
    return maxvalue

def BetterFrequentWords(text,k):
    table = FrequencyTable(text,k)
    maxvalue = MaxMap(table)
    maxcount = 0 
    pattern_list = ''
    print(table)
    print(maxvalue)
    for key in table:
        if table[key] == maxvalue:
            if maxcount == 0:
                pattern_list = pattern_list + key
            else:
                pattern_list = pattern_list +" "+ key
            maxcount = maxcount+1
           
            
    return pattern_list

def ReverseComplement(pattern):
    asList = list(pattern)
    k = len(pattern)
    
    i=0
    while i < k:
        
        if pattern[i] == 'T':
            asList[i] = 'A'
        if pattern[i] == 'A':
            asList[i] = 'T'
        if pattern[i] == 'C':
            asList[i] = 'G'
        if pattern[i] == 'G':
            asList[i] = 'C'
        i = i+1
    complement = "".join(asList)
    reverse_complement = complement[::-1]
    return reverse_complement
        
def PatternMatching(pattern,gnome):
    index_list = list()
    
    
    pattern_len = len(pattern)
    
    gnome_len = len(gnome)
    index = 0
    while index < (gnome_len - pattern_len):
        sliced = gnome[index:(index+pattern_len)]
        
        if sliced == pattern:
            
            index_list.append(str(index))
        index = index+1
    result_string = " ".join(index_list)
    return result_string

def FindClumps(text,k,L,t,mode):
    #mode 0 returns string of K-mers mode 1 returns count
    text_len = len(text)
    index = 0 
    result = list()
    while index < text_len - L:
        window = text[index:index+text_len]
        freqMap = FrequencyTable(window,k)
        for key in freqMap:
            if freqMap[key] >= t:
                result.append(key)
        index = index +1     
    clump_list = list(set(result))
    if mode == 0:
        clump_string = " ".join(clump_list)
        return clump_string
    else:
        return len(clump_list)
    
def MinimumSkew(pattern):
    pattern_len = len(pattern)
    min_skew_pos = list()
    min_skew_val = 0
    skew = list()
    skew.insert(0,0)
    index = 0
    while index < pattern_len:
      
      cur = pattern[index]
      skew_index = index+1
      
      
      if cur == 'C':
            skew.insert(skew_index,skew[index]-1)
            
      elif cur == 'G':
            skew.insert(skew_index,skew[index]+1)
            
      else:
            skew.insert(skew_index,skew[index])
      if skew[skew_index] == min_skew_val:
             min_skew_pos.append(skew_index)
      elif skew[skew_index] < min_skew_val:
            min_skew_val = skew[skew_index]
            min_skew_pos = list()
            min_skew_pos.append(skew_index)
      index = index+1
    result = " ".join(map(str,min_skew_pos))
    return result

def DrawSkew(pattern):
    pattern_len = len(pattern)
    min_skew_pos = list()
    min_skew_val = 0
    skew = list()
    skew.insert(0,0)
    index = 0
    while index < pattern_len:
      
      cur = pattern[index]
      skew_index = index+1
      
      
      if cur == 'C':
            skew.insert(skew_index,skew[index]-1)
            
      elif cur == 'G':
            skew.insert(skew_index,skew[index]+1)
            
      else:
            skew.insert(skew_index,skew[index])
      
      index = index+1
    import matplotlib.pyplot as plt
    x_indices = range(len(skew))
    plt.plot(x_indices, skew)
    plt.show()
    
    
def HammingDistance(p,q):
    p_len = len(p)
    q_len = len(q)
    dist = 0 
    index = 0
    while index < p_len:
        if p[index] != q[index]:
            dist = dist+1
        index = index+1
    return dist

def ApproximatePatternMatching(pattern,gnome,d):
    index_list = list()
    
    
    pattern_len = len(pattern)
    
    gnome_len = len(gnome)
    print("Gnome:",gnome)
    print("Pattern:",pattern)
    print("D:",d)
    print("Genome Length:",gnome_len)
    print("Pattern_Len:",pattern_len)
    print("Index upper Bound:",(gnome_len - pattern_len)+1)
    index = 0
    while index < (gnome_len - pattern_len)+1:
        sliced = gnome[index:(index+pattern_len)]
        print("Index:",index)
        print("Sliced:",sliced)
        if HammingDistance(sliced,pattern) <= d:
            
            index_list.append(str(index))
        index = index+1
    result_string = " ".join(index_list)
    return result_string
def ApproximatePatternCount(text,pattern,d):
    count = 0
    pattern_len = len(pattern)
    text_len = len(text)
    #print(text_len)
    #print(pattern_len)
    index = 0
    while index < (text_len - pattern_len)+1:
        data = text[index:(index+len(pattern))]
        #print(data)
        if HammingDistance(data,pattern) <= d:
            count = count+1
        index = index+1
    return count

def Suffix(pattern):
    return pattern[1:len(pattern)]
def Neighbors(pattern, d):
    
    pattern_len = len(pattern)
    if d == 0:
        return {pattern}
    if pattern_len == 1:
        return {'A','T','C','G'}
    Neighborhood = list()
    SuffixNeighbors = Neighbors(Suffix(pattern),d)
    for val in SuffixNeighbors:
        if HammingDistance(Suffix(pattern), val) < d:
            Neighborhood.append('T'+val)
            Neighborhood.append('A'+val)
            Neighborhood.append('C'+val)
            Neighborhood.append('G'+val)
        else:
            Neighborhood.append(pattern[0]+val)

    return Neighborhood  
def FrequentWordsWithMismatches(text, k, d):
    pattern_list = list()
    frequencyMap = {}
    index = 0
    text_len = len(text)
    while index < (text_len - k)+1:
        pattern = text[index:index+k]
        neighborhood  = Neighbors(pattern,d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if frequencyMap.get(neighbor) is not None:
                old_value = frequencyMap.get(neighbor)
                new_value = old_value + 1
                frequencyMap[neighbor] = new_value
            else:
                frequencyMap[neighbor] = 1
        index = index+1
    
    maxVal = MaxMap(frequencyMap)
    
    for pattern_t in frequencyMap:
        if frequencyMap[pattern_t] == maxVal:
            pattern_list.append(pattern_t)
            
    return pattern_list
def FrequentWordsWithMismatchesRC(text, k, d):
    
    pattern_list = list()
    frequencyMap = defaultdict(int)
    index = 0
    text_len = len(text)
    rc_text = ReverseComplement(text)
    rc_len = len(rc_text)
    while index < (text_len - k):
        pattern = text[index:index+k]
        
        neighborhood  = Neighbors(pattern,d)
        for neighbor in neighborhood:
            rc_neighbor = ReverseComplement(neighbor)
            frequencyMap[neighbor]+=1
            frequencyMap[rc_neighbor]+=1
            
        
        index = index+1
    
    maxVal = MaxMap(frequencyMap)
    print(maxVal)
    for pattern_t in frequencyMap:
        if frequencyMap[pattern_t] == maxVal:
            pattern_list.append(pattern_t)
            
    return pattern_list

def FrequentWordsWithMismatchesRCNew(Text, k, d):
    
    freq = defaultdict(int)

    for i in range(len(Text) - k + 1):

        pattern = Text[i:i+k]

        neighborhood = Neighbors(pattern, d)

        for neighbor in neighborhood:

            freq[neighbor] += 1

            freq[ReverseComplement(neighbor)] += 1  # Count reverse complement too

    max_freq = max(freq.values())

    return [pattern for pattern, count in freq.items() if count == max_freq]

def MotifEnumeration(Dna,k,d):
    dnaStrings = Dna.split()
    dna_len = len(dnaStrings)
    kmers_in_dna = defaultdict(int)
    patterns = list()
    for string in dnaStrings:
        #print(string)
        str_len = len(string)
        kmers_in_string = list()
        for index in range(str_len-k+1):
            
            k_mer = string[index:index+k]
            neighbors = Neighbors(k_mer,d)
            kmers_in_string = kmers_in_string+neighbors
            #print(k_mer +":",neighbors)
        kmers_in_string = list(set(kmers_in_string))
        #print(kmers_in_string)
        for kmers in kmers_in_string:
            kmers_in_dna[kmers] +=1
    for pattern in kmers_in_dna:
        if kmers_in_dna[pattern]== dna_len:
            patterns.append(pattern)

    return patterns


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    dnaList = Dna.split()
    k = len(Pattern)
    distance = 0
    for dnaString in dnaList:
        
        hammingDist = 99999
        k_mer_list = GenerateKmers(k,dnaString)
        
        for kmer in k_mer_list:
            
            dis = HammingDistance(Pattern,kmer)
            
            if hammingDist > dis:
                hammingDist = dis
       
        distance = distance + hammingDist
    return distance
def AllStrings(k):
    
    pattern_list = list()
    for index in range(k):
        pattern_list.append('A')
    pattern = "".join(pattern_list)
    result = Neighbors(pattern,k)
    return result


def GenerateKmers(k,data):
    data_len = len(data)
    k_mer_list = list()
    for index in range(data_len-k+1):
        k_mer = data[index:index+k]
        if k_mer_list.count(k_mer) == 0:
            k_mer_list.append(k_mer)
    return k_mer_list
def Motif_Score(motif):
    final_score = 0 
    k = len(motif[0])
    t = len(motif)
    for j in range(k):
        column_score_map = defaultdict(int)
        column_score = 0 
        for i in range(t):
            column_score_map[motif[i][j]]+=1
        
        max_value_key = max(column_score_map, key=column_score_map.get)
        
       
        
        for key in column_score_map:
           
            if key != max_value_key:
                   
                    column_score += column_score_map[key]
        final_score += column_score
    return final_score
def Apply_Laplace(count_matrix):
    
    k = len(count_matrix[0])
    for i in range(4):
        for j in range(k):
            count_matrix[i][j]+=1
    return count_matrix
    
def Count_Matrix(motif):
   
    k = len(motif[0])
    
    t = len(motif)
   
    count_matrix = []
    A_COUNT = list()
    C_COUNT = list()
    G_COUNT = list()
    T_COUNT = list()
    
    for j in range(k):
        column_score_map = defaultdict(int)
        column_score = 0 
        for i in range(t):
            column_score_map[motif[i][j]]+=1
            
        A_COUNT.append(column_score_map['A'])
        C_COUNT.append(column_score_map['C'])
        G_COUNT.append(column_score_map['G'])
        T_COUNT.append(column_score_map['T'])
    
    count_matrix.append(A_COUNT)
    count_matrix.append(C_COUNT)
    count_matrix.append(G_COUNT)
    count_matrix.append(T_COUNT)
    count_matrix = Apply_Laplace(count_matrix)
    return count_matrix
def Profile_Matrix(count_matrix):
    profile_matrix = []
    k = len(count_matrix[0])
    column_sums = [0]*k
    for row in count_matrix:
        for i in range(k):
            column_sums[i] += row[i]
            
   
    for row in count_matrix:
        prob = [0]*k
        for i in range(k):
            prob[i] = row[i]/column_sums[i]
        profile_matrix.append(prob)
    return profile_matrix
    
def Get_Profile_Matrix(motifs):
    count_matrix = Count_Matrix(motifs)
    
    profile_matrix = Profile_Matrix(count_matrix)
    return profile_matrix
def Most_Probable_Kmer(k,Text,profile_matrix):
    #print(Text)
    prob = -1
    most_prob_kmer = ''
    
    kmer_list = GenerateKmers(k,Text)
    for kmer in kmer_list:
        #print(kmer+":",Pr(kmer,profile_matrix))
        if Pr(kmer,profile_matrix) > prob:
            prob = Pr(kmer,profile_matrix)
            most_prob_kmer = kmer
           
           
    return most_prob_kmer
def Pr(kmer,Profile):
    
    k = len(kmer)
    prob = 1
    for index in range(k):
        
        if kmer[index] == 'A':
            prob = prob*Profile[0][index]
        elif kmer[index] == 'C':
            prob = prob*Profile[1][index]
        elif kmer[index] == 'G':
            prob = prob*Profile[2][index]
        elif kmer[index] == 'T':
            prob = prob*Profile[3][index]
    return prob

'''This method returns Motiifs from a DNA string based on a Profile Matrix '''
def Motiffs(Profile,DNA):
    k = len(Profile[0])
    
    DNA_LIST  = DNA.split()
   
    NUM = len(DNA_LIST)
    
   
    MOTIFS = []
    for i in range(NUM):
        CUR_STRING = DNA_LIST[i]
        BEST_KMER  = Most_Probable_Kmer(k,CUR_STRING,Profile)
        #print("CURRENT STRING:"+CUR_STRING+" BEST KMER:"+BEST_KMER)
        MOTIFS.append(list(BEST_KMER))
    return MOTIFS
''' Below Method can be used to test with a known Profile matix '''
def HARD_CODE_PROFILE_MATRIX():
    row1 = "0.8 0 0 0.2"
    row2 = "0 0.6 0.2 0"
    row3 = "0.2 0.2 0.8 0"
    row4 = "0 0.2 0 0.8"
    row1_list = row1.split()
    row2_list = row2.split()
    row3_list = row3.split()
    row4_list = row4.split()
    row1_float = [float(s) for s in row1_list]
    row2_float = [float(s) for s in row2_list]
    row3_float = [float(s) for s in row3_list]
    row4_float = [float(s) for s in row4_list]
    profile_matrix = [row1_float,row2_float,row3_float,row4_float]
    return profile_matrix

'''**Randomized Motiff Search**
Now we will be using **Monte-Carlo** simulation method in our Algorithm. As per this, we will randomly select K-mer from each of the DNA string, and use that as the starting motiff to create a starting profile.

After that we will be Iterating over all the DNA strings and find Most probable K-mer from each and with them after each iteration, we will have a new Motiff.

We will calculate score and until we get a better score, we will keep doing the same loop. in next loop, this motiff will be used as base for starting Profile.
'''
def RandomizedMotifSearch (DNA, k , t):
    DNA_LIST  = DNA.split()
    DNA_LEN = len(DNA_LIST)
    
    INIT_MOTIF = []
    for i in range(DNA_LEN):
        CUR_STRING = DNA_LIST[i]
        KMERS = GenerateKmers(k,CUR_STRING)
        NUM_KMERS = len(KMERS)
        RANDOM_POSITION = random.randint(0, NUM_KMERS-1)
        RANDOM_KMER = KMERS[RANDOM_POSITION]
        INIT_MOTIF.append(list(RANDOM_KMER))
        BEST_MOTIF  = INIT_MOTIF
        
        
    while True:
        INIT_PROFILE = Get_Profile_Matrix(BEST_MOTIF)
        MOTIFS = Motiffs(INIT_PROFILE,DNA)
        #print(Motif_Score(MOTIFS))
        if Motif_Score(MOTIFS) < Motif_Score(BEST_MOTIF):
                
                BEST_MOTIF = MOTIFS 
        else:
                return BEST_MOTIF