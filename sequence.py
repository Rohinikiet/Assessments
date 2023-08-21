def samePatterns(color1, patterns):
    if len(color1) != len(patterns):
        return False

    color_to_pattern = {} 
    pattern_to_color = {}  

    for i in range(len(color1)):
        color = color1[i]
        pattern = patterns[i]
        if color in color_to_pattern and color_to_pattern[color] != pattern:
            return False
        if pattern in pattern_to_color and pattern_to_color[pattern] != color:
            return False

        color_to_pattern[color] = pattern
        pattern_to_color[pattern] = color

    return True

color1 = ["red", "blue", "blue"]
patterns = ["a", "b", "b"]
print(samePatterns(color1, patterns))  

color2 = ["red", "blue", "bluee"]
print(samePatterns(color2, patterns)) 
