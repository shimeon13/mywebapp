from decimal import Decimal
import sys

opioids = ["経口トラマドール",
           "経口タペンタドール",
           "経口ヒドロモルフォン",
           "経口モルヒネ",
           "経口オキシコドン",
           "坐剤モルヒネ",
           "注射モルヒネ",
           "注射フェンタニル",
           "注射オキシコドン",
           "フェントステープ",
           "デュロテップパッチ"]

def opi_dose_conv_mor(opioid_use, input_opioid_dose):
  if opioid_use == opioids[0]:
    return input_opioid_dose / 5
  elif opioid_use == opioids[1]:
    return input_opioid_dose / 10 * 3
  elif opioid_use == opioids[2]:
    return input_opioid_dose * 5
  elif opioid_use == opioids[3]:
    return input_opioid_dose
  elif opioid_use == opioids[4]:
    return input_opioid_dose * 3 / 2
  elif opioid_use == opioids[5]:
    return input_opioid_dose * 2
  elif opioid_use == opioids[6]:
    return input_opioid_dose * 3
  elif opioid_use == opioids[7]:
    return input_opioid_dose * 100
  elif opioid_use == opioids[8]:
    return input_opioid_dose * 2
  elif opioid_use == opioids[9]:
    return input_opioid_dose * 30
  elif opioid_use == opioids[10]:
    return input_opioid_dose / 4.2 * 60
  else:
    sys.exit()




def mor_conv_opioids(odcm):
  return [
    odcm * 5,
    odcm / 3 * 10,
    odcm / 5,
    odcm,
    odcm * 2 / 3,
    odcm / 2,
    odcm / 3,
    odcm / 100,
    odcm / 2,
    odcm / 30,
    odcm / 60 * Decimal(4.2)
    ]
