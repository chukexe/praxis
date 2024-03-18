#!/usr/bin/env python

balance = 0
day = 1
signup_bonus = 3
upline_gift = 4

print('Day' + ' ' + str(day))
print("Welcome to CloudMall.")
print("Enjoy your signup bonus of £3")
balance += signup_bonus

print('Balance:' + ' £' + '{:,.1f}'.format(balance))
print("Your upline has gifted you with £4")
balance += upline_gift

print('Balance:' + ' £' + '{:,.1f}'.format(balance))

level_counter = 0
balances = [7,22,150,600,2250,5300,11000,30000,75000,225000,375000]
upgrade_bonuses = [0,4,5,8,12,70,150,300,500,800,1000]
daily_earnings = [0.7,2.2,10.0,30.0,112.5,265.0,440.0,1200.0,3000.0,9000.0,15000.0]
reqIVs = [0,0,0,1,2,5,10,15,22,28,35]

while True:
      if reqIVs[0] == 1:
          member = 'member'
      else:
          member = 'members'
            
      if balance < balances[0]:
            balance = balance + earning_pot[0]
            day += 1
            print('Day' + ' ' + str(day))
            print('Balance:' + ' £' + '{:,.1f}'.format(balance))
            
      elif balance >= 375000:
            if level_counter == 10:
                print("You've invited  " + str(reqIVs[0]) + ' ' + str(member))
                print(f"Welcome to VIP{level_counter}!")
                level_counter = 0
                balance = balance + upgrade_bonuses[0]
                print("Upgrade bonus: " + ' £' + str(upgrade_bonuses[0]) )
                print('Balance:' + ' £' + '{:,.1f}'.format(balance))
                input('Press Enter to continue.')
            else:
                pass
            
            earning_pot[0] = 15000
            day += 1
            print('Day' + ' ' + str(day))
            balance = balance + earning_pot[0]
            print('Balance:' + ' £' + '{:,.1f}'.format(balance))
            
            if balance > 750000:
                  break
      else:
            if reqIVs[0] == 0:
                pass
            else:
                print("You've invited  " + str(reqIVs[0]) +  ' ' + str(member))
            print(f"Welcome to VIP{level_counter}!")
            level_counter += 1
            balance = balance + upgrade_bonuses[0]
            if upgrade_bonuses[0] == 0:
                pass
            else:
                print("Upgrade bonus: " + ' £' + str(upgrade_bonuses[0]) )

            print('Balance:' + ' £' + '{:,.1f}'.format(balance))
            
            upgrade_bonuses.remove(upgrade_bonuses[0])
            balances.remove(balances[0])
            earning_pot = []
            earning_pot.append(daily_earnings[0])
            daily_earnings.remove(daily_earnings[0])
            reqIVs.remove(reqIVs[0])
            
            input('Press Enter to continue.')
            
