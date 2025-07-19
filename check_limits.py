def is_temperature_ok(temp):
  if temp >=0 and temp <= 45:
    return True
  print('Temperature is out of range!')
  return False

def is_soc_ok(soc1):
  if soc1 < 20 or soc1 > 80:
    return False
    print('State of Charge is out of range!')
  else:
    return True

def is_charge_ok(c1):
  if c1 > 0.8:
    return False
  else:
    return True

def battery_is_ok(temperature, soc, charge_rate):
  return all([is_temperature_ok(temperature), is_soc_ok(soc), is_charge_ok(charge_rate)])


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
