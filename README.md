Unit-on-That
============

- ie. Perhaps something just fell from a north-bound low-flying Piper-Cub to your farm on the Florida panhandle. Now, with apologies to the Reverend Horton Heat, you need to know when a certain number of "grains" becomes a gram and then grams an ounce, and then ounces in a kilo. Wanting to only look it up once in the course of developing your business,, you use a chart or web-site to get the decimal notations of those quantities into two lists - labels and conversions - as you go up the ladder from smallest to biggest for a Unit-on-That instance. You avoid problems of meaningless significant digits without having to think about where fractions of this-and-that fall. You may create your own units, like eighth-ounces or quarter-grams or 1/42 cents - without further burdening yourself or the user - (well... the user of the program, I mean).

Finds the maximum unit-chunk that fits inside the successive remainder-chunks 
until the smallest grained (base) unit is exhausted.  Info presented in an
ordered dictionary for easy comparisons or display.

Uses: 
count out change in appropriate currency units 
- ie. pennies nickles, dimes, quarters, 5s, 10s, 20s all get counted out
  using biggest-first. Any that aren't used are left-out, avoiding confusion.

give a good sense of time from a time.time()-style blob of seconds
  - yes asctime is there, but it isn't clear how easily I might,
  for instance, show the user time since creation of a file 'f' via 
  its os.stat(f).st_ctime.  With this I just subtract st_ctime from now()
  and show them whatever units are appropriate in the dict. Maybe they don't need minutes & seconds.

deal with Imperial weights / measures 
- you can use all ounces / inches until you need to translate for user-comprehension

cooking volumes 
- ie. gallons, cups, tablespoons in 234234215 teaspoons?

heck, even metric 
- benefits from having the units tagged,
- then use another instance with conversions built in for your Imperialist users.

If dealing with metric-to-imperial or imperial-to-metric you need only convert 
the finest-grained units once 

- use just your required precicion (as long as that requirement doesn't approach the bit-depth of the number-types you are using) Then let Unit-on-That do the rest of the work.  If a nanosecond gives time for about 1.017 feet of lightspeed travel in a vacuum and copper conducts at about half that speed...

__main__:

- example below: note that the .92... part is discarded as it is smaller than the smallest unit

- between 1000000000 sec, and 1383112218.92 sec
- (0.921365022659 = fractional sec from given 383112218.921)
a stringy-list breakdown (joined): 
 : 12 year, 3 month, 24 day, 4 hr, 3 min, 38 sec
- (0.921365022659 = fractional sec from given 383112218.921)
a dictionary breakdown:{
year       :    12 ,
month      :     3 ,
day        :    24 ,
hr         :     4 ,
min        :     3 ,
sec        :    38 ,
}

 **
- between 100000 penny, and 78947 penny
- (0.0 = fractional penny from given -21053)
a stringy-list breakdown (joined): 
 : 2 Benjamin, 1 Hamilton, 2 Quarter, 3 penny
- (0.0 = fractional penny from given -21053)
a dictionary breakdown:{
Benjamin   :     2 ,
Hamilton   :     1 ,
Quarter    :     2 ,
penny      :     3 ,
}

Process finished with exit code 0


