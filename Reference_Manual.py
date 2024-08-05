def generate_reference_manual():
    manual = []
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual.append(f'{pair_number}: {color_pair_to_string(major_color, minor_color)}')
    return '\n'.join(manual)
 
