# Project 6
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05
timelist = []

class Crime:

   def __init__(self, ID, category='ROBBERY'):
      timelist = get_timelist()
      length = 0
      self.ID = ID
      self.category = category
      self.time = 0
      self.month = 0
      self.day = ''
      times = []
      daysofweek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
      temp = 0
      lines = []
      line = None
      line = find_crimes(timelist,self.ID)

   def get_time(self):
      if self.ID == ID and 0 <= self.time <= 24 and 0 <= self.month <= 12:
         if line[1] in daysofweek:
            self.day = line[1]
            self.month = int_split_first2(line[2], 'month')
            self.time = int_split_first2(line[3], 'time')
            if int_split_first2(line[3],'time') >= 12:
               temp = 24 - self.time
               self.time = '{}PM'.format(temp)
            else:
               self.time = '{}AM'.format(self.time)


   def __repr__(self):
      return '{} {} {} {} {}\n'.format(self.ID, self.category, self.month, self.day, self.time)


   def __eq__(self, other):
      if self.ID == self.ID:
         return True
      else:
         return False


def get_timelist():
   #makes list of times
   # none -> list
   attempt = 1
   timelist = []
   if attempt == 1:
      times = open('times.tsv', 'r')
      for line in times:
         timelist.append(line)
      attempt += 1
   return timelist


def get_lines(file):
   #str->list
   #gets lines from file
   lines = []
   file = open(file)
   for line in file:
      lines.append(line)
   return lines


def int_split_first2(input,timeormonth):
   #splits first 2 off string
   #str,str -> str
   chars = input.split()
   c = ''
   index = 0
   first2 = ''
   if timeormonth == 'month':
      for i in chars:
         c += i
      i = str(i[8] + i[9])
   elif timeormonth == 'time':
      for i in chars:
         c += i
      i = str(i[0]+i[1])
   return int(i)


def create_crimes(lines):
   #list -> list
   #Takes as input a list of strings Returns a list of Crime objects
   robberies = []
   ID = None
   c = 0
   line = None
   newline = None
   newlines = ''
   for i in lines:
      if i != '\n':
         newlines += str(i)
      else:
         newlines += ','
   newlines = newlines.split()
   for i in newlines:
      if i == 'ROBBERY':
         ID = newlines[c-1]
         robberies.append(Crime(ID))
      c += 1
   return robberies


def update_crimes(crimes, lines):
   #list -> list
   #Takes as input a list of Crime objects and a list of strings updates their time attributes Returns a list of Crime objects with updated attributes.
   timelist = get_timelist()
   i = timelist[0]
   newlist = []
   x = find_crimes(i[0])
   for i in crimes:
      newlist += Crime(i[0])
   return crimes


def binary_search(list,item):
   #list+str ->int
   #proforms binary search
   first = 0
   last = len(list)-1
   found = False
   while first<=last and not found:
      mid = (first + last)//2
      if list[mid] == item :
         found = True
      else:
         if item < list[mid]:
            last = mid - 1
         else:
            first = mid + 1
   return found

def find_crimes(crimes, crime_id):
   #proforms search to find info on id
   #list int-> object
   idindex = binary_search(crimes, crime_id)
   crime = '{}{}{}{}'.format(crimes[idindex],crimes[idindex+1],crimes[idindex+2],crimes[idindex+3])
   return crime





def most_frequent(list):
   #list -> str
   #finds most frequent item in list
   dict = {}
   count, itm = 0, ''
   for item in (list):
      dict[item] = dict.get(item, 0) + 1
      if dict[item] >= count:
         count, itm = dict[item], item
   return itm


def main():
   ID = ''
   idlist = []
   robberycount = 0
   maxday = 'No Max Day'
   maxtime = 0
   maxmonth = 0
   day = []
   month = []
   time = []
   robberies = []
   file = open('crimes.tsv', 'r')
   lines = get_lines('crimes.tsv')
   robberies = create_crimes(lines)
   for i in robberies:
      robberycount += 1
      day += str(i[2])
      month += i[2]
      time += i[2]
   maxday = most_frequent(day)
   maxmonth = most_frequent(month)
   maxtime = most_frequent(time)
   print(
      """   
      NUMBER OF PROCESSED ROBBERIES: {}
      DAY WITH MOST ROBBERIES: {}         
      MONTH WITH MOST ROBBERIES: {}
      HOUR WITH MOST ROBBERIES: {}
""".format(robberycount, maxday, maxmonth, maxtime))

   output = open('robberies.tsv', 'w+')
   x = 0
   for line in idlist:
      output.write(Crime(line[0]))
      x += 1

if __name__ == '__main__':
   main()
