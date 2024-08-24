from scan1 import scan1
from scan2 import scan2

while True:
        product_no, quantity, expiry_date = scan1()
        scan_two = scan2()
        if scan_two == "next euro":
                continue                
        lot_no, pallet_no = scan_two            
        print(lot_no)
        break
print("End")