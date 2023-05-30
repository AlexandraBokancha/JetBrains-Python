chain_el = {key: value for key, value in zip('ACTG', 'TGAC')}


def create_comp_strand(sequence):
    return ''.join(chain_el.get(k, k) for k in sequence)


def make_ligation(element1, original_seq, element2):
    return element1 + original_seq + element2


file = input()
with open(f'{file}', 'r') as f:
    content = f.read().split()


# Find the location of the plasmid restriction site within the plasmid sequence
cut_position = content[0].find(content[1]) + len(content[1]) - 1

# Cut the plasmid sequence at the restriction site to create two fragments
fragment1, fragment2 = content[0][:cut_position], content[0][cut_position:]

# Check the closest site
comp_cut1 = content[2].find(content[3]) + len(content[3]) - 1
comp_cut2 = content[2].rfind(content[4]) + len(content[4]) - 1
if comp_cut1 < len(content[2]) - comp_cut2:
    gfp_fragment1 = content[2][:comp_cut1]
    gfp_fragment2 = content[2][comp_cut1:comp_cut2]
    gfp_fragment3 = content[2][comp_cut2:]
else:
    gfp_fragment1 = content[2][:comp_cut2]
    gfp_fragment2 = content[2][comp_cut2:comp_cut1]
    gfp_fragment3 = content[2][comp_cut1:]

# Ligate the sticky parts together
modified_plasmid = make_ligation(fragment1, gfp_fragment2, fragment2)
comp_modified_plasmid = create_comp_strand(modified_plasmid)
print(modified_plasmid)
print(comp_modified_plasmid)