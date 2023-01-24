import os
import datetime
import hashlib

start_date = datetime.date.today()
date = start_date
result = 1

while(result != 0):
    key = str(date)  + " bigtent"
    print("Trying " + key)
    result = os.system( "gpg --batch  --passphrase " + (hashlib.sha256(key.encode('utf-8'))).hexdigest() + " --output firefox.log.gz --decrypt firefox.log.gz.gpg " )
    date = date + datetime.timedelta(days=-1)
    if result != 0:
        print("\tFailed")
