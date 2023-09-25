import random
import numpy as np
# generate a random closed mesh with n edges; output next and opp for the halfedge structure
# faces can be found as cycles of next, and vertices as cycles of opp[next]
def generate_random_mesh(n):
    next = list(range(2*n))
    p = list(range(2*n))
    random.shuffle(next)
    
    # random p is used to generate a permutation with all cycles of length 2
    random.shuffle(p)
    opp = [0]*(2*n)
    
    for i in range(0, 2*n, 2):
        a, b = p[i], p[i + 1]
        opp[p[i]] = p[i+1]
        opp[p[i+1]] = p[i]
        
    return np.array(next),np.array(opp)

def build_orbits(perm): 
    visited = [False]*(max(perm)+1)
    cycles = []
    for i in range(0,max(perm)+1):
        if not visited[i]:
            cycles.append([])
            i_it = i
            while True: 
                visited[i_it] = True
                cycles[-1].append(i_it)
                i_it = perm[i_it]
                if i_it == i:
                    break
    return cycles  

# m = number of faces in the triangle mesh, the number of halfedges = 3*m
# m should be even, because the number of halfedges is 2*edges, so 3*m is divisible by 2

def generate_random_tri_mesh(m):
    if m % 2 != 0: 
        print('error, number of faces should be even')
        return None
        
    p = list(range(3*m)) 
    random.shuffle(p)
    next = [0] * (3*m)
    
    # Fill the permutation array by creating cycles of length 3
    for i in range(m):
        next[p[3*i]]=p[3*i+1]
        next[p[3*i+1]]=p[3*i+2]
        next[p[3*i+2]]=p[3*i]
        
    p = list(range(3*m)) 
    random.shuffle(p)
    opp = [0]*(3*m)
    
    for i in range(0, 3*m, 2):
        a, b = p[i], p[i + 1]
        opp[p[i]] = p[i+1]
        opp[p[i+1]] = p[i]

    return np.array(next),np.array(opp)

next,opp = generate_random_mesh(1)
cw_circ = opp[next]

# vertices correspond to cycles of opp x next, faces to cycles of next, one can construct 
# halfedge to vertex and halfedge to face maps from this 
vert_cycles = build_orbits(cw_circ)
face_cycles = build_orbits(next)

next,opp = generate_random_tri_mesh(2)
cw_circ = opp[next]

vert_cycles = build_orbits(cw_circ)
face_cycles = build_orbits(next)

