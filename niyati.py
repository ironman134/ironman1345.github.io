def iron_logo():
      print("\n\n")
      print("#####################################################################################")
      print("                                                                                   ##")
      print("###  ###  ###  ###  #  #    ### #   #  ##   # #  ###  ###  ### ###  ###  ###      ##")
      print("#     #   # #  # #  # #      #  ##  #  # #  # #  #     #   # #  #   #    #       ##")
      print("###   #   ###  ##   ##       #  # # #  # #  # #  ###   #   ##   #   ###  ###    ##")
      print("  #   #   # #  # #  # #      #  #  ##  # #  # #    #   #   # #  #   #      #   ##")
      print("###   #   # #  # #  #  #    ### #   #  ##   ###  ###   #   # # ###  ###  ###  ##")
      print("                                                                              #")
      print("                                                                             #")
      print("\n\n")

def spider_logo():
    print("\n\n")
    print("                      +.                                                                   .+")
    print("                      ##o\                                                               /o##")
    print("                      ####:                                                             :####")
    print("                      ####:                                                             :####")
    print("                      ####:    +\.                                               ./+    :####")
    print("                      ####:    o##+-                                           -+##o    :####")
    print("                      ####:    o###+                                           +###o    :####")
    print("                      ####:    o###+                                           +###o    :####")
    print("                      ####:    o###+                                           +###o    :####")
    print("                      ####:    o###+                                           +###o    :####")
    print("                      ####:    o###+                                           +###o    :####")
    print("                      ####:    o###+                .-//+o+//-.                +###o    :####")
    print("                      ####:    o###+             -+############o/-             +###o    :####")
    print("                      ####:    o###+           :o#################o-           +###o    :####")
    print("                      ####:    o#####+/-      +#####################/      -/+#####o    :####")
    print("                      ####+.   +########o    o#######################+    o########+   .+####")
    print("                      #######+/---/o####o   /#########################:   o####o/---/+#######")
    print("                      \+#########+ .####o  .###########################   o####. +#########+/")
    print("                         .-+######..####o  -###########################.  o####..######+-.")
    print("                          -+######..####o  -###########################   o####..######+-")
    print("                       -+########/ .####o   o#########################+   o####. \########+-")
    print("                    -/########/  ./o####o   -#########################.   o####o\.  \########\-")
    print("                 ./########/  ./o#######:   :########################o-   :#######o\. .\########\-")
    print("              ./#######o/. ./o#######/. .:o#############################o-  .\########\. .\o#######\.")
    print("           ./o######o/. ./o######o/. .:o###################################+:. .\o######o\. .\o######o\.")
    print("          o######o/.  :o######o/.  :o#########################################o:  .\o######o:  .:o######o")
    print("          ####o:.    -######/.  :o###############################################o/  .\######-    .:o####")
    print("          ####:      -####.    /###################################################\    .####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################\     ####-      -####")
    print("          ####:      -####.    /###################################################:     ####-      -####")
    print("          ####:      -####.     -/o#############################################o:.      ####-      -####")
    print("          ####:      -####.        .:+#######################################+-          ####-      -####")
    print("          ####:      -###+             -/o###############################o/-             +###-      -####")
    print("          ####:      -#o-                 .:o#########################o:.                 -o#-      -####")
    print("          ####:      -:                      .-+###################+-.                      :-      -####")
    print("          ####:                                  -/o############/-                                  -####")
    print("          ####:                                      .:+#####o/.                                    -####")
    print("          ####:                                          -/:                                        -####")
    print("          ####:                                                                                     -####")
    print("          ###+                                                                                       +###")
    print("          #+.                                                                                         .+#")
    print("          .                                                                                             .")    

def speak(data, mode : int):
    if mode == 1:
        print(data)
        import text_to_speech
        q = text_to_speech
        q.speak(data, "en")
    else:
        print(data)
        from win32com.client import Dispatch
        y = Dispatch("SAPI.Spvoice")
        y.Speak(data)
    	

def tts(data, mode : int):
    if mode == 1:
        import text_to_speech
        q = text_to_speech
        q.speak(data, "en")
    else:
        from win32com.client import Dispatch
        y = Dispatch("SAPI.Spvoice")
        y.Speak(data)

