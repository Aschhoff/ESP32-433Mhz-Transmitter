
# Config File for tx433_pi.py


tx_pin=13           # ESP Pin for Tx

# devicename {protokoll,addresse 1-4095 ,unit 1-n}      quigg7000
# devicename {protokoll,addresse 1-1000000 ,state 1-15} ev1527
# rawdata {define your one output}
# pt8a978 {transmit a special protokol}

devices={"Switch_on":{"prot":"tx_quigg7000","addr":"2816","unit":"2","state":"1"},
         "Switch_off":{"prot":"tx_quigg7000","addr":"2816","unit":"2","state":"0"},
         "Bell":{"prot":"tx_ev1527","addr":"535723","state":"1"},
         "Gong":{"prot":"pt8a978","code":"40","tx_pin":tx_pin},
         "rawdata":{"sync":"14000","short":"400","long":"1400","code":"111011001000011111111100"}
        
       }
















