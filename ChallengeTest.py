'''
tuple = מכיל אובייקטים,ניתן להוסיף את אותם ערכים, אבל לא ניתן לשנות את מה שהוא מכיל
List = מכיל אובייקטים, ניתן להוסיף או לשנות את מה קיים בו, יכול להכיל את אותם ערכים
SET = מכיל אובייקטים, וניתן לעריכה, אבל לא שומר בתוכו אובייקטים בעלי ערך זהה
'''

num = int(input('choose number: '))

for i in range(num+1):
  i = i - (num//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (num - i*2) + " "*i)

