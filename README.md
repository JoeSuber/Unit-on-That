Unit-on-That
============

Finds the maximum unit-chunk that fits inside the successive remainder-chunks 
until the smallest grained (base) unit is exhausted.

Uses: 
count change in whatever currency units 
ie. pennies nickles, dimes, quarters, 5s, 10s, 20s all get counted out
  using biggest-first. Any that aren't used are left-out, avoiding confusion.

give a good sense of time from a time.time()-style blob of seconds
  - yes asctime is there, but it isn't clear how easily I might,
  for instance, show the user time since creation of a file 'f' via 
  its os.stat(f).st_ctime.  With this I just subtract st_ctime from now()
  and show them whatever units are appropriate in the dict.

deal with Imperial weights / measures - all in ounces / inches 
  until you need to translate for user-comprehension

cooking volumes - ie. gallons, cups in 234234215 teaspoons?

heck, even metric benefits from having the units tagged,
then use another instance with conversions built in for your Imperialist
users.

use instances of this with different unit-list-depth to show how much of
  one top-unit is in another.

__main__:

between 1000000000 sec, and 1383112218.92 sec
(0.921365022659 = fractional sec from given 383112218.921)
a stringy-list breakdown (joined): 
 : 12 year, 3 month, 24 day, 4 hr, 3 min, 38 sec
(0.921365022659 = fractional sec from given 383112218.921)
a dictionary breakdown:
year       :    12
month      :     3
day        :    24
hr         :     4
min        :     3
sec        :    38

Process finished with exit code 0
