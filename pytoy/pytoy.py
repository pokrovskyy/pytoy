def teddy(do_print = True):
    """
    Returns and optionally prints a teddy bear ASCII art.

    Arguments
    ---------
    do_print : bool
        Whether to print the teddy bear.

    Returns
    -------
    str :
        Reeturns a teddy bear ASCII art.

    Examples
    --------
    teddy()
    """

    # Art by Joan G. Stark
    # https://www.asciiart.eu/toys/teddy-bears
    teddy_str = """
          ___   .--.
    .--.-"   "-' .- |
   / .-,`          .'
   \   `           \
    '.            ! \\
      |     !  .--.  |
      \        '--'  /.____
     /`-.     \__,'.'      `\\
  __/   \`-.____.-' `\      /
  | `---`'-'._/-`     \----'    _ 
  |,-'`  /             |    _.-' `\\
 .'     /              |--'`     / |
/      /\              `         | |
|   .\/  \      .--. __          \ |
 '-'      '._       /  `\         /
    jgs      `\    '     |------'`
               \  |      |
                \        /
                 '._  _.'
                    ``"""
    if (do_print):
        print(teddy_str)

    return teddy_str
