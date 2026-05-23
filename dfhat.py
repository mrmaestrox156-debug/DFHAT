import os
import sys
import time

# Garante que a pasta 'modules' está visível no path de execução do Python
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from modules.phone import analyze_phone
    from modules.email import analyze_email
    from modules.link_site import analyze_target
except ImportError as e:
    print(f"\033[91m[-] Fatal Import Error: Modules not found. Ensure the directory architecture is correct.\nDetail: {e}\033[0m")
    sys.exit(1)

# Artes isoladas para evitar poluição visual nas funções
WELCOME_ART = """\033[1;37m╭─────────────────────────────────────────────────────────╮
 │    WELCOME TO THE DFHAT                        │
 ├─────────────────────────────────────────────────────────┤
 │                                                         │
 │  WARNING: This tool is developed for educational and    │
 │  security auditing purposes only. Mishandling or illegal│
 │  use of this software may violate local laws.           │
 │                                                         │
 │  The developer assumes NO liability for damages caused. │
 │                                                         │
 ├─────────────────────────────────────────────────────────┤
 │  Are you responsible for the use of the tool?           │
 │                                                         │
 │              [ Y ] Yes       [ N ] No                   │
 ╰─────────────────────────────────────────────────────────╯\033[0m"""

MAIN_ART = """\033[91m
DDDDDDDDDDDDD      FFFFFFFFFFFFFFFFFFFFFFHHHHHHHHH     HHHHHHHHH               AAA         TTTTTTTTTTTTTTTTTTTTTTT
D::::::::::::DDD   F::::::::::::::::::::FH:::::::H     H:::::::H              A:::A        T:::::::::::::::::::::T
D:::::::::::::::DD F::::::::::::::::::::FH:::::::H     H:::::::H             A:::::A       T:::::::::::::::::::::T
DDD:::::DDDDD:::::DFF::::::FFFFFFFFF::::FHH::::::H     H::::::HH            A:::::::A      T:::::TT:::::::TT:::::T
  D:::::D    D:::::D F:::::F       FFFFFF  H:::::H     H:::::H             A:::::::::A     TTTTTT  T:::::T  TTTTTT
  D:::::D     D:::::DF:::::F               H:::::H     H:::::H            A:::::A:::::A            T:::::T
  D:::::D     D:::::DF::::::FFFFFFFFFF     H::::::HHHHH::::::H           A:::::A A:::::A           T:::::T
  D:::::D     D:::::DF:::::::::::::::F     H:::::::::::::::::H          A:::::A   A:::::A          T:::::T
  D:::::D     D:::::DF:::::::::::::::F     H:::::::::::::::::H         A:::::A     A:::::A         T:::::T
  D:::::D     D:::::DF::::::FFFFFFFFFF     H::::::HHHHH::::::H        A:::::AAAAAAAAA:::::A        T:::::T
  D:::::D     D:::::DF:::::F               H:::::H     H:::::H       A:::::::::::::::::::::A       T:::::T
  D:::::D    D:::::D F:::::F               H:::::H     H:::::H      A:::::AAAAAAAAAAAAA:::::A      T:::::T
DDD:::::DDDDD:::::DFF:::::::FF           HH::::::H     H::::::HH   A:::::A             A:::::A   TT:::::::TT
D:::::::::::::::DD F::::::::FF           H:::::::H     H:::::::H  A:::::A               A:::::A  T:::::::::T
D::::::::::::DDD   F::::::::FF           H:::::::H     H:::::::H A:::::A                 A:::::A T:::::::::T
DDDDDDDDDDDDD      FFFFFFFFFFF           HHHHHHHHH     HHHHHHHHHAAAAAAA                   AAAAAAATTTTTTTTTTT
\033[1;37m"V.1.0 © copyright mrmaestrox "

                                                      .**                         .**
                                                     * .*                         .* **
                                                    *  *.                          #  .*
                                                   *   #.                          #.  **
                                                  **   **        *#######**       .#.   *
                                                  *.    *.  .*.              **   *.    #
                                              .   *.     .##**               .**#*      #   *
                                              .*  .*         *               *         .*  *#
                                               **. **    ...**                *...    .*  * *
                                               ** *. ***...*.                  **..***. * .*
                                               ...* .*.                              ** .* *
                                                #  .*#.  .          .  .         .   **.. *
                                                 *    ..                            #    .*
                                                   *  *    #**.        .     .**.   *. ..
                                                     *.      *..*#**   *.**..*.      *
                                                      *.                            *.
                                                       .*  **.     *   .      **  **
                                                         #.   #.  .     *  ..***.
                                                       .**.    . *.*.  * ** *  *  *
                                                      **#****  .*** .**. ***  .*..
                                                  .*.** #  * .* *.   .    * .* ..#*.
                                              **     *. #   *****......*....#**  *..#*.
                                         .*.         #  *.    #.**        **##   *. .*  *.
                                     .*.            .*  .*     *#**     *** #    .*  .*     **.
                                 **                 **   #      .*        .*      #   **        .*.
                              *#*.                  *.   **       .#     **       #    **         .  .*
                            *.      **.             *     #        .#*.. **       #     #.              ..
                          .*           **          .#     .*     .*.       **    *#      *                .#.
                         .*              *.        **      *#.  *..*      .* *. **#       #               ***.
                         *.               **       *.       ###*    *     *    *. #        *              *  *
                         #                 .*      *         *       *####       .*        .#            **  ..
                         *                   #     #         **      *.  **      .*         **           *   .*
                         *.                   *   .#          #.     #    *      *.          **         .#   .*
                          #                   .*  ***.         *     #    #.     *.         .*#.        #.   *.
                          .*                   **      .*#*.   .*   .*    .*     #    .*#*.             #    *.
                           #                    #       **      *.  **     *    **     **              *.    * l
                           *.     ...           #.    ** ** **   *  *.     *.   *.       **            *     *
                           .*          .**.     .#    *..*   #.  .# *.      #   #         ***##***.   **     *
                           *.              .*.   #     #*    #.   **#       #  **        **      .*   *      *.
                          .*                  #* *  .**      #     *#       *# *.       #*       #   **      *.
                          *            ...     *##.         **     .#        *.#       *. *#     *.  #       ..
                         .*     .*.     **.  .**#         *#*       **       *#*      *.*#####   .*  #       .*
                          .*         **    .*  **       *.   *.      *.       #      *   *#*#     #  #       .*
                           #       .*     *.  **        *.    **     .*      .#    .#.           .*  #        *
                          .*      *      *   **         .*     .*     **     *.   .*.*.         **   #        #
                          .*     *      *   **          **       **    #     *   **    *#*  .**.     #        #
                          *.           *   .#.          #.        .#   .*   **  **        .*         #        #.
                          *.          *.   ##.         .**          *.  *.  #  *.                    #        *.
                          .*          *   .* *     .*     *          .* .* .# *.                     #        ..
                           **         #   ** .#*    *     .*           *.#.#**                       #.       .*
                            .*        *   **  **    *.     *            *####                        #.        *
                              *.      *.  .*   #    *     .*              #*                         *.        .
                               **      *.  **  *    #  .  .*              **                         *.         *
                                 #*     *#.  ##*   .#  .*  .*             #*                         .*         #
                                   **      **##*   .*   * * **            #.                         .*         #
                                   *.         **   **   .* *..#.          #.                         .*         #
                                   *          #    ***    *  * .**        #.                          *         #
                                   *         .*    #  *.   *.  *. .**     #.                          *         #
                                   *         **   *.   **   .*   .*  *.   #.                          #         #
                                  **                      #.  .#*#   #    #.                          #.        *
                                  *                        **  #  .**#    #.                          #*        *
                                  *#############################################################################*


\033[0m"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_welcome_banner():
    print(WELCOME_ART)

def draw_main_banner():
    print(MAIN_ART)

def draw_options_menu():
    print("\033[90m ┌────────────────────────────────────────────────────────┐")
    print(" │  SELECT AN OPTION                                      │")
    print(" └────────────────────────────────────────────────────────┘")
    print("  [1] ── SPAM NUMBER")
    print("  [2] ── FAKE EMAIL")
    print("  [3] ── LINK")
    print("  [4] ── SITE")
    print("  [5] ── EXIT")
    print(" ──────────────────────────────────────────────────────────\033[0m")

def loading_bar():
    print("\n\033[90m[+] Booting DFHAT Core System Engine...\033[0m")
    bar_width = 40
    sys.stdout.write("Progress: [")
    sys.stdout.flush()
    
    for i in range(bar_width):
        time.sleep(0.04)
        sys.stdout.write("█")
        sys.stdout.flush()
        
    sys.stdout.write("] 100% Complete\n")
    time.sleep(0.5)

def main():
    clear_screen()
    draw_welcome_banner()
    
    selection = input(" ❯ Selection: ").strip().upper()
    
    if selection == 'N':
        print("\n\033[91m[-] Security Audit Aborted by User. Exiting...\033[0m")
        sys.exit(0)
    elif selection == 'Y':
        loading_bar()
        
        while True:
            clear_screen()
            draw_main_banner()
            draw_options_menu()
            
            try:
                opt = input(" ❯ Digite a sua opção: ").strip()
                
                if opt == '1':
                    num = input("\n❯ Enter Target Phone Number (e.g., +5511999999999): ").strip()
                    analyze_phone(num)
                elif opt == '2':
                    email = input("\n❯ Enter Target Email Address: ").strip()
                    analyze_email(email)
                elif opt == '3':
                    lnk = input("\n❯ Enter Target Link String: ").strip()
                    analyze_target(lnk, "link")
                elif opt == '4':
                    ste = input("\n❯ Enter Target Site Domain/URL: ").strip()
                    analyze_target(ste, "site")
                elif opt == '5':
                    print("\n\033[91m[+] System Terminated. Goodbye.\033[0m")
                    break
                else:
                    print("\033[91m[-] Invalid option. Selection bounds are 1 to 5.\033[0m")
                    time.sleep(1.5)
            except KeyboardInterrupt:
                print("\n\n\033[91m[!] Execution Interrupted. Returning to main engine...\033[0m")
                time.sleep(1.5)
    else:
        print("\033[91m[-] Argument Error: Please choose between [Y] or [N].\033[0m")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
