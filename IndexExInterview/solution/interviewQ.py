import MySQLdb as mdb
import sys
import re

try:
    con = mdb.connect('localhost', 'root', '123', 'interview');
    cur = con.cursor(mdb.cursors.DictCursor)

    #-----------------------------------------------------------
    # Step 1
    # counting the number of email address by their domain name
    # and store these number in dictionary by domain name
    # dic{'hotmail' , 10}
    #-----------------------------------------------------------
    cur.execute("SELECT * FROM mailing")
    dic = {}
    for i in range(cur.rowcount):
        email = cur.fetchone()
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email['addr']): #Firstly, check the validation of email address
            print 'Bad Email format, ignore it '

        else: # valid email format
            domain = re.search("@[\w.]+", email['addr'])
            if domain.group().split("@")[1] not in dic: #domain name does not in dictionary
                dic[domain.group().split("@")[1]] = 1
            else:
                dic[domain.group().split("@")[1]] += 1


    #-------------------------------------------------------------------------------------
    # Step 2.1
    # Store updated values of last 30 days in updated dictionary 
    #-------------------------------------------------------------------------------------
    cur.execute("SELECT * FROM daily_record")
    list = []
    updated_dic = {}
    clo_num = len(cur.description) - 1
    for i in range(cur.rowcount):
        row = cur.fetchone()

        list.append(dic[row['domain_name']]) #Fist, add today's new count to list that already stroe in dictionary
        # add count of each day to list 
        for day in range( 1, clo_num ):
            list.append(row['d' + str(day)])
        
        updated_dic[row['domain_name']] = list
        list = [] # empty this list for the use of next round of loop

    #-------------------------------------------------------------------------------------
    # Step 2.2
    # update another table, daily_record, with today's count of email by their domain name
    #-------------------------------------------------------------------------------------
    for key in updated_dic.keys():
        for day in range(1, clo_num + 1):    #update one row of daily_record
            cur.execute("UPDATE daily_record set d" + str(day) + "=%s WHERE domain_name=%s", ( updated_dic[key][day-1], key ))
        con.commit()

    #-------------------------------------------------------------------------------------
    # Step 3.1 
    # calculate percentage growth of last 30 days compared to total number at the last 30th 
    #-------------------------------------------------------------------------------------
    cur.execute("SELECT * FROM daily_record")
    growth_dic = {}
    for i in range(cur.rowcount):
        row = cur.fetchone()
        growth_dic[row['domain_name']] = (int(row['d1']) - int(row['d30'])) / float(row['d30']) * 100

    #-------------------------------------------------------------------------------------
    # Step 3.2 
    # Sort result stored in growth_dic with descending order
    # And store the reuslts in nested list 'report'
    #-------------------------------------------------------------------------------------   
    report = [] 
    for val,i in zip(sorted(growth_dic.items(), key=lambda (k, v): v, reverse=True), range(5)): # advanced looping technique
        print val[0], val[1] ,i
        list = [val[0], round(val[1],2)] #rounded to two decimal
        report.append(list)

    #-------------------------------------------------------------------------------------
    # Step 3.3 
    # Write results to output file
    #-------------------------------------------------------------------------------------   
    with open('report.txt', 'w') as f:
        for row in report:
            print row
            f.write("%s\n" % str(row))

except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
        
    if con:
        con.rollback()
    con.close()

finally:
    if con:
        con.close
        f.close()