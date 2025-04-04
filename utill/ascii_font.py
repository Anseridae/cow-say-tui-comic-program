letterGlyphs = {
    "a": (
        r"||\    ",
        r"||\\   ",
        r"|| \\  ",
        r"||//\\ ",
        r"||/  \\"
    ),

    "b": (
        r"||\ ",
        r"||\\",
        r"||//",
        r"||\\",
        r"||//"
    ),

    "c": (
        r"  //",
        r" // ",
        r"||  ",
        r" \\ ",
        r"  \\"
    ),

    "d": (
        r"|\\  ",
        r"||\\ ",
        r"|| \\",
        r"|| //",
        r"||// "
    ),

    "e": (
        r"/\/\/\/",
        r"||     ",
        r"|\/\/\ ",
        r"||     ",
        "|/\\/\\/\\"
    ),

    "f": (
        r"/\/\/\/",
        r"||     ",
        r"|\/\/  ",
        r"||     ",
        r"|/     "
    ),

    "g": (
        r"/\/\/\/ ",
        r"||      ",
        r"||  \/\|",
        r"||    ||",
        r"|\/\/\/ "

    ),

    "h": (
        "/|    |\\",
        r"||    ||",
        r"|\/\/\/|",
        r"||    ||",
        r"||    ||"
    ),

    "i": (
        r"\/\||/\/",
        r"   ||   ",
        r"   ||   ",
        r"   ||   ",
        "/\\/||\\/\\"
    ),

    "j": (
        r" /\/\/",
        r"    ||",
        r"    ||",
        r"    //",
        r"/\/\/ "
    ),

    "k": (
        r"||  //",
        r"|| // ",
        r"||/\\ ",
        r"|// \\",
        r"|/  |/"
    ),

    "l": (
        r"|\    ",
        r"||    ",
        r"||    ",
        r"||    ",
        "\\|/\\/\\"
    ),

    "m": (
        r"|\    /|",
        r"|\\  //|",
        r"||\\//||",
        r"|| \/ ||",
        r"|/    \|"
    ),

    "n": (
        r"|\\  /|",
        r"||\\ ||",
        r"|| \\||",
        r"||  \\|",
        r"|/   \|"
    ),

    "o": (
        " //\\  ",
        r"// \\ ",
        r"\\  \\",
        r" \\ //",
        r"  \\/ "
    ),

    "p": (
        r"|\\ ",
        r"||\\",
        r"||//",
        r"||/ ",
        r"||  "
    ),

    "q": (
        r" /.|",
        r"//||",
        r"\\||",
        r" \||",
        r"  ||"
    ),

    "r": (
        r"|\\  ",
        r"||\\ ",
        r"||// ",
        r"||\\ ",
        r"|| \\"
    ),

    "s": (
        " /\\",
        r"// ",
        r"\\ ",
        r" \\",
        r"\//"
    ),

    "t": (
        r"\/\||/\/",
        r"   ||   ",
        r"   ||   ",
        r"   ||   ",
        r"   ||   "
    ),

    "u": (
        "/|    |\\",
        r"||    ||",
        r"||    ||",
        r"\\    //",
        r" \\/\// "
    ),

    "v": (
        "||  /\\",
        r"|| // ",
        r"||//  ",
        r"|//   ",
        r"|/    "
    ),

    "w": (
        r"|\    /|",
        r"|| /\ ||",
        r"||//\\||",
        r"||/  \||",
        r"|/    \|"
    ),

    "x": (
        "|\\   |\\",
        r" \\  //",
        r"  \\// ",
        r"  //\\ ",
        r" //  \\"
    ),

    "y": (
        "/| |\\",
        r"\\ //",
        r" \\/ ",
        r" //  ",
        r"//   "
    ),

    "z": (
        r"/\/\/\/",
        r"    // ",
        r"   //  ",
        r"  //   ",
        r"/\/\/\/"
    ),
    " ": (
        r"  ",
        r"  ",
        r"  ",
        r"  ",
        r"  "
    ),

    "_": (
        r" ",
        r" ",
        r" ",
        r" ",
        r" "
    ),

    "R": (
        "\033[91m",
        "\033[91m",
        "\033[91m",
        "\033[91m",
        "\033[91m"
    ),

    "B": (
        "\033[94m",
        "\033[94m",
        "\033[94m",
        "\033[94m",
        "\033[94m"
    ),

    "E": (
        "\033[0m",
        "\033[0m",
        "\033[0m",
        "\033[0m",
        "\033[0m"
    )
}


def combineGlyphs(glyphs: str) -> list[list[str]]:
    """combines separate 5 line glyphs into a single set of 5 strings"""
    gottenGlyphs = []
    compiledGlyphs = [[], [], [], [], []]

    for i in glyphs:
        gottenGlyphs.append(letterGlyphs[i])

    def addGlyph(index: int):
        for j in gottenGlyphs:
            compiledGlyphs[index].append(j[index])

    for dex in range(5):
        addGlyph(dex)

    return compiledGlyphs


def glyphsPrint(letters: str, spacing: str):
    """prints letter glyphs in my custom ascii font with spacing characters between each letter glyph"""
    for k in combineGlyphs(letters):
        print(spacing.join(k))


def exampleGlyphsPrint():
    glyphsPrint("the_ RquickE_ brown_ fox", " ")
    print("")
    glyphsPrint("jumps_ over the_ BlazyE_ dog", " ")