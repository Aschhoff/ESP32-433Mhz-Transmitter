




# Config for IR Tx

IRtx= 12            # IR Tx Pin 
IRrx= 14            # IR Rx Pin
TX433=13            # 433Mhz Pin
#-----------------------------------------------------------------------

ssid      = "Aschi"              # WLan Name
password  = "2482694733144611"  # Password
# for static IP
ip        = "192.168.10.201"
subnet    = "255.255.255.0"
gateway   = "192.168.10.1"
dns       = "8.8.8.8"
#openhab_url="192.168.10.123"     # for OPENHAB
socket_ip=("192.168.10.26",8888)  # TCP Socket 

#-----------------------------------------------------------------------

# devicename {protokoll,addresse 1-4095 ,unit 1-n}      quigg7000
# devicename {protokoll,addresse 1-1000000 ,state 1-15} ev1527
# rawdata {define your one output}
# pt8a978 {transmit a special protokol}

devices={"Switch_on":{"prot":"tx_quigg7000","addr":"2016","unit":"2","state":"1"},
         "Switch_off":{"prot":"tx_quigg7000","addr":"2016","unit":"2","state":"0"},
         "Bell":{"prot":"tx_ev1527","addr":"535723","state":"1"},
         "Gong":{"prot":"pt8a978","code":"40","tx_pin":TX433},
         "Kerze_on" :{"prot":"IRNEC","code":"00000000111111111000000001111111","tx_pin":IRtx},
         "Kerze_off":{"prot":"IRNEC","code":"00000000111111111001000001101111","tx_pin":IRtx},
         "rawdata":{"sync":"14000","short":"400","long":"1400","code":"111011001000011111111100"}
        
       }





















