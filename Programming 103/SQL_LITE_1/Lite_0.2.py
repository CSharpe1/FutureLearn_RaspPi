#! python3
import sqlite3
conn = sqlite3.connect(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\FutureLearn_RaspPi\Programming 103\SQL_LITE_1\computer_cards.db")





def create(name, cores, cpu_speed, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, cost) VALUES ('{}', {}, '{}','{}')".format(name, cores, cpu_speed, cost)

    conn.execute(insert_sql)

    conn.commit()





#create('test', 4, 2.0, 2000)

print("Enter the details:")
name = input("Name >")
cores = input("Cores >")
cpu_speed = input("CPU speed (GHz) >")
#ram = input("RAM (MB) >")
cost = input("Power usage ($) >")
create(name, cores, cpu_speed, cost)

result = conn.execute("SELECT * FROM computer")
print(result)

computers = result.fetchall()

for computer in computers:
    name = computer[0:]
    print(name)


conn.close()


