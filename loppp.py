 
import os
import sys
from time import sleep as timeout
from core.smtcore import *

def main():
	banner()
        print "    \033[1;33m[01] Nmap"
        print "    [02] Red Hawk"
	print "    [03] D-Tect"
        print "    [04] sqlmap"
	print "    [05] Infoga"
	print "    [06] ReconDog"
	print "    [07] AndroZenmap"
        print "    [08] sqlmate"
        print "    [09] AstraNmap"
	print "    [10] WTF"
	print "    [11] Easymap"
	print "    [12] BlackBox"
	print "    [13] XD3v"
	print "    [14] Crips"
	print "    [15] SIR"
	print "    [16] EvilURL"
	print "    [17] Striker"
	print "    [18] Xshell"
	print "    [19] OWScan"
	print "    [20] OSIF"
        print "    [21] Torshammer"
        print "    [22] Slowloris"
        print "    [23] InfoSploit"
        print "    [24] GoldenEye"
        print "    [25] Xerxes"
        print "    [26] Planetwork-DDOS"
        print "    [27] Hydra"
        print "    [28] Black Hydra"
        print "    [29] Optiva-Framework"
        print "    [30] santet-online"
        print "    [31] SMfbBrute"
        print "    [32] Metasploit"
        print "    [33] commix"
        print "    [34] sqlscan"
        print "    [35] Brutal"
        print "    [36] A-Rat"
        print "    [37] WPSploit"
        print "    [38] Websploit"
        print "    [39] Routersploit"
        print "    [40] BlackBox"
        print "    [41] XAttacker"
        print "    [42] TXTool"
        print "    [43] Cloak"
        print "    [44] Rat_Hunter"
        print "    [45] Locky"
        print "    [46] ShodanHat"
        print "    [47] HatCloud"
        print "    [48] Blazy"
        print "    [49] Droid-Hunter"
        print "    [50] DSSS"
        print "    [51] InstaHack"
        
        print "    [52] Exit from smtools\n" 
        smtool = raw_input("smts > ")
		
	if smtool == "1" or smtool == "01":
			nmap()
	elif smtool == "2" or smtool == "02":
			red_hawk()
	elif smtool == "3" or smtool == "03":
			dtect()
	elif smtool == "4" or smtool == "04":
			sqlmap()
	elif smtool == "5" or smtool == "05":
			infoga()
	elif smtool == "6" or smtool == "06":
			reconDog()
	elif smtool == "7" or smtool == "07":
			androZenmap()
	elif smtool == "8" or smtool == "08":
			sqlmate()
	elif smtool == "9" or smtool == "09":
			astraNmap()
	elif smtool == "10":
         		wtf()
	elif smtool == "11":
			easyMap()
	elif smtool == "12":
			blackbox()
	elif smtool == "13":
			xd3v()
	elif smtool == "14":
			crips()
	elif smtool == "15":
			sir()
	elif smtool == "16":
			evilURL()
	elif smtool == "17":
			striker()
	elif smtool == "18":
			xshell()
	elif smtool == "19":
			owscan()
	elif smtool == "20":
			osif()
        elif smtool == "21":
                        torshammer()
        elif smtool == "22":
                        slowloris()
        elif smtool == "23":
                        info()
        elif smtool == "24":
                        goldeneye()
        elif smtool == "25":
                        xerxes()
        elif smtool == "26":
                        planetwork_ddos()
        elif smtool == "27":
                        hydra()
        elif smtool == "28":
                        black_hydra()
        elif smtool == "29":
                        optiva()
        elif smtool == "30":
                        sanlen()
        elif smtool == "31":
                        smfb()
        elif smtool == "32":
                        metasploit()
        elif smtool == "33":
                        commix()
        elif smtool == "34":
                        sqlscan()
        elif smtool == "35":
                        brutal()
        elif smtool == "36":
                        a_rat()
        elif smtool == "37":
                        wpsploit()
        elif smtool == "38":
                        websploit()
        elif smtool == "39":
                        routersploit
        elif smtool == "40":
                        blackbox()
        elif smtool == "41":
                        xattacker()
        elif smtool == "42":
                        txtool()
        elif smtool == "43":
                        cloak()
        elif smtool == "44":
                        rat()
        elif smtool == "45":
                        locky()
        elif smtool == "46":
                        shodan()
        elif smtool == "47":
                        hatcloud()
        elif smtool == "48":
                        blazy()
        elif smtool == "49":
                        droid()
        elif smtool == "50":
                        dsss()
        elif smtool == "51":
                        instaHack() 
        elif smtool == "52":
            sys.exit()
            print "\nBYE!!!!!"
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
