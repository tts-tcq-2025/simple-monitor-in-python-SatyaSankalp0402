
def battery_is_ok(temperature, soc, charge_rate):
  if temperature < 0 or temperature > 45:
    Print1(temperature)
    return False
  elif soc < 20 or soc > 80:
    Print1(soc)
    return False
  elif charge_rate > 0.8:
    Print1(charge_rate)
    return False
  else
  return True

def Print1(word):
    print( word 'is out of range!')

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
