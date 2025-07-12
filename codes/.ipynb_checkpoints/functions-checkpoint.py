# functions.py>
from collections import defaultdict

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